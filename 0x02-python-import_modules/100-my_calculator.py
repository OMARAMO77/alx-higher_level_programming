#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    n = len(argv) - 1
    if n == 3:
        if argv[2] == '+':
            result = add(int(argv[1]), int(argv[3]))
            print('{:s} + {:s} = {:d}'.format(argv[1], argv[3], result))
        elif argv[2] == '-':
            result = sub(int(argv[1]), int(argv[2]))
            print('{:s} - {:s} = {:d}'.format(argv[1], argv[3], result))
        elif argv[2] == '*':
            result = mul(int(argv[1]), int(argv[2]))
            print('{:s} * {:s} = {:d}'.format(argv[1], argv[3], result))
        elif argv[2] == '/':
            result = div(int(argv[1]), int(argv[2]))
            print('{:s} / {:s} = {:d}'.format(argv[1], argv[3], result))
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
