import numpy as np

def readfile(name):
    file = open(name, 'r')
    length = int(file.readline())
    # print(length)
    # data_arr = np.zeros(length, dtype=np.unicode_)
    data = []
    for i, line in enumerate(file):
        data.append(line)
        # data_arr[i] = line
        print(line)
    # print(data)
    return data

def main():
    name = 'a_example.txt'
    data = readfile(name)
    print(data)


if __name__ == '__main__':
    main()
