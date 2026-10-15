# Controle Financeiro em Python | Personal Finance Tracker

## 🇧🇷 Português

### Sobre o projeto

Aplicação de controle financeiro desenvolvida em Python para registrar receitas e despesas, consultar o saldo e acompanhar movimentações financeiras por meio de relatórios e gráficos.

O projeto demonstra conceitos de programação, manipulação de arquivos CSV, organização de funções, validação de dados e visualização de informações.

### Funcionalidades

- Cadastro de receitas e despesas.
- Validação de valores informados.
- Registro automático da data das movimentações.
- Armazenamento persistente em arquivo CSV.
- Consulta de receitas, despesas e saldo atual.
- Histórico de movimentações financeiras.
- Relatórios financeiros mensais.
- Exportação de relatórios para CSV.
- Gráficos de receitas e despesas.
- Comparação mensal de receitas e despesas.
- Salvamento de gráficos em formato PNG.

### Tecnologias utilizadas

- Python
- CSV
- Matplotlib
- Git e GitHub

### Estrutura do projeto

```text
controle-financeiro-python/
├── controle_financeiro.py
├── grafico_financeiro.py
├── movimentacoes.csv
├── grafico_mensal.png
├── README.md
└── .gitignore
```

Os arquivos `movimentacoes.csv` e `grafico_mensal.png` são gerados durante a utilização do programa. O CSV com movimentações pessoais não deve ser publicado no repositório.

### Como executar

1. Instale o Python 3.
2. Crie um ambiente virtual:

   ```bash
   python3 -m venv .venv
   ```

3. Ative o ambiente virtual no Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Instale a biblioteca de gráficos:

   ```bash
   python -m pip install matplotlib
   ```

5. Execute o controle financeiro:

   ```bash
   python controle_financeiro.py
   ```

6. Para gerar os gráficos, execute:

   ```bash
   python grafico_financeiro.py
   ```

### Aprendizados

Este projeto foi desenvolvido para praticar:

- Lógica de programação.
- Funções e estruturas de repetição.
- Condicionais e tratamento de erros.
- Leitura e escrita de arquivos CSV.
- Organização e persistência de dados.
- Criação de relatórios.
- Visualização de dados com Matplotlib.

---

## 🇺🇸 English

### About the project

A personal finance tracking application built with Python to record income and expenses, calculate balances, and analyze financial transactions through reports and charts.

The project demonstrates programming fundamentals, CSV file handling, function organization, data validation, and data visualization.

### Features

- Income and expense registration.
- Input validation.
- Automatic transaction dates.
- Persistent CSV storage.
- Income, expense, and balance summaries.
- Transaction history.
- Monthly financial reports.
- CSV report export.
- Income and expense charts.
- Monthly financial comparisons.
- PNG chart export.

### Technologies

- Python
- CSV
- Matplotlib
- Git and GitHub

### Project structure

```text
controle-financeiro-python/
├── controle_financeiro.py
├── grafico_financeiro.py
├── movimentacoes.csv
├── grafico_mensal.png
├── README.md
└── .gitignore
```

The `movimentacoes.csv` and `grafico_mensal.png` files are generated while using the application. Personal financial data should not be published in the repository.

### How to run

1. Install Python 3.
2. Create a virtual environment:

   ```bash
   python3 -m venv .venv
   ```

3. Activate it on Linux:

   ```bash
   source .venv/bin/activate
   ```

4. Install the charting library:

   ```bash
   python -m pip install matplotlib
   ```

5. Run the finance tracker:

   ```bash
   python controle_financeiro.py
   ```

6. Generate the charts:

   ```bash
   python grafico_financeiro.py
   ```

### Learning outcomes

This project provides hands-on practice with:

- Programming logic.
- Functions and loops.
- Conditional statements and error handling.
- CSV file processing.
- Data persistence and organization.
- Financial reporting.
- Data visualization with Matplotlib.

---

## Author

**Python | Data Analytics | Data Visualization**

This project is part of my programming and data analytics portfolio.
