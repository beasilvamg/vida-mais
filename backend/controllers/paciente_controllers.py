# Lista global que armazena os dados da Clínica
dados_pacientes = []

# Importação dos módulos criados
from backend.models.paciente import Paciente
from backend.utils.validacoes import validar_nome, validar_idade, validar_telefone

class PacienteController:
    # Função para cadastrar paciente
    def cadastrar_paciente(self, nome, idade_str, telefone):
        #Chamando as funções do módulo utils
        validar_nome(nome)
        idade = validar_idade(idade_str)
        validar_telefone(telefone)

        novo_paciente = Paciente(nome, idade, telefone)
        dados_pacientes.append(novo_paciente)
        return novo_paciente

    # Lista de todos os pacientes cadastrados
    def listar_pacientes(self):
        return dados_pacientes

    # Buscar paciente pelo nome
    def buscar_paciente(self, nome):
        resultado = list(filter(lambda paciente: nome.lower() in paciente.nome.lower(), dados_pacientes))
        return resultado