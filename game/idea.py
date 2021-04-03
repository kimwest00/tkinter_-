'''import tkinter as Tk

class SampleApp(tk.Tk):
    def__init__(self,*args,**kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        self.title_font=tkfont.Font(family='')'''
'''try:
    import Tkinter as tk
except:
    import tkinter as tk
    
class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go to page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        tk.Button(self, text="Go to page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()

class PageOne(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='blue')
        tk.Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Frame.configure(self,bg='red')
        tk.Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()'''

#btn1 우유 버튼, btn3 최준 이미지, btn4 무야호 아저씨
#import pygame

import tkinter as tk

window = tk.Tk()

print(type(window))

window.title("방탈출 게임")
window.geometry("640x400+100+100")

window.resizable(False,False)
Label = tk.Label(window,bg ="magenta",width = 10, height = 3)
Label.place(x=0,y=0)
Label1 = tk.Label(window,bg ='blue',width=10,height = 3)
Label1.place(x=80,y=0)




def milk_clicked(): #우유가 리스트에 없으면 리스트에 추가하고 리스트에 있는 상태면 최준이나 무야호 아저씨한테 주는 함수(give) 호출
    if 'milk' in list:
        milk_give()
    else: 
        milk.place(x=0,y=0)
        list.append('milk')
def danso_clicked(): #우유가 리스트에 없으면 리스트에 추가하고 리스트에 있는 상태면 최준이나 무야호 아저씨한테 주는 함수(give) 호출
    if 'danso' in list:
        danso_give()
    else: 
        danso.place(x=80,y=0)
        list.append('danso')
       
def joon_clicked():

    joon['text'] = '어? 예쁘다'

def muya_clicked():  #무야호 아저씨 눌렀을때(우유받지 않음)
    muya['text']='우유 아직 안받은 상태(무야 음성 재생)'
    #pygame.mixer.music.load(soundfile) #음악 재생 (무야~) 파일 없어서 주석처리함
    #pygame.mixer.music.play()

def danso_nam_clicked():  #단소아저씨(단소받지 않음)
    danso_nam['text']='후얼유!(후얼유 음성 재생)'

def changeColor(item):
    item.configure(bg="yellow")

def milk_give():
    changeColor(milk)
    joon.config(command=joon_give)
    muya.config(command=muya_give)

def danso_give():
    changeColor(danso)
    danso_nam.config(command = danso_nam_give)


def joon_give():
    joon['text']="제 옆의 신사분께 주고 싶어요"
def muya_give():
    muya['text']="우유를 받음"
    # pygame.mixer.music.load(soundfile) #음악 재생 (무야호~). 음악 파일없어서 주석처리
    #pygame.mixer.music.play()
def danso_nam_give():
    danso_nam['text']="히얼유"
   


global list 
list = []

#버튼 위치(추후 변경)
milk = tk.Button(window,text = '아이럽우유', fg='blue')
milk.config(command=milk_clicked) #우유 누르면 btn_clicked함수로
milk.pack(side = 'left',pady=20)

danso = tk.Button(window,text = '단소', fg='blue')
danso.config(command=danso_clicked) #우유 누르면 btn_clicked함수로
danso.pack(side = 'right',pady=50)
#유민언니가 한 코드에서 단소파트 삭제 (btn2)

joon = tk.Button(window,text='최준',fg='green')
joon.pack(side='bottom',pady=80)
joon.config(command=joon_clicked) #최준 누르면 btn3_clicked로

muya = tk.Button(window, text='무야호 아저씨',fg='green')
muya.pack(side = 'bottom',pady=50)
muya.config(command=muya_clicked) #무야호 아저씨 누르면 btn4_clicekd로

danso_nam = tk.Button(window, text='단소 아저씨',fg='green')
danso_nam.pack(side = 'left',pady=20)
danso_nam.config(command=danso_nam_clicked) #무야호 아저씨 누르면 btn4_clicekd로

window.mainloop()