

# python-course

## Задание 1

### Описание

Реализовать конвертер c форматированием. На входе файл *.py c содержимым в виде описания задачи и исходного кода задачи, на выходе файл *.md с оформленным форматированием под markdown формат. Если *.md файл не пуст, то осуществить дозапись в файл новой задачи без перезаписи содержимого.
Программа должна быть покрыта тестами.

### Пример 1
<details><summary>Вход</summary><blockquote>
    
solution.py

```
# title Print Hello
# description Напечатать на экран Hello!
# ---end----

def print_hello():
    print('Hello!')
    
```    
 
out.md
````

````
</blockquote></details>


<details><summary>Выход</summary><blockquote>

out.md

````
+ [Print Hello](#print-hello)

## Print Hello

Напечатать на экран Hello!

```python 
def print_hello():
    print('Hello!')
```

````
</blockquote></details>

### Пример 2

<details><summary>Вход</summary><blockquote>

solution.py

```
# title Print Greeting
# description Напечатать на экран Greeting!
# ---end----

def print_greeting():
    print('Greeting!')
    
```    
 
out.md

````
+ [Print Hello](#print-hello)

## Print Hello

Напечатать на экран Hello!

```python 
def print_hello():
    print('Hello!')
```
````
</blockquote></details>
    
<details><summary>Выход</summary><blockquote>

out.md

````
+ [Print Hello](#print-hello)
+ [Print Greeting](#print-greeting)

## Print Hello

Напечатать на экран Hello!

```python 
def print_hello():
    print('Hello!')
```

## Print Greeting

Напечатать на экран Greeting!

```python 
def print_greeting():
    print('Greeting!')
```
````
</blockquote></details>

## Задание 2

### Описание

Реализовать конвертер из csv файла в json объект. На вход программа принимает csv файл, результатом работы программы является файл *.json, содержимым которого является сконвертированные csv в json.
Программа должна быть покрыта тестами, учесть крайние случаи, что файл может быть пустым, некоторых значений может и не быть в csv

Необходимо реализовать 2 решения:
1. Без использования сторонних модулей
2. С использованием модулей import csv, import json 



### Пример

<details><summary>Вход</summary><blockquote>

input.csv

```
id,name,birth,salary,department
1,Ivan,1980,150000,1
2,Alex,1960,200000,5
3,Ivan,,130000,8
```
</blockquote></details>

<details><summary>Выход</summary><blockquote>

output.json

```
[
 {
   id: 1,
   name: Ivan,
   birth: 1980,
   salary: 150000,
   department: 1
 },
 {
   id: 2,
   name: Alex,
   birth: 1960,
   salary: 200000,
   department: 5
 },
 {
   id: 3,
   name: Ivan,
   birth: null,
   salary: 130000,
   department: 8
 }
]
```
</blockquote></details>

## Задание 3

### Описание

string = "A simple sentence has the most basic elements that make it a sentence: a subject a verb and a completed thought"

1. Найти все числа от 1 до 1000, которые делятся на 17

2. Найти все числа от 1 до 1000, которые содержат в себе цифру 2

3. Найти все числа от 1 до 10000, которые являются палиндромом	

4. Посчитать количество пробелов в строке

5. Есть любая последовательность непробельных символов латинского алфавита, удалить все гласные из этого слова

6. На входе строка со словами, разделенными через 1 пробел. Найти все слова, длина которых не больше 5

7. На входе строка со словами, разделенными через 1 пробел. Получить словарь, где в качестве ключа используется само слово, а в значении длина этого слова.

8. На входе предложение со всеми пробельными и непробельными символами латинского алфавита. Получить словарь используемых букв в строке, то есть на выходе список уникальных букв.

9. На входе список чисел, получить список квадратов этих чисел / use map

10. На входе список координат, например, [(1, 1), (2, 3), (5, 3)]. Найти все точки, которые принадлежат прямой y = 5 * x - 2. 
На выходе получить словарь из самой точки и расстоянии до этой точки из начала координат (0, 0)

11. Возвести в квадрат все четные числа от 2 до 27. На выходе список.

12. На входе список из координат точек на плоскости. Найти расстояние до самой удаленной точку от начала координат (0, 0) в первой четверти 

13. На входе два списка чисел nums_first = [1, 2, 3, 5, 8] и nums_second = [2, 4, 8, 16, 32]. Получить пары сумм и разниц, [(3, -1), (6, -2), (11, -5), ...]

14. На входе список строк из чисел, например, ['43141', '32441', '431', '4154', '43121']. Найти четные квадраты этих чисел. Ответ записать снова в список из строк, то есть сформировать обратно список строк, но уже отфильтровать все четные квадраты.

15. Менеджер как обычно придумал свое представление данных, а нам оно не подходит

input_str = """name,Petya,Vasya,Masha,Vova
grade,5,5,8,3
subject,math,language,physics,math
year,1999,2000,1995,1998"""


Мы хотим получить нормальную таблицу, чтобы импортировать в csv


[
  {
    'name': 'Petya',
    'grade': '5'
    'subject': 'math'
    'year': '1999'
  },
  {
    'name': 'Vasya',
    'grade': '5'
    'subject': 'language'
    'year': '2000'
  },
  ...
]


16. Получить сумму по столбцам у двумерного списка

a = [[11.9, 12.2, 12.9],
    [15.3, 15.1, 15.1], 
    [16.3, 16.5, 16.5],
    [17.7, 17.5, 18.1]]
    
result = [61.2, 61.3, 62.6]  




## Задание 4

### Описание

Реализовать менеджер задач.
Покрыть тестами TaskManager класс. Например, что подзадачи, ведет к тому, что и из соответствующей ComplexTask удаляется эта подзадача. 


<details><summary>Исходный код</summary><blockquote>

````
class Task:
    def __init__(self, id, name, description, ):
        self.__id = id
        self.__name = name
        self.__description = description
        
    def get_id(self):
        return self.__id
        
    def get_name(self):
        return self.__name


class Subtask(Task):
    # have comlex task id
    def __init__(self):
        self.parent_id = 
    

class ComplexTask(Task):
    # contains list of subtasks
    def __init__(self):
        self.subtasks = []  

  
class TaskManager:
    
    id_series = 0
    
    def __init__(self):
        self.tasks = {}
        self.subtasks = {}
    
    
    def __get_and_increment_id(self):
        next_id_value = TaskManager.id_series
        TaskManager.id_series += 1 
        return next_id_value
        
    
    def create_task(self, name, description):
        current_id = self.__get_and_increment_id()
        new_task = Task(current_id, name, description)
        self.tasks[current_id] = new_task
        return new_task
    
    
    def create_subtask(self, subtask):
        pass
    
    def create_complex_task(self, complex_task):
        pass
    
    def get_tasks(self):
        pass
    
    def get_subtasks(self):
        pass
    
    def get_complex_tasks(self):
        pass
    
    def get_tasks_by_id(self, id):
        pass
    
    def get_subtasks_by_id(self, id):
        pass
    
    def get_complex_tasks_by_id(self, id):
        pass
    
    def remove_tasks(self):
        pass
    
    def remove_subtasks(self):
        pass
    
    def remove_complex_tasks(self):
        pass
    
    def remove_task_by_id(self, id):
        pass
    
    def remove_subtask_by_id(self, id):
        pass
    
    def remove_complex_task_by_id(self, id):
        pass
    
    def update_status(self, task):
        pass
````

</blockquote></details>


## Задание 5

### Описание

Создать сервис для расчета своей почасовой ставки.

Большинство наемных сотрудников имеют фиксированную оплачиваемую ставку. Как-то раз стало интересно, сколько случайно выбранный сотрудник получает в час.
Почасовая ставка отличается из-за праздников и разных выходных от года к году.

1. Сервис должен возвращать ответ в формате JSON вида:
```
{
  "year": 2016,
  "month": "JULY",
  "salary": 1000000,
  "hour_income": 49950.87
}
```
2. Округление почасовой ставки должно быть до копеек
3. Покрыть тестами код



<details><summary>Вход</summary><blockquote>
input.json
```
{
  "year": 2016,
  "month": "JULY",
  "salary": 1000000
}
```
</blockquote></details>

<details><summary>Выход</summary><blockquote>
output.json
```
{
  "year": 2016,
  "month": "JULY",
  "salary": 1000000,
  "hour_income": 49950.87
}
```
</blockquote></details>


## Задание 6

### Описание

Реализовать класс для комплексных чисел ComplexNumber. Основные операции: сложение, вычитание, умножение, модуль числа. Покрыть тестами.
 
### Пример

```python
first = ComplexNumber(1, 2)
second = ComplexNumber(2, 3)
third = first + second
print(third) # 3 + 5i

d = {}
d[first] = 0
d[second] = 1
d[third] = d[first] + d[second]
print(d[third]) # 1
```
