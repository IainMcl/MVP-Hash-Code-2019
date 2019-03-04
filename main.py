import numpy as np
import sys

class Image:
    def __init__(self, string, index):
        # takes line from input, makes image object with it
        string_list = string.split(" ")
        if(string_list[0] == "H"):
            self.HV = 0  # 0 == horizontal
        else:
            self.HV = 1  # 1 == Vertical
        self.tag_number = string_list[1]
        self.tag_list = string_list[2:]
        self.origenal_pos = index

class SlideShow:
    def __init__(self, images):
        self.image_list = images
        self.length = self.calc_len()

    def calc_len(self):
        nslides = len(self.image_list)
        for pic in self.image_list:
            # print(pic.origenal_pos)
            if pic.HV == 1:
                nslides -= 0.5
        if nslides - int(nslides) != 0:
            print("Incompatable number of verticle slides.")
        self.length = int(nslides)
        return int(nslides)

    def shuffle_order(self):
        np.random.shuffle(self.image_list)

        first_vert = 0
        found_vert = 0

        for i in range(len(self.image_list)):
            if self.image_list[i].HV == 1:
                if(found_vert % 1 == 0):
                    self.swap_positions(first_vert, i-1)
                else:
                    first_vert = i
                found_vert += 0.5
            # print(found_vert)

        return self.image_list


    def swap_positions(self, index1, index2):
        temp = self.image_list[index1]
        self.image_list[index1] = self.image_list[index2]
        self.image_list[index2] = temp
        return 1

    def make_output(self):
        nslides = len(self.image_list)
        for pic in self.image_list:
            if pic.HV == 1:
                nslides -= 0.5
        if nslides - int(nslides) != 0:
            print("Incompatable number of verticle slides.")
            sys.exit()
        # output = np.zeros((int(nslides+1), 3), dtype=str)
        output = []
        # output[0][0] = str(int(nslides))
        output.append(str(int(nslides)))
        length = len(self.image_list)
        vert = False
        j = 0
        my_itter = iter(range(0, length-1))
        for i in my_itter:
            # print(type(i))
            # print(i)
            if self.image_list[i].HV == 1:
                output.append(str(self.image_list[i].origenal_pos) + ' ' + str(self.image_list[i+1].origenal_pos))
                # print("HERE")
                next(my_itter, None)
            else:
                output.append(str(self.image_list[i].origenal_pos))
        # print(output)
        return output

    def slideshow_score(self):
        # returns the score of all transitions in the slideshow
        score = 0
        for i in range(self.length):
            if(self.image_list[i].HV == 1 and self.image_list[i + 1] == 1):
                temp_image = temp_image(self.image_list[i], self.image_list[i + 1])
                i += 1
        return score

def compare_tags(image1, image2):
    # takes two images and counts number of common tags

    tag_max = min(image1.tag_number, image2.tag_number)
    n = 0
    for i in range(tag_max):
        if(image1.tag_list[i] == image2.tag_list[i]):
            n += 1
    return n


def composite_tags(image1, image2):
    # for two images returns list of unique tags
    duplicate_count = 0

    for i in range(image1.tag_number):
        for j in range(image2.tag_number):
            if(image1.tag_list[i] == image2.tag_list[j]):
                duplicate_count += 1
                j -= 1
                for k in range(j, image2.tag_number):
                    image2.tag_list[k] = image2.tag_list[k + duplicate_count]

    ammended_2 = image2.tag_list[:-duplicate_count]
    shared_list = image1.tag_list.append(ammended_2)
    return shared_list


def temp_image(image1, image2):
    # produces an Image object of the 2 images together (for verticals)
    tags = composite_tags(image1, image2)
    tag_string = ' '.join(tags)
    init_string = "H " + len(tags) + " " + tag_string
    temp = Image(init_string, 0)

    return temp


def transition_score(image1, image2):
    # returns the score for a transition between slide 1 and slide 2
    common_tags = compare_tags(image1, image2)
    unique_slide1_tags = image1.tag_number - common_tags
    unique_slide2_tags = image2.tag_number - common_tags

    return min(common_tags, unique_slide1_tags, unique_slide2_tags)



def readfile(name):
    file = open(name, 'r')
    length = int(file.readline())
    data = []
    for i, line in enumerate(file):
        data.append(line)
    return data


def output(slideshow, outfile='output.txt'):
    out = open(outfile, 'w')
    out.write(str(len(slideshow)-1)+"\n")
    for i in range(1, len(slideshow)):
        line = ''.join(slideshow[i])
        # print(line)
        out.write(line + "\n")
    return 0




def main():
    name = 'c_memorable_moments.txt'
    data = readfile(name)
    images = np.zeros(len(data), dtype=object)
    for i, point in enumerate(data):
        # print(i)
        # print(point)
        images[i] = Image(point, i)
    slideshow = SlideShow(images)
    slideshow.shuffle_order()
    output_slides = slideshow.make_output()

    # sample_slides = ['3', '1 2', '3', '0']
    output(output_slides, outfile='c.txt')


if __name__ == '__main__':
    main()
