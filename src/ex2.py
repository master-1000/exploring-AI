string = input("Digite uma string: ")
palindromo = True

for i in range(len(string)):
    if string[i] != string[-i-1]:
        palindromo = False
        break

if palindromo:
    print("A string é um palíndromo!")
else:
    print("A string não é um palíndromo.")