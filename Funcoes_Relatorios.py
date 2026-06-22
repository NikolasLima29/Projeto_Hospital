import os
from datetime import datetime

# =============================================== ARQUIVOS =============================================== #

def Limpar_Tela():
    # Limpa o terminal independente do sistema operacional (Windows ou Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')

# =============================================== FUNÇÕES AUXILIARES =============================================== #

def Menu():
    Limpar_Tela()
    print("Menu Relatórios")
    print("1 - Médicos por especialidade")
    print("2 - Pacientes menores de X anos")
    print("3 - Consultas dos últimos X dias")
    print("4 - Sair")
    print()
    i = input("Digite sua escolha: ")
    return i

def Gravar_Arquivo_Relatorio(nome_arquivo, linhas):
    with open(nome_arquivo, "w", encoding="utf-8") as arq:
        for linha in linhas:
            arq.write(linha + "\n")

# Ordem: Médico = [CRM (0), Nome (1), Data de Nascimento (2), Sexo (3), Especialidade (4), Universidade em que se formou (5), E-mails (6), Telefones (7)]
# Ordem: PAcientes = [CPF(0), Nome(1), Data de Nascimento(2), Sexo(3), Plano de Saúde(4), [E-mails](5), [Telefones](6)]
# Ordem: Consulta = [CRM (0), CPF (1), Data (2), Hora (3), Diagnóstico (4), Medicamentos (5)]

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

def Calcular_Idade(data_nascimento):
    data_atual = datetime.now()
    data_nasc = datetime.strptime(data_nascimento, "%d/%m/%Y")

    idade = data_atual.year - data_nasc.year

    if (data_atual.month, data_atual.day) < (data_nasc.month, data_nasc.day):
        idade -= 1

    return idade

# =============================================== 1 - RELATÓRIO: MÉDICOS POR ESPECIALIDADE =============================================== #

def Relatorio_Medicos_Por_Especialidade(Medicos):
    Limpar_Tela()
    print("-------------------------Relatório de Médicos por Especialidade----------------------------")
    print()
    especialidade = input("Digite a especialidade desejada: ").strip()

    resultados = []
    linhas_relatorio = []

    for medico in Medicos:
        if medico[4].lower() == especialidade.lower():
            resultados.append(medico)

    if len(resultados) == 0:
        print("Nenhum médico encontrado para essa especialidade.")
        input("Pressione enter para voltar ao menu de relatórios...")
        return

    print()
    Limpar_Tela()
    print(f"=============== Relatório: Médicos por especialidade ({especialidade}) ===============")
    print("Médico/s encontrados:")
    print()

    linhas_relatorio.append(f"=============== Relatório: Médicos por especialidade ({especialidade}) ===============")
    linhas_relatorio.append("")

    for medico in resultados:
        CRM = medico[0]
        Nome = medico[1]
        Data_Nasc = medico[2]
        Sexo = medico[3]
        Especialidade = medico[4]
        Universidade = medico[5]
        Emails = medico[6]
        Telefones = medico[7]

        
        print(f"Médico: {Nome} ({Especialidade})")
        print(f"┌{'─'*32} INFO. GERAIS {'─'*37}┐")
        print(f"│ {'CRM: ' + CRM:<81} │")
        print(f"│ {'Nome: ' + Nome:<81} │")
        print(f"│ {'Data de Nascimento: ' + Data_Nasc:<81} │")
        print(f"│ {'Sexo: ' + Sexo:<81} │")
        print(f"│ {'Especialidade: ' + Especialidade:<81} │")
        print(f"│ {'Universidade em que se formou: ' + Universidade:<81} │")
        print(f"└{'─'*83}┘")
        print()
        print(f"┌{'─'*35} CONTATOS {'─'*38}┐")
        print(f"│ {'-- TELEFONES --':<81} │")
        for telefone in Telefones:
            print(f"│ {'• ' + telefone:<81} │")
        print(f"│ {'':<81} │")
        print(f"│ {'-- E-MAILS --':<81} │")
        for email in Emails:
            print(f"│ {'• ' + email:<81} │")
        print(f"└{'─'*83}┘")
        print()
        print("=" * 85)
        print()

        linhas_relatorio.append("")
        linhas_relatorio.append(f"Médico: {Nome} ({Especialidade})")
        linhas_relatorio.append(f"┌{'─'*32} INFO. GERAIS {'─'*37}┐")
        linhas_relatorio.append(f"│ {'CRM: ' + CRM:<81} │")
        linhas_relatorio.append(f"│ {'Nome: ' + Nome:<81} │")
        linhas_relatorio.append(f"│ {'Data de Nascimento: ' + Data_Nasc:<81} │")
        linhas_relatorio.append(f"│ {'Sexo: ' + Sexo:<81} │")
        linhas_relatorio.append(f"│ {'Especialidade: ' + Especialidade:<81} │")
        linhas_relatorio.append(f"│ {'Universidade em que se formou: ' + Universidade:<81} │")
        linhas_relatorio.append(f"└{'─'*83}┘")
        linhas_relatorio.append("")
        linhas_relatorio.append(f"┌{'─'*35} CONTATOS {'─'*38}┐")
        linhas_relatorio.append(f"│ {'-- TELEFONES --':<81} │")
        for telefone in Telefones:
            linhas_relatorio.append(f"│ {'• ' + telefone:<81} │")
        linhas_relatorio.append(f"│ {'':<81} │")
        linhas_relatorio.append(f"│ {'-- E-MAILS --':<81} │")
        for email in Emails:
            linhas_relatorio.append(f"│ {'• ' + email:<81} │")
        linhas_relatorio.append(f"└{'─'*83}┘")
        linhas_relatorio.append("")
        linhas_relatorio.append("=" * 85)
        linhas_relatorio.append("")

    Gravar_Arquivo_Relatorio("Relatorio_Medicos.txt", linhas_relatorio)
    print("Relatório salvo no arquivo Relatorio_Medicos.txt")
    input("Pressione enter para voltar ao menu de relatórios...")

