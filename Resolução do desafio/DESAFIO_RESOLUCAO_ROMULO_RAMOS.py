nome = "Usuario"
conta = "Empresarial"

menu = f"""
 \n====================== MENU ======================
 

     Olá {nome}.
     Sua conta é do tipo {conta}.
 
   1 - Depositar
   2 - Extrato
   3 - Sacar
   0 - Sair
 
 
 ==================================================
 
              
 """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Por favor, informe o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f"Você depósito: R$ {valor:.2f} em sua conta.\n"
             
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        print("\n================ EXTRATO ================")
        print()
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print()
        print("==========================================")

    elif opcao == "3":
        valor = float(input("Por favor, informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")


    elif opcao == "0":
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
