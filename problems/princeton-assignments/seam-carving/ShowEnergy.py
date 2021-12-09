from Picture import Picture
from SeamCarver import SeamCarver
from SCUtility import SCUtility
import sys


def main(filename):
    picture = Picture(filename=filename)
    print(f"Image is {picture.width()} columns by {picture.height()} rows\n")
    picture.show()
    print(picture.image)
    
    sc = SeamCarver(picture)
    print(f"Displaying energy calculated for each pixel.\n")
    SCUtility.show_energy(sc)
    return


if __name__ == "__main__":
    # filename = sys.argv[1]
    # filename = '/Users/sravan/Projects/ds_algo/problems/princeton-assignments/seam-carving/data/seam/10x10.png'
    filename = '/Users/sravan/Projects/ds_algo/problems/princeton-assignments/seam-carving/data/images/img_01.jpg'
    main(filename)
