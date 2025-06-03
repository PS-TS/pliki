import numpy as np

if __name__ == '__main__':
    file_path = 'values.txt'
    array = np.loadtxt(file_path, dtype=int)
    decisions = array[:, 6]
    newarray = []
    seen = set()  # Do przechowywania unikalnych wpisów

    for z in range(len(array)):
        for y in range(6):
            wartosc = array[z, y]
            decyzja = decisions[z]
            test = True

            for x in range(len(array)):
                if array[x, y] == wartosc and decisions[x] != decyzja:
                    test = False
                    break

            if test:
                entry = (y + 1, int(wartosc), int(decyzja))
                if entry not in seen:
                    print(f"Rząd {z + 1} Kolumna {y + 1} = {wartosc} Wynik {decyzja}")
                    newarray.append(entry)
                    seen.add(entry)

    print(newarray)

