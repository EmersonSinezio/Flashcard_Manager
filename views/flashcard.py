import random
from models.database import carregar_flashcards, salvar_flashcards

def selecionar_materia():
    dados = carregar_flashcards()
    materias = list(dados.keys())

    print("\nMatérias disponíveis:")
    for i, materia in enumerate(materias, 1):
        print(f"{i}. {materia}")
    print(f"{len(materias) + 1}. Criar nova matéria")

    escolha = int(input("Escolha uma matéria: "))

    if escolha == len(materias) + 1:
        nova_materia = input("Digite o nome da nova matéria: ").strip()
        if nova_materia in materias:
            print("Essa matéria já existe!")
            return selecionar_materia()
        dados[nova_materia] = []
        salvar_flashcards(dados)
        return nova_materia

    return materias[escolha - 1]

def adicionar_flashcard(materia):
    dados = carregar_flashcards()
    pergunta = input("Digite a pergunta: ").strip()
    resposta = input("Digite a resposta: ").strip()
    dados[materia].append({"pergunta": pergunta, "resposta": resposta})
    salvar_flashcards(dados)
    print("Flashcard adicionado com sucesso!")

def remover_flashcard(materia):
    dados = carregar_flashcards()
    flashcards = dados[materia]

    if not flashcards:
        print("Não há flashcards nesta matéria.")
        return

    print("\nFlashcards disponíveis:")
    for i, flashcard in enumerate(flashcards, 1):
        print(f"{i}. {flashcard['pergunta']}")

    escolha = int(input("Escolha o flashcard para remover: ")) - 1
    flashcards.pop(escolha)
    salvar_flashcards(dados)
    print("Flashcard removido com sucesso!")

def editar_flashcard(materia):
    dados = carregar_flashcards()
    flashcards = dados[materia]

    if not flashcards:
        print("Não há flashcards nesta matéria.")
        return

    print("\nFlashcards disponíveis:")
    for i, flashcard in enumerate(flashcards, 1):
        print(f"{i}. {flashcard['pergunta']}")

    escolha = int(input("Escolha o flashcard para editar: ")) - 1
    flashcard = flashcards[escolha]

    nova_pergunta = input(f"Nova pergunta (atual: {flashcard['pergunta']}): ").strip()
    nova_resposta = input(f"Nova resposta (atual: {flashcard['resposta']}): ").strip()

    flashcard['pergunta'] = nova_pergunta or flashcard['pergunta']
    flashcard['resposta'] = nova_resposta or flashcard['resposta']
    salvar_flashcards(dados)
    print("Flashcard editado com sucesso!")

def comecar_flashcards(materia):
    dados = carregar_flashcards()
    flashcards = dados[materia]

    if not flashcards:
        print("Não há flashcards nesta matéria.")
        return

    acertos = 0
    total = 0

    while True:
        flashcard = random.choice(flashcards)
        print("\nPergunta:", flashcard['pergunta'])
        resposta = input("Sua resposta: ").strip()

        if resposta.lower() == flashcard['resposta'].lower():
            print("Resposta correta!")
            acertos += 1
        else:
            print(f"Resposta incorreta. Resposta correta: {flashcard['resposta']}")

        total += 1
        percentual_acerto = (acertos / total) * 100

        print(f"\nAcertos: {acertos}/{total} ({percentual_acerto:.2f}%)")

        if percentual_acerto >= 80:
            print("Parabéns! Você atingiu 80% de acerto.")
            break
