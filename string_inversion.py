from stack import Stack

start = True

def invert_word(word):
    pilha = Stack()
    formatted_word = word.upper().replace(" ", "")
    inverted_word = ''

    for x in formatted_word:
        pilha.push(x)
    for _ in formatted_word:
        inverted_word += pilha.pop()
    return inverted_word

while start:
    word = input('Insira uma palavra: ')

    if (word.replace(" ", "") == '' or word is None):
        continue
    
    if (len(word.replace(" ", "")) < 2):
        print('\n[ATENÇÃO] A palavra inserida deve ter mais de um caractere.\n')
        continue

    print(invert_word(word))
    decision = input('Finalizar programa (S/N): ').upper()
    start = decision != 'S'