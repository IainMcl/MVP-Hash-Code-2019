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
        # print(line)
    # print(data)
    return data

def alt_input():
    n = int(input(""))

    for i in range(n):
        pass

def output(slideshow, outfile='output.txt'):
    out = open(outfile, 'w')
    print(len(slideshow))
    out.write(str(len(slideshow))+"\n")
    for i in range(1, len(slideshow)):
        out.write(str(slideshow[i])+ "\n")
        print(slideshow[i])
    return 0


def main():
    name = 'a_example.txt'
    data = readfile(name)
    # print(data)
    sample_slides = ['3', '1 2', '3', '0']
    output(sample_slides)


if __name__ == '__main__':
    main()
