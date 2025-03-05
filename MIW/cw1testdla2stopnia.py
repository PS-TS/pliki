import numpy as np
from itertools import combinations

if __name__ == '__main__':
    file_path = 'values.txt'  # Path to your file
    array = np.loadtxt(file_path, dtype=int)
    print(array)

    # Extract decisions
    decisions = array[:, 6]

    # Iterate over all pairs of attributes (combinations of columns)
    for col1, col2 in combinations(range(6), 2):
        print(f"\nChecking rules for attributes {col1+1} and {col2+1}:")

        # Iterate over each row
        for z in range(len(array)):
            value1 = array[z, col1]
            value2 = array[z, col2]
            decision_value = decisions[z]

            # Check if this pair of attribute values always leads to the same decision
            consistent = True
            for x in range(len(array)):
                if (array[x, col1] == value1 and array[x, col2] == value2 and 
                        decisions[x] != decision_value):
                    consistent = False
                    break

            if consistent:
                print(f"Rule: ({col1+1}={value1}, {col2+1}={value2}) -> Decision {decision_value}")
