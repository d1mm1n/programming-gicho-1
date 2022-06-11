#20224021 컴퓨터공학과 홍지민 9장 임의

from tkinter import*
from tkinter import filedialog as fd



#파일 열기 해서 이미지 불러온다음 그림 그릴 수 있도록
#그림판 만들기 참고- https://sxyzn.tistory.com/11
#위젯에 배경(bg)과 전경(fg) 변수를 사용하여 위젯 및 텍스트 색상을 지정할 수 있다.
#이미지 위에 그림이 안그려짐-> 캔버스에 이미지 넣기 


app=Tk()
app.title("20224021 이미지 꾸미기")
app.geometry("500x400")


color='blue'   #초기 색 설정 값

#캔버스 위에 그림 그릴 수 있도록 하기 위해 함수 정의
def draw(d):
    x1, y1 =( d.x-1), (d.y-1)
    x2, y2 =(d.x+1), (d.y+1)
    canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)


#버튼 누르면 색 바뀔 수 있게 함수 정의
def change_red():
    global color
    color ='red'
    
def change_yellow():
    global color
    color ='yellow'
    
def change_blue():
    global color
    color ='blue'
    
def change_green():
    global color
    color ='green'

def change_black():
    global color
    color ='black'
    
def change_brown():
    global color
    color ='brown'
      

#위의 함수 이용해서 버튼 누르면 색 바뀌도록 command 설정
redbutton=Button(app, text="빨간색", command=change_red)
redbutton['fg'] ='red'
redbutton.place(x=10, y=10)

yellowbutton=Button(app, text="노란색", command=change_yellow)
yellowbutton['fg'] ='yellow'
yellowbutton.place(x=10, y=40)

bluebutton=Button(app, text="파란색", command=change_blue)
bluebutton['fg'] ='blue'
bluebutton.place(x=10, y=70)

greenbutton=Button(app, text="초록색", command=change_green)
greenbutton['fg'] ='green'
greenbutton.place(x=10, y=100)

brownbutton=Button(app, text="갈색", command=change_brown)
brownbutton['fg'] ='brown'
brownbutton.place(x=10, y=130)

blackbutton=Button(app, text="검정색", command=change_black)
blackbutton['fg'] ='black'
blackbutton.place(x=10, y=160)


def callback():
    name=fd.askopenfilename()
    global img                  
    global canvas                #캔버스에 이미지 넣으려고 했는데 안넣어져서 글로벌 사용
    img =PhotoImage(file= name)  #file= name 으로 내가 연 파일이 나오게 설정
    canvas.create_image(0, 0, image=img, anchor=NW)      #캔버스에 이미지 만들기
    



canvas=Canvas(app)
canvas.pack()   
canvas.bind("<B1-Motion>", draw)


Button(app, text='이미지 고르기', command=callback).pack(side='bottom')   #버튼 누르면 파일 열리도록 command 설정
app.mainloop()