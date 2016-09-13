class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast


try:
    text = str(input('Ingrese algo --> '))
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
    print(text + "estuvo bien")
except EOFError:
    print('por que me diste un EOF?')
except ShortInputException as ex:
    print(('ShortInputException: La entrada fue de' +
           '{0} de longitud, se esperaba al menos {1}')
          .format(ex.length, ex.atleast))
else:
    print('No hubo ningua excepcion')