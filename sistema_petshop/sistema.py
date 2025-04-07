#-*- CODING: UTF-8 -*-

"""
Nesse código teremos a escolha de serviços de um pet shop
"""
def mostrar_menu():
    print("1 - Banho")
    print("3 - Vacinação")
    print("4 - Sair")

def escolher_servico(opcao):
    if opcao == "1": 
    elif opcao == "3":
        print("Você escolheu o serviço de Vacinação. 💉")
    elif opcao == "4":
        print("Obrigado por visitar o Pet Shop! Até logo! 🐶🐱")
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")

def main():
    while True:
        mostrar_menu()
        opcao = input("Digite o número da opção desejada: ")
        if opcao == "4":
            escolher_servico(opcao)
            break
        else:
            escolher_servico(opcao)
            break

# Inicia o programa
main()
