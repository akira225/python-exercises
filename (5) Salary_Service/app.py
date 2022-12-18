import requests
from utils import month_conversion
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
# migrate = Migrate(app, db)


class Cache(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    month = db.Column(db.String, nullable=False)
    days = db.Column(db.Integer, nullable=False)


@app.route('/', methods=['GET'])
def success_response():
    return jsonify({'status': 'ok'})


@app.route('/calculate', methods=['GET'])
def process_request():
    year = request.json.get('year')
    month = request.json.get('month')
    salary = request.json.get('salary')
    if not (year and month and salary and month_conversion.get(month.upper())):
        return jsonify({'msg': "Incorrect data"}), 400
    if not (year is int and (salary is int or salary is float)):
        return jsonify({'msg': "Incorrect data"}), 400
    month_number = month_conversion.get(month.upper())
    ph_sal = calculate_per_hour_salary(year, month_number, salary)
    return jsonify({
        "year": year,
        "month": month.upper(),
        "salary": salary,
        "hour_income": ph_sal
    })


def calculate_per_hour_salary(year, month, salary):
    cached_result = Cache.query.filter_by(year=year, month=month).first()
    if cached_result:
        return round(salary/cached_result.days/8, 2)
    else:
        days = get_working_days_from_api(year, month)
        return round(salary/days/8, 2)


def get_working_days_from_api(year, month):
    url = f'''https://isdayoff.ru/api/getdata?year={year}&month={month}'''
    res = requests.get(url)
    working_days = res.text.count("0")
    cache_api_response(year, month, working_days)
    return working_days


def cache_api_response(year, month, working_days):
    db.session.add(Cache(year=year, month=month, days=working_days))
    db.session.commit()


if __name__ == '__main__':
    app.run()
