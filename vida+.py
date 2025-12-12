# Importação das bibliotecas
import matplotlib.pyplot as plt
import seaborn as sns

# Classe que herda os dados da classe paciente
class Clinica():

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
