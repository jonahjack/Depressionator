import gtts
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
import json

#now supporting git

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

global Information
Information = {}

triggerWord1 = ""
triggerWord2 = ""
triggerWord3 = ""
triggerWord4 = ""

twitchmode = False
regulatmode = True
isInsult = False


# speech_recognition functions
def get_Audio(): # gets audio from user mic and parses it
    r = sr.Recognizer() # used to get the audio library
    with sr.Microphone() as source: # uses the sr.Microphone() function as source for refference
        
        r.adjust_for_ambient_noise(source, duration=1) # adjusts for background noise
        audio = r.listen(source) # makes a var audio that is using source as a listening device
        said = "" # empty placeholder var

        try: 
            said = r.recognize_google(audio) # sets said to = tghe output of our audio passed throug a google api that tries to figure out what is being said
        except Exception as e:
            print("Exception" + str(e)) # if the api cant recognize the audio, or any other errors happen, it will print the error in the log instead of stopping the program
    
    startVoice(audio=said) # starts the filters for the trigegr words

def startVoice(audio): # filters the words in the sentence to see if they are any of the preset trigger words.

    if triggerWord1 != "null": # Checks to see if the word is set, the word will be "null" by default.
        if triggerWord1 in audio: # Checks for the word in the sentence
            randomInsult()  # if it finds the word
            return # if it does it triggers the Insult generator and ends the cycle until insult is generated and spoken
        else:
            pass # if not conite to the next word and rinse and repeat for the rest
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

    get_Audio() # is it doest find a word it just restarts the whole loop

# random insult genorator functions
def randomInsult(): # Makes A Random Insult Using randon.choice and the columns of insults above
    
    randomcol1 = random.choice(col1) # chooses a random word from the columns above
    randomcol2 = random.choice(col2) # chooses a random word from the columns above
    randomcol3 = random.choice(col3) # chooses a random word from the columns above
    InsultFinal = "Thou " + randomcol1+ " " + randomcol2 + " " + randomcol3 + "!" # puts the insult together
    TTS(InsultFinal) # sends it to the TTS function

# Google tts functions
def TTS(ins): # Uses google TTS modual to turn our insult variable to audiable speech
    insulttts = gTTS(ins) # initiates google tts
    date_string = datetime.datetime.now().strftime("%d%m%Y%H%M%S") #creates a datestring for the file name to be unique
    filename = "voice"+date_string+".mp3" # makes the name of the file for future use
    insulttts.save(filename) # saves the file with the name made above
    playsound.playsound(filename) # plays the file without need of groove music being opened
    os.remove(filename) # deletes the file to keep folder size low
    get_Audio() # starts the cycle all over again




"""
this is the explanation of everything in the tkinter section, as it would be painful to leave this as a string of hashtag im just using quotes to keep it uniform
A quick overview of the libraries i used bellows' functions so you'll know what im doing bellow, i'll still leave comments in confusing areas tho
tk = tkinter so anything starting with that is here
.TK: Makes a window to host our widgets
.Frame: Makes a frame similar to a TK, exept its soul purpose os to hold widgets but still be movable and seperate from the rest of the Window
.Button: Makes a button
.Label: Makes text
.OptionMenu: Makes a Drop Down Menu
.Entry: Makes a user input text field
.StringVar: Makes a string variable that can be used by entry fields of any kind
.IntVar: Same as .StringVar but for ints
.grid: places the items on a predetermined grid instead of randomly, keeps things orginized
.pack: places things in a top to bottom order in the middle on the x axis
.destroy: destroys the widget
.winfo_children: Gets a list of children in an object
.geometry: sets size of a window
.title: sets the name of a window
.resizable: says if the window is resizable, and on what axis
.mainloop: loops as long as tkinter window is open

webbrowser: opens a tab on the browser for the link you set


"""


# webbrowser functions
def takeChannel():
    webbrowser.open_new_tab('https://www.youtube.com/channel/UCEsSazCLxuFXYxZAx2BmOMQ')

def takeTutorial():
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=zNFospmOFdg')

# Tkinter Functions
def clearframe(clear): # clears the frame of widgets
    for widgets in clear.winfo_children():
      widgets.destroy()

def makeRegButton(): # makes the Regular mode buttons
    global regular_button
    regular_button = tk.Button(root, text="Regular Mode", command= regularMode)
    regular_button.grid(row=4, column=0,pady=3)

def makeStreamButton(): # makes the Twitch mode buttons
    global stream_button
    stream_button = tk.Button(root, text="Twitch Mode   ", command= streamMode)
    stream_button.grid(row=3,column=0,pady=3)

def makeFrame(): # makes the frame used for either mode 
    global frame
    frame = tk.Frame(root, width=600, height=445)
    frame.grid(row=5,column=0, pady=15)


def regularMode(): # makes the menu and variables for the regular mode
    clearframe(clear=frame) # clears the frame for the new menu to be created
    regulatmode = True
    twitchmode = False
    global regEntryText
    regEntryText = tk.Label(frame, text="Trigger Word Count:")
    regEntryText.pack()
    global drop
    drop = tk.OptionMenu( frame , clicked , *options )
    drop.pack()
    global regEntryButton
    regEntryButton = tk.Button(frame, text="Enter Numbers", command=loadEntry)
    regEntryButton.pack()
    
