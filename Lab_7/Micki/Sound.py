import pygame
import keyboard
import os

pygame.mixer.init()

MUSIC_FOLDER = "D:\gitHub\pp2_labs_python\song"
songs = [f for f in os.listdir(MUSIC_FOLDER) if f.endswith('.mp3')]
current_index = 0  

def play_song():
    global current_index
    pygame.mixer.music.load(os.path.join(MUSIC_FOLDER, songs[current_index]))
    pygame.mixer.music.play()
    print(f"Now playing: {songs[current_index]}")

def stop_song():
    pygame.mixer.music.stop()
    print("Music stopped")

def next_song():
    global current_index
    current_index = (current_index + 1) % len(songs) 
    play_song()

def quit_song():
    print("Exiting Music Player...")
    pygame.mixer.music.stop()
    os._exit(0) 


keyboard.add_hotkey("space", play_song) 
keyboard.add_hotkey("s", stop_song)  
keyboard.add_hotkey("n", next_song)  
keyboard.add_hotkey("w", quit_song)

print("Music player controls: [Space] Play, [S] Stop, [N] Next, [W] Quit")

keyboard.wait()
