from stack import Stack

start = True

def is_input_valid(input):
    pilha = Stack()
    formatted_input = input.replace(" ", "")
    for x in formatted_input:
        if x == "(":
            pilha.push(x)
        elif x == ")":
            if len(pilha) == 0:
                return False
            pilha.pop()

    return len(pilha) == 0

while start:
    user_input = input('Insira uma expressão utilizando parênteses: ')

    if (user_input.replace(" ", "") == '' or user_input is None):
        continue
    
    if (len(user_input.replace(" ", "")) < 2):
        print('\n[ATENÇÃO] O input inserido deve ter mais de um caractere.\n')
        continue

    if(is_input_valid(user_input)):
        print('Os parênteses estão balanceados!\n')
    else:
        print('Os não parênteses estão balanceados :(\n')

    decision = input('Finalizar programa (S/N): ').upper()
    start = decision != 'S'