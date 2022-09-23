from unittest import result


sum = lambda a,b: a+b
minus = lambda a,b: a-b
mult = lambda a,b: a*b
div = lambda a,b: a/b
degree = lambda a,b: a**b

def calc(op, a,b):
    return op(a,b)

def opChoice(key,a,b):
    dictOper = {
        '+': sum,
        '-': minus,
        '*': mult,
        '/': div,
        '^': degree
}
    result = calc(dictOper[key], a, b)
    return result