import os

# =============================================== ARQUIVOS =============================================== #

def Existe_Arquivo(nome):
    if os.path.exists(nome):
        return True
    else:
        return False

def Gravar_Dados_Arquivo_Consultas(Consultas):
    arq = open("Consultas.txt", "w", encoding="utf-8")
    for i in range(len(Consultas)):
        consulta = ""
        Medicamentos = ""
        
        # Junta os medicamentos no arquivo
        for qtd_med in range(len(Consultas[i][5])):
            Medicamentos += Consultas[i][5][qtd_med] + "|"
            
        # Ordem: Consulta = [CRM (0), CPF (1), Data (2), Hora (3), Diagnóstico (4), Medicamentos (5)]
        consulta += Consultas[i][0] + ";" + Consultas[i][1] + ";" + Consultas[i][2] + ";" + Consultas[i][3] + ";" + Consultas[i][4] + ";" + Medicamentos
        
        arq.write(consulta + "\n")
    arq.close()

def Carregar_Dados_Arquivo_Consultas(Consultas):
    if Existe_Arquivo("Consultas.txt"):
        with open("Consultas.txt", "r", encoding="utf-8") as arq:
            for linha in arq:
                linha = linha.strip()
                if not linha:
                    continue
                partes = linha.split(";")
                medicamentos_brutos = partes[5].split("|")
                
                medicamentos = []
                for m in medicamentos_brutos:
                    med_limpo = m.strip()
                    if med_limpo:
                        medicamentos.append(med_limpo)
                
                # Criando a lista da Consulta de forma direta
                Consulta = [
                    partes[0].strip(),  # CRM
                    partes[1].strip(),  # CPF
                    partes[2].strip(),  # Data
                    partes[3].strip(),  # Hora
                    partes[4].strip(),  # Diagnóstico
                    medicamentos        # Lista de medicamentos
                ]
                
                # Insere a consulta na lista principal
                Consultas.append(Consulta)

# =============================================== OUTRAS FUNÇÕES =============================================== #

def Limpar_Tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def Consulta_Duplicada(Consultas, CRM, CPF, Data, Hora):
    for c in Consultas:
        if c[0] == CRM and c[1] == CPF and c[2] == Data and c[3] == Hora:
            return True
    return False

def Buscar_Medico_Por_CRM(Medicos, CRM):
    for i in range(len(Medicos)):
        if Medicos[i][0] == CRM:
            return True, Medicos[i][1]
    return False, ""

def Buscar_Paciente_Por_CPF(Pacientes, CPF):
    for i in range(len(Pacientes)):
        if Pacientes[i][0] == CPF:
            return True, Pacientes[i][1]
    return False, ""

# =============================================== 1 - LISTAR TODAS CONSULTAS =============================================== #

def Listar_Todas_Consultas(Consultas):
    if len(Consultas) == 0:
        print("Nenhuma consulta cadastrada no sistema.")
        return

    for i in range(len(Consultas)):
        print("____________________________________________________________________________________")
        print()
        
        print(f"CONSULTA 0{1+i}")
        print("┌" + "─"*32 + " INFO. GERAIS " + "─"*37 + "┐")
        print(f"│ CRM do Médico: {Consultas[i][0]:<66} │")
        print(f"│ CPF do Paciente: {Consultas[i][1]:<64} │")
        print(f"│ Data: {Consultas[i][2]:<75} │")
        print(f"│ Hora: {Consultas[i][3]:<75} │")
        print(f"│ Diagnóstico: {Consultas[i][4]:<68} │")
        print("└" + "─"*83 + "┘\n")

        print("┌" + "─"*34 + " MEDICAMENTOS " + "─"*35 + "┐")
        for k in range(len(Consultas[i][5])):
            texto_med = f"{k+1}° Medicamento: {Consultas[i][5][k]}"
            print(f"│ {texto_med:<81} │")
        print("└" + "─"*83 + "┘\n")

# =============================================== 2 - LISTAR UMA CONSULTA =============================================== #

def Validar_e_Obter_CPF():
    CPF = input("Digite o CPF do paciente (apenas números): ").strip()
    cpf_valido = False
    
    while not cpf_valido:
        digitos = "0123456789"
        contador = len(CPF)
        Tem_Letra = False
        
        for i in range(len(CPF)):
            if CPF[i] not in digitos:
                Tem_Letra = True
                
        if not Tem_Letra and contador == 11:
            cpf_valido = True
        else:
            if Tem_Letra:
                print("CPF inválido. Digite novamente, deve conter apenas números.")
            elif contador != 11:
                print("CPF inválido. Digite novamente, deve conter exatamente 11 números.")
            print()
            CPF = input("Digite o CPF do paciente novamente: ").strip()
            
    return CPF

