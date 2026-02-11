def pedirOp():
    while True:
        print('[1] = Comprimento(m)\n[2] = Capacidade(l)\n[3] = Massa(g)\n[4] = \033[31mSair\033[m')
        try:
            op = int(input('Digite sua escolha: '))
        except ValueError:
            continue
        if op not in range(1,5): continue
        return op

unidades = {
    'comprimento': {'mm':0.001, 'cm':0.01, 'dm':0.1, 'm':1, 'dam':10, 'hm':100, 'km':1000},
    'capacidade': {'ml':0.001, 'cl':0.01, 'dl':0.1, 'l':1, 'dal':10, 'hl':100, 'kl':1000},
    'massa': {'mg':0.001, 'cg':0.01, 'dg':0.1, 'g':1, 'dag':10, 'hg':100, 'kg':1000}
}

def pedirUnidade(fluxo, op):
    tipo_medida = {1:'comprimento', 2:'capacidade', 3:'massa'}[op]
    unidades_tipo = unidades[tipo_medida]
    
    if fluxo == 1:
        mensagem = 'Unidade de origem: '
    else:
        mensagem = 'Unidade desejada: '

    while True:
        print(f"Unidades disponíveis: {', '.join(unidades_tipo.keys())}")
        unidade = input(mensagem).strip().lower()
        if unidade in unidades_tipo:
            return [unidades_tipo[unidade], unidade]

def pedirQuantidade(uni):
    while True:
        try:
            quantidade = float(input(f'Quantos {uni}? '))
        except ValueError:
            continue
        if quantidade <= 0: continue
        return quantidade

def converterMedidas(quant, uni):
    return quant * uni


print(f'Bem-vindo ao conversor de medidas.')

op = pedirOp()
if op != 4:
    unidade1 = pedirUnidade(1, op)
    quantidade = pedirQuantidade(unidade1[1])
    unidadeBase = quantidade * unidade1[0]
    unidade2 = pedirUnidade(2, op)
    quantidadeConvertida = converterMedidas(unidadeBase, 1/unidade2[0])  
    print(f'\033[33m{quantidade:.2f}{unidade1[1]}\033[m => \033[32m{quantidadeConvertida:.2f}{unidade2[1]}\033[m')

print('Obrigado por usar o conversor!')