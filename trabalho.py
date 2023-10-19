ALUNOS = []

def menu():
    print("\n MENU: ")
    print("1 - Listar Alunos")
    print("2 - Cadastrar Aluno")
    print("3 - Editar Aluno")
    print("4 - Remover Aluno")  
    print("5 - Resumo Estatisco")
    print("6 - Importar Informacao")
    print("7 - Exportar Informacao")
    print(" ")
    print("0 - Sair")


def ler_opcao():
    opcao = int(input("Digite uma opcao: "))
    while opcao < 0 or opcao > 7:
        print("Opção Inválida! Tente novamente.")
        menu()
        opcao = int(input("Digite uma opcao: "))
    return opcao

def cadastro_de_aluno():
    try:
        ra = int(input("RA: "))
        
        for aluno in ALUNOS:
            if aluno['RA'] == ra:
                print("Erro: Já exite um aluno com o mesmo RA. ")
                return
            
        nome = input("Nome: ")
        nota = float(input("Nota: "))
        dados = {
                "RA": ra,
            "Nome": nome,
            "Nota": nota
        }
        ALUNOS.append(dados)
        print("Aluno Cadastrado com sucesso!")
    except ValueError:
        print("Erro: Certifique-se de que o RA seja um número inteiro e a nota seja um número decimal.")

def buscar_por_ra(ra_desejado):
    global ALUNOS
    for elemento in ALUNOS:
        if elemento["RA"] == ra_desejado:
            return elemento  
    return None 

def edicao_de_aluno():
    ra = int(input("Digite o RA do aluno que deseja editar: "))
    aluno_encontrado = False
    
    for aluno in ALUNOS:
        if aluno["RA"] == ra:
            try:
                novo_nome = input("Digite o nome: ")  
                nova_nota = float(input("Digite a nota: "))
                aluno["Nome"] = novo_nome
                aluno["Nota"] = nova_nota
                aluno_encontrado = True

            except ValueError:
                print("Erro: Certifique-se que a nota seja um número decimal.")    
            break

        if not aluno_encontrado:
            print("Aluno com RA: " , ra," não encontrado.")  


def remocao_de_aluno():
    ra = int(input("Digite o RA do aluno que deseja excluir: "))
    global ALUNOS
    print("alunos",  ALUNOS)
    aluno = buscar_por_ra(ra)
    if aluno:
        ALUNOS.remove(aluno)
        print("Aluno deletado: ", aluno)
    else:
        print("Aluno com RA: ", ra, "não encontrado.")
        
   


def resumo_estatistico():
    if not ALUNOS:
        return None

    notas = [aluno["Nota"] for aluno in ALUNOS]
    quantidade = len(ALUNOS)
    maior_nota = max(notas)
    menor_nota = min(notas)
    media = sum(notas) / quantidade

    resultado =  {
        "Quantidade de alunos": quantidade,
        "Maior nota": maior_nota,
        "Menor nota": menor_nota,
        "Média das notas": media,
    }

    for chave, valor in resultado.items():
        print(f"{chave}: {valor}")

    return resultado




def importar_dados():
    nome_arquivo = (input("Digite o nome do arquivo que deseja importar os dados: "))
    global alunos
    try:
        with open(nome_arquivo, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                partes = linha.strip().split(",")
                if len(partes) == 3:
                    ra, nome, nota = partes
                    ALUNOS.append({
                        "RA": int(ra),
                        "Nome": nome,
                        "Nota": float(nota)
                    })
        print("Dados importados como sucesso. ")
        print("Alunos importados: ")
        for aluno in ALUNOS:
            print(f"RA: {aluno['RA']}, Nome: {aluno['Nome']}, Nota: {aluno['Nota']}")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except ValueError:
        print("Erro: Certifique-se de que o arquivo de importção tenha o formato correto (RA, nome, nota).")

def exportar_dados():
    nome_arquivo = (input("Digite o nome do arquivo que deseja exportar os dados: "))
    with open(nome_arquivo, "w") as arquivo:
        for aluno in ALUNOS:
            arquivo.write(f"{aluno['RA']}, {aluno['Nome']}, {aluno['Nota']}\n")
    print("Dados exportados com sucesso.")

   


if __name__ == "__main__":

    while True:
        menu()
        opcao = ler_opcao()
        if opcao == 0:
            break
        elif opcao == 1:
            print(ALUNOS)
        elif opcao == 2:
            cadastro_de_aluno()
        elif opcao == 3:
            edicao_de_aluno()
        elif opcao == 4:
            remocao_de_aluno()
        elif opcao == 5:
            resumo_estatistico()
        elif opcao == 6:
            importar_dados()
        elif opcao == 7:
            exportar_dados()
        
        