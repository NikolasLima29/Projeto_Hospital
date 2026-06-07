import os
import string

def Limpar_Tela():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    
# Ordem: [CPF(0), Nome(1), Data de Nascimento(2), Sexo(3), Plano de Saúde(4), [E-mails](5), [Telefones](6)]
# =========================== ARQUIVOS===================================================== 

def Existe_Arquivo(nome):
    import os
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
            
    # =========================================================//================================================= 
    
    
    
    
    
# =============================================== 2 - Listar um paciente =============================================

# =============================== BLOCO 1: FORMATAR =============================================
def Formatar_CPF(CPF):
    CPF = CPF[0:3]+"."+CPF[3:6]+"."+CPF[6:9]+"-"+CPF[9:12]  
    return CPF
            
# ============================== BLOCO 2: VALIDAR CPF =============================================
def Validar_e_Obter_CPF(CPF):
    # O .strip() limpa os espaços do CPF que veio do main
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
  
# =============================== BLOCO 3: LISTAR TODOS OS DADOS DE UM PACIENTE =============================================  
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
    
# =============================== BLOCO 4: LISTAR UM DADO ESPECÍFICO DE UM PACIENTE =============================================  
def Listar_Dado_Especifico_Paciente(Pacientes, indice, dado):
    Nome_Paciente = Pacientes[indice][1]
    
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
        print(f"\nEXIBINDO DADO DE: {Nome_Paciente}")
        print("┌" + "─"*58 + "┐")
        print(f"│ CPF: {CPF:<51} │")
        print("└" + "─"*58 + "┘")
        
    elif dado == "2": # NOME
        print("___________________________________________________________________________________")
        print(f"\nEXIBINDO DADO DE: {Nome_Paciente}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Nome: {Nome:<50} │")
        print("└" + "─"*58 + "┘")
        
    elif dado == "3": # Data_Nascimento
        print("___________________________________________________________________________________")
        print(f"\nEXIBINDO DADO DE: {Nome_Paciente}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Data de Nascimento: {Nasc:<36} │")
        print("└" + "─"*58 + "┘")
        
    elif dado == "4": # Sexo
        print("___________________________________________________________________________________")
        print(f"\nEXIBINDO DADO DE: {Nome_Paciente}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Sexo: {Sexo:<50} │")
        print("└" + "─"*58 + "┘")
        
    elif dado == "5": # Plano_saúde
        print("___________________________________________________________________________________")
        print(f"\nEXIBINDO DADO DE: {Nome_Paciente}")
        print("┌" + "─"*58 + "┐")
        print(f"│ Plano de Saúde: {Plano:<40} │")
        print("└" + "─"*58 + "┘")
        
    elif dado == "6": # E-mails
        print("___________________________________________________________________________________")
        print(f"\nEXIBINDO DADO DE: {Nome_Paciente}")
        print("┌" + "─"*58 + "┐")
        print(f"│ {'-- E-MAILS --':<56} │")
        print("├" + "─"*58 + "┤")
        for k in range(len(Emails)):
            texto_email = f"{k+1}° E-mail: {Emails[k]}"
            print(f"│ {texto_email:<56} │")
        print("└" + "─"*58 + "┘")
            
    elif dado == "7": # Telefones
        print("___________________________________________________________________________________")
        print(f"\nEXIBINDO DADO DE: {Nome_Paciente}")
        print("┌" + "─"*58 + "┐")
        print(f"│ {'-- TELEFONES --':<56} │")
        print("├" + "─"*58 + "┤")
        for k in range(len(Telefones)):
            texto_tel = f"{k+1}° Telefone: {Telefones[k]}"
            print(f"│ {texto_tel:<56} │")
        print("└" + "─"*58 + "┘")
            
    elif dado == "8": # Sair deste sub-menu
        Limpar_Tela()
        return "1"
    
    else:
        Limpar_Tela()
        print("Opção inválida. Digite um número entre 1 e 8.")
        input("\nPressione Enter para continuar... ") # Adicionado para dar tempo de ler o erro
        Limpar_Tela()
        return "2"

    input("\nPressione Enter para continuar... ")
    Limpar_Tela()
    return "2"
     







