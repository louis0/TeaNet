import os

def delete(f):
    if not (os.path.exists(f + ".XML") or os.path.exists(f + ".xml")):
        os.remove(f + ".JPEG")

def loop():
    for i in os.listdir():
        if i[-5:] == ".JPEG":
            delete(i[:-5])


if __name__ == '__main__':
    loop()