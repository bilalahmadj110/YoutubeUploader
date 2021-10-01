import os
from youtube_uploader_selenium import YouTubeUploader, save_cookies_

# 1 means default
# Channels numbers are in "switch account" tab on youtube
# Note: the sequence of multiple account in button "Switch Account" on youtube page at time of cookies saving
# Choose channel number accordingly
# By: Bilal Ahmad (bilalahmadj.110@gmail.com)
WHICH_CHANNEL = 1

VIDEO_PATH = r"up.avi"
VIDEO_TITLE = "MP4"
VIDEO_DESC = "This is mp4 spinner."
VIDEO_TAGS = ['abc', 'def', 'ghi']
VIDEO_PRIVACY = 'public'
# Thumbnail must be less than 2MB
VIDEO_THUMB_PATH = "noise.png"

SAVE_COOKIES = 0 # False if cookies already saved
COOKIES_NAME = 'youtube2'

if SAVE_COOKIES:
    YT = save_cookies_.YouTubeCookiesSaver(COOKIES_NAME)
    if not YT.setup():
        print("QUITING SCRIPT")
        exit()

if not os.path.exists(VIDEO_PATH):
    exit(('=' * 30) + '\nVideo path doesn\'t exists.\n' + ('=' * 30))
if len(VIDEO_TITLE.strip()) > 70 or '>' in VIDEO_TITLE or '<' in VIDEO_TITLE:
    exit((
                 '=' * 100) + '\nKeep your video title within 70 characters (including spaces). Angles and brackets are not allowed\n' + (
                 '=' * 100))
if len(VIDEO_DESC.strip()) > 5000:
    exit(('=' * 70) + '\nYou are allowed up to 55,000 characters for the video description.\n' + ('=' * 70))
if VIDEO_PRIVACY.lower().strip() != 'unlisted' and VIDEO_PRIVACY.lower().strip() != 'public' and VIDEO_PRIVACY.lower().strip() != 'private':
    exit(('=' * 60) + '\nVideo privacy can only be "public", "private" or "unlisted".\n' + ('=' * 60))

counter = lambda x: len(x)
if sum(list(map(counter, VIDEO_TAGS))) > 400:
    exit(('=' * 60) + '\nTags can\'t be greater than of total 500 characters.\n' + ('=' * 60))

uploader = YouTubeUploader(VIDEO_PATH.strip(),
                           VIDEO_TITLE.strip(),
                           VIDEO_DESC.strip(),
                           VIDEO_TAGS,
                           VIDEO_PRIVACY.strip(),
                           WHICH_CHANNEL,
                           thumbnail_path=VIDEO_THUMB_PATH,
                           add_extra_click=0,
                           add_second_click=0,
                           cookies_name=COOKIES_NAME)

was_video_uploaded, video_id = uploader.upload()
# try:
    
    # assert was_video_uploaded
# except:
    # print("failed to get uploaded video ID, maybe video was not uploaded too.")
    # input('Press any key to close browser (if open): ')
