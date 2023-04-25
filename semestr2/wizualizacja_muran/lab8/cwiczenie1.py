import numpy as np

def Change(A, x):
    output = A.copy()
    output[output == 0] = x

    return output

my_array = np.array([num for num in range(10, 40, 2)])
print(my_array.shape)
my_array = my_array.reshape(3, 5)
print(my_array)
my_array = np.resize(my_array, (10, 10))
print(my_array)

# Reshape musi odpowiadać ilości danych w macierzy oraz zmienia jej kształt
# Resize zmienia wielkość macierzy na dowolną, uzupełniając nowe wiersza wiersze jeśli wymiar będzie większy

my_array += 3
print(my_array)

my_array *= 2
print(my_array)

my_array[my_array % 6 == 0] = 0
print(my_array)

print(Change(my_array, 70))
