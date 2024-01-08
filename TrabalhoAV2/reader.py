from pprint import pprint

class Reader():
    def __init__(self, filename: str) -> None:
        with open(filename) as file:
            lines = file.readlines()
            new_lines = [line.replace("\n", "") for line in lines]

            # PEGANDO QNT DE ORIGENS E DESTINOS
            first_line = new_lines[0]
            splitted_line = first_line.split(" ")

            self.quantidadeDeOrigens = int(splitted_line[0])
            self.quantidadeDeDestinos = int(splitted_line[1])

           
            # PEGANDO PRODUÇÃO DE ORIGENS E DEMANDA DE DESTINOS

            #PRODUÇÃO
            second_line = new_lines[1].split(" ")
            #DEMANDA
            third_line = new_lines[2].split(" ")

            self.producoes = [int(element) for element in second_line]
            self.demandas = [int(element) for element in third_line]
            

            caso = ""
            somaProd = sum(self.producoes)
            somaDemand = sum(self.demandas)

            self.somaProducao = somaProd
            self.somaDemanda = somaDemand
            
            if somaProd == somaDemand:
                caso = "Balanceado."
            elif somaProd < somaDemand:
                caso = "Desbalanceado Produção."
            elif somaProd > somaDemand:
                caso = "Desbalanceado Demanda."

            self.caso = caso

            data = new_lines[3:]
            formatar = [string.split(" ") for string in data]
            for array in formatar:
                for index, element in enumerate(array):
                    array[index] = int(element)

            self.data = formatar


    

# with open("balanceado.txt") as file:
#             lines = file.readlines()
#             new_lines = [line.replace("\n", "") for line in lines]

#             # PEGANDO QNT DE ORIGENS E DESTINOS
#             first_line = new_lines[0]
#             splitted_line = first_line.split(" ")

#             quantidadeDeOrigens = int(splitted_line[0])
#             quantidadeDeDestinos = int(splitted_line[1])

#             pprint(f"Origens: {quantidadeDeOrigens}")
#             pprint(f"Destinos: {quantidadeDeDestinos}")
            

#             # PEGANDO PRODUÇÃO DE ORIGENS E DEMANDA DE DESTINOS

#             #PRODUÇÃO
#             second_line = new_lines[1].split(" ")
#             #DEMANDA
#             third_line = new_lines[2].split(" ")

#             producoes = [int(element) for element in second_line]
#             demandas = [int(element) for element in third_line]
            

#             print(producoes)
#             print(demandas)

#             caso = ""
#             somaProd = sum(producoes)
#             somaDemand = sum(demandas)
            
            
#             if somaProd == somaDemand:
#                 caso = "Balanceado."
#             elif somaProd < somaDemand:
#                 caso = "Desbalanceado Produção."
#             elif somaProd > somaDemand:
#                 caso = "Desbalanceado Demanda."

#             print(caso)

#             data = new_lines[3:]
#             formatar = [string.split(" ") for string in data]
#             for array in formatar:
#                 for index, element in enumerate(array):
#                     array[index] = int(element)

#             pprint(formatar)

            

            

