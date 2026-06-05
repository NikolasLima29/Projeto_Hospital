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
    CRM_Valido = False
    while not CRM_Valido:
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
            else:
                CRM_Valido = True

    Medico.append(CRM)


    # Validação do nome do médico
    Nome_Valido = False
    while not Nome_Valido:
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
            else:
                Nome_Valido = True

    Nome = Nome.title()
    Nome_sem_espacos = Nome.replace(" ", "")
    Nome_formatado = ""

    for i in range(len(Nome_sem_espacos)):
        letra = Nome_sem_espacos[i]
        if letra.isupper() and i > 0:
            Nome_formatado += " " + letra
        else:
            Nome_formatado += letra

    Nome = Nome_formatado
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


    # Validação do sexo
    Sexo_Valido = False
    while not Sexo_Valido:
        Sexo_Do_Medico = input("Digite o sexo do médico (M para masculino ou F para feminino): ")
        Sexo_Do_Medico = Sexo_Do_Medico.upper()
        if Sexo_Do_Medico != "M" and Sexo_Do_Medico != "F":
            print("Sexo inválido! O sexo deve ser apenas M ou F!")
        else:
            Sexo_Valido = True

    Medico.append(Sexo_Do_Medico)


    # Validação da especialidade
    Especialidade_Valida = False
    while not Especialidade_Valida:
        Especialidade = input("Digite a especialidade do médico: ")
        Especialidade = Especialidade.lower()
        if len(Especialidade) == 0:
            print("Especialidade inválida! A especialidade não pode estar vazia!")
        else:
            Tem_Numero = False
            So_Espaco = True

            for i in range(len(Especialidade)):
                if Especialidade[i] not in Letras:
                    Tem_Numero = True
                if Especialidade[i] != " ":
                    So_Espaco = False
            if Tem_Numero:
                print("Especialidade Inválida! Contém números e só pode conter letras!")
            elif So_Espaco:
                print("Especialidade Inválida! A especialidade não pode ser composto apenas por espaços!")
            else:
                Especialidade_Valida = True

    Especialidade = Especialidade.title()
    Especialidade_sem_espacos = Especialidade.replace(" ", "")
    Especialidade_formatada = ""

    for i in range(len(Especialidade_sem_espacos)):
        letra = Especialidade_sem_espacos[i]
        if letra.isupper() and i > 0:
            Especialidade_formatada += " " + letra
        else:
            Especialidade_formatada += letra
            
    Especialidade = Especialidade_formatada
    Medico.append(Especialidade)


    # Validação da universidade em que se formou
    Universidade_Valida = False
    while not Universidade_Valida:
        Universidade = input("Digite a universidade do médico: ")
        Universidade = Universidade.lower()
        if len(Universidade) == 0:
            print("Universidade inválida! A universidade não pode estar vazia!")
        else:
            Tem_Numero = False
            So_Espaco = True

            for i in range(len(Universidade)):
                if Universidade[i] not in Letras:
                    Tem_Numero = True
                if Universidade[i] != " ":
                    So_Espaco = False

            if Tem_Numero:
                print("Universidade Inválida! Contém números e só pode conter letras!")
            elif So_Espaco:
                print("Universidade Inválida! A universidade não pode ser composto apenas por espaços!")
            else:
                Universidade_Valida = True

    Universidade = Universidade.title()
    Universidade_sem_espacos = Universidade.replace(" ", "")
    Universidade_formatada = ""

    for i in range(len(Universidade_sem_espacos)):
        letra = Universidade_sem_espacos[i]
        if letra.isupper() and i > 0:
            Universidade_formatada += " " + letra
        else:
            Universidade_formatada += letra

    Universidade = Universidade_formatada
    Medico.append(Universidade)


    # Validação dos Emails
    Emails_Do_Medico = []
    Continuar = True
    
    while Continuar:
        Email_Valido = False
        while not Email_Valido:
            Email = input("Digite o e-mail do médico: ")
            Email = Email.lower()

            Tem_Espaco = False
            Qtd_Arroba = 0

            # Conta os arrobas e verifica se tem espaços
            for i in range(len(Email)):
                if Email[i] == " ":
                    Tem_Espaco = True
                if Email[i] == "@":
                    Qtd_Arroba += 1

            if Tem_Espaco:
                print("E-mail inválido! O e-mail não pode conter espaços.")
            elif Qtd_Arroba != 1:
                print("E-mail inválido! O e-mail deve conter exatamente um '@'.")
            else:
                # Divide a string no '@'
                Partes = Email.split("@")
                Usuario = Partes[0]
                Dominio = Partes[1]

                Qtd_Ponto_Dominio = 0
                for i in range(len(Dominio)):
                    if Dominio[i] == ".":
                        Qtd_Ponto_Dominio += 1

                if len(Usuario) < 1:
                    print("E-mail inválido! Deve conter letras ou números antes do '@'.")
                elif Qtd_Ponto_Dominio < 1:
                    print("E-mail inválido! O domínio deve conter pelo menos um ponto ('.').")
                else:
                    # Verifica se os pontos não estão vazios (ex: falta do "a" depois do ponto)
                    Partes_Dominio = Dominio.split(".")
                    Dominio_Valido = True
                    
                    for parte in Partes_Dominio:
                        if len(parte) == 0:
                            Dominio_Valido = False

                    if not Dominio_Valido:
                        print("E-mail inválido! Formato incorreto (exemplo válido: a@a.a).")
                    else:
                        Email_Valido = True
                        Emails_Do_Medico.append(Email)
                        print("E-mail adicionado com sucesso!")


        # Pergunta se o usuário quer adicionar outro e-mail
        Opcao_Valida = False
        while not Opcao_Valida:
            Opcao = input("Deseja adicionar mais um e-mail? (S para Sim / N para Não): ")
            Opcao = Opcao.upper()
            
            if Opcao == "S":
                Opcao_Valida = True
            elif Opcao == "N":
                Opcao_Valida = True
                Continuar = False
            else:
                print("Opção inválida! Digite apenas S ou N.")

    Medico.append(Emails_Do_Medico)

    print(Medico)


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