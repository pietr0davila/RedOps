
def maskify(cc: str):
    # args: cc = credit number
    # returns: masked string
    last = cc[-4:] # -4: reserva os 4 indices antes do final
    start = cc[:-4] # :-4 Excluí somente os últimos 4
    for text in start:
        text = '#'
        last = text + last
        
    return last

# Correção:

# def maskify(cc: str):
#     return "#"*len(cc) - 4 + cc[-4:]

maskify("1234567889")