def Formatar_CPF(CPF):
    CPF = CPF[0:3] + "." + CPF[3:6] + "." + CPF[6:9] + "-" + CPF[9:12]  
    return CPF

def Buscar_Consulta(Consultas, CRM, CPF, Data, Hora):
    for i in range(len(Consultas)):
        if Consultas[i][0] == CRM and Consultas[i][1] == CPF and Consultas[i][2] == Data and Consultas[i][3] == Hora:
            return True, i
    return False, None

def Listar_Todos_Dados_Consulta(Consultas, indice, Medicos, Pacientes):
    print("_____________________________________________________________________________________")
    print()
    
    CRM = Consultas[indice][0]
    CPF = Consultas[indice][1]
    Data = Consultas[indice][2]
    Hora = Consultas[indice][3]
    Diagnostico = Consultas[indice][4]
    Medicamentos = Consultas[indice][5]

    achou_med, nome_med = Buscar_Medico_Por_CRM(Medicos, CRM)
    achou_pac, nome_pac = Buscar_Paciente_Por_CPF(Pacientes, CPF)

    if not achou_med: nome_med = "Médico não encontrado"
    if not achou_pac: nome_pac = "Paciente não encontrado"

    print(f"CONSULTA 0{1+indice}")
    print("┌" + "─"*32 + " INFO. GERAIS " + "─"*37 + "┐")
    print(f"│ Médico: {nome_med} (CRM: {CRM}){' '*max(0, 56 - len(nome_med) - len(CRM))} │")
    print(f"│ Paciente: {nome_pac} (CPF: {CPF}){' '*max(0, 51 - len(nome_pac) - len(CPF))} │")
    print(f"│ Data: {Data:<76} │")
    print(f"│ Hora: {Hora:<76} │")
    print(f"│ Diagnóstico: {Diagnostico:<69} │")
    print("└" + "─"*83 + "┘\n")

    print("┌" + "─"*34 + " MEDICAMENTOS " + "─"*35 + "┐")
    for k in range(len(Medicamentos)):
        texto_med = f"{k+1}° Medicamento: {Medicamentos[k]}"
        print(f"│ {texto_med:<81} │")
    print("└" + "─"*83 + "┘\n") 
    
# =============================================== 3 - INSERIR CONSULTA =============================================== #

