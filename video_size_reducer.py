import glob
import os
import argparse

parser = argparse.ArgumentParser(
    description=
    'Reduces size of the video files in a selected folder. Path can be relative of start from root. Paths that starting from roots are better choice.'
)

parser.add_argument('--crf', type=int, default=24, help='CRF Ratio')
parser.add_argument('--pre', type=str, default="", help='prefix')
parser.add_argument('--folder',
                    type=str,
                    default="",
                    help='folder that contains videos')
parser.add_argument('--ext', type=str, default="", help='video extension')

opt = parser.parse_args()
if opt.folder == "":
    videos = glob.glob(fr"*.MP4")
else:
    print(opt.folder)
    videos = glob.glob(fr"{opt.folder}/*.MP4")
    print(videos)

if opt.ext == "":
    exit("Please Enter An Extension")

for video in videos:
    os.system(
        f'ffmpeg -hwaccel cuda -i "{video}" -vcodec libx265 -crf {opt.crf} "{video.split(f".{opt.ext}")[0]}_{opt.pre}_CRF_{opt.crf}".mp4'
    )
