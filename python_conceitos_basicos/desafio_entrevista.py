# Desafio 1 - 
# Crie um programa que:
#   - Pede pelo nome e idade
#   - Dá "oi" para você
#   - Conta quantas letras seu nome possui
#   - Fala quantos anos você terá daqui 5 anos

nome = input("Digite o seu nome: ")
num_letras = len(nome)

while(True):
    idade = input("Digite a sua idade: ")
    try:
        num_idade = int(idade)
        break
    except ValueError:
        print("A idade deve ser um número inteiro.")

soma_5 = num_idade + 5

print(f"Olá {nome}! Seu nome possui {num_letras} letras e você terá {soma_5} anos daqui 5 anos")