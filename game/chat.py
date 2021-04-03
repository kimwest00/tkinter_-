import tkinter as Tk
import pygame
from PIL import ImageTk, Image
try:
    import Tkinter as tk
except:
    import tkinter as tk
pygame.init()

class SampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(FirstPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()
   
    def milk_clicked(self):
        self.milk = tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//game//milk.png").subsample(5)
        self.milk_Button=tk.Button(self, image=self.milk,activebackground="red").place(x=60,y=10)
        
    def danso_clicked(self):
        self.danso = tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//game//danso.png").subsample(5)
        self.danso_Button=tk.Button(self, image=self.danso,activebackground="red").place(x=220,y=10)
        
global list 
list = [0,0]
class FirstPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.img= tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//Start.png")#.subsample(10)
        tk.Label(self,image=self.img).grid()
        self.button=tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//game//Start_button.png").subsample(1)
        tk.Button(self, image=self.button,
                  command=lambda: master.switch_frame(MainPage)).place(x=500,y=600)
        
class MainPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        #my_img = tk.PhotoImage(file=("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//게임//Pygame//project//images//gunchim_character.png"))
        
        
        self.img= tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//배경.png")
        self.back_Label=tk.Label(self,image=self.img).grid()
        #self.background_label.place(relx=5, rely=5, anchor="center")
        #self.background_label.place(x=0,y=0,relwidth=1, relheight=1)
        #tk.Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        #self.joon = tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//game//최준.png").subsample(5)
        
        #self.milk = tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//game//milk.png").subsample(10)
        #self.danso_nam = tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//danso.png").subsample(10)
        #self.ddung = tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//game//ddung.png").subsample(25)
        
        tk.Button(self, text="준이에요~",borderwidth=0,
                  command=lambda: master.switch_frame(joon)).place(x=150,y=360)
        tk.Button(self, text="뭘봐 씻팔",
                  command=lambda: master.switch_frame(danso_nam),borderwidth=0).place(x=400,y=360)
        tk.Button(self, text="사랑~해요~",
                  command=lambda: master.switch_frame(ddung)).place(x=520,y= 250)
        self.danso = tk.Button(self, width = 8,height=1,command=lambda: master.danso_clicked(),bg="#B59757",borderwidth=0).place(x=920,y=450)
        self.milk = tk.Button(self, text="알랍우유",command=lambda: master.milk_clicked(),fg="blue").place(x=850,y=150)
        
        #milk.config(command=milk_clicked)
        tk.Button(self, text="무한~",
                  command=lambda: master.switch_frame(muya)).place(x=1200,y=360)
        #tk.Button(self, text="쫙벌남",
                  #command=lambda: master.switch_frame(leg)).grid()
        #tk.Button(self, text="정답",
                  #command=lambda: master.switch_frame(answer)).grid()
        #tk.Button(self, text="지도",
                  #command=lambda: master.switch_frame(map)).grid()
        
    
               
        
        
    
    
    '''def milk_give(self):
        joon.config(command=lambda:self.joon_give)
        muya.config(command=lambda:self.muya_give)
    def danso_give(self):
        danso_nam.config(command = lambda:self.danso_nam_give)
    def joon_give():
        joon['text']="저쪽신사분께 주고싶어요"'''
class joon(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.joon = tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//kiss.png").subsample(5)
        tk.Label(self, image = self.joon).grid()
        tk.Label(self, text="어?예쁘다", font=('Helvetica', 18, "bold")).place(x=80,y=400)
        tk.Button(self, text="(메인화면으로)뭔가 알럽우유 드립칠거같이 생겼다",
                  command=lambda: master.switch_frame(MainPage)).grid()
        pygame.mixer.music.load('최준키스.wav')
        pygame.mixer.music.play()
class danso_nam(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.danso_nam = tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//후알유!.png").subsample(5)
        tk.Label(self, image = self.danso_nam).grid()
        tk.Label(self, text="후얼유!", font=('Helvetica', 18, "bold")).grid()
        tk.Button(self, text="(메인화면으로)왜 화가 났지...손이 허전해보이긴한다",
                  command=lambda: master.switch_frame(MainPage)).grid()
        pygame.mixer.music.load('후얼유.wav')
        pygame.mixer.music.play()
class ddung(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.ddung = tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//바보뚱이.png").subsample(5)
        tk.Label(self, image = self.ddung).grid()
        tk.Label(self, text="저는 뚱인데여?", font=('Helvetica', 18, "bold")).grid()
        tk.Button(self, text="(메인화면으로)아무 쓸모가 없어보인다",
                  command=lambda: master.switch_frame(MainPage)).grid() 
        
        pygame.mixer.music.load('뚱.wav')
        pygame.mixer.music.play()
        
class muya(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #my_img = ImageTk.PhotoImage(Image.open("background.jpg"))
        #tk.Frame.configure(self,bg=my_img)
        self.ddung = tk.PhotoImage(file="C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//muyaho.png").subsample(5)
        tk.Label(self, image = self.ddung).grid()
        #pygame.mixer.music.load("C://Users//김민서//Downloads//Carl Storm - Warm.wav") #음악 재생 (무야호~). 음악 파일없어서 주석처리
        #pygame.mixer.music.play()
        #music = r'C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//무야호.wav'
        
        pygame.mixer.music.load('무야호.wav')
        pygame.mixer.music.play(3)
        tk.Button(self, text="(메인화면으로)그만큼 신나시는구나..",
                  command=lambda: master.switch_frame(MainPage) and pygame.mixer.music.stop()).grid()
        

class answer(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        #my_img = ImageTk.PhotoImage(Image.open("background.jpg"))
        #tk.Frame.configure(self,bg=my_img)
        tk.Label(self, text="정답을 입력하십시오", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="메인화면으로",
                  command=lambda: master.switch_frame(MainPage)).grid()
class map(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        my_img = ImageTk.PhotoImage(Image.open("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//d//game//background.jpg"))
        #tk.Frame.configure(self,bg=my_img)
        tk.Label(self, text="map", font=('Helvetica', 18, "bold"),bg=my_img).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="메인화면으로",
                  command=lambda: master.switch_frame(MainPage)).grid()
   

class leg(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        
        tk.Label(self, text="게임을 하면 단소를 주겠다", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        tk.Button(self, text="메인화면으로",
                  command=lambda: master.switch_frame(MainPage)).grid()


   
if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()