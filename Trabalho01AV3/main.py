# PEÇA MAIOR: 25
# CORTES: 12, 10, 3
# PRECISO DE 8 DE 12, 10 DE 10 E 12 DE 5
from pprint import pprint

chapa = 25
cortes = [12, 10, 5]

VETOR_ARMAZENAMENTO = []

dicionario_base = {corte:0 for corte in cortes}
def funcao_recursiva(dic_base: dict, chapa: int, VETOR_ARMAZENAMENTO: list, cortes: list):
    cortou = False

    for corte in cortes:
        restante = chapa - corte

        if restante >= 0:
            cortou = True
            novo_dic_base = dic_base.copy()
            novo_dic_base[corte] = novo_dic_base.get(corte, 0) + 1
            funcao_recursiva(novo_dic_base, restante, VETOR_ARMAZENAMENTO, cortes)

    if not cortou:
        VETOR_ARMAZENAMENTO.append(dic_base.copy())

funcao_recursiva(dicionario_base, chapa, VETOR_ARMAZENAMENTO, cortes)
new_list = []
for dic in VETOR_ARMAZENAMENTO:
    if dic not in new_list:
        new_list.append(dic)
print("Nova lista")
pprint(new_list)

"2x1 + x2 + x3 + 0x4 + 0x5 + 0x6 >= 8"
