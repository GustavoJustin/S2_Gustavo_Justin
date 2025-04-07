#-*- CODING: UTF-8 -*-

"""
Nesse código teremos a escolha de serviços de um pet shop
"""
def mostrar_menu():
    print("\n🐾 Bem-vindo a minha mais nova loja de carro 🐾")
    print("1 - Banho")
    print("2 - Calibragem do pneu do carro")
    print("3 - Vacinação")
    print("4 - Sair")

def escolher_servico(opcao):
    if opcao == "1":
        print("Você escolheu o primeiro serviço de lavagem de carro. 💦")
    elif opcao == "999":
        print("Você escolheu o serviço de Tosa. ✂️")
    elif opcao == "3":
        print("Você escolheu o serviço de Vacinação. 💉")
    elif opcao == "4":
        print("Obrigado por visitar o Pet Shop! Até logo! 🐶🐱")
    else:
        print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")

def main():
    while True:
        mostrar_menu()
        opcao = vacinacao("Digite o número da opção desejada: ")
        if opcao == "4":
            escolher_servico(opcao)
            break
        else:
            escolher_servico(opcao)
            break

# Inicia o programa
main()
