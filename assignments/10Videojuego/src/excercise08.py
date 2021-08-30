def main():
    # escribe tu código abajo de esta línea
    j_nuevos = int(input('dame la cantidad de juegos nuevos'))
    j_usados = int(input('dame la cantidad de juegos usados'))
    m = (j_nuevos*1000)+(j_usados*350)
    print('El total de su compra es de:', m)


if __name__ == '__main__':
    main()
