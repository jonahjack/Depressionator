import gtts
from httpx import get
import numpy as np
import random
from gtts import gTTS
import speech_recognition as sr
import os
import asyncio
import tkinter as tk
import webbrowser
import playsound
import datetime

# making the insults
col1 = ["Artless","Bawdy","Beslubbering","Bootless","Churlish","Cockered ","Clouted","Craven","Currish","Dankish","Dissembling","Droning","Errant","Fawning","Fobbing","Froward","Frothy","Gleeking","Goatish","Gorbellied","Impertinent","Infectious","Jarring","Loggerheaded","Lumpish","Mammering","Mangled","Mewling","Paunchy","Pribbling","Puking","Puny","Qualling","Rank","Reeky","Roguish","Ruttish","Saucy","Spleeny","Spongy","Surly","Tottering","Unmuzzled","Vain","Venomed","Villainous","Warped"]
col2 = ["base-court","bat-fowling","beef-witted","beetle-headed","boil-brained","common-kissing","crook-pated","dismal-dreaming","dizzy-eyed","dog-hearted","dread-bolted","earth-vexing","elf-skinned","fat-kidneyed","fen-sucked","flap-mouthed","fly-bitten","folly-fallen","fool-born","full-gorged","futs-griping","half-faced","hasty-witted ","hedge-born","hell-hated","idle-headed","ill-nurtured","knotty-pated","milk-livered","motley-minded","onion-eyed","plume-plucked","pottle-deep ","pox-marked","reeling-ripe","rough-hewn","rude-growing","rump-fed","shard-borne","sheep-biting","spur-galled","swag-bellied","tardy-gaited","tickle-brained","toad-spotted","unchin-snouted","weather-bitten"]
col3 = ["apple-john","baggage","barnacle","bladder","boar-pig","bugbear","bum-bailey","canker-blossom","clack-dish","clotpole","coxcomb","death-token","dewberry","flap-dragon","flax-wench","flirt-gill","foot-licker","fustilarian","giglet","gudgeon","haggard","harpy","hedge-pig","horn-beast","hugger-mugger","jolthead","lewdster","lout","maggot-pie","malt-worm","mammet","measle","minnow","miscreant","moldwarp","mumble-news","nut-hook","pigeon-egg","pignut","puttock","pumpion","ratsbane","scut","skainsmate","strumpet","vartlot","vassal"]

# making variables
global options
options = [
    "1",
    "2",
    "3",
    "4"
]

triggerWord1 = ""
triggerWord2 = ""
triggerWord3 = ""
triggerWord4 = ""

isInsult = False


def randomInsult():
    
    randomcol1 = random.choice(col1)
    randomcol2 = random.choice(col2)
    randomcol3 = random.choice(col3)
    InsultFinal = "Thou " + randomcol1+ " " + randomcol2 + " " + randomcol3 + "!"
    TTS(InsultFinal)

def TTS(ins):
    insulttts = gTTS(ins)
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S")
    filename = "voice"+date_string+".mp3"
    insulttts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)
    get_Audio()



def takeChannel():
    webbrowser.open_new_tab('https://www.youtube.com/channel/UCEsSazCLxuFXYxZAx2BmOMQ')

def takeTutorial():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=zNFospmOFdg')

def makeRegButton():
    global regular_button
    regular_button = tk.Button(root, text="Regular Mode", command= regularMode)
    regular_button.grid(row=4, column=0,pady=3)

def makeStreamButton():
    global stream_button
    stream_button = tk.Button(root, text="Streamer Mode(Coming Soon)", command= streamMode)
    stream_button.grid(row=3,column=0,pady=3)

def makeFrame():
    global frame
    frame = tk.Frame(root, width=600, height=445)
    frame.grid(row=5,column=0, pady=15)


