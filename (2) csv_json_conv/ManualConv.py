DEFAULT_INPUT_FILE_NAME = 'input.csv'
DEFAULT_OUTPUT_FILE_NAME = 'output.json'
DEFAULT_SEPARATOR = ','


class Converter:

    @staticmethod
    def convert(input_file_path: str = DEFAULT_INPUT_FILE_NAME,
                output_file_path: str = DEFAULT_OUTPUT_FILE_NAME):

        with open(input_file_path, "r") as f:
            content = f.readlines()

        header = content[0]
        data = content[1:]

        ans = []
        for record in data:
            l = []
            for pair in zip(header.split(DEFAULT_SEPARATOR), record.split(DEFAULT_SEPARATOR)):
                l.append(f'''"{pair[0].strip()}": "{pair[1].strip()}"''')
            tmp = f'''{{{", ".join(l)}}}'''
            ans.append(tmp)

        json_string = f'''[{", ".join(ans)}]'''

        with open(output_file_path, "w") as f:
            f.write(json_string)
