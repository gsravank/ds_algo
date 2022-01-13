from SeamCarver import SeamCarver
import sys
from Picture import Picture


class PrintSeams:
    def __init__(self):
        return

    @staticmethod
    def print_seam(seam_carver, seam_indices, horizontal_flag):
        total_seam_energy = 0.0
        width = seam_carver.width()
        height = seam_carver.height()

        for row in range(height):
            for col in range(width):
                energy = seam_carver.energy(col, row)
                marker = " "
                if (horizontal_flag and row == seam_indices[col]) or (not horizontal_flag and col == seam_indices[row]):
                    marker = "*"
                    total_seam_energy += energy
                print(f"{energy:7.2f}{marker}\t", end='')
            print("")
        print(f"Total energy = {total_seam_energy}")
        print("")


def main(arguments):
    pic = Picture(arguments[0])
    print(f"{arguments[0]} ({pic.width()}-by-{pic.height()} image)\n")
    print("The table gives the dual-gradient energies of each pixel.")
    print("The asterisks denote a minimum energy vertical or horizontal seam.")

    carver = SeamCarver(pic)

    print("Vertical seam: {", end='')
    vseam = carver.find_vertical_seam()
    for x in vseam:
        print(f"{x} ", end="")
    print("}")
    PrintSeams.print_seam(carver, vseam, False)

    print("Horizontal seam: {", end='')
    hseam = carver.find_horizontal_seam()
    for x in hseam:
        print(f"{x} ", end="")
    print("}")
    PrintSeams.print_seam(carver, hseam, True)

    return


if __name__ == '__main__':
    # args = sys.argv[1:]
    # fn = '/Users/sravan/Projects/ds_algo/problems/princeton_assignments/seam-carving/data/images/img_01.jpg'
    fn = '/Users/sravan/Projects/ds_algo/problems/princeton_assignments/seam-carving/data/seam/6x5.png'
    args = [fn]
    main(args)
