"""
Python GUI Code to simuluate an M/M/1 Queue v0.1
By Swarup Sahoo
"""
#Required Libraries
from tkinter import *
import random
from math import *
import time


class client(object): #The dots we use for active clients and client footprint in queue
    def __init__(self, canvas, num, phase):
        self.canvas=canvas
        self.canvas.after(0, self.animation(num, phase))
    def animation(self, num, phase):
        track = phase
        x = 720
        y = 0
        if track == 11: #Active clients in Queue 1
            self.client = self.canvas.create_oval(10, 65, 30, 85, outline='white', fill='black')
            self.canvas.move(self.client, x-num*20, y)
            self.canvas.update()
        elif track==12: #Footprint of clients in Queue 1
            self.noclient = self.canvas.create_oval(10, 65, 30, 85, outline='white', fill='grey')
            self.canvas.move(self.noclient, x-(num+1)*20, y)
            self.canvas.update()
        elif track==21: #Active clients in Queue 2
            self.client1 = self.canvas.create_oval(10, 115, 30, 135, outline='white', fill='black')
            self.canvas.move(self.client1, x-num*20, y)
            self.canvas.update()
        elif track==22: #Footprint of clients in Queue 2
            self.noclient1 = self.canvas.create_oval(10, 115, 30, 135, outline='white', fill='grey')
            self.canvas.move(self.noclient1, x-(num+1)*20, y)
            self.canvas.update()


