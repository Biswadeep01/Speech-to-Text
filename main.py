import speech_recognition as sr
import pyttsx3
from tkinter import *
import os


def SpeakText(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def get_input():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            SpeakText('listening')
            audio = r.listen(source)
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()
    except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    except sr.UnknownValueError:
        Label(root, text="Unknown Error Occured").pack(ipadx = 40, ipady = 20)
        SpeakText('unknown error occured')
    except sr.WaitTimeoutError:
        Label(root, text="Wait Timeout Error Occured").pack(ipadx = 40, ipady = 20)
        SpeakText('wait timeout error occured')
    return MyText


def get_audio():
    while True:
        input = get_input()
        if 'stop' in input:
            SpeakText('Thank you for using the program')
            break
        elif 'open' in input:
            SpeakText('Opening file explorer')
            os.system('explorer')
            break
        elif 'append' in input:
            input = input.replace("append", "")
            SpeakText(input)
            Label(root, text=input, font=('Times New Roman', 14)).pack(ipadx = 40, ipady = 20)
            file = open('text.txt', 'a+')
            file.writelines("\n", input)
            file.close()
            SpeakText('appended')
            break
        else:
            SpeakText(input)
            Label(root, text=input, font=('Times New Roman', 14)).pack(ipadx = 40, ipady = 20)
            file = open('text.txt', 'w+')
            file.write(input)
            file.close()
            SpeakText('file created')
            break


root = Tk()
root.title('Speech to TEXT')
root.geometry('600x400')
root.configure(background='#f2f2f2')
MyText = StringVar()
label = Label(root, text='Instructions :-', font=('Times New Roman', 12, 'bold'))
label.pack()
label = Label(root, text='Click Start to start the process', font=('Times New Roman', 16, 'bold'))
label.pack()
label1 = Label(root, text='Say Stop to stop giving input', font=('Times New Roman', 16, 'bold'))
label1.pack()
label2 = Label(root, text='Say Open to open the File explorer', font=('Times New Roman', 16, 'bold'))
label2.pack()
label3 = Label(root, text='Say Append in speech to append in existing file', font=('Times New Roman', 16, 'bold'))
label3.pack()
button = Button(root, text='Start', command=get_audio)
button.place(x = 200, y = 230, width = 50, height = 50)
button1 = Button(root, text='Exit', command=root.destroy)
button1.place(x = 300, y = 230, width = 50, height = 50)


root.mainloop()