def Incluir_Nova_Consulta(Consultas, Medicos, Pacientes):
    Consulta = []    
    Digitos = "0123456789"
    
    Limpar_Tela()
    print("3 - Incluir uma nova consulta:")
    print()
    
    # Validação do CRM
    CRM_Valido = False
    while not CRM_Valido:
        CRM = input("Digite o CRM do médico (6 dígitos): ")
        if len(CRM) != 6:
            print("CRM inválido! Deve conter exatos 6 dígitos! \n")
        else:
            Tem_Letra = False
            for i in range(len(CRM)):
                if CRM[i] not in Digitos:
                    Tem_Letra = True
            if Tem_Letra:
                print("CRM inválido! Contém letras e só pode ter números! \n")
            else:
                achou, nome = Buscar_Medico_Por_CRM(Medicos, CRM)
                if not achou:
                    print("CRM não encontrado no cadastro de médicos! Cadastre o médico primeiro.\n")
                    return None
                else:
                    print(f"Médico selecionado: {nome}\n")
                    CRM_Valido = True

    Consulta.append(CRM)

    # Validação do CPF
    print("-------------------------CPF do Paciente-----------------------------")
    CPF_Formatado = Formatar_CPF(Validar_e_Obter_CPF())
    achou_paciente, nome_paciente = Buscar_Paciente_Por_CPF(Pacientes, CPF_Formatado)
    
    if not achou_paciente:
        print("CPF não encontrado no cadastro de pacientes! Cadastre o paciente primeiro.\n")
        return None
    else:
        print(f"Paciente selecionado: {nome_paciente}\n")
        Consulta.append(CPF_Formatado)

    # Validação da Data
    print("-------------------------Data da Consulta-----------------------------")
    Data_Valida = False
    while not Data_Valida:
        Data = input("Digite a data da consulta (DD/MM/AAAA): ")
        if len(Data) != 10 or Data[2] != '/' or Data[5] != '/':
            print("Formato de data inválido! Use DD/MM/AAAA.\n")
        else:
            Data_Valida = True
    Consulta.append(Data)

    # Validação da Hora
    print("-------------------------Hora da Consulta-----------------------------")
    Hora_Valida = False
    while not Hora_Valida:
        Hora = input("Digite a hora da consulta (HH:MM): ")
        if len(Hora) != 5 or Hora[2] != ':':
            print("Formato de hora inválido! Use HH:MM.\n")
        else:
            Hora_Valida = True
    
    # Checagem de Duplicidade (Chaves Compostas)
    if Consulta_Duplicada(Consultas, CRM, CPF_Formatado, Data, Hora):
        print("ERRO: Já existe uma consulta cadastrada para este Médico e Paciente nesta mesma Data e Hora!\n")
        return None
        
    Consulta.append(Hora)

    # Validação do Diagnóstico
    print("-------------------------Diagnóstico-----------------------------")
    Diag_Valido = False
    while not Diag_Valido:
        Diagnostico = input("Digite o diagnóstico: ")
        if len(Diagnostico.strip()) == 0:
            print("O diagnóstico não pode ficar em branco!\n")
        else:
            Diag_Valido = True
    Consulta.append(Diagnostico.capitalize())

    # Validação dos Medicamentos
    print("-------------------------Medicamentos-----------------------------")
    Medicamentos_Da_Consulta = []
    Continuar_Med = True
    
    while Continuar_Med:
        Med_Valido = False
        while not Med_Valido:
            Medicamento = input("Digite o nome do medicamento receitado: ")
            if len(Medicamento.strip()) == 0:
                print("O medicamento não pode ficar em branco!\n")
            else:
                Medicamentos_Da_Consulta.append(Medicamento.title())
                print("Medicamento adicionado com sucesso!\n")
                Med_Valido = True

        Opcao_Valida = False
        while not Opcao_Valida:
            Opcao = input("Deseja adicionar mais um medicamento? (S para Sim / N para Não): ").upper()
            if Opcao == "S":
                Opcao_Valida = True
            elif Opcao == "N":
                Opcao_Valida = True
                Continuar_Med = False
            else:
                print("Opção inválida! Digite apenas S ou N.\n")

    Consulta.append(Medicamentos_Da_Consulta)
    return Consulta

# =============================================== 4 - ALTERAR CONSULTA =============================================== #

def Alterar_Consulta(Consultas, indice):
    Limpar_Tela()
    CRM = Consultas[indice][0]
    CPF = Consultas[indice][1]
    Data = Consultas[indice][2]
    Hora = Consultas[indice][3]
    
    print("___________________________________________________________________________________")
    print(f"\nALTERANDO CONSULTA: Médico {CRM} | Paciente {CPF} | {Data} às {Hora}")
    print()
    print("O que deseja alterar?")
    print("1 - Diagnóstico")
    print("2 - Medicamentos (Sobrescrever todos)")
    print("3 - Cancelar")
    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        Diag_Valido = False
        while not Diag_Valido:
            Diagnostico = input("Digite o novo diagnóstico: ")
            if len(Diagnostico.strip()) == 0:
                print("O diagnóstico não pode ficar em branco!\n")
            else:
                Consultas[indice][4] = Diagnostico.capitalize()
                Diag_Valido = True
        print("\nDiagnóstico atualizado com sucesso!")
        
    elif escolha == "2":
        Medicamentos_Da_Consulta = []
        Continuar_Med = True
        while Continuar_Med:
            Med_Valido = False
            while not Med_Valido:
                Medicamento = input("Digite o nome do medicamento receitado: ")
                if len(Medicamento.strip()) == 0:
                    print("O medicamento não pode ficar em branco!\n")
                else:
                    Medicamentos_Da_Consulta.append(Medicamento.title())
                    Med_Valido = True

            Opcao_Valida = False
            while not Opcao_Valida:
                Opcao = input("Deseja adicionar mais um medicamento? (S para Sim / N para Não): ").upper()
                if Opcao == "S":
                    Opcao_Valida = True
                elif Opcao == "N":
                    Opcao_Valida = True
                    Continuar_Med = False
                else:
                    print("Opção inválida! Digite apenas S ou N.\n")
        Consultas[indice][5] = Medicamentos_Da_Consulta
        print("\nLista de medicamentos atualizada com sucesso!")

    elif escolha == "3":
        print("\nAlteração cancelada.")
    else:
        print("\nOpção inválida.")
        
    input("\nPressione Enter para continuar... ")

