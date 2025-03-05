import numpy as np

if __name__ == '__main__':
    file_path = 'values.txt'
    array = np.loadtxt(file_path, dtype=int)
    print(array)
    decisions = array[:, 6]

    for z in range(len(array)):
        for y in range (6):
            test = True
            wartosc = array[z,y]
            decyzja = decisions[z]
            for x in range(len(array)):
                if array[x,y] == wartosc and decisions[x] != decyzja:
                    test = False
                    break
            if test:
                print(f"Rzad {z+1} Kolumna {y+1} = {wartosc} Wynik {decyzja}")
