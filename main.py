cores = ['preto', 'branco', 'bege', 'cinza', 'marrom', 'vermelho', 'vinho', 'amarelo', 'amarelo claro', 'laranja', 'verde folha', 'verde claro', 'verde musgo', 'azul royal', 'azul bb', 'azul marinho', 'turquesa', 'rosa bb', 'rosa pink', 'roxo', 'lilás']
resultado = []
length = 0

print("Tá faltando?")
print("sim = 'y', não = 'qualquer tecla'")

for i in range(len(cores)):

    apd = str(input(f'{cores[length]}: '))
    if apd == "y":
        resultado.append(cores[length])
        
    length += 1
        
resultado = ', '.join(resultado)

print(resultado)
