from Picture import Picture
from SeamCarver import SeamCarver
import sys
import time
from tqdm import tqdm


def main(arguments):
    if len(arguments) != 3:
        print(f"Usage:\npython {__file__} [image filename] [num cols to remove] [num rows to remove]")
        return

    filename = arguments[0]
    num_cols = int(arguments[1])
    num_rows = int(arguments[2])

    input_img = Picture(filename=filename)
    print(f"Image is {input_img.width()} columns by {input_img.height()} rows\n")
    sc = SeamCarver(input_img)

    t1 = time.time()
    for _ in tqdm(range(num_rows)):
        horizontal_seam = sc.find_horizontal_seam()
        # print(horizontal_seam)
        sc.remove_horizontal_seam(horizontal_seam)
    for _ in tqdm(range(num_cols)):
        t2 = time.time()
        vertical_seam = sc.find_vertical_seam()
        t3 = time.time()
        # print(vertical_seam)
        sc.remove_vertical_seam(vertical_seam)
        t4 = time.time()
    output_img = sc.picture()
    print(f"New image is {output_img.width()} columns by {output_img.height()} rows\n")
    print(f"Resizing time: {time.time() - t1} seconds")
    print(f"Time to find seam: {t3 - t2}\nTime to remove seam: {t4 - t3}")

    input_img.show()
    output_img.show()

    print(input_img.image[0][0])
    print(output_img.image[0][0])

    return


if __name__ == '__main__':
    # args = sys.argv[1:]
    # fn = '/Users/sravan/Projects/ds_algo/problems/princeton-assignments/seam-carving/data/seam/10x10.png'
    fn = '/Users/sravan/Projects/ds_algo/problems/princeton-assignments/seam-carving/data/images/img_01.jpg'
    args = [fn, 1, 0]
    main(args)
