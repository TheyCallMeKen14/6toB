def fibinacci_ciclos(n):
    ant = 1
    post = 1
    
    #caso base
    if n == 1 or n == 0:
        return 1
    
    while n:
        if n == 1:
            return ant
        
       ant = ant + post
       n = n -1 
       post = ant - post
       
resultado = fibonacci_ciclos(8)
print(resultado)


# Fibonacci recursivo
def fibonacci_recursivo(n):
    
    # caso base
    if n == 1 or n == 0:
        return 1
    
    # caso recursivo
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo( n - 2)

resultado = fibonacci_recursivos(8)
print(resultado)



# !4 = 4 x 3 x 2 x 1 = 24
# !5 = 5 x 4 x 3 x 2 x 1 = 120

# caso base


def fact_recursivo(n):
    
    
    if n == 1 or n == 0:
        return
    
    
    return n * fact_recursivo(n-1)
    
resultado = fibonacci_recursivos(8)
print(resultado)













