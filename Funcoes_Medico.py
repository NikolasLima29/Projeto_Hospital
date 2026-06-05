import os

def Limpar_Tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def Incluir_Novo_Medico():
    Medico = []
    Digitos = "0123456789"
    Letras = "abcdefghijklmnopqrstuvwxyzçãâáéêíôõóú "
    Limpar_Tela()
    print("3 - Incluir um novo médico:")
    print()

    # Validação do CRM do médico
    CRM = ""
    Tem_Letra = False
    while len(CRM) != 6 or Tem_Letra:
        CRM = input("Digite o CRM do médico (6 dígitos): ")
        if len(CRM) != 6:
            print("CRM inválido! Deve conter exatos 6 dígitos! ")
        else:
            Tem_Letra = False
            for i in range(len(CRM)):
                if CRM[i] not in Digitos:
                    Tem_Letra = True
            if Tem_Letra:
                print("CRM inválido! Contém letras e só pode ter números! ")
    Medico.append(CRM)

    # Validação do nome do médico
    Nome = ""
    Tem_Numero = True
    So_Espaco = True
    while len(Nome) == 0 or Tem_Numero or So_Espaco:
        Nome = input("Digite o nome do médico: ")
        Nome = Nome.lower()
        if len(Nome) == 0:
            print("Nome inválido! O nome não pode estar vazio!")
        else:
            Tem_Numero = False
            So_Espaco = True
            for i in range(len(Nome)):
                if Nome[i] not in Letras:
                    Tem_Numero = True
                if Nome[i] != " ":
                    So_Espaco = False
            if Tem_Numero:
                print("Nome Inválido! Contém números e só pode conter letras!")
            elif So_Espaco:
                print("Nome Inválido! O nome não pode ser composto apenas por espaços!")
    Nome = Nome.title()
    Medico.append(Nome)

    # Data de nascimento do médico
    Data_De_Nascimento = ""
    Dia_De_Nascimento = ""
    Mes_De_Nascimento = ""
    Ano_De_Nascimento = ""

    # Validação do dia de nascimento do médico
    Dia_Valido = False
    while not Dia_Valido:
        Dia_De_Nascimento = input("Digite o dia de nascimento do médico (1 a 31): ")
        if len(Dia_De_Nascimento) < 1 or len(Dia_De_Nascimento) > 2:
            print("Dia inválido! O dia deve conter 1 ou 2 dígitos!")
        else:
            Tem_Letra = False
            for i in range(len(Dia_De_Nascimento)):
                if Dia_De_Nascimento[i] not in Digitos:
                    Tem_Letra = True
            if Tem_Letra:
                print("Dia inválido! Contém letras e só pode ter números!")
            else:
                Dia_De_Nascimento = int(Dia_De_Nascimento)
                if Dia_De_Nascimento < 1 or Dia_De_Nascimento > 31:
                    print("Dia inválido! Os dias vão de 1 a 31!")
                else:
                    Dia_De_Nascimento = str(Dia_De_Nascimento)
                    Dia_Valido = True
    if len(Dia_De_Nascimento) == 1:
        Dia_De_Nascimento = "0" + Dia_De_Nascimento

    # Validação do mes de nascimento do médico
    Mes_Valido = False
    while not Mes_Valido:
        Mes_De_Nascimento = input("Digite o mês de nascimento do médico (1 a 12): ")
        if len(Mes_De_Nascimento) < 1 or len(Mes_De_Nascimento) > 2:
            print("Mês inválido! O mês deve conter 1 ou 2 dígitos!")
        else:
            Tem_Letra = False
            for i in range(len(Mes_De_Nascimento)):
                if Mes_De_Nascimento[i] not in Digitos:
                    Tem_Letra = True
            if Tem_Letra:
                print("Mês inválido! Contém letras e só pode ter números!")
            else:
                Mes_De_Nascimento = int(Mes_De_Nascimento)
                if Mes_De_Nascimento < 1 or Mes_De_Nascimento > 12:
                    print("Mês inválido! Os meses vão de 1 a 12!")
                else:
                    Mes_De_Nascimento = str(Mes_De_Nascimento)
                    Mes_Valido = True
                            
    if len(Mes_De_Nascimento) == 1:
        Mes_De_Nascimento = "0" + Mes_De_Nascimento

    # Validação do ano de nascimento do médico
    Ano_Valido = False
    while not Ano_Valido:
        Ano_De_Nascimento = input("Digite o ano de nascimento do médico (acima de 1900): ")
        if len(Ano_De_Nascimento) != 4:
            print("Ano inválido! O ano deve conter exatamente 4 dígitos!")
        else:
            Tem_Letra = False
            for i in range(len(Ano_De_Nascimento)):
                if Ano_De_Nascimento[i] not in Digitos:
                    Tem_Letra = True
            if Tem_Letra:
                print("Ano inválido! Contém letras e só pode ter números!")
            else:
                Ano_De_Nascimento = int(Ano_De_Nascimento)
                if Ano_De_Nascimento < 1900:
                    print("Ano inválido! Digite um ano acima de 1900!")
                else:
                    Ano_De_Nascimento = str(Ano_De_Nascimento)
                    Ano_Valido = True
            
    Data_De_Nascimento = Dia_De_Nascimento + "/" + Mes_De_Nascimento + "/" + Ano_De_Nascimento
    Medico.append(Data_De_Nascimento)

def Main_Funcoes_Medico():
    # Ordem: Médico = (CRM, Nome, Data de Nascimento, Sexo, Especialidade, Universidade em que se formou, E-mails, Telefones) 
    Medicos = []

    # Sub menu médicos
    i = ""
    while i != "6":
        Limpar_Tela()
        print("Escolha uma das opções abaixo:")
        print()
        print("1 - Listar todos os médicos")
        print("2 - Listar um médico")
        print("3 - Incluir um novo médico")
        print("4 - Alterar")
        print("5 - Excluir")
        print("6 - sair")
        print()

        i = input("Digite sua escolha: ")


        while i == "1":

            i = input(
                (
                    "Fim do exercício, digite 1 para refazer o exercício ou enter para voltar ao menu "
                )
            )
        while i == "2":
        
                
            i = input(
                (
                    "Fim do exercício, digite 2 para refazer o exercício ou enter para voltar ao menu "
                )
            )
        
        while i == "3":
            Incluir_Novo_Medico()

            i = input(
                (
                    "Fim do exercício, digite 3 para refazer o exercício ou enter para voltar ao menu "
                )
            )
            
        while i == "4":
    
            
            i = input(
                (
                    "Fim do exercício, digite 4 para refazer o exercício ou enter para voltar ao menu "
                )
            )
            
        while i == "5":
            
            
            i = input(
                (
                    "Fim do exercício, digite 5 para refazer o exercício ou enter para voltar ao menu "
                )
            )   


Main_Funcoes_Medico()