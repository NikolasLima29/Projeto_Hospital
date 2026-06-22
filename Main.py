import os

from Funcoes_Medico import Carregar_Dados_Arquivo_Medicos, Main_Funcoes_Medico
from Funcoes_Paciente import Carregar_Dados_Arquivo_Pacientes, Main_Funcoes_Pacientes
from Funcoes_Consultas import Carregar_Dados_Arquivo_Consultas, Main_Funcoes_Consulta
from Funcoes_Relatorios import Main_Funcoes_Relatorios

def Limpar_Tela():
    # Limpa o terminal independente do sistema operacional (Windows ou Linux/Mac)
    os.system('cls' if os.name == 'nt' else 'clear')
            
def Menu():
    Limpar_Tela()
    print("Menu")
    print("1 - Submenu de Médicos")
    print("2 - Submenu de Pacientes")
    print("3 - Submenu de Consultas")
    print("4 - Submenu Relatórios")
    print("5 - Sair")
    i = input("Digite sua escolha: ")
    return i

def Main():

    Medicos = []
    Pacientes = []
    Consultas = []

    Carregar_Dados_Arquivo_Medicos(Medicos)
    Carregar_Dados_Arquivo_Pacientes(Pacientes)
    Carregar_Dados_Arquivo_Consultas(Consultas)

    i = ""
    while i != "5":
        i = Menu()
        if i == "1":
            Main_Funcoes_Medico(Medicos)
        elif i == "2":  
            Main_Funcoes_Pacientes(Pacientes)
        elif i == "3":
            Main_Funcoes_Consulta(Medicos, Pacientes)
        elif i == "4":
            Main_Funcoes_Relatorios(Medicos, Pacientes, Consultas)
        elif i == "5":
            print("Fim do programa!")
        else:
            input("Opção inválida! Pressione ENTER para voltar ao menu: ")

Main()