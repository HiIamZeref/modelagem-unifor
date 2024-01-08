from pprint import pprint

class Reader():
    def __init__(self, filename: str) -> None:
        with open(filename) as file:
            lines = file.readlines()
            new_lines = [line.replace("\n", "") for line in lines]

            first_line = new_lines[0]
            splitted_line = first_line.split(" ")

            self.quantidadeDePontos = int(splitted_line[0])
            self.quantidadeDeRuas = int(splitted_line[1])

            data = new_lines[1: len(new_lines)]

            self.data = [string.split(" ") for string in data]


    



