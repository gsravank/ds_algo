import urllib3
from utils.GenUtils import read_lines, write_lines
import time
from tqdm import tqdm

link_file = '/Users/sravan/Spotify.txt'
outfile = '/Users/sravan/SpotifyLinkData.txt'
song_links = read_lines(link_file)

http = urllib3.PoolManager()
fin_lines = list()

for each_link in tqdm(song_links):
    try:
        r = http.request('GET', each_link)
        data = r.data
        data_s = data.decode()
        fin_lines.append(data_s)
    except Exception as e:
        print(each_link)
        print(e.__str__())
        print('\n====\n\n=====\n')

    time.sleep(1)

write_lines(fin_lines, outfile)
