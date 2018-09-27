import sys
import deleteimages
import OverlayBB

if __name__ == "__main__":
    if sys.argv[1] == "--del":
        deleteimages.loop()

    if sys.argv[1] =="--overlay":
        OverlayBB.run()