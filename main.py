import tkinter as tk
from tkinter import messagebox as msg
import os
try:
    from elevate import elevate
except:
    os.system("pip install elevate")
    from elevate import elevate
elevate(show_console=False)

root = tk.Tk()
root.title("Youtube URL downloader installer")
root.geometry("400x400")
root.resizable(False, False)
root.config(bg="light blue")
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)
introLabel = tk.Label(root, text="The YT Protocol Installer", font=("Times New Roman", 24), justify="center", bg="light blue")
introLabel.grid(row=0, column=1)
introText = tk.Label(root, text="This install wizard will guide you \nthrough installing the YT protocol\n onto your system", font=("Times New Roman", 18))
introText.grid(row=1, column=1)
def showInfo():
    msg.showinfo("What",
                 "The YT protocol will allow you to download a youtube video simply by adding yt:// in front of the URL in your browser. (super nerd stuff) The way this works is by adding a registry key that defines a yt:// protocol which when visited, runs the python file this program installs.")

whatButton = tk.Button(root, width=46, height=4, text="What is that?", font=("Arial", 12), command=showInfo)
whatButton.grid(row=2, column=1)
def startThing():
    introLabel.destroy()
    whatButton.destroy()
    startButton.destroy()
    introText.config(text="EULA\nLong story short, while this program is \nnot designed to screw up your pc, \nin the (legitimately unlikely) scenario \nthat this messes up your pc, \nit's not my fault")
    def install():
        agreeButton.destroy()
        textV = ""
        introText.config(text="", height=9, justify="center")
        e = os.popen("python --version")
        if not e.read().startswith("Python 3"):
            msg.showerror("Fatal Error", "Python 3 is not installed on your system or in your PATH. Please install Python 3, and then continue with setup")
            exitThing()
        textV += "Python is installed!\n\nPlease enter where you would like\n the videos to be saved"
        introText.config(text=textV)
        dest="notReady"
        def getT():
            dest = inputB.get()
            textV = "Python is installed!\nSave spot picked!\nCreating registry tweak!"
            introText.config(text=textV)
            pyFile = open("ytDown.py", "w+")
            strT = f"""try:
    import sys
    import os

    try:
        from moviepy.editor import *
    except:
        os.system("pip install moviepy")
        from moviepy.editor import *
    try:
        from pytube import YouTube
        import pytube
    except:
        os.system("pip install pytube")
        from pytube import YouTube
        import pytube
    
    def MP4ToMP3(mp4, mp3):
        FILETOCONVERT = AudioFileClip(mp4)
        FILETOCONVERT.write_audiofile(mp3)
        FILETOCONVERT.close()
    
    if "/?" in sys.argv:
        print("YouTube downloader///nUsage:///n  /?  Displays this prompt///nArguments:///n  ytmp3 (save to) (video link 1) (link 2) (link 3)...")
    if "python" in sys.argv[0]:
        SAVE_PATH = "{dest}"
    else:
        try:
            SAVE_PATH = "{dest}"
        except:
            SAVE_PATH = "{dest}"

    if SAVE_PATH == None or SAVE_PATH == "" or "." in SAVE_PATH:
        SAVE_PATH = "{dest}"
    link = sys.argv
    e = 0
    print("///nSAVE PATH " + SAVE_PATH + "///n")
    if "yt://" in link[0]:
        link[0] = link[0].replace("C:/users/nkett/onedrive/pycharmprojects/ytmp3/ytmp3.pyyt://", "")
    for i in link:
        if "ytmp3.py" in i:
            continue
    #try:
        if "list" in i:
            p = pytube.Playlist(i)
            for video in p.videos:
                print(f"downloading <video.title>, video <e>/<p.length>")
                e+=1
                video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)
                if "-mp3" in sys.argv:
                    tit = video.title
                    tit = tit.replace(":", "")
                    tit = tit.replace("?", "")
                    tit = tit.replace("'", "")
                    tit = tit.replace("!", "")
                    tit = tit.replace(",", "")
                    if SAVE_PATH.endswith("/") or SAVE_PATH.endswith("\\\\"):
                        tit = SAVE_PATH + tit
                    else:
                        tit = SAVE_PATH + "/" + tit
                    print(tit)
                    MP4ToMP3(tit + ".mp4", tit + ".mp3")
                    os.remove(tit + ".mp4")
                    print("converted")
        else:
            if ".com" in i or "youtu.be" in i:
                print(f"dling <i>")
                yt = YouTube(i)
                yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)
                print(f"<i> dl")
                if "-mp3" in sys.argv:
                    tit = yt.title
                    tit = tit.replace(":", "")
                    tit = tit.replace("?", "")
                    tit = tit.replace("'", "")
                    tit = tit.replace("!", "")
                    tit = tit.replace(",", "")
                    if SAVE_PATH.endswith("/") or SAVE_PATH.endswith("//////"):
                        tit = SAVE_PATH + tit
                    else:
                        tit = SAVE_PATH + "/" + tit
                    print(tit)
                    MP4ToMP3(tit + ".mp4", tit + ".mp3")
                    os.remove(tit + ".mp4")
                    print("converted")
            else:
                print(f"Skipping <i> because it didnt pass the website filter")
    #except Exception as e:
    #    print(f"issue <i>, <e>")

    print('download Completed!')
except Exception as e:
    input(e)


""".replace("///", "\\").replace("<", "{").replace(">", "}")
            pyFile.write(strT)
            pyFile.close()
            textV += "\nPython file created!"
            introText.config(text=textV)
            regFile = open("regTweak.reg", "w+")
            working = os.popen("cd").read().removesuffix("\n").replace("\\", "/")
            regFile.write(f"""Windows Registry Editor Version 5.00\n\n[HKEY_CLASSES_ROOT\yt]\n"URL Protocol"=""\n@="URL:yt"\n\n[HKEY_CLASSES_ROOT\yt\shell]\n@="opennew"\n\n[HKEY_CLASSES_ROOT\yt\shell\open]\n\n[HKEY_CLASSES_ROOT\yt\shell\open\command]\n@="C:\\\\Users\\\\{os.getlogin()}\\\\AppData\\\\Local\\\\Programs\\\\Python\\\\Python311\\\\python.exe {working}/ytDown.py %1" """)
            regFile.close()
            textV += "\nRegistry file created"
            introText.config(text=textV)
            e = os.system("reg import regTweak.reg")
            print(f"thing {e}")
            if e==1:
                msg.showerror("Fatal Error", f"Install failed when adding the registry tweak")
                exitThing()
            #r = os.system("REG ADD HKCR\yt\shell\open\command /v Data /t REG_BINARY /d fe340ead")
            textV += "\nRegistry file possibly installed"
            introText.config(text=textV)
            msg.showinfo("Status", "We're done! Try it out now!")
            exitThing()
        contBut = tk.Button(root, text="Next", command=getT)
        contBut.grid(row=3, column=1)
        inputB = tk.Entry(root)
        inputB.grid(row=2, column=1)

    agreeButton = tk.Button(root, width=46, height=4, text="Aight, lets go!", font=("Arial", 12), command=install)
    agreeButton.grid(row=3, column=1)

startButton = tk.Button(root, width=46, height=4, text="Lets go!", font=("Arial", 12), command=startThing)
startButton.grid(row=3, column=1)
def exitThing():
    root.destroy()
    exit()
cancelButton = tk.Button(root, width=46, height=4, text="Wait go back", font=("Arial", 12), command=exitThing)
cancelButton.grid(row=4, column=1)



root.mainloop()
