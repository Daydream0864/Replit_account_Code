#from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    stop_playback = int(input("Press 2 anytime to stop playback and go back to the menu : ")) # giving the user the option to stop playback
    if stop_playback == 2:
      source.paused = True # let's pause the file 
      return # let's go back from this play() subroutine
    else: 
      continue

while True:
  print("🎵 MyPOD Music Player")
  # clear the screen 
  time.sleep(1)
  os.system("clear")

  # Show the menu
  print("Press 1 to Play")
  print("Press 2 to Exit")
  
  press = int(input("ds"))
  
  # take user's input
  if press == 1:
    play()
  elif press == 2:
    exit()
  else:
    os.system("clear")
    continue

  # check whether you should call the play() subroutine depending on user's input