import math

class Scanner:

    def scan(self):
        result = ""
        print("Ahora ingresaras los numeros del ROMPECABEZAS por FILAS. Usa 0 para indicar EL ESPACIO EN BLANCO")
        print()
        datos = []
        for i in range(9):
            x = math.trunc(i / 3)
            y = i % 3
            print("Dame el dato numero " + str(x) + "," + str(y) + ": ")
            nuevoDato = int(input())
            datos.append(nuevoDato)

        puzzle = ''.join(str(e) for e in datos)
        result = puzzle
        for j in range(9):
            if j not in datos:
                print("\n" + "ERROR!!! NO agregaste un numero a la lista o agregaste un numero inadecuado")
                print("Recuerda que DEBE CONTENER LOS NUMEROS DEL 0 al 8")
                result = ""
                break

        print()
        print("La numeros del rompecabezas son: ")
        print()
        for i, char in enumerate(puzzle):
            print(char, end=" ")
            if (i + 1) % 3 == 0:
                print()
        return result