def Main_Funcoes_Pacientes():
# Ordem: [CPF(0), Nome(1), Data de Nascimento(2), Sexo(3), Plano de Saúde(4), [E-mails](5), [Telefones](6)]
    Pacientes = []


    Carregar_Dados_Arquivo_Pacientes(Pacientes)
    i = ""
    while i != "6":
        print("Escolha uma das opções:")
        print("1 - Listar todos pacientes")
        print("2 - Listar um paciente")
        print("3 - Inserir paciente")
        print("4 - Alterar")
        print("5 - Excluir")
        print("6 - Sair")
        i = input("Digite sua escolha: ")
        print()
        while i == "1" :
            # ======================================LISTAR TODOS PACIENTES================================
            Limpar_Tela()
            print("LISTA - PACIENTES")
            Listar_Todos_Pacientes(Pacientes)
            # ==================================================================================================
            i = input(
                (
                    "Fim da lista, digite 1 para rever a lista de todos os pacientes ou enter para voltar ao menu: "
                )
            )
            Limpar_Tela()
            
        while i == "2":
            
            # ==================================BUSCAR UM PACIENTE==================================
            Limpar_Tela()
           
            CPF = input("Digite o CPF do paciente que deseja visualizar: ").strip() 
            
            CPF = Validar_e_Obter_CPF(CPF)
                
            CPF = Formatar_CPF(CPF)
            
            achou_paciente = False
            indice_encontrado = -1
            j = "" #váriavel p/ escolher a opção dentro de listar um

            # Loop p/ descobrir quem é o paciente
            for i in range(len(Pacientes)):
                if Pacientes[i][0] == CPF:  
                    achou_paciente = True
                    indice_encontrado = i  

            #Sub-menu para visualizar info sobre o paciente
            if achou_paciente:
                
                Nome_Paciente = Pacientes[indice_encontrado][1]
                
                
                
                print(f"\nPaciente {Nome_Paciente} encontrado/a!")
                
                while j != "3": # Mudou para string
                    print("\nEscolha uma das opções:")
                    print(f"1 - Listar todos os dados de {Nome_Paciente}")
                    print("2 - Listar um paciente")
                    print("3 - Sair deste menu") 
                    
                    
                    j = input("Digite sua escolha : ").strip()
                    
                    while j == "1": 
                        Limpar_Tela()
                        Listar_Todos_Dados_Paciente(Pacientes, indice_encontrado)
                        
                        
                        j = input("Pressione enter para voltar...") 
                        Limpar_Tela()
                        
                    while j == "2":
                        print(f"\nEscolha um dos dados de {Nome_Paciente} que gostaria de vizualizar :")
                        print("1 - CPF")
                        print("2 - Nome")
                        print("3 - Data de Nascimento")
                        print("4 - Sexo")
                        print("5 - Plano de Saúde")
                        print("6 - E-mails")
                        print("7 - Telefones")
                        print("8 - Sair deste menu") 
                        k = input("Digite sua escolha : ")
                        
                       
                        j = Listar_Dado_Especifico_Paciente(Pacientes, indice_encontrado, k)
                                                
                  
                    if j != "1" and j != "2" and j != "3" and j != "":
                        print("Opção inválida. Digite um número entre 1 e 3.")
                        
                        
                        
                        
                    
            else:
                print("Paciente não encontrado no sistema.")
                j = input("Pressione enter para voltar...") 
                
           
            if j == "1" or j == "2" or j == "3": 
                i = "1"
            else:
                i = "1"
                
          
            Limpar_Tela()
            
        
        while i == "3":
            
               
               
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
    Gravar_Dados_Arquivo_Pacientes(Pacientes)

Main_Funcoes_Pacientes()