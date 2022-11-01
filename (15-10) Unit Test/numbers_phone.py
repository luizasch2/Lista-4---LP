def number_phone_br(number):
    try:
        #verificando pela tabela ASCCI
        number = ''.join([n for n in number if ord(n) >= 48 and ord(n) <= 57])
    except TypeError:
        return number
    if number[0:2] == '55':
        number = number[2:]
    elif len(number) == 9:
        number = '21' + number
    return int(number)
    


    






        


