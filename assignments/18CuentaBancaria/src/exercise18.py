def main():
    # escribe tu código abajo de esta línea
    saldo_anterior = float(input('dame el saldo del mes anterior'))
    ingresos = float(input('dame el numero de ingresos'))
    egresos = float(input('dame el numero de egresos'))
    num_cheques = int(input('dame el numero de cheques expedidos'))
    final = saldo_anterior+ingresos-egresos-(num_cheques*13)
    print('el saldo final de la cuenta es de:', final)


if __name__ == '__main__':
    main()
