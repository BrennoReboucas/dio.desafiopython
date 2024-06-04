import time

menu = """

[d] Depositar
[s] Sacar
[l] Saldo
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

while True:
    opcao = input(menu)

    if opcao == "s":

        if saldo > 0: 
            if numero_saques < 3:
                valor = float(input("Informe quanto deseja sacar:\n"))
                if valor > 0 and valor <= saldo:
                    if valor <= 500:
                        numero_saques += 1
                        saldo -= valor
                        extrato += f"Saque realizado no valor de R${valor:.2f}\n"
                        print(f"Saque efetuado com sucesso!\nSeu saldo é de: R${saldo}\n")
                        print(f"Você já utilizou {numero_saques} de 3 saques diários!\n")
                    else:
                        print(f"Saldo não realizado! O valor limite para saque é de R${limite}")

                else:
                    print("Sem saldo suficiente para realizar a operação!\n")
            
            else:
                print("Limite de saque diario batido. Favor, tente novamente amanhã!\n")

        else:
            print("Sem saldo suficiente para realizar a operação!\n")

    elif opcao == "d":
        valor = float(input("Informe o valor do depósito:\n"))
        saldo += valor
        extrato += f"Depósito realizado no valor de R${valor:.2f}\n"
        print(f"Depósito realizado com sucesso!\nSeu saldo é de: R${saldo}\n")
    
    elif opcao =="l":
        print(f"Seu saldo é de R${saldo:.2f}")

    elif opcao == "e":
        print(f"[ Seu extrato ]\n{extrato}")

        time.sleep(5)

    elif opcao == "q":
        break

    else:
        print("Opção inválida!\n")
