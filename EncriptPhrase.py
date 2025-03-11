alfabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
            "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
            "w", "x", "y", "z"]

def criptografar(frase):
  result = ""
  frase = str.lower(frase)
  for i in frase:
    if i in alfabet:
      result = result + str((alfabet.index(i))) + " "
    else:
      result = result + "("+ i +")" + " "
  return result

frase = input("phrase: ")
print("encripted phrase: " + criptografar(frase))
