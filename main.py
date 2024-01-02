import numpy as np
my_list= [1,2,3]
print(my_list)


arr = np.array(my_list)
print(arr)

my_mat =[[1,2,3],[4,5,6],[7,8,9]]
arr2 = np.array(my_mat)
print(arr2)


arr3 =np.arange(0,10,2)
print(arr3)


arr4 =np.zeros(3)
print(arr4)

##Filas(5) y columnas(5)
arr5 = np.zeros((5,5))
print(arr5)

##Filas(2) y columnas(3)
arr6 = np.zeros((2,3))
print(arr6)


arr7 =np.ones(4)
print(arr7)

arr8 =np.ones((3,4))
print(arr8)

arr9 = np.linspace(0,5,100)
print(arr9)

##Matriz identidad
arr10 =np.eye(4)
print(arr10)

##numeros aleatorios
arr11 =np.random.rand(5)
print(arr11)

##Numeros aleatorios matriz
arr12 =np.random.rand(5,5)
print(arr12)


##Numeros aleatorios
arr13 =np.random.randn(2)
print(arr13)

##Numeros aleatorios matriz
arr14 =np.random.randn(4,4)
print(arr14)

##Numeros aleatorios entre dos numeros(entre 1 y 10)
arr15 =np.random.randint(1,10)
print(arr15)

##Numeros aleatorios entre dos numeros(entre 1 y 100).El 100 no se incluye y le pasamos la cantidad de numeros
## que queremos que para este caso sera 5
arr16 =np.random.randint(1,100,5)
print(arr16)


ranarr = np.random.randint(0,50,10)
print(f'Los valores obtenidos son: {ranarr}')

##Obtener valor maximo
ranarr1 = np.max(ranarr)
print(f'El valor maximo es:{ranarr1} y su indice es {ranarr.argmax()}')

##Obtener valor minimo
ranarr1 = np.min(ranarr)
print(f'El valor minimo es:{ranarr1} y su indice es {ranarr.argmin()}')
