import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
import PIL
import os


def get_files():
    fileList = []
    for i in os.listdir(os.getcwd()):
        if i[-4:] == ".xml" or i[-4:] == ".XML":
            fileList.append(i)

    return fileList


def get_dataset(fileList):
    dataset = []

    for i in fileList:
        a = get_coords(i)
        a.insert(0,i[:-4])
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

    xmin = 0
    xmax = 0
    ymin = 0
    ymax = 0

    for i in root.iter('bndbox'):
        xmin = i.findtext('xmin')
        xmax = i.findtext('xmax')
        ymin = i.findtext('ymin')
        ymax = i.findtext('ymax')

    coordList.append(int(xmin))
    coordList.append(int(xmax))
    coordList.append(int(ymin))
    coordList.append(int(ymax))

    return coordList


def display_image(list):
    im = np.array(PIL.Image.open("n03797390_999.JPEG"))

    fig, ax = plt.subplots(1)

    ax.imshow(im)
    rect = patches.Rectangle((list[1], list[3]), list[2]-list[1], list[4]-list[2], linewidth=5, edgecolor='y', fill=False)
    ax.add_patch(rect)
    plt.gca().invert_yaxis()
    plt.show()


def save_plots(ds):
    for i in range(len(ds)):
        print("processing "+ds[i][0])
        try:
            image = PIL.Image.open(ds[i][0]+".JPEG")
        except:
            continue



        im = np.array(image)

        imsize = image.getbbox()

        dpi = 100
        fig = plt.figure(figsize=(imsize[2]/dpi,imsize[3]/dpi), frameon=False)    #dpi=fig.dpi, figsize=(imsize[2]/image.info['dpi'],imsize[3]/image.info['dpi'])
        ax = plt.Axes(fig, [0., 0., 1., 1.])

        ax.set_axis_off()
        fig.add_axes(ax)

        ax.imshow(im)
        rect = patches.Rectangle((ds[i][1], ds[i][3]), ds[i][2] - ds[i][1], ds[i][4] - ds[i][3], linewidth=2,
                                 edgecolor='y', fill=False)

        ax.add_patch(rect)
        fig.savefig(os.getcwd()+"/mergedimg/"+ds[i][0]+".JPEG")#dpi=fig.dpi)
        plt.close(fig)
        plt.close()


def run():
    fileList = get_files()
    ds = get_dataset(fileList)
    save_plots(ds)

if __name__ == '__main__':
    run()