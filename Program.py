# Importando as bibliotecas necessárias
import pandas as pd

# Definindo os nomes dos arquivos de dados
filename_resultados = "SP_turno_1.csv"
filename_perfil_eleitorado = "perfil_eleitorado_2020.csv"

# Lendo os arquivos CSV utilizando o pandas
# Tabela de resultados das eleições
tabela_resultados = pd.read_csv(filename_resultados, sep=";", encoding="latin1", quotechar='"',
                                na_values=["# NULO#", "#NE"])
# Perfil do eleitorado
perfil_eleitorado = pd.read_csv(filename_perfil_eleitorado, sep=";", encoding="latin1", quotechar='"',
                                usecols=["DS_GENERO", "DS_ESTADO_CIVIL", "CD_FAIXA_ETARIA", "DS_GRAU_ESCOLARIDADE",
                                         "NM_MUNICIPIO"],
                                na_values=["# NULO#", "#NE"])

# Mensagem de boas-vindas
print("Bem-vindo ao programa de informações das eleições de SP 2020")

# Loop principal do programa
while True:
    # Pergunta se o usuário deseja iniciar o programa
    iniciar = input("Deseja iniciar o programa? (S/N): ").lower()

    if iniciar == 'n':
        print("Programa encerrado.")
        break

    elif iniciar == 's':
        while True:
            # Menu principal
            print("\nMENU PRINCIPAL")
            print("1 - Informações sobre um candidato")
            print("2 - Buscar nome de candidatos")
            print("3 - Informacoes gerais")
            print("4 - Sair")

            opcao_inicio = input("Escolha uma opção: ")

            if opcao_inicio == '1':
                # Opção para obter informações sobre um candidato específico
                candidato = input("\nDigite o nome do candidato (ex: BRUNO COVAS): ").upper().strip()
                candidato_votes = tabela_resultados[tabela_resultados["NM_VOTAVEL"] == candidato]
                sg_partido = candidato_votes.iloc[0]["SG_PARTIDO"]
                print(f"\n{candidato} - PARTIDO {sg_partido}")

                if candidato_votes.empty:
                    print("Candidato não encontrado.")
                    continue

                while True:
                    # Menu de dúvidas sobre o candidato
                    print("\nDUVIDAS CANDIDATO")
                    print("1 - Qual município mais votou no candidato(a)?")
                    print("2 - Voltar ao menu principal")

                    opcao_candidato = input("Escolha uma opção: ")

                    if opcao_candidato == "1":
                        most_votes_municipio = candidato_votes.groupby("NM_MUNICIPIO")["QT_VOTOS"].sum().idxmax()
                        print("Município mais votado:", most_votes_municipio)
                    elif opcao_candidato == "2":
                        break

            # Restante das opções do menu principal
            elif opcao_inicio == '2':
                # Código para listar candidatos
                print("\nLISTA DE TODOS OS CANDIDATOS")
                todos_candidatos = tabela_resultados["NM_VOTAVEL"].unique()

                for index, candidato in enumerate(todos_candidatos, start=1):
                    print(f"{index} - {candidato}")

                print("\nFim da lista de candidatos")

                opcao_escolhida = input("Escolha um número de candidato para obter informações (ou 0 para voltar): ")

                if opcao_escolhida == '0':
                    continue  # Volta ao menu principal

                elif opcao_escolhida.isnumeric() and 1 <= int(opcao_escolhida) <= len(todos_candidatos):
                    candidato_escolhido = todos_candidatos[int(opcao_escolhida) - 1]
                    candidato_votes = tabela_resultados[
                        tabela_resultados["NM_VOTAVEL"] == candidato_escolhido]  # Defina candidato_votes aqui

                    sg_partido = candidato_votes.iloc[0]["SG_PARTIDO"]
                    total_votos = candidato_votes["QT_VOTOS"].sum()  # Calcula o total de votos do candidato
                    print(f"\n{candidato_escolhido} - PARTIDO {sg_partido}")
                    print(f"Total de votos: {total_votos}")

                else:
                    print("Opção inválida. Escolha um número válido ou 0 para voltar.")

            elif opcao_inicio == '3':
                # Código para informações gerais da eleição
                print("\nInformações gerais da eleição:")

                print("\nDUVIDAS ELEICAO")
                print("1 - Faixa etária de votos")
                print("2 - Escolaridade de votos")
                print("3 - Quantidade de Gêneros")
                print("4 - Estado civil")
                print("5 - Voltar ao menu principal")

                opcao_eleicao = input("Escolha uma opção: ")

                if opcao_eleicao == "1":
                    faixa_etaria_counts = perfil_eleitorado["CD_FAIXA_ETARIA"].value_counts()
                    print("Quantidade de cada faixa etária dos Candidatos Votantes:")
                    print(faixa_etaria_counts)
                elif opcao_eleicao == "2":
                    escolaridade_counts = perfil_eleitorado["DS_GRAU_ESCOLARIDADE"].value_counts()
                    print("Perfil de Grau de Escolaridade dos Candidatos Votantes:")
                    print(escolaridade_counts)
                elif opcao_eleicao == "3":
                    genero_counts = perfil_eleitorado["DS_GENERO"].value_counts()
                    print("Quantidade de Gêneros dos Candidatos Votantes:")
                    print(genero_counts)
                elif opcao_eleicao == "4":
                    estado_civil_counts = perfil_eleitorado["DS_ESTADO_CIVIL"].value_counts()
                    print("Perfil de Estado Civil dos Candidatos Votantes:")
                    print(estado_civil_counts)
                elif opcao_eleicao == "5":
                    break
                else:
                    print("Opção inválida. Escolha novamente.")

            elif opcao_inicio == '4':
                print("Programa encerrado.")
                exit()

            else:
                print("Opção inválida. Escolha novamente.")

    else:
        print("Opção inválida. Escolha 'S' para iniciar ou 'N' para sair.")
