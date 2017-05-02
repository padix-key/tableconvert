import numpy as np

def convert(table: str, convert_comma: bool = False) -> np.ndarray:
    if convert_comma:
        # convert "," to international "."
        table = table.replace(",",".")
    # separate table into rows
    table = table.split("\n")
    # separate columns by whitespace between values
    for i in range(len(table)):
        table[i] = table[i].split()
    # remove unwanted whitespace
    for i in range(len(table)):
        for j in range(len(table[i])):
            table[i][j] = table[i][j].strip()
    # remove all empty rows
    table = [e for e in table if e != []]
    # create numpy array with same dimensions as the input table
    data = np.zeros((len(table), len(table[0])))
    shape = data.shape
    # fill array with table values
    for i in range(shape[0]):
        for j in range(shape[1]):
            data[i,j] = float(table[i][j])
    return data

if __name__ == '__main__':
    print("Conducting unit test")
    
    table = """
            0,172    0,464    65,586    89
            7        9,8      87,644    897,8
            53       0,123    880       78,85
            """
    
    exp_result = [[1.72000000e-01, 4.64000000e-01, 6.55860000e+01, 8.90000000e+01],
                  [7.00000000e+00, 9.80000000e+00, 8.76440000e+01, 8.97800000e+02],
                  [5.30000000e+01, 1.23000000e-01, 8.80000000e+02, 7.88500000e+01]]
    
    conv_table = convert(table, True)
    
    if (np.array_equal(exp_result, conv_table)):
        print("Success!")
    else:
        print("Failure!")