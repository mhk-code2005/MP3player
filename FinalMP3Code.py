#MODULES=======================================
import os
import time
from tkinter import *
import tkinter
from tkinter import ttk
import helperCommandFunctions
import string
from functools import partial
import sys 
from pygame import mixer 
# GETTING TO FILES====================================
filenames=os.listdir('MUSIC')
categories={}
file_count=0
for file in filenames:
    categories.update({file_count:file})
    file_count+=1
#VARIABLES==================================
e=1
text1='song names here'
f=''
volume=.5
#WINDOW SETTINGS
master=Tk()
master.title('MP 3 PLAYER')
tabControl = ttk.Notebook(master) 
tab1 = ttk.Frame(tabControl) 
tab2 = ttk.Frame(tabControl) 
tab3 = ttk.Frame(tabControl) 
tab4 = ttk.Frame(tabControl) 
tabControl.add(tab1, text ='CATEGORIES') 
tabControl.add(tab2, text ='TO EXPLORE')
tabControl.add(tab3,text='TO LISTEN') 
tabControl.add(tab4,text='LISTENING CONTROLS') 
style=ttk.Style()
tabControl.pack(expand = 4, fill ="both") 
style.theme_create('Cloud', settings={
    ".": {
        "configure": {
            "background": 'white', # All colors except for active tab-button
            "font": 'red'
        }
    },
    "TNotebook": {
        "configure": {
            "background":'black', # color behind the notebook
#           ! "tabmargins": [5, 5, 0, 0], # [left margin, upper margin, right margin, margin beetwen tab and frames]
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": 'red', # Color of non        selected tab-button
            "padding": [100, 2], # [space beetwen text and horizontal tab-button border, space between text and vertical tab_button border]
            "font":"white"
        },
        "map": {
            "background": [("selected", 'yellow')], # Color of active tab
            "expand": [("selected", [1, 1, 1, 1])] # [expanse of text]
        },
    
    }
})

style.theme_use('Cloud')
#HELPER COMMAND FUNCTIONS=====================================
ttk.Style().configure('green/black.TButton', background='white',fg='red',activeforeground='white',highlightbackground='red',highlightforeground='blue',width=60)

def function_scale(val):
                global e
                global master

                global w
                global text1
                global filenames
                global l
                e = w.get()
                text1=categories[e]
                l=ttk.Label(tab1,background='white', text=str(((int(70)-int(len(text1))//2)*'-')+text1+str((int(90)-int(len(text1))//2)*'-')), width=93).grid(row=3, column=1)
                e = w.get()
                text1=categories[e]
                mixer.init()
                mixer.music.set_volume(.5)
                def player(ert):
                    mixer.music.load(ert)
                    mixer.music.play()
#                try:
                for widget in tab3.winfo_children():
                    widget.destroy()
                for widget in tab2.winfo_children():
                    widget.destroy()
                
                filename1='MUSIC/'+text1+'/'
                width=0
                length=0                
                files_inside_a_directory=os.listdir(filename1)
                ert='MUSIC/'+text1+'/'
                ert2=ert[:]
                width=0
                length=0
                for wqr in files_inside_a_directory:
                    ert+=wqr
                    if width%8==0:
                            width=0
                            length+=1
                    
                    ttk.Button(tab3,style='green/black.TButton',text=wqr,command=partial(player,ert)).grid(row=width,column=length)
                    ert=ert2
                    width+=1 
#                except:
#                    
#                    b=ttk.Label(tab2,text='PLEASE SLIDE THE SLIDER TO CHOOSE A CATEGORY',width=60).grid(row=1,column=1)
                    
                try:
                        file='MUSIC/'+text1
                        files_inside_a_directory=os.listdir(file)
                        length=0
                        file+='/'
                        width=0
                        for s in files_inside_a_directory:
                                if width%8==0:
                                        width=0
                                        length+=1
                                c=ttk.Label(tab2,background='dark blue',foreground='white' ,text=s,width=60).grid(row=width,column=length)
                                width+=1
                except:
                        c=Label(tab2,background='white',text='PLEASE SLIDE TO SELECT A CATEGORY',width=60,).grid(row=1,column=1)
                def starter():
                    mixer.music.play()

                def resumer():
                    mixer.music.unpause()
                def pauser():
                    mixer.music.pause()
                def exiter():
                    mixer.music.pause()
                    master.destroy()
                def volume_setter(val):
                    global volumer
                    p=volumer.get()
                volumer=ttk.Scale(tab4,
                      from_=100, to=0)
                def volume_setter(val):
                    p=volumer.get()/100
                    mixer.music.set_volume(p)
                volumer=ttk.Scale(tab4,
                      orient=VERTICAL,
                      from_=100, to=0,
                      command=volume_setter)        
                def rewinder():
                    mixer.music.rewind()
                ttk.Button(tab4,text='▶',command=resumer).grid(row=1,column=2)    
                ttk.Button(tab4,text='||',command=pauser).grid(row=1,column=1)
                ttk.Button(tab4,text='QUIT',command=exiter).grid(row=1,column=3)
                ttk.Button(tab4,text='◀||',command=rewinder).grid(row=1,column=4)
                volumer.grid(row=1,column=5)
    #SCALE=======================================
w = Scale(tab1,
          from_=0, to=len(filenames), 
          length=927,
          tickinterval=8,
          bg='red',
          fg='white',
          activebackground='yellow',
          orient=HORIZONTAL,
          command=function_scale)
w.grid(row=1,column=1)
style.theme_use('Cloud')
mainloop()

