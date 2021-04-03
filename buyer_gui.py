import tkinter as tk
import buyer as b

class Buy_GUI(tk.Frame, b.Buyer):
    def __init__(self,master,money):
        tk.Frame.__init__(self,master)
        b.buyer.__init__(self,money)

    def set_widget(self):
        #사기버튼
        self.apple_label = tk.Label(self,text = "사과")
        #먹기버튼
        self.money_label = tk.Label(self,text= "돈")
        self.apple_show = tk.Label(self, text= self.apple)
        self.money_show = tk.Label(self,text = self.money)
        self.buy_btn = tk.Button(self, text = "사기" )
        self.eat_btn = tk.Button(self, text ="먹기")

        self.apple_label.grid(row=0,column=0)
        self.money_label.grid(row=0,column =1)
        self.apple_show.grid(row=1,column=0)
        self.money_show.grid(row=1,column=1)
        self.buy_btn.grid(row=2,column=0)
        self.eat_btn.grid(row=2,column=1)

    def place_widget(self,row,column):
        self.grid(row=row,column=column)
