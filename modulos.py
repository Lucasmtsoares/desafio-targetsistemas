class ResolverProblemas:
    def Fibonacci(numero):
        sf = [0, 1]
        for i in range(2, numero+2):  # Itera de 2 até o número fornecido
        # O próximo nmero da sequência 
            proximo = sf[-1] + sf[-2]
            sf.append(proximo) #insere a soma do ultimo com o anterior
            if proximo >= numero:
                break
        
        if numero in sf: 
            return "O número FAZ parte da sequência de Fibonacci!" 
        else: #em caso de zero correspondencias então significa que o numero não faz parte da sequencia
            return "O número NÂO FAZ parte da sequência de Fibonacci!"
        
    def Verificar_caracter(palavra):
        palavra = palavra.upper() #coverte a palavra em maiuscula
        div = []
        div.extend(palavra) #reparte a palavra em tokens
        repeticao_a = div.count('A') #verifica 
        print(div)
        return repeticao_a
    

            
        
        