def mm1(): #the mm1 queue generator function

    def generateArr(lam): #Next Arrival Time Generator Function
        ua=random.uniform(0, 1)
        arr= log(1-ua)/(-lam)
        return arr

    def generateServ(mu): #Next Service Time Generator Function
        us=random.uniform(0, 1)
        serv= log(1-us)/(-mu)
        return serv



    root = Tk()
    root.title("M/M/1 Queue Sim "+u"\u00A9"+" Swarup Sahoo")
    root.iconbitmap('icon.ico')

    canvLeft=Canvas(root, height=400, width=400)
    canvLeft.pack(side=LEFT)
    canvRight=Canvas(root, height=400, width=600)
    canvRight.pack(side=LEFT)

    varStopr=IntVar()
    varStopr.set(1)
    R1 = Radiobutton(canvLeft, text="Shift Time", variable=varStopr, value=1)
    R1.pack(anchor=W)
    R2 = Radiobutton(canvLeft, text="Max Service", variable=varStopr, value=2)
    R2.pack(anchor=W)

    var1=IntVar()
    var2=IntVar()

    scale1 = Scale(canvLeft, variable = var1, from_=1, to=1000, orient=HORIZONTAL, label="Max Service Limit")
    scale1.pack()

    scale2 = Scale(canvLeft, variable = var2, from_=1, to=1000, orient=HORIZONTAL, label="Shift Time")
    scale2.pack()

    scaleLambda=Scale(canvLeft,from_=0.1, to=2.0, orient=HORIZONTAL, label='λ', resolution=0.1)
    scaleLambda.pack()

    scaleMu=Scale(canvLeft,from_=0.1, to=2.0, orient=HORIZONTAL,label='μ', resolution=0.1)
    scaleMu.pack()

    canvas = Canvas(root, height=300, width=800)
    canvas.pack()
    canvas.create_rectangle(730, 55, 770, 95, outline='white', fill='red')
    canvas.create_text(750, 75, text="S1")
    canvas.create_rectangle(730, 105, 770, 145, outline='white', fill='red')
    canvas.create_text(750, 125, text="S2")

    #Q1

    textvar1 = StringVar()
    textvar1.set("System Time Q1: 0.000000")

    QVar1=StringVar()
    QVar1.set("Queue Length Q1: 0")

    QMVar1=StringVar()
    QMVar1.set("Max Queue Length Q1: 0")

    labelSysTime1=Label(canvRight, textvariable=textvar1)
    labelSysTime1.pack(anchor=W)

    labelQueue1=Label(canvRight, textvariable=QVar1)
    labelQueue1.pack(anchor=W)

    labelQMax1=Label(canvRight, textvariable=QMVar1)
    labelQMax1.pack(anchor=W)

    AAVar1=StringVar()
    AAVar1.set("Average Arrival Time Q1: 0.000000")

    labelAAvg1=Label(canvRight, textvariable=AAVar1)
    labelAAvg1.pack(anchor=W)

    ASVar1=StringVar()
    ASVar1.set("Average Service Time Q1: 0.000000")

    labelSAvg1=Label(canvRight, textvariable=ASVar1)
    labelSAvg1.pack(anchor=W)

    SVar1=StringVar()
    SVar1.set("Services completed Q1: 0")

    labelServ1=Label(canvRight, textvariable=SVar1)
    labelServ1.pack(anchor=W)

    AVar1=StringVar()
    AVar1.set("People Arrived Q1: 0")

    labelArv1=Label(canvRight, textvariable=AVar1)
    labelArv1.pack(anchor=W)

    #Q2

    textvar2 = StringVar()
    textvar2.set("System Time Q2: 0.000000")

    QVar2=StringVar()
    QVar2.set("Queue Length Q2: 0")

    QMVar2=StringVar()
    QMVar2.set("Max Queue Length Q2: 0")

    labelSysTime2=Label(canvRight, textvariable=textvar2)
    labelSysTime2.pack(anchor=W)

    labelQueue2=Label(canvRight, textvariable=QVar2)
    labelQueue2.pack(anchor=W)

    labelQMax2=Label(canvRight, textvariable=QMVar2)
    labelQMax2.pack(anchor=W)

    AAVar2=StringVar()
    AAVar2.set("Average Arrival Time Q2: 0.000000")

    labelAAvg2=Label(canvRight, textvariable=AAVar2)
    labelAAvg2.pack(anchor=W)

    ASVar2=StringVar()
    ASVar2.set("Average Service Time Q2: 0.000000")

    labelSAvg2=Label(canvRight, textvariable=ASVar2)
    labelSAvg2.pack(anchor=W)

    SVar2=StringVar()
    SVar2.set("Services completed Q2: 0")

    labelServ2=Label(canvRight, textvariable=SVar2)
    labelServ2.pack(anchor=W)

    AVar2=StringVar()
    AVar2.set("People Arrived Q2: 0")

    labelArv2=Label(canvRight, textvariable=AVar2)
    labelArv2.pack(anchor=W)
    

    def looper():
        canvas.delete(ALL)
        canvas.create_rectangle(730, 55, 770, 95, outline='white', fill='red')
        canvas.create_text(750, 75, text="S1")
        canvas.create_rectangle(730, 105, 770, 145, outline='white', fill='red')
        canvas.create_text(750, 125, text="S2")
        varS=varStopr.get()
        maxClient=scale1.get()
        shiftTime=scale2.get()
        lam=scaleLambda.get()
        mu=scaleMu.get()
        n1=0 #number of clients serviced
        t1=0 #overall system time
        ta1=generateArr(lam) #initial approximation of arrival time
        ts1=generateServ(mu) #initial approximation of service time
        p1=0 #number of people that arrived
        q1=0 #queue length
        qMax1=0 #Max length of queue
        taTot1=ta1 #Advance Total of Arrival Times
        tsTot1=ts1 #Advance Total of Service Times
        taTotC1=0 #Current Total of Arrival Times
        tsTotC1=0 #Current Total of Service Times
        s1=0 #number of serviced people

        n2=0 #number of clients serviced
        t2=0 #overall system time
        ta2=generateArr(lam) #initial approximation of arrival time
        ts2=generateServ(mu) #initial approximation of service time
        p2=0 #number of people that arrived
        q2=0 #queue length
        qMax2=0 #Max length of queue
        taTot2=ta2 #Advance Total of Arrival Times
        tsTot2=ts2 #Advance Total of Service Times
        taTotC2=0 #Current Total of Arrival Times
        tsTotC2=0 #Current Total of Service Times
        s2=0 #number of serviced people

        while (varS==1 and t1<shiftTime and t2<shiftTime) or (varS==2 and n1<maxClient and n2<maxClient):

            if q1==0:
                t1=t1+ta1
                q1=1
                ta1=generateArr(lam)
                taTotC1=taTot1
                taTot1+=ta1
                client(canvas,q1,11)
                p1=p1+1

            else:
                if ts1<ta1:
                    t1=t1+ts1
                    if q1>qMax1:
                        qMax1=q1
                    q1=q1-1
                    ta1=ta1-ts1
                    ts1=generateServ(mu)
                    tsTotC1=tsTot1
                    tsTot1+=ts1
                    n1+=1
                    client(canvas,q1,12)
                    s1+=1
                else:
                    t1=t1+ta1
                    q1=q1+1
                    p1=p1+1
                    ts1=ts1-ta1
                    ta1=generateArr(lam)
                    taTotC1=taTot1
                    taTot1+=ta1
                    client(canvas,q1,11)

            
            if q2==0:
                t2=t2+ta2
                q2=1
                ta2=generateArr(lam)
                taTotC2=taTot2
                taTot2+=ta2
                client(canvas,q2,21)
                p2=p2+1

            else:
                if ts2<ta2:
                    t2=t2+ts2
                    if q2>qMax2:
                        qMax2=q2
                    q2=q2-1
                    ta2=ta2-ts2
                    ts2=generateServ(mu)
                    tsTotC2=tsTot2
                    tsTot2+=ts2
                    n2+=1
                    client(canvas,q2,22)
                    s2+=1
                else:
                    t2=t2+ta2
                    q2=q2+1
                    p2=p2+1
                    ts2=ts2-ta2
                    ta2=generateArr(lam)
                    taTotC2=taTot2
                    taTot2+=ta2
                    client(canvas,q2,21)
            
            textvar1.set("System Time Q1: %f"%t1)
            labelSysTime1.update_idletasks()
            QVar1.set("Queue Length Q1: %d"%q1)
            labelQueue1.update_idletasks()
            QMVar1.set("Max Queue Length Q1: %d"%qMax1)
            labelQMax1.update_idletasks()
            AAVar1.set("Average Arrival Time Q1: %f"%(taTotC1/p1))
            labelAAvg1.update_idletasks()
            if s1!=0:
                ASVar1.set("Average Service Time Q1: %f"%(tsTotC1/s1))
            labelSAvg1.update_idletasks()
            SVar1.set("Services Completed Q1: %d"%s1)
            labelServ1.update_idletasks()
            AVar1.set("People Arrived Q1: %d"%p1)
            labelArv1.update_idletasks()

            
            textvar2.set("System Time Q2: %f"%t2)
            labelSysTime2.update_idletasks()
            QVar2.set("Queue Length Q2: %d"%q2)
            labelQueue2.update_idletasks()
            QMVar2.set("Max Queue Length Q2: %d"%qMax2)
            labelQMax2.update_idletasks()
            AAVar2.set("Average Arrival Time Q2: %f"%(taTotC2/p2))
            labelAAvg2.update_idletasks()
            if s2!=0:
                ASVar2.set("Average Service Time Q2: %f"%(tsTotC2/s2))
            labelSAvg2.update_idletasks()
            SVar2.set("Services Completed Q2: %d"%s2)
            labelServ2.update_idletasks()
            AVar2.set("People Arrived Q2: %d"%p2)
            labelArv2.update_idletasks()
            
        #print("%d  %f  %d" %(n,t,q))

    showButton = Button(canvRight, text="Start Sim", command = looper)
    showButton.pack(side=LEFT)

    quitButton = Button(canvRight, text ="Quit", command = root.destroy)
    quitButton.pack(side=RIGHT)

    root.mainloop()

mm1()