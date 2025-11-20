import random

# Desafio 3
# Crie um programa que:
#     - Escolhe um número secreto;
#     - Pede por um chute do usuário;
#     - Indica se o usuário acertou ou não;
#     - Se não acertou, dá uma dica dizendo se o número é maior ou menor do que o número digitado;
#     - Repete isso até 3 vezes

numero_secreto = random.randint(1, 100)

input("Um número inteiro entre zero e 100 foi escolhido. Você tem três chances de acertar este número secreto.")

for numero in range(1,4):
    chute_usuario = input(f"Tentativa {numero}. Digite um número: ")
    try:
        chute = int(chute_usuario)
        
        if(chute > numero_secreto):
            print(f"O número secreto é menor que {chute}")
        elif(chute < numero_secreto):
            print(f"O número secreto é maior que {chute}")
        else:
            print("Parabéns!!! Você acertou o número secreto!");            
    except ValueError:
        print("Número inválido. O número digitado deve ser um número inteiro.")
        
    numero += 1
        
print(f"Suas tentativas acabaram. Número secreto = {numero_secreto}")