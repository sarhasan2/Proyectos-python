#Programa para averiguar si una cadena de texto es Palíndromo

print("BIENVENID@, Consulta si una palabra o frase es Palíndromo \n")

string = input("Ingresa una palabra sin tíldes ni comas: ").lower()

string_2 = "".join(string.split())

nueva = string_2[::-1]
print("Palabra invertida => ", nueva)

if string_2 == nueva:
  print("La palabra es palíndromo")
else:
  print("La palabra no es palíndromo ")

#Desarrollado por sarhasan

#No lata no, la totalidad arada dilato talon a talon
#Anita lava la tina