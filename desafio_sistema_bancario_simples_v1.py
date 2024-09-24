class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.extrato = []
        self.limite_saques_diarios = 3
        self.saques_hoje = 0
        self.limite_valor_saque = 500

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. O depósito deve ser um valor positivo.")

    def sacar(self, valor):
        if self.saques_hoje >= self.limite_saques_diarios:
            print("Limite de saques diários atingido.")
        elif valor > self.saldo:
            print("Saldo insuficiente para saque.")
        elif valor > self.limite_valor_saque:
            print(f"Valor de saque excede o limite de R$ {self.limite_valor_saque:.2f} por saque.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.saques_hoje += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")

    def mostrar_extrato(self):
        if not self.extrato:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for operacao in self.extrato:
                print(operacao)
            print(f"Saldo atual: R$ {self.saldo:.2f}")

# Criar a conta bancária
conta = ContaBancaria()

# Exemplo de como continuar com outras operações
while True:
    print("\nEscolha uma operação:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Extrato")
    print("4 - Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        valor = float(input("Informe o valor do depósito: R$ "))
        conta.depositar(valor)
    elif opcao == '2':
        valor = float(input("Informe o valor do saque: R$ "))
        conta.sacar(valor)
    elif opcao == '3':
        conta.mostrar_extrato()
    elif opcao == '4':
        print("Saindo do sistema.")
        break
    else:
        print("Opção inválida. Tente novamente.")
