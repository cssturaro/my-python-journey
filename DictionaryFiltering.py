import os as os

list_prod = [
    {"nome": "Queijo", "valor": 10},
    {"nome": "Arroz", "valor": 6},
    {"nome": "Feijão", "valor": 12},
    {"nome": "Tomate", "valor": 8},
    {"nome": "Banana", "valor": 14},
    {"nome": "Pão", "valor": 6},
    {"nome": "Azeite", "valor": 24},
    {"nome": "Cebola", "valor": 8},
    {"nome": "Caviar", "valor": 100},
    {"nome": "Bebidas", "valor": 42},
    {"nome": "Batata frita", "valor": 32},
]

def filtrar (lista, pre_max, pre_min):
    filtered_list = []
    for key in lista:
        if key["valor"] > pre_max or key["valor"] < pre_min:
            continue 
        filtered_list.append(key)
    return filtered_list

continuar = "S"
while True:
    os.system("cls")

    if continuar not in ["S", "s", "sim"]:
        break
    
    print("________________________________\n")
    pre_max = int(input("Valor máximo: "))
    pre_min = int(input("Valor mínimo: "))
    print("________________________________\n")
    result = filtrar(list_prod, pre_max, pre_min)
    for product in result:
        print(product)

    continuar = input("Deseja fazer outra busca? sim [S] não [N]: ")
