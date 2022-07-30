#!/usr/bin/env python3
from pytube import *
from  colorama import init
from termcolor import colored
import pytube
import os
import tqdm

init(autoreset=True)

def progress(streams, chunk: bytes, bytes_remaining: int):
    contentsize = streams.filesize
    size = contentsize - bytes_remaining

    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentsize), ' '*(20-int(size*20/contentsize)), float(size/contentsize*100)), end='')


def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def audio(yt, link):
    print(colored("starting the audio download...", 'green'))
    output = yt.streams.get_audio_only().download()
    print(colored("converting into mp3", 'yellow'))
    base, ext = os.path.splitext(output)
    new_file = base + ".mp3"
    os.rename(output,new_file)
    print(colored("Video successfullly downloaded from", 'green'), link)

def video(yt, link):
    print(colored("do you want to:", 'green'))
    print(colored("[1] select resolution", 'green'))
    print(colored("[2] highest resolution", 'green'))
    try:
        inp = int(input(">> "))
    except:
        print(colored("input a number", 'red'))
    else:
        if inp == 1:
            helper = set([
                stream.resolution
                for stream in yt.streams.filter(mime_type="video/mp4",progressive=True)
                if stream.resolution != None])
            print(f"avalible resolusion: {helper}")
            print(colored("select resolusion:", 'green'))
            print(colored("[1] 1080\t[2] 720", 'green'))
            print(colored("[3] 480 \t[4] 360", 'green'))
            print(colored("[5] 240 \t[6] 144", 'green'))
            try:
                inp = int(input(">> "))
            except:
                print(colored("input a number", 'red'))
            else:
                if inp == 1:
                    reso = "1080p"
                elif inp == 2:
                    reso = "720p"
                elif inp == 3:
                    reso = "480p"
                elif inp == 4:
                    reso = "360p"
                elif inp == 5:
                    reso = "240p"
                elif inp == 6:
                    reso = "144p"
                else:
                    reso = ""
                    print(colored("wrong input bye......try again", 'red'))
                try:
                    print(colored("starting the video download", 'yellow'))
                    yt.streams.filter(res=reso,mime_type="video/mp4",progressive=True).first().download()
                except:
                    print(colored("wrong resolusion..try again",'red'))
                else:
                    print(colored("Video successfullly downloaded from", 'green'), link)
        elif inp == 2:
            yt.streams.get_highest_resolution().download()
            print(colored("Video successfullly downloaded from", 'green'), link)
        else:
            print(colored("wrong input bye......try again", 'red'))


def playlist(link):
    p = Playlist(link)
    print(colored("do you want to:", 'green'))
    print(colored("[1] select resolution", 'green'))
    print(colored("[2] highest resolution", 'green'))
    try:
        inp = int(input(">> "))
    except:
        print(colored("input a number", 'red'))
    else:
        if inp == 1:
            for video in p.videos:
                temp = list(set([
                    stream.resolution
                    for stream in video.streams.filter(mime_type="video/mp4",progressive=True)
                    if stream.resolution != None]))

            print(f"avalible resolusion: {set([s for s in temp])}")

            print(colored("select resolusion:", 'green'))
            print(colored("[1] 1080\t[2] 720", 'green'))
            print(colored("[3] 480 \t[4] 360", 'green'))
            print(colored("[5] 240 \t[6] 144", 'green'))
            try:
                inp = int(input(">> "))
            except:
                print(colored("input a number", 'red'))
            else:
                if inp == 1:
                    reso = "1080p"
                elif inp == 2:
                    reso = "720p"
                elif inp == 3:
                    reso = "480p"
                elif inp == 4:
                    reso = "360p"
                elif inp == 5:
                    reso = "240p"
                elif inp == 6:
                    reso = "144p"
                else:
                    reso = ""
                    print(colored("wrong input bye......try again", 'red'))
                try:
                    print(colored("starting the playlist download", 'yellow'))

                    i = 1
                    for video in p.videos:
                        print(f"starting the [{i}] video")
                        video.streams.filter(res=reso,mime_type="video/mp4",progressive=True).first().download()
                        i += 1

                except:
                    print(colored("wrong resolusion..try again", 'red'))
                else:
                    print(colored("Video successfullly downloaded from", 'green'), link)
        elif inp == 2:

            for video in p.videos:
                video.streams.get_highest_resolution().download()
            print(colored("Playlist successfullly downloaded from", 'green'), link)
        else:
            print(colored("wrong input bye......try again", 'red'))



def main():
    print(colored("Welcome to ytDownloader", 'green'))
    print(colored("the link you provide is for 1) video 2) playlist", 'green'))
    try:
        choice = int(input(">> "))
    except:
        print(colored("wrong input try again", 'red'))
    else:
        if choice == 2:
            link = input("your youtube link: ")
            playlist(link)
        elif choice == 1:
            link = input("your youtube link: ")
            yt = pytube.YouTube(link, on_progress_callback=progress)
            print(colored("Title:", 'green'), yt.title)
            print(colored("Published date:", 'green'), yt.publish_date.strftime("%Y-%m-%d"))
            print(colored("Length of video:", 'green'), convert(yt.length), "seconds")
            print(colored("Do you want:", 'green'))
            print(colored("[1] Just audio", 'green'))
            print(colored("[2] Video", 'green'))

            try:
                inp = int(input(">> "))
            except:
                print(colored("input a number it will be defaulted to audio", 'yellow'))
                audio(yt, link)
            else:
                if inp == 1:
                    audio(yt, link)
                elif inp == 2:
                    video(yt, link)
                elif inp == 3:
                    print(colored("comming soon!!!....", 'yellow'))
                else:
                    print(colored("wrong input bye....try again", 'red'))
        else:
            print(colored("wrong choice", 'red'))

if __name__ == '__main__':
    main()  
