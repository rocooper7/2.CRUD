PASSWORD = '12345'

def password_required (func): #Decoradores Funcion dentro de otra funcion
    def wrapper (): #Wrapper asi se le conoce al afuncion interna en decoradores
        password = input('Cuál es la contraseña?')
        
        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta')
    
    return wrapper

@password_required #Se utilizan los decoradores arriba de nuestras funciones y con @
def needs_password ():
    print ('La contraseña es correcta')

def upper(func):
    def wrapper(*args, **kwargs): # parametros son argumentos que tienen keywords o nombre, o posicionale
        result = func(*args,**kwargs)
        return result.upper()
    
    return wrapper

@upper
def say_my_name(name):
    return 'Hola, {}'.format(name)

if __name__ == '__main__': #Punto de entrada de nuestra aplicación
    print (say_my_name('Rodrigo'))
    needs_password()
