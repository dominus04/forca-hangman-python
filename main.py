import random
import os


def choose_word():
    word = random.choice(words)
    return word


def print_hangman(x):
    if x == 0:
        print("|-----------|\n"
              "|           |\n"
              "|           O\n"
              "|          /|\\\n"
              "|          / \\\n"
              "|            \n"
              "|            \n", end="|  ")

    elif x == 1:
        print("|-----------|\n"
              "|           |\n"
              "|           O\n"
              "|          /|\\\n"
              "|          / \n"
              "|            \n"
              "|            \n", end="|  ")
    elif x == 2:
        print("|-----------|\n"
              "|           |\n"
              "|           O\n"
              "|          /|\\\n"
              "|            \n"
              "|            \n"
              "|            \n", end="|  ")
    elif x == 3:
        print("|-----------|\n"
              "|           |\n"
              "|           O\n"
              "|          /|\n"
              "|            \n"
              "|            \n"
              "|            \n", end="|  ")
    elif x == 4:
        print("|-----------|\n"
              "|           |\n"
              "|           O\n"
              "|           |\n"
              "|            \n"
              "|            \n"
              "|            \n", end="|  ")
    elif x == 5:
        print("|-----------|\n"
              "|           |\n"
              "|           O\n"
              "|            \n"
              "|            \n"
              "|            \n"
              "|            \n", end="|  ")
    elif x == 6:
        print("|-----------|\n"
              "|           |\n"
              "|            \n"
              "|            \n"
              "|            \n"
              "|            \n"
              "|            \n", end="|  ")


f = open('Random Words.txt', 'r')
words = f.readlines()
f.close()

start = input("Digite 1 para iniciar o jogo: ")
os.system('cls')

while start != 0:

    word_chose = list(choose_word())
    word_chose.pop(len(word_chose)-1)
    display = []
    life = 6
    tries = []

    for letter in word_chose:
        display += "_"

    os.system('cls')
    print("Letras tentadas: ", end="")

    for letra in tries:
        print(letra.upper(), end=" - ")
    print("\n")

    print_hangman(life)

    while life > 0:

        if word_chose == display:
            break

        for i in display:
            print(i, end=" ")

        answer = input("\n\nTente advinhar uma letra: ")

        os.system('cls')

        if answer not in tries and answer != "":
            tries.append(answer)
            for i in range(len(word_chose)):
                if word_chose[i] == answer:
                    display[i] = answer

            if answer not in display:
                life -= 1

            print("Letras tentadas: ", end="")

            for letra in tries:
                print(letra.upper(), end=" - ")
            print("\n")
            print_hangman(life)
        else:

            print("Letras tentadas: ", end="")

            for letra in tries:
                print(letra.upper(), end=" - ")
            print("\n")
            print("Você já tentou esta letra.\n")
            print_hangman(life)

            if word_chose == display:
            break

    if life >= 1:
        print("\n\n\n\nParabéns você venceu o jogo!!")
    else:
        print("\n\nFim de jogo, a palavra era %s" % ''.join(word_chose))

    start = input("\n\nSe quiser iniciar outro jogo digite 1, caso contrário digite 0: ")
