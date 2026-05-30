import os

def Limpar_Tela():
    os.system('cls' if os.name == 'nt' else 'clear')

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
            Medico = []
            Digitos = "0123456789"
            Letras = "abcdefghijklmnopqrstuvwxyzçãâáéêíôõóú "
            # Incluir um novo médico
            Limpar_Tela()
            print("3 - Incluir um novo médico:")
            print()

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
            print(Medico)
            
            Data_De_Nascimento = ""





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