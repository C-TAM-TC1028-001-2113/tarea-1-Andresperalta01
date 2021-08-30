def main():
    # escribe tu código abajo de esta línea
    msjs = int(input('dame el numero de mensajes'))
    megs = float(input('dame el numero de megas'))
    min = int(input('dame el numero de minutos'))
    m = (msjs+megs+min) * 0.8
    print('el costo mensual es de:', m)


if __name__ == '__main__':
    main()
