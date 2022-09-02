print("- - - - - - -BANCO CENTRAL LP- - - - - - -")
nome_cliente = input("Qual seu primeiro nome? ")
espacamento = (30*"-")
juros = 5
saldo = 0
calculo_saque = 0
print(f"Seja bem vindo {nome_cliente}!!")
print(espacamento)
# Essa parte abaixo coloque algumas infomações que eu precisava sobre cadasto do cliente se caso ele fosse se cadastrar

fazer_cadastro = input("Deseja fazer um cadastro no nosso BANCO CENTRA LP? ")
if fazer_cadastro.upper() == 'SIM' or 'S':
    cadastro_nome_comp = input("Por favor, coloque seu nome completo: ")
    cadastro_numero_conta = input("Por favor, digite o numero da sua conta: ")
    print(
        f"Parabéns, você já é um novo cliente do BANCO CENTRAL LP \n Nome da conta:{cadastro_nome_comp}\n Numero da conta:{cadastro_numero_conta}")
    primeiro_dep = input("Deseja fazer um primeiro deposito ? ")
    print(espacamento)
else:
    print("Tenha um ótimo dia!")
    print(espacamento)
if primeiro_dep.upper() == "SIM" or 'S':
    deposito = float(input("Qual valor do deposito? "))
    saldo = deposito
    print(
        f"Nome:{cadastro_nome_comp}\nNumero da conta:{cadastro_numero_conta}\nSaldo:{saldo}")
    print(espacamento)
else:
    print("Tenha um ótimo dia!")
# Parte abaixo coloquei algumas informações sobre saques, que poderia elabora mais coisas
print('Tudo certo com seu cadastro!')
print(espacamento)

saque = input(f"Deseja faze algum saque sobre o seu Saldo:{saldo}? ")
calculo_saque = deposito

if saque.upper() == "SIM" or "S":
    print('Lembrando que nosso saque tem um custo de juros de 5 reias!')
    valor_retira = float(input("Qual valor do seu saque? "))
    print(espacamento)
    if valor_retira > deposito:
        print("Você não pode fazer esse saque, porque o valor é maior que o valor do seu saldo")
        print(espacamento)
    if valor_retira < deposito:
        calculo_saque = float(calculo_saque - valor_retira - juros)
        print(f"Seu saque foi de = {valor_retira}")
        print(f"Agora você tem esse saldo = {calculo_saque}")
        agradecimento = print("Obrigado pro fazer parte da nossa historia!!")
        print(espacamento)
else:
    print("Tenha um ótimo dia!!")
    print(espacamento)

# Essa parte de baixo precisava fazer algo como um outro deposito para o cliente e somar com o resto se ele tiver feito algum saque

deposito_novo = input("Caro cliente, deseja fazer algum deposito? ")
if deposito_novo.upper() == 'SIM' or deposito_novo.upper() == 'S':
    print(espacamento)
    Valor_novo = float(input('Qual valor do deposito? '))
    calculo_dep = float(calculo_saque + Valor_novo)
    print(f"Tudo certo com seu deposito\nseu saldo: {calculo_dep}")
    print(espacamento)
else:
    print('Ok! Agradecemos muito pelo seu cadastro ')
    print(espacamento)
    print(agradecimento)
    print(espacamento)
