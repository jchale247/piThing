import spotipy
from tkinter import *
from spotipy.oauth2 import SpotifyOAuth

#get and set track title
def getTrackTitle():
    #get track info
    currentTrack = sp.current_user_playing_track()
    #set and position now playing info
    nowPlaying['text'] = currentTrack['item']['name']
    nowPlaying.place(x=240-(nowPlaying.winfo_width()/2), y=30)
    #set and position artist name
    artist['text'] = currentTrack['item']['artists'][0]['name']
    artist.place(x=240-(artist.winfo_width()/2), y=60)
    #do this once every second
    window.after(1000, getTrackTitle)

#determine if track is playin and then either play or pause it
def playPause():
    #if the tracks playing
    if(sp.current_user_playing_track()['is_playing']):
        #change the icon to play and pause the playback
        sp.pause_playback()
        playbtn['image']=playImg
    else:
        #change the icon to pause and start the playback
        sp.start_playback()
        playbtn['image']=pauseImg

#on button click skip track
def skip():
    sp.next_track()

#on button click go to previous track
def prev():
    sp.previous_track()

#configure spotify connection with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope='user-read-currently-playing streaming user-modify-playback-state user-read-playback-state'))
window = Tk()
#define button images
playImg = PhotoImage(file="play.png")
pauseImg = PhotoImage(file="pause.png")
skipImg = PhotoImage(file="skip.png")
prevImg = PhotoImage(file="prev.png")
#define now playing and artist text fields
nowPlaying = Label(window, text="...", bg='#191414', fg='#1DB954', highlightthickness=0, bd=0, font='Helvetica 18 bold')
nowPlaying.place(x=240-(nowPlaying.winfo_width()/2), y=30)
artist = Label(window, text="...", bg='#191414', fg='#1DB954', highlightthickness=0, bd=0)
artist.place(x=240-(artist.winfo_width()/2), y=60)
#configure buttons
playbtn=Button(window, image=playImg, highlightthickness=0, bd=0, bg='#191414', activeforeground='#191414', activebackground='#191414',borderwidth=0, command=playPause)
#set play/pause button to correct image
if(sp.current_user_playing_track()['is_playing']):
    playbtn['image']=pauseImg
else:
    playbtn['image']=playImg
playbtn.place(x=176, y=96)
skipbtn=Button(window, image=skipImg, highlightthickness=0, bd=0, bg='#191414', activeforeground='#191414', activebackground='#191414', borderwidth=0, command=skip)
skipbtn.place(x=332, y=96)
prevbtn=Button(window, image=prevImg, highlightthickness=0, bd=0, bg='#191414', activeforeground='#191414', activebackground='#191414', borderwidth=0, text="prev", command=prev)
prevbtn.place(x=20, y=96)
#configure window
window.title('piThing')
window.configure(bg='#191414')
window.geometry("480x320")
#set track title initial
getTrackTitle()
#start window mainloop
window.mainloop()
