import numpy as np

def convert(table: str, transpose: bool = False) -> np.ndarray:
    conv_table = table.replace(",",".").split("\n")
    for i in range(len(conv_table)):
        conv_table[i] = conv_table[i].strip()
    conv_table = [e for e in conv_table if e != ""]
    for i in range(len(conv_table)):
        conv_table[i] = conv_table[i].split()
    data = np.zeros((len(conv_table), len(conv_table[0])))
    shape = data.shape
    for i in range(shape[0]):
        for j in range(shape[1]):
            data[i,j] = float(conv_table[i][j])
    if transpose:
        data = np.transpose(data)
    return data

if __name__ == '__main__':
    pass