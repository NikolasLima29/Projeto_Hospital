def Listar_Todos_Pacientes(Pacientes):
  for i in range(len(Pacientes)):
    print("___________________________________________")
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
        if j == 5: # Telefones
            print("┌" + "─"*35 + " CONTATOS " + "─"*38 + "┐")
            print(f"│ {'-- TELEFONES --':<81} │")
            for k in range(len(Pacientes[i][j])):
                texto_tel = f"{k+1}° Telefone: {Pacientes[i][j][k]}"
                print(f"│ {texto_tel:<81} │")
                
        if j == 6: # E-mails
            print(f"│ {'':<81} │") 
            print(f"│ {'-- E-MAILS --':<81} │")
            for k in range(len(Pacientes[i][j])):
                texto_email = f"{k+1}° E-mail: {Pacientes[i][j][k]}"
                print(f"│ {texto_email:<81} │")
            print("└" + "─"*83 + "┘\n") # Fecha o bloco de Contatos
           
                
            
            
        
            
            
     
     







def Main_Funcoes_Pacientes():
   # Ordem: [CPF, Nome, Data de Nascimento, Sexo, Plano de Saúde, [E-mails], [Telefones]]
    Pacientes = [
    [
        "123.456.789-10", 
        "João Silva ", 
        "15/04/1985", 
        "M", 
        "Unimed", 
        ["joao.silva@email.com"], 
        ["(16) 99999-1111"]
    ],
    [
        "098.765.432-10", 
        "Maria Oliveira", 
        "22/10/1992", 
        "F", 
        "SulAmérica", 
        ["maria.oliveira@email.com"], 
        ["(16) 97777-3333"]
    ]
]


    
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
           
            print("LISTA - PACIENTES")
            Listar_Todos_Pacientes(Pacientes)
            
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

Main_Funcoes_Pacientes()