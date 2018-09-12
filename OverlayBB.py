import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import PIL

import os

def get_files():
    fileList = []
    for i in os.listdir():
        if i[-4:] == (".XML" or ".xml"):
            fileList.append(i)

    return fileList


def get_dataset(fileList):
    dataset = []

    for i in fileList:
        a = get_coords(i)
        dataset.append(a)

    return dataset


def get_coords(f):
    """
    :param f: xml file
    :return: list in format: [picture id, xmin, xmax, ymin, ymax]
    """
    tree = ET.parse(f)
    root = tree.getroot()

    coordList = []
    coordList.append(f[10:-4])

    for i in root.findall('bndbox'):
        xmin = i.find('xmin').text
        xmax = i.find('xmin').text
        ymin = i.find('ymin').text
        ymax = i.find('ymax').text

    coordList.append(xmin)
    coordList.append(xmax)
    coordList.append(ymin)
    coordList.append(ymax)

    return coordList

def displayImage(list):
    im = np.array(PIL.Image.open("n03797390_999.JPEG"))


    fig, ax = plt.subplots(1)

    ax.imshow(im)
    rect = patches.Rectangle((list[1], list[3]), list[2]-list[1], list[4]-list[2], linewidth=10, edgecolor='y')
    ax.add_patch(rect)
    plt.gca().invert_yaxis()
    plt.show()



if __name__ == '__main__':
    print("a")
    displayImage([0,10,100,10,100])