def loadEntry():  # makes the entry fields and buttons needed to make the new menu using loops that are determined by the number you chose before
    regEntryText.destroy()
    drop.destroy()
    regEntryButton.destroy()
    global num
    num = 0  #num is used allot in this script, it keeps indexes for loops so the dictionaries used can have incremental results, any time you see null = 0 its resetting the index
    global regEntryDic
    regEntryDic = {} # holds the values for the text fields that will be made
    global entered # holds the output of those fields
    entered = {}
    for i in range(4):
        num +=1
        entered["Value%s" %num]= tk.StringVar() # uses % tags to make unique var names inside the dictionatry
        entered["Value%s" %num].set("null") # sets it by default to null
    num = 0 
    for i in range(clicked.get()): # this loop goes for the number of fields you selected
        num +=1
        regEntryDic["regEntry%s" %num] = tk.Entry(frame) # uses % tags to make unique var names inside the dictionatry
        regEntryDic["regEntry%s" %num].pack(pady=3) # packs that variable to the screen
        regEntryDic["regEntry%s" %num].config(textvariable = entered["Value%s" %num])  #sets the texvariable to be the entered dictionary at this index
    global RegSubmit
    RegSubmit = tk.Button(frame, text="Submit", command=regSubmitEntry)
    RegSubmit.pack(pady=3)

def regSubmitEntry():
    clearframe(clear=frame)
    assignVariables()
    closepage = tk.Label(frame, text="Now when you close this window it will listen for those words,\nif you want the program to stop close the terminal that pops up as well,\ndo not close the terminal until you want the program to stop.").pack()

def streamMode(): # makes the menu and variables for the Twitch mode
    clearframe(clear=frame)
    regulatmode = False # Toggles Between Streamer And Reg Mode
    twitchmode = True
    global entry1Sub
    entry1Sub = tk.StringVar()
    entry1text = tk.Label(frame, text="Auth Code").pack()
    entry1 = tk.Entry(frame, textvariable=entry1Sub, show="*") # show makes it possible to protect your password visibly
    entry1.pack(pady=3)
    global entry2Sub
    entry2Sub = tk.StringVar()
    entry1text = tk.Label(frame, text="Username").pack()
    entry2 = tk.Entry(frame, textvariable=entry2Sub)
    entry2.pack(pady=3)
    twitchsubButton = tk.Button(frame, text="Submit", command=streammodeSubmit).pack()
    
def streammodeSubmit(): # send the vars to be used in a txt format
    clearframe(clear=frame)
    closeprompt = tk.Label(frame, text="Trigger words will be determined by audience, suggestions containing Bad Words are thrown out though.\nIf you want to continue in this mode, close this window!").pack()
    Information['Auth'] = entry1Sub.get() # sends the entry data to a dic slot
    Information['Channel'] = entry2Sub.get()
    with open("data.json", "w") as write_file: # opens a json file
        json.dump(Information, write_file) # dumps the data to the json file
        write_file.close() # closes the json file


def assignVariables(): # assigns the variables
    num = 0
    global values
    values = {} # list of variables for text entries
    for i in range(4):
        num+=1
        values["val%s" %num] = entered["Value%s" %num].get() # sets each variable to its corisponding StringVar

#End of Tkinter Functions

    


#Start of tkinter loop
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

title = tk.Label(root, text="Hello and welcome to my game, My name is Code 9Mill and I live to make 'Inovative' programs like this.\nBellow their's some config options, if you get confused just press the tutorial button bellow.\nGood luck, and please give me credit for the hours of dedication I give to these seamingly useless programs.").grid(row=0,column=0)
tutorial_button = tk.Button(root, text="Tutorial", width=10, command=takeTutorial).grid(row=1,column=0,pady=3)
channel_button = tk.Button(root, text="Channel", width=10, command=takeChannel).grid(row=2,column=0,pady=3)

makeStreamButton()
makeRegButton()
makeFrame()




root.mainloop()

#End of tkinter loop

#Start of program after the menu
# playsound.playsound('Intoduction.mp3')

if regulatmode == True:
    try:
        triggerWord1 = values['val1'] # setting the variables to the trigger words
        triggerWord2 = values['val2'] # setting the variables to the trigger words
        triggerWord3 = values['val3'] # setting the variables to the trigger words
        triggerWord4 = values['val4'] # setting the variables to the trigger words
    except Exception as e:
        pass
if twitchmode == True:
    trigger = [] # maeks a trigger list
    Trigger = open('TriggerWords.txt', 'r')  #opens the trigger words file
    for line in Trigger.readlines(): # for each line in this txt file...
        line = line.strip() # gets rid of the \n at the end of each line
        trigger.append(line) # adds the line to the list
    triggerWord1 = random.choice(trigger) # chooses a random item in the list x4
    triggerWord2 = random.choice(trigger)
    triggerWord3 = random.choice(trigger)
    triggerWord4 = random.choice(trigger)

get_Audio() # starts cycle 



#Start of twitch bot