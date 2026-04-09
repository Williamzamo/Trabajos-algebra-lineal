from sympy import Matrix, Rational

MATRICES = {
    "1": ("2x2 básica", Matrix([
        [2, 4],
        [1, 3]
    ])),
    "2": ("3x4 sistema del proyecto", Matrix([
        [1,  2, -1,  8],
        [2, -3,  4, -2],
        [3,  1,  2,  9]
    ])),
    "3": ("4x5 sistema ampliado", Matrix([
        [1,  2, -1,  0,  5],
        [2, -1,  3,  1,  8],
        [0,  1, -2,  4,  3],
        [3,  0,  1, -1,  7]
    ])),
    "4": ("3x3 singular", Matrix([
        [1, 2, 3],
        [2, 4, 6],
        [0, 1, 2]
    ]))
}

def seleccionar_matriz():
    print("\nSelecciona una matriz")
    for clave, (nombre, mat) in MATRICES.items():
        print(f"{clave}. {nombre}:\n{mat}\n")
    opcion=input("Opción: ")
    nombre, mat=MATRICES[opcion]
    print(f"\nTrabajando con: {nombre}")
    return mat.copy()

def intercambiar_filas(M):
    print(f"\nMatriz actual:\n{M}")
    i=int(input("Índice de la primera fila (0 a n-1): "))
    j=int(input("Índice de la segunda fila (0 a n-1): "))
    M[i, :], M[j, :]=M[j, :].copy(), M[i, :].copy()
    print(f"Filas {i} y {j} intercambiadas.")
    return M

def multiplicar_fila(M):
    print(f"\nMatriz actual:\n{M}")
    i=int(input("Índice de la fila a multiplicar (0 a n-1): "))
    k=Rational(input("Escalar (puede ser fracción como '1/2'): "))
    M[i, :]=k * M[i, :]
    print(f"Fila {i} multiplicada por {k}.")
    return M

def eliminar_debajo(M, fila_pivote, col_pivote):
    for i in range(fila_pivote+1, M.rows):
        if M[fila_pivote, col_pivote]!=0:
            factor=M[i, col_pivote]/M[fila_pivote, col_pivote]
            M[i, :]=M[i, :]-factor*M[fila_pivote, :]
    return M

def eliminacion_gauss(M):
    M_temp=M.copy()
    fila_pivot=0
    pivotes=[]
    for col in range(M_temp.cols):
        if fila_pivot>=M_temp.rows:
            break
        for i in range(fila_pivot, M_temp.rows):
            if M_temp[i, col]!=0:
                M_temp[i, :], M_temp[fila_pivot, :]=M_temp[fila_pivot, :].copy(), M_temp[i, :].copy()
                break
        else:
            continue
        pivotes.append((fila_pivot, col, M_temp[fila_pivot, col]))
        M_temp[fila_pivot, :]=M_temp[fila_pivot, :]/M_temp[fila_pivot, col]
        M_temp=eliminar_debajo(M_temp, fila_pivot, col)
        fila_pivot+=1
    return M_temp, pivotes

def mostrar_pivotes(pivotes):
    print("\nPivotes")
    for fila, col, val in pivotes:
        print(f"  Fila {fila}, Columna {col} --> valor original: {val}")

A = seleccionar_matriz()
while True:
    print("\nOPERACIONES")
    print("1. Intercambiar filas")
    print("2. Multiplicar fila por escalar")
    print("3. Eliminación Gaussiana completa")
    print("4. Ver matriz actual")
    print("5. Cambiar de matriz")
    print("6. Salir")

    f = input("\nOpción: ")

    if f == "1":
        A = intercambiar_filas(A)
    elif f == "2":
        A = multiplicar_fila(A)
    elif f == "3":
        A, pivotes = eliminacion_gauss(A)
        print("\nForma Escalonada (REF):")
        print(A)
        mostrar_pivotes(pivotes)
    elif f == "4":
        print(f"\n{A}")
    elif f == "5":
        A = seleccionar_matriz()
    elif f == "6":
        break