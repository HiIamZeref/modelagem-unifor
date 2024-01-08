from pprint import pprint

class Reader():
    def __init__(self, filename: str) -> None:
        with open(filename, 'r') as file:
            lines = file.readlines()
            new_lines = [line.replace("\n", "") for line in lines]

            self.qntVertices = int(new_lines[0])
            self.cores = new_lines[1].split(" ")

            arcosBruto = new_lines[2:]

            self.arcos = [ [int(arco.split(" ")[0]), int(arco.split(" ")[1]), int(arco.split(" ")[2])] for arco in arcosBruto]
