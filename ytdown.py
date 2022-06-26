#!/usr/bin/env python3
from pytube import *
import os
def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60      
    return "%d:%02d:%02d" % (hour, minutes, seconds)

def audio(yt, link):
    print("starting the audio download...")
    output = yt.streams.get_audio_only().download()
    print("converting into mp3")
    base, ext = os.path.splitext(output)
    new_file = base + ".mp3"
    os.rename(output,new_file)
    print("Video successfullly downloaded from", link) 

def video(yt, link):
    print("do you want to:")
    print("[1] select resolution")
    print("[2] highest resolution")
    try:
        inp = int(input(">> "))
    except:
        print("input a number")
    else:
        if inp == 1:
            print(f"avalible resolusion: {set([stream.resolution for stream in yt.streams if stream.resolution != None])}")
            print("select resolusion:")
            print("[1] 1080\t[2] 720")
            print("[3] 480 \t[4] 360")
            print("[5] 240 \t[6] 144")
            try:
                inp = int(input(">> "))
            except:
                print("input a number")
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
                    print("wrong input bye......try again")
                try:
                    print("starting the video download")
                    yt.streams.filter(res=reso,file_extension="mp4").first().download()
                except:
                    print("wrong resolusion..try again")
                else:
                    print("Video successfullly downloaded from", link) 
        elif inp == 2:
            yt.streams.get_highest_resolution().download()
            print("Video successfullly downloaded from", link) 
        else:
            print("wrong input bye......try again")
 

def playlist(link):
    p = Playlist(link)
    print("do you want to:")
    print("[1] select resolution")
    print("[2] highest resolution")
    try:
        inp = int(input(">> "))
    except:
        print("input a number")
    else:
        if inp == 1:
            for video in p.videos:
                temp = list(set([stream.resolution for stream in video.streams if stream.resolution != None]))

            print(f"avalible resolusion: {set([s for s in temp])}")

            print("select resolusion:")
            print("[1] 1080\t[2] 720")
            print("[3] 480 \t[4] 360")
            print("[5] 240 \t[6] 144")
            try:
                inp = int(input(">> "))
            except:
                print("input a number")
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
                    print("wrong input bye......try again")
                try:
                    print("starting the playlist download")
                    
                    i = 1
                    for video in p.videos:
                        print(f"starting the [{i}] video")
                        video.streams.filter(res=reso,file_extension="mp4").first().download()
                        i += 1
                    
                except:
                    print("wrong resolusion..try again")
                else:
                    print("Video successfullly downloaded from", link) 
        elif inp == 2:
            
            for video in p.videos:
                video.streams.get_highest_resolution().download()
            print("Playlist successfullly downloaded from", link) 
        else:
            print("wrong input bye......try again")
 


def main():
    print("Welcome to ytDownloader")
    print("the link you provide is for 1) video 2) playlist")
    try:
        choice = int(input(">> "))
    except:
        print("wrong input try again")
    else:
        if choice == 2:
            link = input("your youtube link: ")
            playlist(link)
        elif choice == 1:
            link = input("your youtube link: ")
            yt = pytube.YouTube(link)
            print("Title:", yt.title)
            print("Published date:", yt.publish_date.strftime("%Y-%m-%d"))
            print("Length of video:", convert(yt.length), "seconds")
            print("Do you want:")
            print("[1] Just audio")
            print("[2] Video")
            
            try:
                inp = int(input(">> "))
            except:
                print("input a number it will be defaulted to audio")
                audio(yt, link)
            else:   
                if inp == 1:
                    audio(yt, link)
                elif inp == 2:
                    video(yt, link)
                elif inp == 3:
                    print("comming soon!!!....")
                else:
                    print("wrong input bye....try again")
        else:
            print("wrong choice")

if __name__ == '__main__':
    main()

