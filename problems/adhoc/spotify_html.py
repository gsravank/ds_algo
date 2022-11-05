from utils.GenUtils import read_lines, write_lines
import time
from tqdm import tqdm
import re
from bs4 import BeautifulSoup as bs


infile = '/Users/sravan/SpotifyLinkData.txt'
outfile = '/Users/sravan/SpotifyTitles.txt'


def get_pieces(tot_string):
    substr = '</html>'
    idx_obj = re.finditer(pattern=substr, string=tot_string)
    indices = [index.start() for index in idx_obj]

    pieces = list()
    end_indices = [0] + [x + len(substr) for x in indices]
    for first, sec in zip(end_indices[:-1], end_indices[1:]):
        curr_piece = tot_string[first:sec]
        pieces.append(curr_piece)

    return pieces


def get_title_from_piece(piece):
    soup = bs(piece, 'html.parser')
    return soup.title.contents[0].strip().split('|')[0].strip()

in_string = '\n'.join(read_lines(infile))
pieces = get_pieces(in_string)
print(len(pieces))

titles = [get_title_from_piece(piece) for piece in tqdm(pieces)]
print(titles[:10])

write_lines(titles, outfile)