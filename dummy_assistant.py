import wolframalpha
import wikipedia
from tkinter import *
#import tkinter_messagebox
import speech_recognition as sr

while True:
    r=sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration = 1)
        r.energy_threshold=140
        r.pause_threshold=0.5
        print("speak  now...")
        audio=r.listen(source)
        try:
            text=r.recognize_google(audio)
            print(text)
            if text=='stop':
                break
            else:
                window =Tk()
                #window.geometry("700x600")
                try:
                    app_id="HQVT8K-XXYAW3HETJ"
                    client=wolframalpha.Client(app_id)
                    res = client.query(text)
                    answer= next(res.results).text
                    T=Text(window,bg='pink')
                    T.pack(expand=True)
                    T.insert(END,answer)
                    window.after(8000,lambda:window.destroy())
                    window.mainloop()
                except:
                    answer=wikipedia.summary(text)
                    T=Text(window,bg='pink')
                    T.pack(expand=True)
                    T.insert(END,answer)
                    window.after(20000,lambda:window.destroy())
                    window.mainloop()
                
        except:
            answer="oops!Didn't get you.Try again"
            print(answer)
            """
 try:
                    app_id="HQVT8K-XXYAW3HETJ"
                    client=wolframalpha.Client(app_id)
                    answer= next(res.results).text
                    label1= label(window,justify='LEFT',compound='CENTER',padx=10,text=answer,font='times 15 bold')
                    label1.pack()
                    window.after(5000,lambda:window.destroy())
                    window.mainloop()
                except:
                    """