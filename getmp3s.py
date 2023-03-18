import os
from youtubesearchpython import *
import subprocess


pl_url = "https://www.youtube.com/playlist?list=PLeNNUmE-BlnEls2kOkiV2CXMezV6oaq8I"
pl = Playlist(pl_url)

print(f'Videos Retrieved: {len(pl.videos)}')

while pl.hasMoreVideos:
    print('Getting more videos...')
    pl.getNextVideos()
    print(f'Videos Retrieved: {len(pl.videos)}')

print('Found all the videos.')

for i in range(3, 16):

  if not os.path.exists(f"audio/{i}.mp3"):
    video_link = pl.videos[i]['link'].split('&')[0]
    command = f"yt-dlp -x --audio-format mp3 -o audio/{i}.mp3 {video_link}"
    print(command)
    cp = subprocess.run(command.split(), capture_output=True, text=True)
    print(cp.stdout)
    print(cp.stderr)

  print("Finished converting episode {} to mp3".format(pl.videos[i]['title']))
