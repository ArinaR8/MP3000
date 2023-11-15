from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os
mixer.init()

songsDictionary = {}


def openfiles():
    global songsDictionary
    songs = filedialog.askopenfilenames(initialdir='tracks/', title='Выберите песню(-и)',
                                        filetypes=(('mp3 Files', '*.mp3'),))
    for song in songs:
        song_box.insert(END, os.path.basename(song))
        songsDictionary = {**songsDictionary, **{os.path.basename(song): song}}


def play():
    global songsDictionary
    if song_state['text'] == 'Пауза':
        mixer.music.unpause()
    else:
        song = song_box.get(ACTIVE)
        mixer.music.load(songsDictionary[song])
        mixer.music.play()
        song_state['text'] = 'Воспроизведение'


def stop():
    mixer.music.stop()
    song_box.selection_clear(ACTIVE)
    song_state['text'] = 'Остановлено'


def pause():
    mixer.music.pause()
    song_box.selection_clear(ACTIVE)
    song_state['text'] = 'Пауза'


def next_song():
    global songsDictionary
    next_s = song_box.curselection()[0] + 1
    song_box.selection_clear(next_s - 1)
    if next_s > song_box.size() - 1:
        next_s = 0
    song = song_box.get(next_s)
    mixer.music.load(songsDictionary[song])
    mixer.music.play()
    song_box.selection_set(next_s, last=None)


def back():
    global songsDictionary
    b_s = song_box.curselection()[0] - 1
    song_box.selection_clear(b_s + 1)
    if b_s == -1:
        b_s = 0
    song = song_box.get(b_s)
    mixer.music.load(songsDictionary[song])
    mixer.music.play()
    song_box.selection_set(b_s, last=None)


root: Tk = Tk()
root.title('Музыкальный плеер 3000')
root.minsize(650, 270)
root.maxsize(650, 270)
root.configure(background="#34495e")

master_frame = Frame(background="#34495e")
info_frame = Frame(master_frame, background="#34495e")
controls_frame = Frame(master_frame, background="#34495e")
file_frame = Frame(master_frame, background="#34495e")

song_state = Label(info_frame, width=60, text='Остановлено', foreground='white',
                   font='Arial 10 bold', background="#34495e")
song_box = Listbox(info_frame, width=60, selectforeground='white', selectbackground='blue', background='#F6F7F9')
back_button = Button(controls_frame, text='⏮', command=back, background="#D9E1F2")
forward_button = Button(controls_frame, text='⏭', command=next_song, background="#D9E1F2")
play_button = Button(controls_frame, text='▶', command=play, background="#D9E1F2")
pause_button = Button(controls_frame, text='⏸', command=pause, background="#D9E1F2")
stop_button = Button(controls_frame, text='⏹️', command=stop, background="#D9E1F2")

openfolder_button = Button(file_frame, text='Открыть файл(ы)', command=openfiles, background="#D9E1F2")

master_frame.grid()
info_frame.grid(row=0, column=0)
controls_frame.grid(row=1, column=0)
file_frame.grid(row=0, column=5)
song_state.grid(row=0, column=0)
song_box.grid(row=1, column=0)
back_button.grid(row=0, column=0)
play_button.grid(row=0, column=1)
pause_button.grid(row=0, column=2)
stop_button.grid(row=0, column=3)
forward_button.grid(row=0, column=4)
openfolder_button.grid(row=0, column=0)

root.mainloop()

