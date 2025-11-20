# Desafio 2 
# Crie um código que:
#     - Pede por um nome de usuário e uma senha;
#     - Se ambos forem corretos, exibe a mensagem de sucesso;
#     - Senão, exibe uma mensagem de erro. A mensagem é diferente quando o usuário está incorreto e quando a senha está incorreta
#     - O usuário/senha corretos podem ser definidos como variáveis dentro do próprio código

usuario_correto = "usuario"
senha_correta = "senha"


while(True):
    usuario_digitado = input("Digite o nome do usuário: ")
    senha_digitada = input("Digite a senha do usuário: ")
    
    if(usuario_digitado == usuario_correto and senha_digitada == senha_correta):
        print("Login realizado com sucesso")
        break
    elif(usuario_digitado != usuario_correto and senha_digitada == senha_correta):
        print("Usuário incorreto.")
    elif(usuario_digitado == usuario_correto and senha_digitada != senha_correta):
        print("Senha incorreta.")

