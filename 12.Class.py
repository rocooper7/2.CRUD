class Person: #Se pone la clase en forma de Camel Case: EjemploDeNomenclatura, estructura
    def __init__(self,name,age):
        self.name = name
        self.age = age    
    
    def say_hello(self): #Puede haber otra función interna
        print('Hello my name is {} and I am {} years old'.format(self.name,self.age))

if __name__ == '__main__':
    name = input('Cual es tu nombre?')
    edad = input('Cual es tu edad?')
    person = Person(name,edad)
    print('Age: {}'.format(person.age))
    print('Name: {}'.format(person.name))
    person.say_hello()
