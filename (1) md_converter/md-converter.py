import sys
import os


INPUT_CODE_SEPARATOR = "# ---end---"


def read_data(file_name):
    with open(file_name, "r") as f:
        return f.read()


def write_data(file_name, data):
    with open(file_name, 'a+') as file:
        if os.stat(file_name).st_size == 0:
            file.write(data)
            file.close()
        else:
            file.close()
            old_md_data = read_data(file_name)
            new_data = add_data(old_md_data, data)
            file = open(file_name, 'w')
            file.write(new_data)
            file.close()
        return


def add_data(old_md_data, data):
    old_md_links, old_content = old_md_data.split("<!---sep--->")
    md_link, content = data.split("<!---sep--->")
    template = "{}\n{}\n\n<!---sep--->\n\n{}\n\n{}"

    return template.format(old_md_links.rstrip(), md_link.strip(), old_content.strip(), content.strip())


def prepare_md_titles(data):
    title, description = None, None

    for line in data.split('\n'):
        if line.startswith('# title'):
            title = line.replace('# title ', '')
        elif line.startswith('# description'):
            description = line.replace('# description ', '')

    return title, description


def prepare_md_format(title, description, source_code):
    md_link = '-'.join(title.lower().split())
    template = "+ [{}](#{})\n\n<!---sep--->\n\n## {}\n\n{}\n\n```python\n{}\n```"

    return template.format(title, md_link, title, description, source_code.lstrip())


def convert_data(data):
    titles, source_code = data.split(INPUT_CODE_SEPARATOR)
    title, description = prepare_md_titles(titles)
    result_md = prepare_md_format(title, description, source_code)

    return result_md


def main():
    input_file, output_file = sys.argv[1::]
    content = read_data(input_file)
    result = convert_data(content)
    write_data(output_file, result)


if __name__ == "__main__":
    main()
