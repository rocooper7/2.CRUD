import random # Utilizamos nuetro módulo random

def binary_search(data,target,low,high): #Se utiliza la recursión
    if low > high: #Para saber si se paso del indice inicial
        return False
    mid = (low + high) // 2 #Con parentesis pq es una operación

    if target == data[mid]:
        return True
    elif target < data[mid]:
        return binary_search(data,target,low,mid - 1) #Esto es la recursión de la función
    else:
        return binary_search(data,target,mid + 1,high) #Recursión   
    
    
if __name__ == '__main__': #Punto de entrada de nuestra aplicación
    data = [random.randint(0,100) for i in range(10)] #list comprehension en lugar de for
    data.sort() #modifíca directamente la variable 
    # sorted data = sorted(data) #No modifica nuestra primera variable
    
    print(data) #[15, 26, 31, 36, 49, 54, 59, 79, 88, 89]

    target = int(input('What number would you like to find?')) #49,35 
    found = binary_search(data,target,0,len(data)-1)  
        
    print(found) #True,False
