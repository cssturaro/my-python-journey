import os

lista_compras = []

while True:
    opcao = input("Selecione uma opção: \n [I]nserir [A]pagar [L]istar \n> ").upper()
    os.system("cls")
    if opcao.startswith("I"): 
        insert = input("Produto: ")
        lista_compras.append(insert)
    if opcao.startswith("A"):
        try:
            for item in enumerate(lista_compras):
                a, b = item
                print(a, b)
            pop = int(input("Número do produto: "))
            lista_compras.pop(pop)
        except:
            print('\033[2;31m Digite um número de produto válido! \033[m')
    if opcao.startswith("L"): 
        for item in enumerate(lista_compras):
            a, b = item
            print(a, b)
    
