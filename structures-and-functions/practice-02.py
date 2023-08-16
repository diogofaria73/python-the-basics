# 4) Crie um programa que sorteia aleatoriamente um número inteiro menor que 100
from random import choice
from math import pow

start = -100
stop = 0
step = 1

dynamic_range = range(start, stop, step)

print(f'Sorted number from dynamic range: {choice(dynamic_range)}')

# 5) Crie um programa que solicite à pessoa usuária digitar dois números inteiros e calcular a potência do 1º número elevado ao 2º.

first_input = int(input('Type a number: '))
second_input = int(input('Type another number: '))

print(f'{first_input} to the power of {second_input} is {pow(first_input, second_input)}')
