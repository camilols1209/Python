from NumerosIdenticosException import NumerosIdenticosException

try:
    a=1
    b=1
    if a==b:
        raise NumerosIdenticosException('numeros identicos')
except TypeError as e:
    print(e)