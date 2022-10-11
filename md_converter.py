import sys
import os


DEFAULT_INPUT_FILENAME = "solution.py"
DEFAULT_OUTPUT_FILENAME = "out.txt"

if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        file_name = args[1]
        if file_name.find(".py") == -1:
            file_name = DEFAULT_INPUT_FILENAME
    else:
        file_name = DEFAULT_INPUT_FILENAME

    if not os.path.exists(f"./{file_name}"):
        print(f"File {file_name} does not exist")
        exit(1)

    with open(file_name, "r") as f:
        content = f.read()
    comments_section, code_section = content.split('# ---end---')
    title_description_split_index = comments_section.find("# description")
    title = comments_section[:title_description_split_index].removeprefix("# title").strip()
    description = comments_section[title_description_split_index:].removeprefix("# description").strip()
    processed_title = "-".join(title.lower().split())

    output_content = f"+ [{title}](#{processed_title})\n\n## {title}\n\n{description}\n\n'''python{code_section}'''\n"

    with open(DEFAULT_OUTPUT_FILENAME, "w") as out_file:
        out_file.write(output_content)