# =============================================== 2 - RELATÓRIO: PACIENTES MENORES DE X ANOS =============================================== #

def Relatorio_Pacientes_Menores_De_X_Anos(Pacientes):
    Limpar_Tela()
    print("-------------------------Relatório de Pacientes Menores de X Anos----------------------------")
    print()

    idade_valida = False
    while not idade_valida:
        idade_digitada = input("Digite a idade limite (X): ").strip()
        if idade_digitada.isdigit():
            idade_valida = True
            idade_limite = int(idade_digitada)
        else:
            print("Valor inválido! Digite apenas números.")
            print()

    resultados = []
    linhas_relatorio = []

    for paciente in Pacientes:
        idade = Calcular_Idade(paciente[2])
        if idade < idade_limite:
            resultados.append(paciente)

    if len(resultados) == 0:
        print(f"Nenhum paciente encontrado com idade menor que {idade_limite} anos.")
        input("Pressione enter para voltar ao menu de relatórios...")
        return

    print()
    Limpar_Tela()
    print(f"=============== Relatório: Pacientes menores de {idade_limite} anos ===============")
    print()
    print("Pacientes encontrados:")

    linhas_relatorio.append(f"=============== Relatório: Pacientes menores de {idade_limite} anos ===============")
    linhas_relatorio.append("")

    for paciente in resultados:
        CPF = paciente[0]
        Nome = paciente[1]
        Data_Nasc = paciente[2]
        Sexo = paciente[3]
        Plano = paciente[4]
        Emails = paciente[5]
        Telefones = paciente[6]

        
        idade = Calcular_Idade(Data_Nasc)
        print()
        print(f"Paciente: {Nome} ({idade} anos)")
        print(f"┌{'─'*32} PACIENTE {'─'*41}┐")
        print(f"│ {'CPF: ' + CPF:<81} │")
        print(f"│ {'Nome: ' + Nome:<81} │")
        print(f"│ {'Data de Nascimento: ' + Data_Nasc:<81} │")
        print(f"│ {'Sexo: ' + Sexo:<81} │")
        print(f"│ {'Plano de Saúde: ' + Plano:<81} │")
        print(f"└{'─'*83}┘")
        print()
        print(f"┌{'─'*35} CONTATOS {'─'*38}┐")
        print(f"│ {'-- TELEFONES --':<81} │")
        for telefone in Telefones:
            print(f"│ {'• ' + telefone:<81} │")
        print(f"│ {'':<81} │")
        print(f"│ {'-- E-MAILS --':<81} │")
        for email in Emails:
            print(f"│ {'• ' + email:<81} │")
        print(f"└{'─'*83}┘")
        print()
        print("=" * 85)
        print()

        linhas_relatorio.append("")
        linhas_relatorio.append(f"Paciente: {Nome} ({idade} anos)")
        linhas_relatorio.append(f"┌{'─'*32} PACIENTE {'─'*41}┐")
        linhas_relatorio.append(f"│ {'CPF: ' + CPF:<81} │")
        linhas_relatorio.append(f"│ {'Nome: ' + Nome:<81} │")
        linhas_relatorio.append(f"│ {'Data de Nascimento: ' + Data_Nasc:<81} │")
        linhas_relatorio.append(f"│ {'Sexo: ' + Sexo:<81} │")
        linhas_relatorio.append(f"│ {'Plano de Saúde: ' + Plano:<81} │")
        linhas_relatorio.append(f"└{'─'*83}┘")
        linhas_relatorio.append("")
        linhas_relatorio.append(f"┌{'─'*35} CONTATOS {'─'*38}┐")
        linhas_relatorio.append(f"│ {'-- TELEFONES --':<81} │")
        for telefone in Telefones:
            linhas_relatorio.append(f"│ {'• ' + telefone:<81} │")
        linhas_relatorio.append(f"│ {'':<81} │")
        linhas_relatorio.append(f"│ {'-- E-MAILS --':<81} │")
        for email in Emails:
            linhas_relatorio.append(f"│ {'• ' + email:<81} │")
        linhas_relatorio.append(f"└{'─'*83}┘")
        linhas_relatorio.append("")
        linhas_relatorio.append("=" * 85)
        linhas_relatorio.append("")

    Gravar_Arquivo_Relatorio("Relatorio_Pacientes.txt", linhas_relatorio)
    print("Relatório salvo no arquivo Relatorio_Pacientes.txt")
    input("Pressione enter para voltar ao menu de relatórios...")

