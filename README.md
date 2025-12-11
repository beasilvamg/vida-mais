## 🏥 Clínica Vida+

Este projeto e contruido para gerenciar pacientes e consultas médicas de uma clínica de saúde que  sofre com a grande demanda de serviços médicos e procura por uma solução digital capaz de otimizar o atendimento e a experinecia dos pacientes.

## Visão Geral do Projeto

A contrução do projeto esta sendo criada em duas partes:

1.  **Backend (Python):** Responsável pela lógica de negócio e persistência de dados.
2.  **Frontend (React/JavaScript):** Interface de usuário (a ser iniciada).

## 🚀 Status Atual do Projeto — Fase 1 (Backend)

Atualmente, o foco do projeto está na **organização e refatoração do backend em Python**.

### ✅ O que já foi feito

- Definição e criação da **estrutura modular** completa do backend (models/, controllers/, services/, etc.).
- Criação dos **Modelos (Dados):** A classe **Paciente** foi isolada corretamente em backend/models/paciente.py.
- Criação dos **Utilitários (Ferramentas):** As funções de *validação de *input* (checagem de nome, idade e telefone) foram isoladas no módulo backend/utils/validacoes.py.

### ⏳ Em andamento


- Implementar o Controlador: Mover o código de gerenciamento de dados (cadastro, lista e busca) para a pasta `controllers/`. Este é o próximo passo a ser concluído.
- Implementar o Serviço: Isolar a lógica de cálculos e relatórios de estatísticas no módulo services/estatisticas.py.
-Finalizar o Menu: Ajustar o arquivo app.py para chamar os novos módulos.

### ❌ Ainda não iniciado

- Integração com banco de dados
- Desenvolvimento do frontend
- Comunicação entre frontend e backend
