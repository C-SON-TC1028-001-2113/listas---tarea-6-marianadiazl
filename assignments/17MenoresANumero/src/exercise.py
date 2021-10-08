def menoresDiez(x):
    m=[]
    for i in range(len(x) ):
        for j in range(len(x[i])):
            if x[i][j]<10 :
                m.append(x[i][j])
    return(m)

def main():
    lista = []
    fila = int(input())
    columna = int(input())
    for i in range(fila):
        lista.append([])
        for j in range(columna):
            n = int(input())
            lista[i].append(n)
    r=menoresDiez(lista)
    print(r)
   



if __name__=='__main__':
    main()
