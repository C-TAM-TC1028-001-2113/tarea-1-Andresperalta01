def main():
    # escribe tu código abajo de esta línea
    from math import ceil
    num_palabras = int(input('Dame el numero de palabras:'))
    if num_palabras <= 475:
        costo = 54.0
        print('el costo de la publicacion es:', costo)
    else:
        paginas = float(num_palabras) / 475
        total_pag = int(ceil(paginas))
        costo = float(total_pag*54)
        print('el costo de la publicacion es:', costo)




if __name__ == '__main__':
    main()
