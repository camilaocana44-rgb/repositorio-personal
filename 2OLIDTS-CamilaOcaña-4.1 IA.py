maxf = 3
maxc = 3
def impresion(a):
 print("\nLos valores de la matriz son:\n")
 for f in range(maxf):
 for c in range(maxc):
 print(a[f][c], end=" ")
 print() # salto de línea por cada fila
 print()
def captura_arreglo(a):
 for f in range(maxf):
 for c in range(maxc):
 a[f][c] = float(input(f"Ingrese el valor para la posicion 
[{f}][{c}]: "))
 return a
def main():
 arreglo_bidimensional = [[0.0] * maxc for _ in range(maxf)]
 print("Captura de valores a una Matriz NxM")
 print(f"\nArreglo Bidimensional ({maxf}x{maxc})\n")
 matriz_resultado = captura_arreglo(arreglo_bidimensional)
 impresion(matriz_resultado)
if __name__ == "__main__":
 main()
