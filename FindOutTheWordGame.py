import os
import random

minhas_palavras = [
    "Palavra", "Cinema", "Bola", "Musica", "Caixao", "Caatinga", "Analfabeto", "Safado", "Safari", "Entendimento", 
    "Forca", "Comida", "Beterraba", "Cenoura", "Macarrao", "Mulher", "Cozinha", "Objeto", "Portugues", "Homem", "Primata", 
    "Ogro", "Animal", "Gostoso", "Cachorro", "Marido", "Violencia", "Mae", "Burrice", "Cuiaba", "Brasil", "Bahia", "Brasileiro",
    "Colher", "Goiaba", "Carioca", "Sacola", "Mercado","Aposentadoria", "Consumismo", "Planeta", "Bacteria", "Geladeira", "Garrafa"

]

palavra_secreta = random.choice(minhas_palavras).upper()
finalizou = False
attempt = 0
letras = {}
Descobertas = {}
for i in range(0, len(palavra_secreta)):
    Descobertas[i] = "-"

while True:
    if finalizou == True:
        os.system("cls")
        palavra_secreta = random.choice(minhas_palavras).upper()
        finalizou = False
        attempt = 0
        letras = {}
        Descobertas = {}
        for i in range(0, len(palavra_secreta)):
            Descobertas[i] = "-"


    cancelar = False
    print("\033[1;34m"+"==============================================================")
    letra_atual = input(f"Digite uma tentativa de letra ({attempt}): ").upper()

    if len(letra_atual) > 1 or len(letra_atual) == 0: 
        print("\033[2;31m" + "Digite apenas uma letra!" + + '\033[1;34m')
        continue
    
    for letra in letras:
        if letras[letra] == letra_atual:
            print("\033[2;31m" + "---Você já digitou essa letra!---" + '\033[m')
            cancelar = True
            continue
    if cancelar: continue
    letras[attempt] = letra_atual

    for letra in range(0, len(palavra_secreta)):
        if palavra_secreta[letra] == letra_atual:
            Descobertas[letra] = letra_atual
    palavra = ""
    for i in Descobertas:
        palavra += Descobertas[i]
        
    print('\033[1;33m' + f"Palvra:  {palavra}" + "\033[1;34m")

    if palavra == palavra_secreta:
        for i in letras: 
            if i == 0: 
                minhas_letras = letras[i]
                continue
            minhas_letras = minhas_letras + " " + letras[i]
        os.system("cls")
        print("\033[1;34m"+"==============================================================")
        print("")
        print("\033[1;34m"+"                  Você acertou a palavra!!!")
        print("")
        print('\033[1;33m' +  f"                      -----  {palavra} -----")
        print("")
        print("\033[1;34m"+f"                 Letras: {attempt}")
        print('\033[2;30m' + f"               {minhas_letras}" + '\033[m')
        print("")
        print("\033[1;34m"+"==============================================================")
        
        opcao = input("[S] Sair [R] Repetir \n > ").upper()

        if opcao == "S":
            break
        elif opcao == "R":
            finalizou = True

    attempt += 1 