# =============================================== 5 - EXCLUIR CONSULTA =============================================== #

def Excluir_Consulta(Consultas, indice):
    CRM = Consultas[indice][0]
    CPF = Consultas[indice][1]
    Data = Consultas[indice][2]
    
    print("___________________________________________________________________________________")
    print(f"\nVocê está prestes a excluir a consulta do Médico {CRM} com Paciente {CPF} do dia {Data}.")
    confirmacao = input("Tem certeza que deseja EXCLUIR? (S para Sim / N para Não): ").upper()
    
    if confirmacao == "S":
        Consultas.pop(indice)
        print("\nConsulta excluída com sucesso!")
    else:
        print("\nExclusão cancelada.")
    
    input("\nPressione Enter para continuar... ")

# =============================================== MAIN - SUBMENU =============================================== #

def Main_Funcoes_Consulta(Medicos, Pacientes):
    Consultas = []
    Carregar_Dados_Arquivo_Consultas(Consultas)

    i = ""
    while i != "6":
        Limpar_Tela()
        print("Escolha uma das opções abaixo:")
        print()
        print("1 - Listar todas consultas")
        print("2 - Listar uma consulta")
        print("3 - Incluir uma nova consulta")
        print("4 - Alterar consulta")
        print("5 - Excluir consulta")
        print("6 - Sair")
        print()
        i = input("Digite sua escolha: ")
        
        if i == "1":
            Limpar_Tela()
            print("LISTA - CONSULTAS")
            Listar_Todas_Consultas(Consultas)
            input("Fim da lista! Pressione ENTER para voltar ao submenu de consultas: ")
            
        elif i == "2":
            Limpar_Tela()
            print("--------Busca de Consultas--------")
            CRM = input("Digite o CRM do Médico: ")
            CPF = Formatar_CPF(Validar_e_Obter_CPF())
            Data = input("Digite a Data da consulta (DD/MM/AAAA): ")
            Hora = input("Digite a Hora da consulta (HH:MM): ")
            
            achou_consulta, indice_encontrado = Buscar_Consulta(Consultas, CRM, CPF, Data, Hora)
            
            if achou_consulta:
                Limpar_Tela()
                Listar_Todos_Dados_Consulta(Consultas, indice_encontrado, Medicos, Pacientes)
            else:
                print("\nConsulta não encontrada no sistema com os dados informados.")
            
            input("\nPressione ENTER para voltar ao submenu de consultas:")
            
        elif i == "3":
            Nova_Consulta = Incluir_Nova_Consulta(Consultas, Medicos, Pacientes)
            if Nova_Consulta != None:
                Consultas.append(Nova_Consulta)
                print("\nCadastro da consulta realizado com sucesso!")
            input("Pressione ENTER para voltar ao submenu de consultas: ")
            
        elif i == "4":
            Limpar_Tela()
            print("--------Alterar Consulta--------")
            CRM = input("Digite o CRM do Médico: ")
            CPF = Formatar_CPF(Validar_e_Obter_CPF())
            Data = input("Digite a Data da consulta (DD/MM/AAAA): ")
            Hora = input("Digite a Hora da consulta (HH:MM): ")
            
            achou_consulta, indice_encontrado = Buscar_Consulta(Consultas, CRM, CPF, Data, Hora)
            
            if achou_consulta:
                Alterar_Consulta(Consultas, indice_encontrado)
            else:
                print("\nConsulta não encontrada no sistema com os dados informados.")
                input("\nPressione ENTER para voltar ao submenu de consultas:")
                
        elif i == "5":
            Limpar_Tela()
            print("--------Excluir Consulta--------")
            CRM = input("Digite o CRM do Médico: ")
            CPF = Formatar_CPF(Validar_e_Obter_CPF())
            Data = input("Digite a Data da consulta (DD/MM/AAAA): ")
            Hora = input("Digite a Hora da consulta (HH:MM): ")
            
            achou_consulta, indice_encontrado = Buscar_Consulta(Consultas, CRM, CPF, Data, Hora)
            
            if achou_consulta:
                Excluir_Consulta(Consultas, indice_encontrado)
            else:
                print("\nConsulta não encontrada no sistema com os dados informados.")
                input("\nPressione ENTER para voltar ao submenu de consultas:")
                
        elif i == "6":
            Limpar_Tela()
            Gravar_Dados_Arquivo_Consultas(Consultas)
            input("Pressione ENTER para voltar ao menu principal:")
        else:
            input("Opção inválida! Pressione ENTER para voltar ao submenu de consultas: ")