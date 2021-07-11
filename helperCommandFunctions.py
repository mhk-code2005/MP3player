    #HELPER COMMAND FUNCTIONS=====================================
def file_setter(val):
            global e
            global w
            global text1
            global filenames
            global l
            e = w.get()
            text1=categories[e-1]
            l=Label(master, text=text1, width=93, height=2, background='orange').grid(row=2, column=1)
def play_music1():
    mixer.music.play()
def pause_music():
    mixer.music.pause()
def play_music(file):     
    mixer.init()
    mixer.music.load(file) 
    mixer.music.set_volume(10) 
def file_setter2():
            global e
            global w
            global text1
            global l
            global filenames
            e = w.get()
            text1=categories[e-1]
            print(text1)
            l=Label(master, text=text1, width=93, height=2, background='orange').grid(row=2, column=1)    
def see_files():
    
#    try:
        file_setter2
        global text1
        newWindow=Tk()
        global files_inside_a_directory
        newWindow.title( text1)
        global master
        file='/home/mahir/Desktop/MUSIC/'+text1
        print('file:',file)
        files_inside_a_directory=os.listdir(file)
        length=0
        file+='/'
        width=0
        for s in files_inside_a_directory:
            file1=file+s
            if width%8==0:
                width=0
                length+=1
            b=Button(newWindow,text=s,command=play_music(file1),width=60, height=3 ).grid(row=width, column=length)    
            width+=1
        Button(master,command=play_music1(),text='play').grid(column=1,row=40)
        Button(master,command=pause_music(), text='pause').grid(column=1,row=80)
#    except:
#            s="PLEASE SELECT A CATEGORY BY SLIDING THE SLIDER"    
#            b=Label(newWindow,text=s,width=60, height=3 ).grid(row=1, column=1)
    
        b6=Button(newWindow, text='quit',command=newWindow.destroy).grid(row=7,column=1)