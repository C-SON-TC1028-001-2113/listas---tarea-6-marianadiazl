def main():
    x=-1
    suma=0
    a=1
    b=1
    lista=[]
    while x <= -1 :
        x = int(input())
    if x == 0 :
        print(lista)
    elif x == 1 :
        lista.append(0)
        print(lista)
    elif x == 2:
        lista.append(0)
        lista.append(1)
        print(lista)
    else :
        lista.append(0)
        lista.append(1)
        lista.append(1)
        for i in range(x-3) :
            suma = a + b
            b = a
            a = suma
            lista.append(suma)
        print(lista)
    
    pass

if __name__=='__main__':
    main()