# =============================================== 3 - RELATÓRIO: CONSULTAS DOS ÚLTIMOS X DIAS =============================================== #

def Relatorio_Consultas_Ultimos_X_Dias(Consultas, Medicos, Pacientes):
    Limpar_Tela()
    print("-------------------------Relatório de Consultas dos Últimos X Dias----------------------------")
    print()

    dias_valido = False
    while not dias_valido:
        dias = input("Digite a quantidade de dias: ").strip()
        if dias.isdigit():
            dias_valido = True
            dias = int(dias)
        else:
            print("Valor inválido! Digite apenas números.")
            print()

    resultados = []
    linhas_relatorio = []
    data_atual = datetime.now()

    for consulta in Consultas:
        CRM = consulta[0]
        CPF = consulta[1]
        Data = consulta[2]
        Hora = consulta[3]
        Diagnostico = consulta[4]
        Medicamentos = consulta[5]

        # Verifica primeiro se a data e a hora estão no formato esperado antes de comparar
        if len(Data) == 10 and len(Hora) == 5 and Data[2] == '/' and Data[5] == '/' and Hora[2] == ':':
            data_consulta = datetime.strptime(f"{Data} {Hora}", "%d/%m/%Y %H:%M")
            diferenca = data_atual - data_consulta

            if diferenca.days <= dias:
                resultados.append(consulta)

    if len(resultados) == 0:
        print(f"Nenhuma consulta encontrada nos últimos {dias} dias.")
        input("Pressione enter para voltar ao menu de relatórios...")
        return


    print()
    Limpar_Tela()
    print(f"=============== Relatório: Consultas dos últimos {dias} dias ===============")
    print()
    print("Consultas encontradas:")
    

    linhas_relatorio.append(f"=============== Relatório: Consultas dos últimos {dias} dias ===============")
    linhas_relatorio.append("")

    for consulta in resultados:
        CRM = consulta[0]
        CPF = consulta[1]
        Data = consulta[2]
        Hora = consulta[3]
        Diagnostico = consulta[4]
        Medicamentos = consulta[5]

        achou_med, nome_med = Buscar_Medico_Por_CRM(Medicos, CRM)
        achou_pac, nome_pac = Buscar_Paciente_Por_CPF(Pacientes, CPF)

        if not achou_med:
            nome_med = "Médico não encontrado"
        if not achou_pac:
            nome_pac = "Paciente não encontrado"
            
            
        print()
        print(f"Médico: {nome_med} | Paciente: {nome_pac} | Data e Hora: {Data} {Hora}")
        print(f"┌{'─'*32} CONSULTA {'─'*41}┐")
        print(f"│ {'CRM do Médico: ' + CRM:<81} │")
        print(f"│ {'Nome do Médico: ' + nome_med:<81} │")
        print(f"│ {'CPF do Paciente: ' + CPF:<81} │")
        print(f"│ {'Nome do Paciente: ' + nome_pac:<81} │")
        print(f"│ {'Data: ' + Data:<81} │")
        print(f"│ {'Hora: ' + Hora:<81} │")
        print(f"│ {'Diagnóstico: ' + Diagnostico:<81} │")
        print(f"└{'─'*83}┘")
        print()
        print(f"┌{'─'*35} MEDICAMENTOS {'─'*34}┐")
        for medicamento in Medicamentos:
            print(f"│ {'• ' + medicamento:<81} │")
        print(f"└{'─'*83}┘")
        print()
        print("=" * 85)
        print()

        linhas_relatorio.append("")
        linhas_relatorio.append(f"Médico: {nome_med} | Paciente: {nome_pac} | Data e Hora: {Data} {Hora}")
        linhas_relatorio.append(f"┌{'─'*32} CONSULTA {'─'*41}┐")
        linhas_relatorio.append(f"│ {'CRM do Médico: ' + CRM:<81} │")
        linhas_relatorio.append(f"│ {'Nome do Médico: ' + nome_med:<81} │")
        linhas_relatorio.append(f"│ {'CPF do Paciente: ' + CPF:<81} │")
        linhas_relatorio.append(f"│ {'Nome do Paciente: ' + nome_pac:<81} │")
        linhas_relatorio.append(f"│ {'Data: ' + Data:<81} │")
        linhas_relatorio.append(f"│ {'Hora: ' + Hora:<81} │")
        linhas_relatorio.append(f"│ {'Diagnóstico: ' + Diagnostico:<81} │")
        linhas_relatorio.append(f"└{'─'*83}┘")
        linhas_relatorio.append("")
        linhas_relatorio.append(f"┌{'─'*35} MEDICAMENTOS {'─'*34}┐")
        for medicamento in Medicamentos:
            linhas_relatorio.append(f"│ {'• ' + medicamento:<81} │")
        linhas_relatorio.append(f"└{'─'*83}┘")
        linhas_relatorio.append("")
        linhas_relatorio.append("=" * 85)
        linhas_relatorio.append("")

    Gravar_Arquivo_Relatorio("Relatorio_Consultas.txt", linhas_relatorio)
    print("Relatório salvo no arquivo Relatorio_Consultas.txt")
    input("Pressione enter para voltar ao menu de relatórios...")

# =============================================== MAIN - SUBMENU =============================================== #

def Main_Funcoes_Relatorios(Medicos, Pacientes, Consultas):
    continuar = True

    while continuar:
        opcao = Menu()

        if opcao == "1":
            Relatorio_Medicos_Por_Especialidade(Medicos)
        elif opcao == "2":
            Relatorio_Pacientes_Menores_De_X_Anos(Pacientes)
        elif opcao == "3":
            Relatorio_Consultas_Ultimos_X_Dias(Consultas, Medicos, Pacientes)
        elif opcao == "4":
            Limpar_Tela()
            continuar = False
        else:
            Limpar_Tela()
            print("Opção inválida. Digite um número entre 1 e 4.")
            input("Pressione enter para continuar...")

    