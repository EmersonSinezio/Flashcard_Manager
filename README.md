### README

# Flashcard Manager

## Descrição do Projeto

O **Flashcard Manager** foi criado com o objetivo de ajudar no gerenciamento de flashcards para matérias da faculdade. O foco é facilitar a retenção de conteúdo por meio da prática e revisão constantes. A aplicação é simples e baseada no terminal, mas extremamente funcional para o aprendizado e organização dos estudos.

Este projeto é um reflexo do meu aprendizado em Python e será aprimorado conforme meus conhecimentos na linguagem e nas melhores práticas de desenvolvimento de software evoluírem.

---

## Funcionalidades

- **Gerenciamento de Matérias:** Criação, seleção e troca entre diferentes matérias.
- **Adição de Flashcards:** Crie perguntas e respostas para cada matéria.
- **Edição de Flashcards:** Atualize os conteúdos conforme necessário.
- **Remoção de Flashcards:** Exclua flashcards obsoletos ou errados.
- **Sessão de Perguntas:** Teste seus conhecimentos com feedback sobre acertos e erros, incluindo percentual de acertos.

---

## Estrutura do Projeto

O projeto segue o padrão **MVT (Model-View-Template)** para uma melhor organização:

- **Models:** Gerencia o banco de dados JSON.
- **Views:** Contém a lógica principal do sistema.
- **Templates:** Menus e interação com o usuário.

### Estrutura de Diretórios:

```
flashcard_manager/
├── app.py                # Ponto de entrada
├── models/               # Camada de Modelos
│   ├── database.py       # Gerenciamento de dados
├── views/                # Lógica da aplicação
│   ├── flashcard.py
├── templates/            # Menus e interação com o usuário
│   ├── menu.py
├── db/                   # Base de dados
│   ├── flashcards.json
```

---

## Requisitos

- Python 3.8 ou superior

---

## Como Usar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/flashcard-manager.git
cd flashcard-manager
```

2. Execute o programa:

```bash
python app.py
```

3. Siga as instruções no terminal para gerenciar seus flashcards.

---

## Melhorias Futuras

- Interface gráfica para maior acessibilidade.
- Sistema de agendamento para revisar flashcards automaticamente.
- Relatórios detalhados sobre desempenho nas sessões de perguntas.
- Integração com bases de dados mais robustas, como SQLite ou PostgreSQL.

---

**Autor:** Emerson  
**Objetivo:** Aprender e aplicar conhecimentos em Python enquanto crio ferramentas úteis para meus estudos!
