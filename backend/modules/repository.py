class PacienteRepository:
    def __init__(self):
        self.dados_pacientes = []

    def adicionar(self, novo_paciente):
        self.dados_pacientes.append(novo_paciente)

    def listar(self):
        return self.dados_pacientes
    
    def buscar_por_nome(self, nome):
        return [ p for p in self.pacientes if nome.lower() in p.nome.lower()]
    
    def existe(self):
        return len(self.dados_pacientes) > 0