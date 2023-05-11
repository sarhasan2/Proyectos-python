#Juego piedra, papel o tijera
from random import choice

#options = ("piedra","papel","tijera")
options = ("p","pp","t")

rounds = 1
computer_wins = 0
user_wins = 0

print("Bienvenid@ al juego Piedra, Papel o Tijera \nEl jugador que sume dos puntos gana \n ")
user_name = (input("Hola!!! Ingresa tu nombre => ").title())


while True:

  print("*" * 10)
  print("ROUND",rounds)
  print("*" * 10)
  print("user_wins",user_wins)
  print("computer_wins",computer_wins, "\n")
  
  

  user_option = input("Escribe una opción: 'p' para 'PIEDRA', 'pp' para 'PAPEL' o  't' para 'TIJERA' => ").lower()
  
  if not user_option in options:
    print("Esa opción no es válida")
    continue
  
  rounds += 1

  
  computer_option = choice(options)

  if user_option == "p":
    print("User option => piedra")
  elif user_option == "pp":
    print("User option => papel")
  elif user_option == "t":
    print("User option => tijera")
    
  if computer_option == "p":
    print("Computer option => piedra")
  elif computer_option == "pp":
    print("Computer option => papel")
  elif computer_option == "t":
    print("Computer option => tijera")
  #print('User option => ', user_option)
  #print('Computer option => ', computer_option)
  
  
  if user_option == computer_option:
    print("Es un empate! \n")
  elif user_option == "p":
    if computer_option == "t":
      print("La piedra le gana a la tijera")
      print("El usuario ganó!!! \n")
      user_wins += 1
     
    else:
      print("El papel le gana a la piedra")
      print("Computer ganó!!! \n")
      computer_wins += 1
      
      
  elif user_option == "pp":
    if computer_option == "p":
      print("El papel le gana a la piedra")
      print("El usuario ganó!!! \n")
      user_wins += 1
      
    else:
      print("La tijera le gana al papel")
      print("Computer ganó!!! \n")
      computer_wins += 1
      
      
  elif user_option == "t":
    if computer_option == "pp":
      print("La tijera la gana al papel")
      print("El usuario ganó!!! \n")
      user_wins += 1
     
    else:
      print("La piedra le gana a la tijera")
      print("Computer ganó!!! \n")
      computer_wins += 1
      

  if user_wins == 2:
      print(f"Wuujuu!!! {user_name} GANASTE con {user_wins} puntos!!!")
      break
  
  if computer_wins == 2:
      print(f"Nooo!!! Gana el computador con {computer_wins} puntos!!!")
      break
  
#Desarrollado por sarhasan