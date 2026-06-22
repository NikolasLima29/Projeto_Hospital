import os
import string

def Limpar_Tela():
    os.system('cls' if os.name == 'nt' else 'clear')
# =========================== ARQUIVOS===================================================== 
# Ordem: [CPF(0), Nome(1), Data de Nascimento(2), Sexo(3), Plano de Saúde(4), [E-mails](5), [Telefones](6)]

def Existe_Arquivo(nome):
    if os.path.exists(nome):
        return True
    else:
        return False

def Gravar_Dados_Arquivo_Pacientes(Pacientes):
    arq = open("Pacientes.txt","w", encoding="utf-8")
    for i in range(len(Pacientes)):
            paciente = ""
            fones = ""
            email = ""
            # junta os telefones no arquivo
            for qtd_tel in range(len(Pacientes[i][6])):
                fones += Pacientes[i][6][qtd_tel]+"_"
            # junta os emails no arquivo
            for qtd_email in range(len(Pacientes[i][5])):
                email += Pacientes[i][5][qtd_email]+"|"
            paciente += Pacientes[i][0] + ";" + Pacientes[i][1] + ";" + Pacientes[i][2] + ";" + Pacientes[i][3] + ";" + Pacientes[i][4] + ";" + email + ";" + fones
            arq.write(paciente + "\n")
    arq.close()

