from stack import Stack

start = True

def is_input_valid(input):
    pilha = Stack()
    formatted_input = input.replace(" ", "")
    half = int(len(formatted_input)/2)

    half_a = formatted_input[:half]
    half_b = formatted_input[half:]

    count_a = 0
    count_b = 0

    for x in half_a:
        if (x == '(' or x == ')' ):
            count_a += 1
    for x in half_b:
        if (x == '(' or x == ')' ):
            count_b += 1

    return count_a == count_b

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