from pytube import YouTube, Playlist
from moviepy.editor import *
import os
import sys

def download_and_convert(url, output_dir='.'):
    try:
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file = video.download(output_path=output_dir)
        name_mp3 = os.path.join(output_dir, yt.title + ".mp3")
        video_clip = AudioFileClip(output_file)
        video_clip.write_audiofile(name_mp3)
        os.remove(output_file)
        print(f"File downloaded and converted: {name_mp3}\n")
    except Exception as e:
        print(f"Error downloading {url}: {e}\n")

def download_playlist(playlist_url):
    try:
        pl = Playlist(playlist_url)
        print(f'Downloading playlist: {pl.title}\n')
        playlist_dir = os.path.join("Playlists", pl.title)
        
        for video_url in pl.video_urls:
            print(f'Downloading video: {video_url}')
            download_and_convert(video_url, output_dir=playlist_dir)
    except Exception as e:
        print(f"Error downloading playlist: {e}\n")

def welcome_screen():
    print(r"""
    Welcome to YouTube Downloader CLI
    ------------------------------------
                     Developed by Reub Vega

                     Python Powered
                             ____
                            / . .\
                            \  ---<
                             \  /
                   __________/ /
                -=:___________/""")
    print("\n")

def menu_options():
    print("Select an option:\n[s] Download a single song\n[p] Download a playlist of songs\n[q] Quit\n")

def main_menu():
    welcome_screen()
    while True:
        menu_options()
        choice = input("Enter your choice: ").lower()
        if choice == "s":
            single_song()
        elif choice == "p":
            playlist_download()
        elif choice == "q":
            print("Thank you for using YouTube Downloader CLI. See you soon!")
            sys.exit()
        else:
            print("Invalid option. Please try again.")

def single_song():
    url = input("Enter the song link (x to cancel): ")
    if url == "x":
        return
    download_and_convert(url, output_dir="Songs")
    repeat()

def playlist_download():
    url = input("Enter the playlist link (x to cancel): ")
    if url == "x":
        return
    download_playlist(url)
    repeat()

def repeat():
    choice = input("Do you want to perform another operation? (y/n): ").lower()
    if choice != "y":
        print("Thank you for using YouTube Downloader CLI. See you soon!")
        sys.exit()

if __name__ == "__main__":
    main_menu()
