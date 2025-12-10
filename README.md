## 🏥 Clínica Vida+

Este projeto e contruido para gerenciar pacientes e consultas médicas de uma clínica de saúde que  sofre com a grande demanda de serviços médicos e procura por uma solução digital capaz de otimizar o atendimento e a experinecia dos pacientes.

## Visão Geral do Projeto

A contrução do projeto esta sendo criada em duas partes:

1.  **Backend (Python):** Responsável pela lógica de negócio e persistência de dados.
2.  **Frontend (React/JavaScript):** Interface de usuário (a ser iniciada).

## 🚀 Status Atual do Projeto — Fase 1 (Backend)

Atualmente, o foco do projeto está na **organização e refatoração do backend em Python**.

### ✅ O que já foi feito

- Definição da **estrutura modular** do backend
- Criação dos primeiros módulos:
- A classe **Paciente** foi criada e isolada em `backend/models/paciente.py`.

### ⏳ Em andamento

- Refatoração do código original para a nova estrutura modular
- As funções de validação (nome, idade, telefone) precisam ser isoladas no módulo `utils/validacoes.py`.
- O código de cadastro, lista e busca será movido para a pasta `controllers/`.

### ❌ Ainda não iniciado

- Integração com banco de dados
- Desenvolvimento do frontend
- Comunicação entre frontend e backend
