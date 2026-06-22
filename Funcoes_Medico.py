import os

# =============================================== ARQUIVOS =============================================== #

def Existe_Arquivo(nome):
    if os.path.exists(nome):
        return True
    else:
        return False
    
def Gravar_Dados_Arquivo_Medicos(Medicos):
    arq = open("Medicos.txt","w", encoding="utf-8")
    for i in range(len(Medicos)):
            medico = ""
            Fones = ""
            Email = ""
            
            # junta os emails no arquivo
            for qtd_email in range(len(Medicos[i][6])):
                Email += Medicos[i][6][qtd_email]+"|"
                # junta os telefones no arquivo
            for qtd_tel in range(len(Medicos[i][7])):
                Fones += Medicos[i][7][qtd_tel]+"_"
                
            # Ordem: Médico = [CRM (0), Nome (1), Data de Nascimento (2), Sexo (3), Especialidade (4), Universidade em que se formou (5), E-mails (6), Telefones (7)]

            medico += Medicos[i][0] + ";" + Medicos[i][1] + ";" + Medicos[i][2] + ";" + Medicos[i][3] + ";" + Medicos[i][4] + ";" + Medicos[i][5] + ";" + Email + ";" + Fones
            
            arq.write(medico + "\n")
    arq.close()

def Carregar_Dados_Arquivo_Medicos(Medicos):
    if Existe_Arquivo("Medicos.txt"):

        with open("Medicos.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                partes = linha.split(";")
                emails_brutos = partes[6].split("|")
                telefones_brutos = partes[7].split("_")
                
                emails = []
                for e in emails_brutos:
                    email_limpo = e.strip()
                    if email_limpo:
                        emails.append(email_limpo)
                
                telefones = []
                for t in telefones_brutos:
                    telefone_limpo = t.strip()
                    if telefone_limpo:
                        telefones.append(telefone_limpo)
                
                # Criando a lista do Medico de forma mais direta e limpa
                Medico = [
                    partes[0].strip(),  # CRM
                    partes[1].strip(),  # Nome
                    partes[2].strip(),  # Data de Nascimento
                    partes[3].strip(),  # Sexo
                    partes[4].strip(),  # Especialidade
                    partes[5].strip(),  # Universidade em que se formou
                    emails,             # Lista de e-mails limpa
                    telefones           # Lista de telefones limpa
                ]
                
                # Insere o médico na lista principal
                Medicos.append(Medico)

# ========================================= MENUS DOS MÉDICOS ==================================================

def Menu_Medicos():
    Limpar_Tela()
    print("Menu de Médicos")
    print("1 - Listar todos os médicos")
    print("2 - Listar um médico")
    print("3 - Incluir um novo médico")
    print("4 - Alterar")
    print("5 - Excluir")
    print("6 - Sair")
    i = input("Digite sua escolha: ")
    return i

def Menu_Listar_Um_Medico(Nome_Medico):
    Limpar_Tela()
    print(f"Médico {Nome_Medico} encontrado(a)!")
    print("\nEscolha uma das opções:")
    print(f"1 - Listar todos os dados de {Nome_Medico}")
    print("2 - Listar uma informação do médico")
    print("3 - Sair deste menu") 
    j = input("Digite sua escolha: ")
    return j

def Menu_Listar_Dado_Especifico_Medico(Nome_Medico):
    Limpar_Tela()
    print(f"Escolha um dos dados de {Nome_Medico} que gostaria de visualizar:")
    print("1 - CRM")
    print("2 - Nome")
    print("3 - Data de Nascimento")
    print("4 - Sexo")
    print("5 - Especialidade")
    print("6 - Universidade em que se formou")
    print("7 - E-mails")
    print("8 - Telefones")
    print("9 - Sair deste menu") 
    k = input("Digite sua escolha: ")
    return k

def Menu_Alterar_Dados_Medico(Nome_Medico):
    Limpar_Tela()
    print(f"Escolha um dos dados de {Nome_Medico} que gostaria de alterar:")
    print("1 - Nome")
    print("2 - Data de Nascimento")
    print("3 - Sexo")
    print("4 - Especialidade")
    print("5 - Universidade em que se formou")
    print("6 - E-mails")
    print("7 - Telefones")
    print("8 - Sair deste menu") 
    j = input("Digite sua escolha: ")
    return j

# =============================================== OUTRAS FUNÇÕES =============================================== #

def Limpar_Tela():
    # Limpa o terminal independente do sistema operacional (Windows ou Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

def CRM_Duplicado(Medicos, CRM):

    CRM_Duplicado = False
    for medico_cadastrado in Medicos:
        # O CRM é sempre o primeiro item (índice 0) da lista do médico
        if medico_cadastrado[0] == CRM:
            return True
        
# =============================================== 1 - LISTAR TODOS MÉDICOS =============================================== #

def Listar_Todos_Medicos(Medicos):
    if len(Medicos) == 0:
        print("Nenhum médico cadastrado no sistema!")
        return

    for i in range(len(Medicos)):
        print("____________________________________________________________________________________")
        print()
    # Ordem: Médico = [CRM (0), Nome (1), Data de Nascimento (2), Sexo (3), Especialidade (4), Universidade em que se formou (5), E-mails (6), Telefones (7)]

        for j in range(len(Medicos[i])):

            # ==================== BLOCO 1: INFORMAÇÕES GERAIS ==================== #
            if j == 0: # CRM
                print(f"MÉDICO 0{1+i} - {Medicos[i][1]}")
                # 83 traços + 2 cantos = 85 de largura total
                print("┌" + "─"*32 + " INFO. GERAIS " + "─"*37 + "┐")
                print(f"│ CRM: {Medicos[i][j]:<76} │")

            if j == 1: # NOME
                print(f"│ Nome: {Medicos[i][j]:<75} │")

            if j == 2: # Data_Nascimento
                print(f"│ Data de Nascimento: {Medicos[i][j]:<61} │")

            if j == 3: # Sexo
                print(f"│ Sexo: {Medicos[i][j]:<75} │")

            if j == 4: # Especialidade
                print(f"│ Especialidade: {Medicos[i][j]:<66} │")

            if j == 5: # Universidade em que se formou
                print(f"│ Universidade em que se formou: {Medicos[i][j]:<50} │")
                print("└" + "─"*83 + "┘\n") # Fecha o bloco de Info Gerais


            # ==================== BLOCO 2: CONTATOS ==================== #
            if j == 6: # Email
                print("┌" + "─"*35 + " CONTATOS " + "─"*38 + "┐")
                print(f"│ {'-- E-MAILS --':<81} │")
                for k in range(len(Medicos[i][j])):
                    texto_email = f"{k+1}° Email: {Medicos[i][j][k]}"
                    print(f"│ {texto_email:<81} │")

            if j == 7: # Telefones
                print(f"│ {'':<81} │") 
                print(f"│ {'-- TELEFONES --':<81} │")
                for k in range(len(Medicos[i][j])):
                    texto_tel = f"{k+1}° Telefone: {Medicos[i][j][k]}"
                    print(f"│ {texto_tel:<81} │")
                print("└" + "─"*83 + "┘\n") # Fecha o bloco de Contatos

# =============================================== 2 - LISTAR UM MÉDICO =============================================== #
            
    # ====================BLOCO 1.1 VALIDAR CRM ==================== #

def Validar_CRM(Medicos):
    # Variável de apoio para as validações manuais
    Digitos = "0123456789"

    # Validação do CRM
    CRM_Valido = False
    while not CRM_Valido:
        CRM = input("Digite o CRM do médico (6 dígitos): ")
        
        if len(CRM) != 6:
            print("CRM inválido! Deve conter exatos 6 dígitos! ")
            print()
        else:
            # Percorre toda a string pra garantir que não tenha letras
            Tem_Letra = False
            for i in range(len(CRM)):
                if CRM[i] not in Digitos:
                    Tem_Letra = True

            if Tem_Letra:
                print("CRM inválido! Contém letras e só pode ter números! ")
                print()
            else:
                    return CRM

    # ==================== BLOCO 1.2 BUSCAR MÉDICO ==================== #
def Buscar_Medico(Medicos,CRM):

    for i in range(len(Medicos)):
                    if Medicos[i][0] == CRM:  
                        return True, i
    else:
        return False, None

# ==================== BLOCO 2: LISTAR TODOS OS DADOS DE UM MÉDICO ==================== #
def Listar_Todos_Dados_Medico(Medicos, indice):
    print("_____________________________________________________________________________________")
    print()
    
    CRM =       Medicos[indice][0]
    Nome =      Medicos[indice][1]
    Nasc =      Medicos[indice][2]
    Sexo =      Medicos[indice][3]
    Espec =     Medicos[indice][4]
    Facul =     Medicos[indice][5]
    Emails =    Medicos[indice][6]
    Telefones = Medicos[indice][7]

    # ==================== BLOCO 2.1: INFORMAÇÕES GERAIS ==================== #
    print(f"MÉDICO 0{1+indice} - {Nome}")
    # 83 traços + 2 cantos = 85 de largura total
    print("┌" + "─"*32 + " INFO. GERAIS " + "─"*37 + "┐")
    print(f"│ CRM: {CRM:<76} │")
    print(f"│ Nome: {Nome:<75} │")
    print(f"│ Data de Nascimento: {Nasc:<61} │")
    print(f"│ Sexo: {Sexo:<75} │")
    print(f"│ Especialidade: {Espec:<66} │")
    print(f"│ Universidade em que se formou: {Facul:<50} │")
    print("└" + "─"*83 + "┘\n")

    # ==================== BLOCO 2.2: CONTATOS ==================== #
    print("┌" + "─"*35 + " CONTATOS " + "─"*38 + "┐")
    print(f"│ {'-- TELEFONES --':<81} │")
    
    for k in range(len(Telefones)):
        texto_tel = f"{k+1}° Telefone: {Telefones[k]}"
        print(f"│ {texto_tel:<81} │")
        
    print(f"│ {'':<81} │")
    print(f"│ {'-- E-MAILS --':<81} │")
    
    for k in range(len(Emails)):
        texto_email = f"{k+1}° E-mail: {Emails[k]}"
        print(f"│ {texto_email:<81} │")
        
    print("└" + "─"*83 + "┘\n") 
    
# ==================== BLOCO 3: LISTAR UM DADO ESPECÍFICO DE UM MÉDICO ==================== #

def Listar_Dado_Especifico_Medico(Medicos, indice, dado):
    
    CRM =       Medicos[indice][0]
    Nome =      Medicos[indice][1]
    Nasc =      Medicos[indice][2]
    Sexo =      Medicos[indice][3]
    Espec =     Medicos[indice][4]
    Facul =     Medicos[indice][5]
    Emails =    Medicos[indice][6]
    Telefones = Medicos[indice][7] 

    if dado == "1": # CRM
        Limpar_Tela()
        print(f"\nEXIBINDO DADO DE: {Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ CRM: {CRM:<51} │")
        print("└" + "─"*58 + "┘")
        
    elif dado == "2": # NOME
        Limpar_Tela()
        print(f"\nEXIBINDO DADO DE: {Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Nome: {Nome:<50} │")
        print("└" + "─"*58 + "┘")
        
    elif dado == "3": # Data_Nascimento
        Limpar_Tela()
        print(f"\nEXIBINDO DADO DE: {Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Data de Nascimento: {Nasc:<36} │")
        print("└" + "─"*58 + "┘")
        
    elif dado == "4": # Sexo
        Limpar_Tela()
        print(f"\nEXIBINDO DADO DE: {Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Sexo: {Sexo:<50} │")
        print("└" + "─"*58 + "┘")
        
    elif dado == "5": # Especialidade
        Limpar_Tela()
        print(f"\nEXIBINDO DADO DE: {Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Especialidade: {Espec:<41} │")
        print("└" + "─"*58 + "┘")

    elif dado == "6": # Universidade em que se formou:
        Limpar_Tela()
        print(f"\nEXIBINDO DADO DE: {Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Universidade em que se formou:: {Facul:<24} │")
        print("└" + "─"*58 + "┘")
        
    elif dado == "7": # E-mails
        Limpar_Tela()
        print(f"\nEXIBINDO DADO DE: {Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ {'-- E-MAILS --':<56} │")
        print("├" + "─"*58 + "┤")
        for k in range(len(Emails)):
            texto_email = f"{k+1}° E-mail: {Emails[k]}"
            print(f"│ {texto_email:<56} │")
        print("└" + "─"*58 + "┘")
            
    elif dado == "8": # Telefones
        Limpar_Tela()
        print(f"\nEXIBINDO DADO DE: {Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ {'-- TELEFONES --':<56} │")
        print("├" + "─"*58 + "┤")
        for k in range(len(Telefones)):
            texto_tel = f"{k+1}° Telefone: {Telefones[k]}"
            print(f"│ {texto_tel:<56} │")
        print("└" + "─"*58 + "┘")
            
    elif dado == "9": # Sair deste sub-menu
        return ""
    
    else:
        return "2"

# =============================================== 3 - INSERIR MÉDICOS =============================================== #

def Incluir_Novo_Medico(Medicos):
    Medico = []    
    
    # Variáveis de apoio para as validações manuais
    Digitos = "0123456789"
    Letras = "abcdefghijklmnopqrstuvwxyzçàãâáéêíôõóúü- "

    # Validação do CRM
    Limpar_Tela()
    print("3 - Incluir um novo médico:")
    print()
    CRM_Valido = False
    while not CRM_Valido:
        CRM = input("Digite o CRM do médico (6 dígitos): ")
        
        if len(CRM) != 6:
            print("CRM inválido! Deve conter exatos 6 dígitos! ")
            print()
        else:
            # Percorre toda a string pra garantir que não tenha letras
            Tem_Letra = False
            for i in range(len(CRM)):
                if CRM[i] not in Digitos:
                    Tem_Letra = True

            if Tem_Letra:
                print("CRM inválido! Contém letras e só pode ter números! ")
                print()
            else:

                CRM_Dupli = CRM_Duplicado(Medicos, CRM)
                
                if CRM_Dupli:
                    print("CRM inválido! Este CRM já está cadastrado no sistema!")
                    print()
                else:
                    CRM_Valido = True

    Medico.append(CRM)

    # Validação do nome
    Limpar_Tela()
    print("3 - Incluir um novo médico:")
    print()
    Nome_Valido = False
    while not Nome_Valido:
        Nome = input("Digite o nome do médico: ")
        Nome = Nome.lower()
        
        if len(Nome) == 0:
            print("Nome inválido! O nome não pode estar vazio!")
            print()
        else:
            Caractere_Invalido = False
            So_Espaco = True
            
            # Checa caractere por caractere se tem número ou se é apenas espaço em branco
            for i in range(len(Nome)):
                if Nome[i] not in Letras:
                    Caractere_Invalido = True
                if Nome[i] != " ":
                    So_Espaco = False

            if Caractere_Invalido:
                print("Nome inválido! Use apenas letras e espaços.")
                print()
            elif So_Espaco:
                print("Nome Inválido! O nome não pode ser composto apenas por espaços!")
                print()
            else:
                Nome_Valido = True

    # Padroniza a formatação do nome (Tira espaços extras e deixa iniciais maiúsculas)
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

    # Variáveis para montar a data no final
    Data_De_Nascimento = ""
    Dia_De_Nascimento = ""
    Mes_De_Nascimento = ""
    Ano_De_Nascimento = ""

    # Validação do dia
    Limpar_Tela()
    print("3 - Incluir um novo médico:")
    print()
    Dia_Valido = False
    while not Dia_Valido:
        Dia_De_Nascimento = input("Digite o dia de nascimento do médico (1 a 31): ")
        
        if len(Dia_De_Nascimento) < 1 or len(Dia_De_Nascimento) > 2:
            print("Dia inválido! O dia deve conter 1 ou 2 dígitos!")
            print()
        else:
            Tem_Letra = False
            for i in range(len(Dia_De_Nascimento)):
                if Dia_De_Nascimento[i] not in Digitos:
                    Tem_Letra = True

            if Tem_Letra:
                print("Dia inválido! Contém letras e só pode ter números!")
                print()
            else:
                # Converte pra int pra checar o limite do mês e volta pra string depois
                Dia_De_Nascimento = int(Dia_De_Nascimento)
                if Dia_De_Nascimento < 1 or Dia_De_Nascimento > 31:
                    print("Dia inválido! Os dias vão de 1 a 31!")
                    print()
                else:
                    Dia_De_Nascimento = str(Dia_De_Nascimento)
                    Dia_Valido = True

    # Adiciona o zero na frente se o dia tiver um dígito só
    if len(Dia_De_Nascimento) == 1:
        Dia_De_Nascimento = "0" + Dia_De_Nascimento

    # Validação do mês
    Limpar_Tela()
    print("3 - Incluir um novo médico:")
    print()
    Mes_Valido = False
    while not Mes_Valido:
        Mes_De_Nascimento = input("Digite o mês de nascimento do médico (1 a 12): ")
        
        if len(Mes_De_Nascimento) < 1 or len(Mes_De_Nascimento) > 2:
            print("Mês inválido! O mês deve conter 1 ou 2 dígitos!")
            print()
        else:
            Tem_Letra = False
            for i in range(len(Mes_De_Nascimento)):
                if Mes_De_Nascimento[i] not in Digitos:
                    Tem_Letra = True

            if Tem_Letra:
                print("Mês inválido! Contém letras e só pode ter números!")
                print()
            else:
                Mes_De_Nascimento = int(Mes_De_Nascimento)
                if Mes_De_Nascimento < 1 or Mes_De_Nascimento > 12:
                    print("Mês inválido! Os meses vão de 1 a 12!")
                    print()
                else:
                    Mes_De_Nascimento = str(Mes_De_Nascimento)
                    Mes_Valido = True  

    if len(Mes_De_Nascimento) == 1:
        Mes_De_Nascimento = "0" + Mes_De_Nascimento

    # Validação do ano
    Limpar_Tela()
    print("3 - Incluir um novo médico:")
    print()
    Ano_Valido = False
    while not Ano_Valido:
        Ano_De_Nascimento = input("Digite o ano de nascimento do médico (acima de 1900): ")
        
        # Garante que o ano terá apenas 4 dígitos
        if len(Ano_De_Nascimento) != 4:
            print("Ano inválido! O ano deve conter exatamente 4 dígitos!")
            print()
        else:
            Tem_Letra = False
            for i in range(len(Ano_De_Nascimento)):
                if Ano_De_Nascimento[i] not in Digitos:
                    Tem_Letra = True

            if Tem_Letra:
                print("Ano inválido! Contém letras e só pode ter números!")
                print()
            else:
                Ano_De_Nascimento = int(Ano_De_Nascimento)
                if Ano_De_Nascimento < 1900:
                    print("Ano inválido! Digite um ano acima de 1900!")
                    print()
                else:
                    Ano_De_Nascimento = str(Ano_De_Nascimento)
                    Ano_Valido = True    

    # Concatena a data completa e joga na lista
    Data_De_Nascimento = Dia_De_Nascimento + "/" + Mes_De_Nascimento + "/" + Ano_De_Nascimento
    Medico.append(Data_De_Nascimento)

    # Validação do sexo
    Limpar_Tela()
    print("3 - Incluir um novo médico:")
    print()
    Sexo_Valido = False
    while not Sexo_Valido:
        Sexo_Do_Medico = input("Digite o sexo do médico (M para masculino ou F para feminino): ")
        Sexo_Do_Medico = Sexo_Do_Medico.upper()
        
        # Aceita apenas M ou F
        if Sexo_Do_Medico != "M" and Sexo_Do_Medico != "F":
            print("Sexo inválido! O sexo deve ser apenas M ou F!")
            print()
        else:
            Sexo_Valido = True

    Medico.append(Sexo_Do_Medico)

    # Validação da especialidade
    Limpar_Tela()
    print("3 - Incluir um novo médico:")
    print()
    Especialidade_Valida = False
    while not Especialidade_Valida:
        Especialidade = input("Digite a especialidade do médico: ")
        Especialidade = Especialidade.lower()
        
        if len(Especialidade) == 0:
            print("Especialidade inválida! A especialidade não pode estar vazia!")
            print()
        else:
            Caractere_Invalido = False
            So_Espaco = True

            for i in range(len(Especialidade)):
                if Especialidade[i] not in Letras:
                    Caractere_Invalido = True
                if Especialidade[i] != " ":
                    So_Espaco = False
                    
            if Caractere_Invalido:
                print("Especialidade Inválida! Use apenas letras e espaços.")
                print()
            elif So_Espaco:
                print("Especialidade Inválida! A especialidade não pode ser composto apenas por espaços!")
                print()
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

    # Validação da universidade
    Limpar_Tela()
    print("3 - Incluir um novo médico:")
    print()
    Universidade_Valida = False
    while not Universidade_Valida:
        Universidade = input("Digite a universidade do médico: ")
        Universidade = Universidade.lower()
        
        if len(Universidade) == 0:
            print("Universidade inválida! A universidade não pode estar vazia!")
            print()
        else:
            Caractere_Invalido = False
            So_Espaco = True

            for i in range(len(Universidade)):
                if Universidade[i] not in Letras:
                    Caractere_Invalido = True
                if Universidade[i] != " ":
                    So_Espaco = False

            if Caractere_Invalido:
                print("Universidade Inválida! Use apenas letras e espaços.")
                print()
            elif So_Espaco:
                print("Universidade Inválida! A universidade não pode ser composto apenas por espaços!")
                print()
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
    Limpar_Tela()
    print("3 - Incluir um novo médico:")
    print()
    Emails_Do_Medico = []
    Continuar_Email = True
    
    while Continuar_Email:
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
                print()
            elif Qtd_Arroba != 1:
                print("E-mail inválido! O e-mail deve conter exatamente um @")
                print()
            else:
                # Quebra a string no '@' para validar o nome e o domínio separadamente
                Partes = Email.split("@")
                Usuario = Partes[0]
                Dominio = Partes[1]

                Qtd_Ponto_Dominio = 0
                for i in range(len(Dominio)):
                    if Dominio[i] == ".":
                        Qtd_Ponto_Dominio += 1

                if len(Usuario) < 1:
                    print("E-mail inválido! Deve conter letras ou números antes do @")
                    print()
                elif Qtd_Ponto_Dominio < 1:
                    print("E-mail inválido! O domínio deve conter pelo menos um ponto.")
                    print()
                else:
                    # Verifica se as partes entre os pontos do domínio não estão vazias
                    Partes_Dominio = Dominio.split(".")
                    Dominio_Valido = True
                    
                    for parte in Partes_Dominio:
                        if len(parte) == 0:
                            Dominio_Valido = False

                    if not Dominio_Valido:
                        print("E-mail inválido! Formato incorreto (exemplo válido: a@a.a)")
                    else:
                        Email_Valido = True
                        Emails_Do_Medico.append(Email)
                        print("E-mail adicionado com sucesso!")
                        print()

        # Loop para adicionar mais e-mails caso necessário
        Opcao_Valida = False
        while not Opcao_Valida:
            Opcao = input("Deseja adicionar mais um e-mail? (S para Sim / N para Não): ")
            Opcao = Opcao.upper()
            
            if Opcao == "S":
                Opcao_Valida = True
            elif Opcao == "N":
                Opcao_Valida = True
                Continuar_Email = False
            else:
                print("Opção inválida! Digite apenas S ou N.")
                print()

    Medico.append(Emails_Do_Medico)


    # Validação dos Telefones
    Limpar_Tela()
    print("3 - Incluir um novo médico:")
    print()
    Telefones_Do_Medico = []
    Continuar_Telefone = True
    
    while Continuar_Telefone:
        Telefone_Valido = False
        while not Telefone_Valido:
            Telefone = input("Digite o telefone do médico com DDD (apenas números, 10 ou 11 dígitos): ")
            
            # Limita a 10 (fixo com DDD) ou 11 (celular com DDD) números
            if len(Telefone) < 10 or len(Telefone) > 11:
                print("Telefone inválido! Deve conter 10 ou 11 números (incluindo o DDD).")
                print()
            else:
                Tem_Letra = False
                # Garante que não digitaram letras ou símbolos especiais
                for i in range(len(Telefone)):
                    if Telefone[i] not in Digitos:
                        Tem_Letra = True

                if Tem_Letra:
                    print("Telefone inválido! Digite apenas números.")
                    print()
                else:
                    # Formatação: (XX) XXXXX-XXXX ou (XX) XXXX-XXXX
                    DDD = Telefone[0:2] # Pega os dois primeiros números
                    
                    if len(Telefone) == 10:
                        # Separa o número fixo (4 dígitos + 4 dígitos)
                        Numero_Parte1 = Telefone[2:6]
                        Numero_Parte2 = Telefone[6:10]
                    else:
                        # Separa o número celular (5 dígitos + 4 dígitos)
                        Numero_Parte1 = Telefone[2:7]
                        Numero_Parte2 = Telefone[7:11]
                        
                    # Junta tudo no formato final
                    Telefone_Formatado = "(" + DDD + ") " + Numero_Parte1 + "-" + Numero_Parte2
                    
                    Telefone_Valido = True
                    Telefones_Do_Medico.append(Telefone_Formatado)
                    print("Telefone adicionado com sucesso:", Telefone_Formatado)
                    print()

        # Loop para perguntar se quer adicionar mais um
        Opcao_Valida = False
        while not Opcao_Valida:
            Opcao = input("Deseja adicionar mais um telefone? (S para Sim / N para Não): ")
            Opcao = Opcao.upper()
            
            if Opcao == "S":
                Opcao_Valida = True
            elif Opcao == "N":
                Opcao_Valida = True
                Continuar_Telefone = False
            else:
                print("Opção inválida! Digite apenas S ou N.")
                print()

    Medico.append(Telefones_Do_Medico)

    return Medico

def Main_Funcoes_Medico(Medicos):
    i = ""
    while i != "6":
        i = Menu_Medicos()
        
        if i == "1":
            # ======================================LISTAR TODOS MÉDICOS================================
            Limpar_Tela()
            print("LISTA - MÉDICOS")
            Listar_Todos_Medicos(Medicos)
            input("\nFim da lista! Pressione ENTER para voltar ao menu: ")
            
        elif i == "2":
            # ==================================BUSCAR UM MÉDICO==================================
            Limpar_Tela()
            print("--------Busca de Médicos--------")
            CRM = Validar_CRM(Medicos)
            achou_medico, indice_encontrado = Buscar_Medico(Medicos, CRM)
            
            if achou_medico:
                Nome_Medico = Medicos[indice_encontrado][1]
                j = ""
                while j != "3": 
                    j = Menu_Listar_Um_Medico(Nome_Medico)
                    
                    if j == "1": 
                        Limpar_Tela()
                        Listar_Todos_Dados_Medico(Medicos, indice_encontrado)                       
                        input("\nPressione ENTER para voltar...") 
                        
                    elif j == "2":
                        k = ""
                        while k != "9":
                            k = Menu_Listar_Dado_Especifico_Medico(Nome_Medico)
                            if k in ["1", "2", "3", "4", "5", "6", "7", "8"]:
                                Limpar_Tela()
                                Listar_Dado_Especifico_Medico(Medicos, indice_encontrado, k)             
                                input("\nPressione ENTER para voltar...")
                            elif k == "9":
                                print("Voltando ao Menu...")
                            else:
                                input("\nOpção inválida! Pressione ENTER para tentar novamente...")
                                
                    elif j == "3":
                        print("Voltando ao Menu...")
                    else:
                        input("\nOpção inválida! Pressione ENTER para tentar novamente...")
            else:
                input("\nMédico não encontrado no sistema. Pressione ENTER para voltar...")
                
        elif i == "3":
            # ==================================INSERIR NOVO MÉDICO==================================
            Limpar_Tela()
            Medicos.append(Incluir_Novo_Medico(Medicos))
            input("\nCadastro do médico realizado com sucesso! Pressione ENTER para voltar ao menu: ")
            
        elif i == "4":
            # ==================================ALTERAR DADOS==================================
            Limpar_Tela()
            print("--------Busca de médicos p/ alteração de dados--------")
            CRM = Validar_CRM(Medicos)
            achou_medico, indice_encontrado = Buscar_Medico(Medicos, CRM)

            if achou_medico:
                Nome_Medico = Medicos[indice_encontrado][1]
                j = ""
                while j != "8":
                    j = Menu_Alterar_Dados_Medico(Nome_Medico)
                    if j in ["1", "2", "3", "4", "5", "6", "7"]:
                        Limpar_Tela()
                        # Quando for criar a função de alterar médico, basta chamá-la aqui como no paciente:
                        # Alterar_Dado_Especifico_Medico(Medicos, indice_encontrado, j)
                        print("Função de alterar dado específico do médico em desenvolvimento.")
                        input("\nPressione ENTER para voltar...")
                    elif j == "8":
                        print("Voltando ao Menu...")
                    else:
                        input("\nOpção inválida! Pressione ENTER para tentar novamente...")
            else:
                input("\nMédico não encontrado no sistema. Pressione ENTER para voltar...") 
            
        elif i == "5":
            # ==================================EXCLUIR==================================
            Limpar_Tela()
            print("Função de excluir médico em desenvolvimento.")
            input("\nPressione ENTER para voltar ao menu: ") 
            
        elif i == "6":
            # ==================================SAIR==================================
            Limpar_Tela()
            Gravar_Dados_Arquivo_Medicos(Medicos)
            input("\nDados gravados! Pressione ENTER para voltar ao menu principal: ")
            
        else:
            input("\nOpção inválida! Pressione ENTER para tentar novamente: ")