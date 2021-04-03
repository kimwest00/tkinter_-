from tkinter import *
 

win = Tk()
win.title("game")
win.geometry("600x400+300+100")
win.resizable(False,False)

label = Label(win, text="게임 시작")
label.pack()

button = Button(win, text="네",overrelief="solid",width=15,command=Scene1, height=1, repeatdelay=1000, repeatinterval=100)
button.pack()


def layout(): #기본 배치 함수
    b1 = Button(win, text="최준")
    b2 = Button(win, text="단소")
    b3 = Button(win, text="무야호")
    b4 = Button(win, text="롤린")
    b5 = Button(win, text="지하철 노선도")
    b6 = Button(win, text="마지막에 답 입력하는 곳")
    b7 = Button(win, text="쩍벌")
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4.grid(row=0,column=3)
    b5.grid(row=0,column=4)
    b6.grid(row=0,column=5)
    b7.grid(row=10,column=10)
    b7.config(command=game1)




def Clear(): #화면 지워주는 함수, 지워주고 클래스를 만들어서 기본적인 배치 해야할 듯
    for wg in win.pack_slaves():
        wg.destroy()
    for wg in win.grid_slaves():
        wg.destroy()

    
def Scene1(): #시작하고 눈 뜨기 전
    Clear()
    start=Button(win, bg="black",command=Scene2, height=1, repeatdelay=1000, repeatinterval=100)
    start.pack(expand=True, fill="both")

    
def Scene2(): #시작하고 눈 뜸
    Clear()
    layout()
    
    
def Scene():
    layout()


#나중에 엔트리 이용해서 지하철 역 만드는 곳

#쩍벌게임


from tkinter import *
import time

def game1():
    
    def press(event): #쩍벌게임 공 멈추고 성공 여부 알려주는 함수
        global game_stop, k
        if event.keysym == "space":
            cvs.delete(event_txt)
            game_stop = True

            if 225<=k and 235>=k:
                cvs.create_text(p3, text="성공", font=("Arial",20))
            else:
                cvs.create_text(p3, text="실패", font=("Arial",20))


    game =Tk()
    game.title("game")
    game.geometry("500x500")

    cvs = Canvas(game)
    cvs.config(width=500, height=500, bd=0, highlightthickness=0)

    #space 누르면 시작하라는 text 생성
    p3 = (250, 460)
    event_txt = cvs.create_text(p3, text="멈추려면 space를 누르세요", font=("Arial",20))



    game.bind("<KeyPress>",press)



    p1 = (460, 460)
    p2 = (490, 490)

    ball = cvs.create_oval(p1,p2,fill='red')
    ball_target = cvs.create_oval(460,235,490,265,fill='green')
    cvs.pack()


    game.update()
    k=0
    cnt=0
    game_stop = False
    #속도 더 복잡하게 조절 가능



    while True:
        time.sleep(0.000001) #속도 조절 근데 속도 빠르게 하면 원이 깨짐
        if cnt%2== 0:
            k+=1
        else:
            k-=1

        if k==460 or k==0:
            cnt+=1


        cvs.delete(ball)
        if game_stop ==False :
            p1 = (460, 460-k)
            p2 = (490, 490-k)  
        ball = cvs.create_oval(p1,p2,fill='red')
        game.update()
    

win = mainloop()