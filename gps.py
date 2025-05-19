import csv
import os

def save_to_csv(data):
    # Verifica se o arquivo já existe
    file_exists = os.path.exists("dados.csv")
    
    with open("dados.csv", "a", newline="") as arquivo:
        writer = csv.writer(arquivo)
        
        # Escreve o cabeçalho apenas se o arquivo não existir
        if not file_exists:
            writer.writerow(["ID", "Tarefa", "Responsável", "Duração (dias)", "Esforço (horas)", 
                             "Início", "Fim", "Recurso", "Custo por Hora", "Custo Total"])
        
        # Escreve os dados
        writer.writerow(data)

def cadastrar():
    try:
        id = input("Enter id: ")
        tarefa = input("Enter tarefa: ")
        responsavel = input("Enter responsavel: ")
        duracao = input("Enter duracao em dias: ")
        esporco = input("Enter esporco em horas: ")
        inicio = input("Enter inicio: ")
        fim = input("Enter fim: ")
        recurso = input("Enter recurso: ")
        custo_hora = input("Enter custo_hora: ")
        custo_total = float(custo_hora) * float(esporco)

        # Salva os dados no CSV
        save_to_csv([id, tarefa, responsavel, duracao, esporco, inicio, fim, recurso, custo_hora, custo_total])
        print("Cadastro realizado com sucesso!")
    except ValueError:
        print("Erro: Certifique-se de inserir valores numéricos válidos para custo_hora e esporco.")

def listar():
    if not os.path.exists("dados.csv"):
        print("Nenhum dado encontrado. O arquivo 'dados.csv' não existe.")
        return

    with open("dados.csv", "r") as arquivo:
        reader = csv.reader(arquivo)
        for row in reader:
            print(", ".join(row))

# Main loop
while True:
    print("1 - Cadastrar")
    print("2 - Listar")
    print("3 - Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 1:
            cadastrar()
        elif opcao == 2:
            listar()
        elif opcao == 3:
            print("Sair")
            break
        else:
            print("Opção inválida. Tente novamente.")
    except ValueError:
        print("Erro: Por favor, insira um número válido.")