def Carregar_Dados_Arquivo_Pacientes(Pacientes):
    if Existe_Arquivo("Pacientes.txt"):
        with open("Pacientes.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                partes = linha.split(";")
                emails_brutos = partes[5].split("|")
                telefones_brutos = partes[6].split("_")
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
                # Criando a lista do paciente de forma mais direta e limpa
                Paciente = [
                    partes[0].strip(),  # CPF
                    partes[1].strip(),  # Nome
                    partes[2].strip(),  # Data de Nascimento
                    partes[3].strip(),  # Sexo
                    partes[4].strip(),  # Plano de Saúde
                    emails,             # Lista de e-mails limpa
                    telefones           # Lista de telefones limpa
                ]
                # Insere o paciente na lista principal
                Pacientes.append(Paciente)
# =========================================MENUS DOS PACIENTES==================================================

def Menu_Pacientes():
    Limpar_Tela()
    print("Menu de Pacientes")
    print("1 - Listar todos pacientes")
    print("2 - Listar um paciente")
    print("3 - Inserir um novo paciente")
    print("4 - Alterar")
    print("5 - Excluir")
    print("6 - Sair")
    i = input("Digite sua escolha: ")
    return i

def Menu_Listar_Um_Paciente(Nome_Paciente):
    Limpar_Tela()
    print(f"Paciente {Nome_Paciente} encontrado(a)!")
    print("\nEscolha uma das opções:")
    print(f"1 - Listar todos os dados de {Nome_Paciente}")
    print("2 - Listar um dado específico")
    print("3 - Sair deste menu") 
    j = input("Digite sua escolha: ").strip()
    return j

def Menu_Listar_Dado_Especifico(Nome_Paciente):
    Limpar_Tela()
    print(f"Escolha um dos dados de {Nome_Paciente} que gostaria de visualizar:")
    print("1 - CPF")
    print("2 - Nome")
    print("3 - Data de Nascimento")
    print("4 - Sexo")
    print("5 - Plano de Saúde")
    print("6 - E-mails")
    print("7 - Telefones")
    print("8 - Sair deste menu") 
    k = input("Digite sua escolha: ").strip()
    return k

def Menu_Alterar_Dados(Nome_Paciente):
    Limpar_Tela()
    print(f"Paciente {Nome_Paciente} encontrado(a)!")
    print()
    print(f"Escolha um dos dados de {Nome_Paciente} que gostaria de alterar:")
    print("1 - Nome")
    print("2 - Data de Nascimento")
    print("3 - Sexo")
    print("4 - Plano de Saúde")
    print("5 - E-mails")
    print("6 - Telefones")
    print("7 - Sair deste menu") 
    j = input("Digite sua escolha: ").strip()
    return j

def Menu_Excluir_Dados(Nome_Paciente):
    Limpar_Tela()
    print(f"Paciente {Nome_Paciente} encontrado(a)!")
    print("\nEscolha uma opção:")
    print("1 - Excluir o paciente")
    print("2 - Excluir um e-mail do paciente")
    print("3 - Excluir um telefone do paciente")
    print("4 - Sair deste menu")
    j = input("Digite sua escolha: ").strip()
    return j
# =============================================== 1 - Listar todos pacientes =============================================
def Listar_Todos_Pacientes(Pacientes):
    for i in range(len(Pacientes)):
        print("___________________________________________________________________________________")
        print()
    # Ordem: [CPF(0), Nome(1), Data de Nascimento(2), Sexo(3), Plano de Saúde(4), [E-mails](5), [Telefones](6)]
        for j in range(len(Pacientes[i])):
            # ==================== BLOCO 1: INFORMAÇÕES GERAIS ====================
            if j == 0: # CPF
                print(f"PACIENTE 0{1+i} - {Pacientes[i][1]}")
                # 83 traços + 2 cantos = 85 de largura total
                print("┌" + "─"*32 + " INFO. GERAIS " + "─"*37 + "┐")
                print(f"│ CPF: {Pacientes[i][j]:<76} │")
            if j == 1: # NOME
                print(f"│ Nome: {Pacientes[i][j]:<75} │")
            if j == 2: # Data_Nascimento
                print(f"│ Data de Nascimento: {Pacientes[i][j]:<61} │")
            if j == 3: # Sexo
                print(f"│ Sexo: {Pacientes[i][j]:<75} │")
            if j == 4: # Plano_saúde
                print(f"│ Plano: {Pacientes[i][j]:<74} │")
                print("└" + "─"*83 + "┘\n") # Fecha o bloco de Info Gerais
            # ==================== BLOCO 2: CONTATOS ====================
            if j == 5: # Email
                print("┌" + "─"*35 + " CONTATOS " + "─"*38 + "┐")
                print(f"│ {'-- E-MAILS --':<81} │")
                for k in range(len(Pacientes[i][j])):
                    texto_email = f"{k+1}° Email: {Pacientes[i][j][k]}"
                    print(f"│ {texto_email:<81} │")
            if j == 6: # Telefones
                print(f"│ {'':<81} │") 
                print(f"│ {'-- TELEFONES --':<81} │")
                for k in range(len(Pacientes[i][j])):
                    texto_tel = f"{k+1}° Telefone: {Pacientes[i][j][k]}"
                    print(f"│ {texto_tel:<81} │")
                print("└" + "─"*83 + "┘\n") # Fecha o bloco de Contatos
# /////////////======================== 2 - LISTAR UM PACIENTE ======================================\\\\\\\\\\\\\
    
# ====================== BLOCO 1: FORMATAR CPF ==================================================
def Formatar_CPF(CPF):
    CPF = CPF[0:3]+"."+CPF[3:6]+"."+CPF[6:9]+"-"+CPF[9:12]  
    return CPF
# ====================== BLOCO 2: VALIDAR CPF e BUSCAR PACIENTE ==================================

    # =========================BLOCO 2.1 VALIDAR CPF ==============================
def Validar_e_Obter_CPF():
    CPF = input("Digite o CPF do paciente: ")
    CPF = CPF.strip()
    cpf_valido = False
    while not cpf_valido:
        dígitos = "0123456789"
        contador = len(CPF)
        Tem_Letra = False
        # 1. Valida o CPF atual (seja o do main ou o do novo input)
        for i in range(len(CPF)):
            if CPF[i] not in dígitos:
                Tem_Letra = True
        # 2. Se estiver correto, muda a flag e o loop vai fechar
        if not Tem_Letra and contador == 11:
            cpf_valido = True
        else:
            # Se encontrou erro, mostra a mensagem e pede um NOVO input aqui dentro
            if Tem_Letra:
                print("CPF inválido. Digite novamente, deve conter apenas números.")
            elif contador != 11:
                print("CPF inválido. Digite novamente, deve conter exatamente 11 números.")
            # Sobrescreve a variável para a próxima volta do while testar o novo valor
            CPF = input("Digite o CPF do paciente novamente: ").strip()
    return CPF
    # ===================== BLOCO 2.2 BUSCAR PACIENTE =================================
def Buscar_Paciente(Pacientes,CPF):
    for i in range(len(Pacientes)):
                    if Pacientes[i][0] == CPF:  
                        return True, i
    else:
        return False, None
# =========================== BLOCO 3: LISTAR TODOS OS DADOS DE UM PACIENTE ===============================
def Listar_Todos_Dados_Paciente(Pacientes, indice):
    print("____________________________________________________________________________________")
    print()
    CPF =       Pacientes[indice][0]
    Nome =      Pacientes[indice][1]
    Nasc =      Pacientes[indice][2]
    Sexo =      Pacientes[indice][3]
    Plano =     Pacientes[indice][4]
    Emails = Pacientes[indice][5]
    Telefones =    Pacientes[indice][6]
    # ==================== BLOCO 3.1: INFORMAÇÕES GERAIS ====================
    print(f"PACIENTE 0{1+indice} - {Nome}")
    # 83 traços + 2 cantos = 85 de largura total
    print("┌" + "─"*32 + " INFO. GERAIS " + "─"*37 + "┐")
    print(f"│ CPF: {CPF:<76} │")
    print(f"│ Nome: {Nome:<75} │")
    print(f"│ Data de Nascimento: {Nasc:<61} │")
    print(f"│ Sexo: {Sexo:<75} │")
    print(f"│ Plano: {Plano:<74} │")
    print("└" + "─"*83 + "┘\n")
    # ==================== BLOCO 3.2: CONTATOS ====================
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
# ====================== BLOCO 4: LISTAR UM DADO ESPECÍFICO DE UM PACIENTE =============================== 
def Listar_Dado_Especifico_Paciente(Pacientes, indice, dado):
    # Suas variáveis declaradas no topo de forma limpa
    CPF =       Pacientes[indice][0]
    Nome =      Pacientes[indice][1]
    Nasc =      Pacientes[indice][2]
    Sexo =      Pacientes[indice][3]
    Plano =     Pacientes[indice][4]
    Emails =    Pacientes[indice][5] 
    Telefones = Pacientes[indice][6] 
    if dado == "1": # CPF
        print("___________________________________________________________________________________")
        print(f"\n{Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ CPF: {CPF:<51} │")
        print("└" + "─"*58 + "┘")
        print("___________________________________________________________________________________")
    elif dado == "2": # NOME
        print("___________________________________________________________________________________")
        print()
        print("┌" + "─"*58 + "┐")
        print(f"│ Nome: {Nome:<50} │")
        print("└" + "─"*58 + "┘")
        print("___________________________________________________________________________________")
    elif dado == "3": # Data_Nascimento
        print("___________________________________________________________________________________")
        print(f"\n{Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Data de Nascimento: {Nasc:<36} │")
        print("└" + "─"*58 + "┘")
        print("___________________________________________________________________________________")
    elif dado == "4": # Sexo
        print("___________________________________________________________________________________")
        print(f"\n{Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Sexo: {Sexo:<50} │")
        print("└" + "─"*58 + "┘")
        print("___________________________________________________________________________________")  
    elif dado == "5": # Plano_saúde
        print("___________________________________________________________________________________")
        print(f"\n{Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Plano de Saúde: {Plano:<40} │")
        print("└" + "─"*58 + "┘")
        print("___________________________________________________________________________________")
    elif dado == "6": # E-mails
        print("___________________________________________________________________________________")
        print(f"\n{Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ {'-- E-MAILS --':<56} │")
        print("├" + "─"*58 + "┤")
        for k in range(len(Emails)):
            texto_email = f"{k+1}° E-mail: {Emails[k]}"
            print(f"│ {texto_email:<56} │")
        print("└" + "─"*58 + "┘")
        print("___________________________________________________________________________________")
    elif dado == "7": # Telefones
        print("___________________________________________________________________________________")
        print(f"\n{Nome}")
        print("┌" + "─"*58 + "┐")
        print(f"│ {'-- TELEFONES --':<56} │")
        print("├" + "─"*58 + "┤")
        for k in range(len(Telefones)):
            texto_tel = f"{k+1}° Telefone: {Telefones[k]}"
            print(f"│ {texto_tel:<56} │")
        print("└" + "─"*58 + "┘")
        print("___________________________________________________________________________________")
    elif dado == "8": # Sair deste sub-menu
        Limpar_Tela()
        return "1"
    return "1"
# ///////////======================= 3 - INSERIR UM NOVO PACIENTE =======================================\\\\\\\\\\\

# ====================BLOCO 1: VERIFICAÇÃO SE JA EXISTE O CPF NO "BANCO DE DADOS"===================
def Verificar_CPF_Ja_Existe(Pacientes):
    CPF_Duplicado = True
    while CPF_Duplicado:
        CPF = Validar_e_Obter_CPF()
        CPF = Formatar_CPF(CPF)
        achou = False
        i = 0
        while i < (len(Pacientes)) and not achou:
            if Pacientes[i][0] == CPF:
                print("Este CPF Já está cadastrado! Digite novamente...") 
                print() 
                CPF_Duplicado = True
                achou = True
            else:
                CPF_Duplicado = False
            i +=1
    if not CPF_Duplicado:
        return CPF
# =========================BLOCO 2: INCLUIR NOVO PACIENTE NO BANCO =================================
def Incluir_Novo_Paciente(Pacientes):
    Paciente = []    
    # Variáveis de apoio para as validações manuais
    Digitos = "0123456789"
    Letras = "abcdefghijklmnopqrstuvwxyzçàãâáéêíôõóúü- "
    # Validação do CPF   
    print("3 - Inserir um novo paciente:")
    print()
    print("-------------------------CPF-----------------------------")
    CPF = Verificar_CPF_Ja_Existe(Pacientes)
    Paciente.append(CPF)
    # Validação do nome
    print()
    print("-------------------------Nome----------------------------")
    Nome_Valido = False
    while not Nome_Valido:
        Nome = input("Digite o nome do paciente: ")
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
    Paciente.append(Nome)
    # Variáveis para montar a data no final
    Data_De_Nascimento = ""
    Dia_De_Nascimento = ""
    Mes_De_Nascimento = ""
    Ano_De_Nascimento = ""
    # Validação do dia
    print()
    print("-------------------------Data de Nascimento----------------------------")
    Dia_Valido = False
    while not Dia_Valido:
        Dia_De_Nascimento = input("Digite o dia de nascimento do paciente (1 a 31): ")
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
    Mes_Valido = False
    while not Mes_Valido:
        Mes_De_Nascimento = input("Digite o mês de nascimento do paciente (1 a 12): ")
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
    Ano_Valido = False
    while not Ano_Valido:
        Ano_De_Nascimento = input("Digite o ano de nascimento do paciente (acima de 1900): ")
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
    Paciente.append(Data_De_Nascimento)
    # Validação do sexo
    print()
    print("-------------------------Sexo----------------------------")
    Sexo_Valido = False
    while not Sexo_Valido:
        Sexo_Do_Paciente = input("Digite o sexo do paciente (M para masculino ou F para feminino): ")
        Sexo_Do_Paciente = Sexo_Do_Paciente.upper()
        # Aceita apenas M ou F
        if Sexo_Do_Paciente != "M" and Sexo_Do_Paciente != "F":
            print("Sexo inválido! O sexo deve ser apenas M ou F!")
            print()
        else:
            Sexo_Valido = True
    Paciente.append(Sexo_Do_Paciente)
    # Validação da Plano_Saude
    print()
    print("-------------------------Plano de Saúde----------------------------")
    Plano_Saude_Valida = False
    while not Plano_Saude_Valida:
        Plano_Saude = input("Digite o Plano de Saúde do paciente: ")
        Plano_Saude = Plano_Saude.lower()
        if len(Plano_Saude) == 0:
            print("Plano de Saúde inválido O Plano de Saúde não pode estar vazia!")
            print()
        else:
            Caractere_Invalido = False
            So_Espaco = True
            for i in range(len(Plano_Saude)):
                if Plano_Saude[i] not in Letras:
                    Caractere_Invalido = True
                if Plano_Saude[i] != " ":
                    So_Espaco = False
            if Caractere_Invalido:
                print("Plano de Saúde Inválido! Use apenas letras e espaços.")
                print()
            elif So_Espaco:
                print("Plano de Saúde Inválida! o Plano de Saúde não pode ser composto apenas por espaços!")
                print()
            else:
                Plano_Saude_Valida = True
    Plano_Saude = Plano_Saude.title()
    Plano_Saude_sem_espacos = Plano_Saude.replace(" ", "")
    Plano_Saude_formatada = ""
    for i in range(len(Plano_Saude_sem_espacos)):
        letra = Plano_Saude_sem_espacos[i]
        if letra.isupper() and i > 0:
            Plano_Saude_formatada += " " + letra
        else:
            Plano_Saude_formatada += letra
    Plano_Saude = Plano_Saude_formatada
    Paciente.append(Plano_Saude)
    # Validação dos Emails
    print()
    print("-------------------------Emails----------------------------")
    Emails_Do_Paciente = []
    Continuar_Email = True
    while Continuar_Email:
        Email_Valido = False
        while not Email_Valido:
            Email = input("Digite o e-mail do paciente: ")
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
                        Emails_Do_Paciente.append(Email)
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
    Paciente.append(Emails_Do_Paciente)
    # Validação dos Telefones
    print()
    print("-------------------------TelefoneS----------------------------")
    Telefones_Do_Paciente = []
    Continuar_Telefone = True
    while Continuar_Telefone:
        Telefone_Valido = False
        while not Telefone_Valido:
            Telefone = input("Digite o telefone do paciente com DDD (apenas números, 10 ou 11 dígitos): ")
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
                    Telefones_Do_Paciente.append(Telefone_Formatado)
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
    Paciente.append(Telefones_Do_Paciente)
    return Paciente
# =============================== 4 - ALTERAR DADOS ESPECÍFICOS =========================================
def Escolher_Email_Especifico(Pacientes, indice):
    print("\nEscolha um e-mail pela posição dele:")
    limite_emails = len(Pacientes[indice][5])
    while True:
        Escolha = input("\nDigite o número da posição do e-mail: ").strip()
        if Escolha.isdigit():
            Escolha = int(Escolha)
            if 1 <= Escolha <= limite_emails:
                return Escolha
            else:
                print(f"Opção inválida! Digite um número entre 1 e {limite_emails}.")
        else:
            print("Opção inválida! Digite apenas um número.")

def Escolher_Telefone_Especifico(Pacientes, indice):
    print("\nEscolha um telefone pela posição dele:")
    limite_telefones = len(Pacientes[indice][6])
    while True:
        Escolha = input("\nDigite o número da posição do telefone: ").strip()
        if Escolha.isdigit():
            Escolha = int(Escolha)
            if 1 <= Escolha <= limite_telefones:
                return Escolha
            else:
                print(f"Opção inválida! Digite um número entre 1 e {limite_telefones}.")
        else:
            print("Opção inválida! Digite apenas um número.")
            
def Alterar_Dado_Especifico_Paciente(Pacientes, indice, dado):
    # Variáveis de apoio para as validações manuais
    Digitos = "0123456789"
    Letras = "abcdefghijklmnopqrstuvwxyzçàãâáéêíôõóúü- "
    #Transformando em int para poder acrescentar +1 na opção que ele escolheu, já que o cpf não é alterável, para não ter que imprimir tudo de novo
    dado = int(dado)
    dado = dado +1
    dado = str(dado)
    Nome =      Pacientes[indice][1]
    Nasc =      Pacientes[indice][2]
    Sexo =      Pacientes[indice][3]
    Plano =     Pacientes[indice][4]
    Emails =    Pacientes[indice][5] 
    Telefones = Pacientes[indice][6] 
    if dado == "2": # NOME
        print("-------------------------Alteração do Nome----------------------------")
        Listar_Dado_Especifico_Paciente(Pacientes,indice, dado)
        print()
        Nome_Valido = False
        while not Nome_Valido:
            Nome = input("Digite o novo nome do paciente: ")
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
        Pacientes[indice][1] = Nome
        Limpar_Tela()
        print(f"NOME ATUALIZADO!")
        Listar_Dado_Especifico_Paciente(Pacientes,indice, dado)
        input("Pressione enter para voltar ao menu...")
        Limpar_Tela()
        return 1
    elif dado == "3": # Data_Nascimento
        print("-------------------------Alteração de Data de Nascimento----------------------------")
        Listar_Dado_Especifico_Paciente(Pacientes,indice, dado)
        print()
        # Variáveis para montar a data no final
        Data_De_Nascimento = ""
        Dia_De_Nascimento = ""
        Mes_De_Nascimento = ""
        Ano_De_Nascimento = ""
        # Validação do dia
        Dia_Valido = False
        while not Dia_Valido:
            Dia_De_Nascimento = input("Digite o dia de nascimento do paciente (1 a 31): ")
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
        Mes_Valido = False
        while not Mes_Valido:
            Mes_De_Nascimento = input("Digite o mês de nascimento do paciente (1 a 12): ")
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
        Ano_Valido = False
        while not Ano_Valido:
            Ano_De_Nascimento = input("Digite o ano de nascimento do paciente (acima de 1900): ")
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
        Pacientes[indice][2] = Data_De_Nascimento
        Limpar_Tela()
        print(f"DATA DE NASCIMENTO ATUALIZADA!")
        Listar_Dado_Especifico_Paciente(Pacientes,indice, dado)
        input("Pressione enter para voltar ao menu...")
        Limpar_Tela()
        return 2
    elif dado == "4": # Sexo
        print("-------------------------Alteração de Sexo----------------------------")
        Listar_Dado_Especifico_Paciente(Pacientes,indice, dado)
        print()
        Sexo_Valido = False
        while not Sexo_Valido:
            Sexo_Do_Paciente = input("Digite o sexo do paciente (M para masculino ou F para feminino): ")
            Sexo_Do_Paciente = Sexo_Do_Paciente.upper()
            # Aceita apenas M ou F
            if Sexo_Do_Paciente != "M" and Sexo_Do_Paciente != "F":
                print("Sexo inválido! O sexo deve ser apenas M ou F!")
                print()
            else:
                Sexo_Valido = True
        Pacientes[indice][3] = Sexo_Do_Paciente
        Limpar_Tela()
        print(f"DATA DE NASCIMENTO ATUALIZADA!")
        Listar_Dado_Especifico_Paciente(Pacientes,indice, dado)
        input("Pressione enter para voltar ao menu...")
        Limpar_Tela()
        return 3
    elif dado == "5": # Plano_saúde
        print("-------------------------Alteração do Plano de Saúde----------------------------")
        Listar_Dado_Especifico_Paciente(Pacientes,indice, dado)
        print()
        Plano_Saude_Valida = False
        while not Plano_Saude_Valida:
            Plano_Saude = input("Digite o Plano de Saúde do paciente: ")
            Plano_Saude = Plano_Saude.lower()           
            if len(Plano_Saude) == 0:
                print("Plano de Saúde inválido O Plano de Saúde não pode estar vazia!")
                print()
            else:
                Caractere_Invalido = False
                So_Espaco = True
                for i in range(len(Plano_Saude)):
                    if Plano_Saude[i] not in Letras:
                        Caractere_Invalido = True
                    if Plano_Saude[i] != " ":
                        So_Espaco = False
                if Caractere_Invalido:
                    print("Plano de Saúde Inválido! Use apenas letras e espaços.")
                    print()
                elif So_Espaco:
                    print("Plano de Saúde Inválida! o Plano de Saúde não pode ser composto apenas por espaços!")
                    print()
                else:
                    Plano_Saude_Valida = True
        Plano_Saude = Plano_Saude.title()
        Plano_Saude_sem_espacos = Plano_Saude.replace(" ", "")
        Plano_Saude_formatada = ""
        for i in range(len(Plano_Saude_sem_espacos)):
            letra = Plano_Saude_sem_espacos[i]
            if letra.isupper() and i > 0:
                Plano_Saude_formatada += " " + letra
            else:
                Plano_Saude_formatada += letra
        Plano_Saude = Plano_Saude_formatada
        Pacientes[indice][4] = Plano_Saude
        Limpar_Tela()
        print(f"DATA DE NASCIMENTO ATUALIZADA!")
        Listar_Dado_Especifico_Paciente(Pacientes,indice, dado)
        input("Pressione enter para voltar ao menu...")
        Limpar_Tela()
        return 4
    elif dado == "6": # E-mails
        print("-------------------------Alteração E-mails----------------------------")
        Listar_Dado_Especifico_Paciente(Pacientes, indice, dado)
        print()
        # Se houver apenas 1 e-mail, evita pedir posição novamente
        if len(Pacientes[indice][5]) == 1:
            Email_Escolhido = 1
            print(f"O email '{Pacientes[indice][5][0]}' é o único na lista de emails do paciente,\nentão ele será o escolhido para alteração.")
            print()
        else:
            Email_Escolhido = Escolher_Email_Especifico(Pacientes, indice)
            Limpar_Tela()
            print(f"O email escolhido para alteração foi: {Pacientes[indice][5][Email_Escolhido - 1]}")
        Email_Valido = False
        print()
        while not Email_Valido:
            Email = input("Digite o novo e-mail do paciente: ")
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
                        Pacientes[indice][5][Email_Escolhido - 1] = Email
        Limpar_Tela()
        print("EMAIL ATUALIZADO!")
        Listar_Dado_Especifico_Paciente(Pacientes, indice, dado)
        input("Pressione enter para voltar ao menu...")
        Limpar_Tela()
        return 6
    elif dado == "7": # Telefones
        print("-------------------------Alteração Telefones----------------------------")
        # Mostra os dados atuais desse campo antes de alterar
        Listar_Dado_Especifico_Paciente(Pacientes, indice, dado)
        print()
        # Se houver apenas 1 telefone, evita pedir posição novamente
        if len(Pacientes[indice][6]) == 1:
            Telefone_Escolhido = 1
            print(f"O telefone '{Pacientes[indice][6][0]}' é o único na lista de telefones do paciente,\nentão ele será o escolhido para alteração.")
            print()
        else:
            # Se houver mais de um, pede para escolher qual telefone alterar
            Telefone_Escolhido = Escolher_Telefone_Especifico(Pacientes, indice)
            Limpar_Tela()
            print(f"O telefone escolhido para alteração foi: {Pacientes[indice][6][Telefone_Escolhido - 1]}")
        # Limpa a tela antes de pedir o novo telefone
        print()
        Telefone_Valido = False
        # Loop para validar o novo telefone digitado
        while not Telefone_Valido:
            # Pede o novo telefone ao usuário
            Telefone = input("Digite o novo telefone do paciente com DDD (apenas números, 10 ou 11 dígitos): ")
            # Verifica se o tamanho está certo
            if len(Telefone) < 10 or len(Telefone) > 11:
                print("Telefone inválido! Deve conter 10 ou 11 números (incluindo o DDD).")
                print()
            else:
                # Verifica se há letras no telefone
                Tem_Letra = False
                for i in range(len(Telefone)):
                    if Telefone[i] not in Digitos:
                        Tem_Letra = True
                if Tem_Letra:
                    print("Telefone inválido! Digite apenas números.")
                    print()
                else:
                    # Separa o DDD e o número
                    DDD = Telefone[0:2]
                    if len(Telefone) == 10:
                        Numero_Parte1 = Telefone[2:6]
                        Numero_Parte2 = Telefone[6:10]
                    else:
                        Numero_Parte1 = Telefone[2:7]
                        Numero_Parte2 = Telefone[7:11]
                    # Formata o telefone como (XX) XXXX-XXXX ou (XX) XXXXX-XXXX
                    Telefone_Formatado = "(" + DDD + ") " + Numero_Parte1 + "-" + Numero_Parte2
                    Telefone_Valido = True
                    # Atualiza o telefone escolhido na lista do paciente
                    Pacientes[indice][6][Telefone_Escolhido - 1] = Telefone_Formatado
        # Limpa a tela e mostra a confirmação
        Limpar_Tela()
        print("TELEFONE ATUALIZADO!")
        # Exibe o dado atualizado
        Listar_Dado_Especifico_Paciente(Pacientes, indice, dado)
        input("Pressione enter para voltar ao menu...")
        Limpar_Tela()
        return 7
    elif dado == "8": # Sair deste sub-menu
        Limpar_Tela()
        return "7"
    else:
        Limpar_Tela()
        print("Opção inválida. Digite um número entre 1 e 7.")
        input("\nPressione Enter para continuar... ") # Adicionado para dar tempo de ler o erro


def Deletar_Dado_Paciente(Pacientes, indice, opcao):
    Nome_Paciente = Pacientes[indice][1]

    if opcao == "1":
        Limpar_Tela()
        print(f"Tem certeza que deseja excluir o paciente {Nome_Paciente}?")
        confirmacao = input("Digite S para confirmar ou N para cancelar: ").strip().upper()

        if confirmacao == "S":
            Limpar_Tela()
            Pacientes.pop(indice)
            print(f"Paciente {Nome_Paciente} excluído com sucesso!")
            input("Pressione enter para voltar ao menu principal...")
            Limpar_Tela()
            return True # O paciente inteiro foi deletado, então avisa o Main para fechar o submenu
        else:
            Limpar_Tela()
            print("Exclusão cancelada.")
            input("Pressione enter para voltar...")
            Limpar_Tela()
            return False # Retorna False para manter o menu aberto

    elif opcao == "2":
        if len(Pacientes[indice][5]) <= 1:
            Limpar_Tela()
            print("Não é possível excluir o e-mail porque o paciente possui apenas um e-mail cadastrado.")
            input("Pressione enter para voltar...")
            Limpar_Tela()
            return False

        Limpar_Tela()
        Listar_Dado_Especifico_Paciente(Pacientes, indice, "6")
        Email_Escolhido = Escolher_Email_Especifico(Pacientes, indice)
        Limpar_Tela()
        print(f"O e-mail escolhido para exclusão foi: {Pacientes[indice][5][Email_Escolhido - 1]}")
        confirmacao = input("Digite S para confirmar ou N para cancelar: ").strip().upper()

        if confirmacao == "S":
            Limpar_Tela()
            Pacientes[indice][5].pop(Email_Escolhido - 1)
            print("E-mail excluído com sucesso!")
            input("Pressione enter para voltar...")
            Limpar_Tela()
            return False # Retorna False para manter o menu aberto
        else:
            Limpar_Tela()
            print("Exclusão cancelada.")
            input("Pressione enter para voltar...")
            Limpar_Tela()
            return False

    elif opcao == "3":
        if len(Pacientes[indice][6]) <= 1:
            Limpar_Tela()
            print("Não é possível excluir o telefone porque o paciente possui apenas um telefone cadastrado.")
            input("Pressione enter para voltar...")
            Limpar_Tela()
            return False

        Limpar_Tela()
        Listar_Dado_Especifico_Paciente(Pacientes, indice, "7")
        Telefone_Escolhido = Escolher_Telefone_Especifico(Pacientes, indice)
        Limpar_Tela()
        print(f"O telefone escolhido para exclusão foi: {Pacientes[indice][6][Telefone_Escolhido - 1]}")
        confirmacao = input("Digite S para confirmar ou N para cancelar: ").strip().upper()

        if confirmacao == "S":
            Limpar_Tela()
            Pacientes[indice][6].pop(Telefone_Escolhido - 1)
            print("Telefone excluído com sucesso!")
            input("Pressione enter para voltar...")
            Limpar_Tela()
            return False # Retorna False para manter o menu aberto
        else:
            Limpar_Tela()
            print("Exclusão cancelada.")
            input("Pressione enter para voltar...")
            Limpar_Tela()
            return False

    else:
        Limpar_Tela()
        print("Opção inválida.")
        input("Pressione enter para voltar...")
        Limpar_Tela()
        return False


def Main_Funcoes_Pacientes(Pacientes):
    i = ""
    while i != "6":
        i = Menu_Pacientes()
        if i == "1":
            # ======================================LISTAR TODOS PACIENTES================================
            Limpar_Tela()
            print("LISTA - PACIENTES")
            Listar_Todos_Pacientes(Pacientes)
            input("\nFim da lista. Pressione ENTER para voltar ao menu: ")
            
        elif i == "2":
            # ==================================BUSCAR UM PACIENTE==================================
            Limpar_Tela()
            print("--------Busca de Pacientes--------")
            CPF = Validar_e_Obter_CPF()
            CPF = Formatar_CPF(CPF)
            achou_paciente, indice_encontrado = Buscar_Paciente(Pacientes, CPF)

            if achou_paciente:
                Nome_Paciente = Pacientes[indice_encontrado][1]
                j = ""
                while j != "3": 
                    j = Menu_Listar_Um_Paciente(Nome_Paciente)
                    if j == "1": 
                        Limpar_Tela()
                        Listar_Todos_Dados_Paciente(Pacientes, indice_encontrado)
                        input("\nPressione ENTER para voltar...") 
                    elif j == "2":
                        k = ""
                        while k != "8":
                            k = Menu_Listar_Dado_Especifico(Nome_Paciente)
                            if k in ["1", "2", "3", "4", "5", "6", "7"]:
                                Limpar_Tela()
                                Listar_Dado_Especifico_Paciente(Pacientes, indice_encontrado, k)
                                input("\nPressione ENTER para voltar...")
                            elif k != "8":
                                input("\nOpção inválida! Pressione ENTER para tentar novamente...")
                    elif j != "3":
                        input("\nOpção inválida! Pressione ENTER para tentar novamente...")
            else:
                input("\nPaciente não encontrado no sistema. Pressione ENTER para voltar...") 
                
        elif i == "3":
            # ==================================INSERIR NOVO PACIENTE==================================
            Limpar_Tela()
            Pacientes.append(Incluir_Novo_Paciente(Pacientes))
            input("\nPaciente incluído com sucesso! Pressione ENTER para voltar ao menu: ")
            
        elif i == "4":
            # ==================================ALTERAR DADOS==================================
            Limpar_Tela()
            print("--------Busca de pacientes p/ alteração de dados--------")
            CPF = Validar_e_Obter_CPF()
            CPF = Formatar_CPF(CPF)
            achou_paciente, indice_encontrado = Buscar_Paciente(Pacientes, CPF)

            if achou_paciente:
                Nome_Paciente = Pacientes[indice_encontrado][1]
                j = ""
                while j != "7":
                    j = Menu_Alterar_Dados(Nome_Paciente)
                    if j in ["1", "2", "3", "4", "5", "6"]:
                        Limpar_Tela()
                        Alterar_Dado_Especifico_Paciente(Pacientes, indice_encontrado, j)
                    elif j != "7":
                        input("\nOpção inválida! Pressione ENTER para tentar novamente...")
            else:
                input("\nPaciente não encontrado no sistema. Pressione ENTER para voltar...") 
                
        elif i == "5":
            # ==================================EXCLUIR==================================
            Limpar_Tela()
            print("--------Busca de pacientes para exclusão--------")
            CPF = Validar_e_Obter_CPF()
            CPF = Formatar_CPF(CPF)
            achou_paciente, indice_encontrado = Buscar_Paciente(Pacientes, CPF)
            
            if achou_paciente:
                Nome_Paciente = Pacientes[indice_encontrado][1]
                j = ""
                continuar_exclusao = True

                while continuar_exclusao and j != "4":
                    j = Menu_Excluir_Dados(Nome_Paciente)

                    if j in ["1", "2", "3"]:
                        paciente_foi_deletado = Deletar_Dado_Paciente(Pacientes, indice_encontrado, j)
                        if paciente_foi_deletado:
                            continuar_exclusao = False
                    elif j != "4":
                        input("\nOpção inválida! Pressione ENTER para tentar novamente...")
            else:
                input("\nPaciente não encontrado no sistema. Pressione ENTER para voltar...")
                
        elif i == "6":
            # ==================================SAIR==================================
            Limpar_Tela()
            Gravar_Dados_Arquivo_Pacientes(Pacientes)
            input("\nDados gravados! Pressione ENTER para voltar ao menu principal: ")
            
        else:
            input("\nOpção inválida! Pressione ENTER para tentar novamente: ")