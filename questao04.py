print("--- Inicio ---")

# resolução a):

print("a) -------------------------->")
entrada = [1,2,3,4,5,6,7,8,9,10]
saida = []
numero = 0
for i in entrada:
    if i % 2 != 0:
        numero = i
        saida.append(i)


print(f"O proximo numero da sequência é: {numero}")
print(saida)

# resolução b)
print("b) -------------------------->")
entrada = 1
ultimo = 0
while entrada <= 100:
    entrada *= 2
    ultimo = entrada
    print(entrada)
print(f"O proximo numero da sequência (2, 4, 8, 16, 32, 64) é: {ultimo}")

# resolução c)
print("c) -------------------------->")
entrada = 2

ultimo = 0

for i in range(0, 8):
    ultimo = i * i
    print(ultimo)
print(f"O proximo numero da sequência (0, 1, 4, 9, 16, 25, 36) é: {ultimo}")

# resolução d)
print("d) -------------------------->")
entrada = 2
ultimo = 0

for i in range(0, 12):
    if i % 2 == 0:
        ultimo = i * i
        print(ultimo)
print(f"O proximo numero da sequência (4, 16, 36, 64) é: {ultimo}")

# resolução e)
print("e) -------------------------->")
fibonacci = [0, 1]
ultimo = 0
for i in range(2, 8):  # Itera de 2 até o número fornecido
# O próximo nmero da sequência 
    proximo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo) 
    ultimo = proximo
print(fibonacci)    
print(f"O proximo numero da sequência (1, 1, 2, 3, 5, 8) é: {ultimo}")

# resolução f)
print("f) -------------------------->")
    
print("Como não há um padrão dominante, acredito que o próximo numero da sequencia seja 20. Pois, observando a diferença entre os termos -> 8,2,4,1,1,1 a tendencia é que o padrão se repita mais uma vez. Assim, conclui-se que a resposta seja 20.")
print("--- Fim ---")