area_triangulo = lambda base, altura: (base * altura) / 2
print(area_triangulo(10, 5))

numeros=[1,2,3,5,7,11,13]
multiplos_3 = list(filter(lambda n: n % 3 == 0, numeros))
numeros_por_5 = list(map(lambda n: n * 5, numeros))
print(multiplos_3, numeros_por_5)
