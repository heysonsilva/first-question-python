import json


# Tratamento de erro para entrada incorreta do úsuario ou indisponibilidade do arquivo
try:
    ano = input("=="*32 + "\n|| INSIRA O NÚMERO REFERENTE AO ANO QUE VOCÊ DESEJA ACESSAR:\n|| 1 - 2021\n|| 2 - 2022\n"+"=="*30 + "\n>>> ")
    with open(f"cartola_fc_{ano}.txt", "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
except FileNotFoundError:
    print("O arquivo não foi encontrado.")
except IOError:
    print("Erro ao acessar o arquivo.")
    