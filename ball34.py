from tkinter import *
from time import sleep
from random import shuffle
from math import sqrt
def xcomb(seq,length):
    if not length:
        yield []
    else:
        for i in range(len(seq)):
            for result in xcomb(seq[i+1:],length-1):
                yield [seq[i]]+result
class Ball:
    def __init__(self,x,y,ys):
        self.w=c.winfo_width()
        self.h=c.winfo_height()
        self.id=c.create_oval(x,y,20+x,20+y,fill=ys)
        self.x=sd[0]
        self.y=sd[0]
        self.p=[]
    def move(self):
        c.move(self.id,self.x,self.y)
        self.p=c.coords(self.id)
        shuffle(sd)
        if self.p[1]<=0:
            self.y=sd[0]
        if self.p[3]>=self.h:
            self.y=-sd[0]
        if self.p[0]<=0:
            self.x=sd[0]
        if self.p[2]>=self.w:
            self.x=-sd[0]
        sleep(0.010)
tk=Tk()
tk.title('')
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
c=Canvas(tk,width=200,height=200)
c.pack()
c.update()
sd=[1,2,3]
b0=Ball(15,10,'red')
b1=Ball(80,50,'blue')
b2=Ball(30,150,'gold')
b3=Ball(180,30,'green')
box=[b0,b1,b2,b3]
comb=list(xcomb(box,2))
while 1:
    ss=[]
    for i in box:
        i.move()
    for j in comb:
        m,n=j
        if (m.p[0]-n.p[0])**2+(m.p[1]-n.p[1])**2<=20**2:
            m.x,n.x=n.x,m.x 
            m.y,n.y=n.y,m.y
        ss=ss+[c.create_line(m.p[0]+10,m.p[1]+10,n.p[0]+10,n.p[1]+10,dash=(4,4))]
    c.update()
    for k in ss:
        c.delete(k)
tk.mainloop()
    
