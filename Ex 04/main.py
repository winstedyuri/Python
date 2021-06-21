def repstr(string, length):
    return (string * length)

def funcao_yuri (tamanhoDaLinha):
    frase = repstr("_", tamanhoDaLinha)
    return frase

tamanho =  int(input("Qual o tamanho da linha?"))

invocandoAFuncao = funcao_yuri(tamanho)

print(invocandoAFuncao) 