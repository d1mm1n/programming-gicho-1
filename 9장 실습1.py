#20224021 컴퓨터공학과 홍지민 9장 실습1

from tkinter import*
import pygame.mixer

app=Tk()
app.title("Head First Mix")
app.geometry('250x100+200+100')

sound_file="50459_M_RED_Nephlimizer.wav"  

mixer=pygame.mixer
mixer.init()


def track_start():          #play() 함수에 loops 인자 값을 -1 로 지정하면
    track.play(loops=-1)    #stop()을 호출할 때 까지 계속 반복 연주

def track_stop():
    track.stop()

def shutdown():
    track.stop()
    app.destroy()

track=mixer.Sound(sound_file)

start_button=Button(app, command=track_start, text ="Start")

start_button.pack(side =LEFT)

stop_button=Button(app, command=track_stop, text="Stop")

stop_button.pack(side=RIGHT)

app.protocol("WM_DELETE_WINDOW", shutdown)

app.mainloop()
