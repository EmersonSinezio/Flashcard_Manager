from views.flashcard import (
    selecionar_materia,
    adicionar_flashcard,
    remover_flashcard,
    editar_flashcard,
    comecar_flashcards,
)
from models.database import inicializar_db

def menu_principal():
    inicializar_db()

    while True:
        materia = selecionar_materia()
        print(f"\nGerenciando flashcards para: {materia}")

        print("\nEscolha uma opção:")
        print("1. Adicionar flashcard")
        print("2. Remover flashcard")
        print("3. Editar flashcard")
        print("4. Começar a perguntar")
        print("5. Trocar de matéria")
        print("6. Sair")

        opcao = int(input("Opção: "))

        if opcao == 1:
            adicionar_flashcard(materia)
        elif opcao == 2:
            remover_flashcard(materia)
        elif opcao == 3:
            editar_flashcard(materia)
        elif opcao == 4:
            comecar_flashcards(materia)
        elif opcao == 5:
            continue
        elif opcao == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
