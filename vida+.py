# Importação das bibliotecas
import re
import matplotlib.pyplot as plt
import seaborn as sns


# Definindo classe pai
class Paciente:
    def __init__(self, nome, idade, telefone):
        self.nome = nome
        self.idade = idade
        self.telefone = telefone

    def __str__(self):
        return f' Nome: {self.nome} | Idade: {self.idade} | Telefone: {self.telefone}\n'


# Classe que herda os dados da classe paciente
class Clinica():
    def __init__(self):
        # lista para armazenar os dados dos pacientes
        self.dados_pacientes = []

    # Gerenciar os dados dos pacientes
    # Função para cadatrar paciente
    def cadastrar_paciente(self):
        print("\n" + "="*45)
        print("🩺 CADASTRO DE PACIENTE")
        print("="*45)
        print("Preencha os campos abaixo: \n")

        try:
            nome = input("Nome do Paciente: ").strip()
            if not re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
                raise ValueError("O nome deve conter apenas letras e espaços.")
            

            idade_str = input("Idade: ").strip()
            if not idade_str.isdigit():
                raise ValueError("A idade deve conter apenas números.")
            idade = int(idade_str)
            if idade <= 0 or idade > 120:
                raise ValueError("A idade deve estar entre 1 e 120.") 


            telefone = input("Telefone (formato (99) 98765-4321): ").strip()
            if not re.match(r"^\(\d{2}\)\s9\d{4}-\d{4}$", telefone):
                raise ValueError("Telefone inválido! Use o formato (99) 98765-4321.")  
             

            #Adiciona paciente na lista
            novo_paciente = Paciente(nome, idade, telefone)
            self.dados_pacientes.append(novo_paciente)
            print('\n✅ Paciente cadastrado com sucesso!\n')

        except ValueError as erro:
            print(f"\n Erro: {erro}\nTente novamente.\n")
            # Chama novamente a função para o usuário tentar de novo
            self.cadastrar_paciente()


    # Lista em ordem de todos os pacientes cadastrados
    def lista_paciente(self):
        print("\n" + "="*45)
        print("📋 LISTA DE PACIENTES")
        print("="*45)

        if not self.dados_pacientes:
            print('Nemhum paciente cadastrado ainda.\n')
            print()
            return
        else:
            for i, paciente in enumerate(self.dados_pacientes, start=1):
                print(f'{i}.{paciente}')


    # Buscar paciente pelo nome
    def buscar_paciente(self):
        print("\n" + "="*45)
        print("🔎 BUSCAR PACIENTE")
        print("="*45)

        nome = input('Digite o nome do paciente: ').strip()
        print()

        resultado = list(filter(lambda paciente: nome.lower() in paciente.nome.lower(), self.dados_pacientes))
        # Condição caso o nome do paciente não seja encontrado
        if resultado:
            print(f'\nForam encontrados {len(resultado)} paciente(s) com esse nome: \n')
            for paciente_encontrado in resultado:
                print(f'Nome: {paciente_encontrado.nome}, Idade: {paciente_encontrado.idade}, Telefone: {paciente_encontrado.telefone}')
        else:
            print(f'Nenhum paciente encontrado. Você pode cadastrá-lo no sistema.\n')


    # Mostrar as estatísticas da clínica
    def estatistica_clinica(self):
        print("\n" + "="*45)
        print("📊 ESTATÍSTICAS GERAIS DA CLÍNICA VIDA+")
        print("="*45)

        if not self.dados_pacientes:
            print('Nenhum paciente cadastrado ainda.\n')
            return
        
        # Coletar dados
        idades = [paciente.idade for paciente in self.dados_pacientes]
        total = len(idades)
        media = sum(idades) / total
        mais_novo = min(self.dados_pacientes, key=lambda p: p.idade)
        mais_velho = max(self.dados_pacientes, key=lambda p: p.idade)

       #Relatório
        print(f'Total de pacientes cadastrados: {total}')
        print(f'Idade média dos pacientes: {media:.1f} anos')
        print(f'Pacientes mais novo: ({mais_novo.idade}) anos')
        print(f'Pacientes mais velhos: ({mais_velho.idade}) anos\n')
        print("\nGerando gráfico...\n")


        #Gráfico
        dados = {
            'Categoria': ['Idade Média', 'Paciente Mais Novo', 'Paciente Mais Velho', 'Total De Pacientes'],
            'Valor': [media, mais_novo.idade, mais_velho.idade, total]
        }

        #Estilo do gráfico
        plt.figure(figsize=(8,5))
        sns.barplot(
            x='Categoria',
            y='Valor',
            data=dados,
            palette="coolwarm",
            hue='Categoria',
            legend=False)

        plt.title('Estatísticas Gerais da Clínica Vida+', fontsize=14, fontweight='bold')
        plt.ylabel('Valores')
        plt.xlabel('')

        #Para ver valores a cima da barra do gráfico
        for i, v in enumerate(dados['Valor']):
            plt.text(i, v + 0.3, str(v), ha='center', fontweight='bold')

        plt.tight_layout()
        plt.show()

clinica = Clinica()


# menu rodando em loop
def menu():
    while True:
        print("\n" + "="*50)
        print("🏥 SISTEMA CLÍNICA VIDA+")
        print("="*50)
        print('Bem-Vindo(a)! Selecione uma das opções abaixo para começar:')
        print()
        print('1 - Cadastrar paciente')
        print('2 - Lista de pacientes')
        print('3 - Buscar paciente')
        print('4 - Ver as estatísticas da clínica')
        print('0 - Sair')
        print()

        opcao = input('Escolha uma opção: ')
        print()

        if opcao == '1':
            clinica.cadastrar_paciente()
        elif opcao == '2':
            clinica.lista_paciente()
        elif opcao == '3':
            clinica.buscar_paciente()
        elif opcao == '4':
            clinica.estatistica_clinica()
        elif opcao == '0':
            print('Encerrando o sistema...Até logo!\n')
            break
        else:
            print('Opção invalida! Por favor, tente novamente.\n')

menu()