def regularMode():
    clearframe(clear=frame)
    global regEntryText
    regEntryText = tk.Label(frame, text="Trigger Word Count:")
    regEntryText.pack()
    global drop
    drop = tk.OptionMenu( frame , clicked , *options )
    drop.pack()
    global regEntryButton
    regEntryButton = tk.Button(frame, text="Enter Numbers", command=loadEntry)
    regEntryButton.pack()
    
def loadEntry():
    regEntryText.destroy()
    drop.destroy()
    regEntryButton.destroy()
    global num
    num = 0
    global regEntryDic
    regEntryDic = {}
    global entered
    entered = {}
    for i in range(4):
        num +=1
        entered["Value%s" %num]= tk.StringVar()
        entered["Value%s" %num].set("null")
    num = 0
    for i in range(clicked.get()):
        num +=1
        regEntryDic["regEntry%s" %num] = tk.Entry(frame)
        regEntryDic["regEntry%s" %num].pack(pady=3)
        regEntryDic["regEntry%s" %num].config(textvariable = entered["Value%s" %num])
    global RegSubmit
    RegSubmit = tk.Button(frame, text="Submit", command=regSubmitEntry)
    RegSubmit.pack(pady=3)
    
def clearframe(clear):
    for widgets in clear.winfo_children():
      widgets.destroy()

def regSubmitEntry():
    clearframe(clear=frame)
    num = 0
    for i in range(clicked.get()):
        num +=1
        regEntryDic["regEntry%s" %num].destroy()
        RegSubmit.destroy()
    num = 0
    for i in range(4):
        num +=1
    assignVariables()
    closepage = tk.Label(frame, text="Now when you close this window it will listen for those words,\nif you want the program to stop close the terminal that pops up as well,\ndo not close the terminal until you want the program to stop.").pack()

def streamMode():
    clearframe(clear=frame)
    comingsoon = tk.Label(frame, text="Coming Soon").pack()


def speak(text):
    ttsb = gTTS(text=text, lang="en")
    filenameb = "voice.mp3"
    ttsb.save(filenameb)
    playsound.playsound(filenameb)

def assignVariables():
    num = 0
    global values
    values = {}
    for i in range(4):
        num+=1
        values["val%s" %num] = entered["Value%s" %num].get()


def get_Audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:  
            print("Exception" + str(e))
    
    startVoice(audio=said)

def startVoice(audio):

    if triggerWord1 != "null":
        if triggerWord1 in audio:
            randomInsult()
            return
        else:
            pass
    if triggerWord2 != "null":
        if triggerWord2 in audio:
            randomInsult()
            return
        else:
            pass
    if triggerWord3 != "null":
        if triggerWord3 in audio:
            randomInsult()
            return
        else:
            pass
    if triggerWord4 != "null":
        if triggerWord4 in audio:
            randomInsult()
            return
        else:
            pass

    get_Audio()
    


global root
root = tk.Tk()
# getting window close to center
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("600x600")
root.geometry("+{}+{}".format(positionRight - 300, positionDown - 300))
root.title('Depressionator')
root.resizable(False, False)

global clicked
clicked = tk.IntVar()
clicked.set("1")

root.grid_rowconfigure(0, weight=0)
root.grid_columnconfigure(0, weight=0)

title = tk.Label(root, text="Hello and welcome to my game, My name is Code 9Mill and I live to make 'Inovative' programs like this.\nBellow their's some config options, if you get confused just press the tutorial button bellow.\nGood luck, and please give me credit for the hours of dedication I give to these seamingly useless programs.").grid(row=0,column=0)
tutorial_button = tk.Button(root, text="Tutorial", width=10, command=takeTutorial).grid(row=1,column=0,pady=3)
channel_button = tk.Button(root, text="Channel", width=10, command=takeChannel).grid(row=2,column=0,pady=3)

makeStreamButton()
makeRegButton()
makeFrame()




root.mainloop()

playsound.playsound('Intoduction.mp3')


triggerWord1 = values['val1']
triggerWord2 = values['val2']
triggerWord3 = values['val3']
triggerWord4 = values['val4']


get_Audio()





