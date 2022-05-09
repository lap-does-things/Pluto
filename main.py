import re, requests, subprocess, urllib.parse, urllib.request
import pafy
from selenium import webdriver
from tkinter import ttk


from tkinter import *

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('ignoreDefaultArgs')
options.add_argument('--autoplay-policy=no-user-gesture-required')
options.add_experimental_option("detach", True)
#options.add_argument('window-size=1200x600')

driver = webdriver.Chrome(options=options)

def setch(x):
    global ch
    ch = x
    if x ==0:
        option1.configure(bg='#888f03')
        option2.configure(bg='#333333')
        option3.configure(bg='#333333')
        option4.configure(bg='#333333')
        option5.configure(bg='#333333')
        option6.configure(bg='#333333')
        option7.configure(bg='#333333')
    if x ==1:
        option1.configure(bg='#333333')
        option2.configure(bg='#888f03')
        option3.configure(bg='#333333')
        option4.configure(bg='#333333')
        option5.configure(bg='#333333')
        option6.configure(bg='#333333')
        option7.configure(bg='#333333')
    if x==2:
        option1.configure(bg='#333333')
        option2.configure(bg='#333333')
        option3.configure(bg='#888f03')
        option4.configure(bg='#333333')
        option5.configure(bg='#333333')
        option6.configure(bg='#333333')
        option7.configure(bg='#333333')
    if x==3:
        option1.configure(bg='#333333')
        option2.configure(bg='#333333')
        option3.configure(bg='#333333')
        option4.configure(bg='#888f03')
        option5.configure(bg='#333333')
        option6.configure(bg='#333333')
        option7.configure(bg='#333333')
    if x==4:
        option1.configure(bg='#333333')
        option2.configure(bg='#333333')
        option3.configure(bg='#333333')
        option4.configure(bg='#333333')
        option5.configure(bg='#888f03')
        option6.configure(bg='#333333')
        option7.configure(bg='#333333')
    if x==5:
        option1.configure(bg='#333333')
        option2.configure(bg='#333333')
        option3.configure(bg='#333333')
        option4.configure(bg='#333333')
        option5.configure(bg='#333333')
        option6.configure(bg='#888f03')
        option7.configure(bg='#333333')
    if x==6:
        option1.configure(bg='#333333')
        option2.configure(bg='#333333')
        option3.configure(bg='#333333')
        option4.configure(bg='#333333')
        option5.configure(bg='#333333')
        option6.configure(bg='#333333')
        option7.configure(bg='#888f03')

root = Tk()
frame = Frame(root,width=370,height=250)
option1=Button(frame,width=350,command=lambda :setch(0))
#option1.place(x=0,y=20)
option2=Button(frame,width=350,command=lambda :setch(1))
#option2.place(x=0,y=45)
option3=Button(frame,width=350,command=lambda :setch(2))

option4=Button(frame,width=350,command=lambda :setch(3))

option5=Button(frame,width=350,command=lambda :setch(4))

option6=Button(frame,width=350,command=lambda :setch(5))
#
option7=Button(frame,width=350,command=lambda :setch(6))
#




def on_closing():
    driver.close()
    exit()





def search():
    music_name = searchbar.get()
    query_string = urllib.parse.urlencode({"search_query": music_name})

    formatUrl = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)

    search_results = re.findall(r"watch\?v=(\S{11})", formatUrl.read().decode())
    global clip
    global clip2
    clip = requests.get("https://www.youtube.com/watch?v=" + "{}".format(search_results[0]))
    clip2 = "https://www.youtube.com/watch?v=" + "{}".format(search_results[0])
    i=0
    l=['','','','','','','','']
    global links
    links=['','','','','','','','']
    for i in range(7):
        c="https://www.youtube.com/watch?v=" + "{}".format(search_results[0+i])
        links[i]=c
        video=pafy.new(c)
        l[i] = video.title


    option1.configure(text=l[0], anchor="w")
    option1.place(x=0, y=20)

    option2.configure(text=l[1], anchor="w")
    option2.place(x=0, y=45)

    option3.configure(text=l[2], anchor='w')
    option3.place(x=0,y=70)

    option4.configure(text=l[3],anchor = 'w')
    option4.place(x=0,y=95)

    option5.configure(text=l[4],anchor='w')
    option5.place(x=0,y=120)

    option6.configure(text=l[5],anchor='w')
    option6.place(x=0, y=145)

    option7.configure(text=l[6],anchor='w')
    option7.place(x=0, y=170)

def play():

    go2.configure(bg='#888f03')
    if ch == 0:
        driver.get(links[0] + "?autoplay=1")
    if ch==1:
        driver.get(links[1]+ "?autoplay=1")
    if ch==2:
        driver.get(links[2]+ "?autoplay=1")
    if ch==3:
        driver.get(links[3]+ "?autoplay=1")
    if ch==4:
        driver.get(links[4]+ "?autoplay=1")
    if ch==5:
        driver.get(links[5] + "?autoplay=1")
    if ch==6:
        driver.get(links[6] + "?autoplay=1")
    # time.sleep(2)
    # pyautogui.press('space')
    #while (True):
    #    pass
def stop():
    go2.configure(bg='#333333')
    global driver
    driver.close()
    driver = webdriver.Chrome(options=options)


root.geometry('370x250')
root.geometry('+300+200')
root.resizable(False,False)


searchbar = Entry(frame, width=290)
searchbar.place(x=0,y=0)

go = Button(frame, command=lambda :search(), text = 'Поиск',width=10)
go2= Button(frame,command=lambda :play(), text = '►', font='20')
go.place(x=290,y=-5)
go2.place(x=0,y=220)
stop1=Button(frame,command=lambda :stop(),text =' | | ', font='20',width=3)
stop1.place(x=30,y=220)

#shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe',
                   #          lpParameters='/b ' + "start Миша\Documents\Pluto\mpv\mpv.exe --no-video")
#subprocess.Popen("start /b " + "mpv\mpv.exe " + clip2 + " --no-video", shell=True)

style = ttk.Style(root)
root.tk.call('source', 'src1/azure.tcl')
style.theme_use('azure')
style.configure("Accentbutton", foreground='white')
style.configure("Togglebutton", foreground='white')
credit=Label(frame,text='Pluto. For Russians by Lap.',font = '6')
credit.place(x=75,y=222)
frame.place(x=0,y=0)
root.title('Pluto')
root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()

