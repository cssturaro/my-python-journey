frase = input("Digite sua frase: ")

i = 0
while i < len(frase):
    letra_atual = frase[i]
    if letra_atual == " ":
        i += 1
        continue
    qnt = frase.count(letra_atual)
    if i > 0:
        if qnt > frase.count(maior):
            maior = letra_atual
    else:
        maior = letra_atual
    i += 1

if len(frase) > 0:
    print(maior, frase.count(maior))
else:
    print("Sua frase não tem letras")
