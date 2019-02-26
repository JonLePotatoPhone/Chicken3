import tkinter as tk

def getResY(scrY,scrAsp,percentTakenUp):
    if (scrAsp > 1.68 and scrAsp < 1.8): #Looking for 1.77
        return int( 9 * (percentTakenUp*(scrY/ 9)))
    elif (scrAsp > 1.58 and scrAsp < 1.70): #Looking for 1.6
        return int(10 * (percentTakenUp*(scrY/10)))
    else: #Resolution for peasents or people with weird tastes
        return 480
    
def newFrame(cRoot,background):
    retFrame = tk.Frame(cRoot,bg=background)
    retFrame.grid(row=0,column=0, sticky="nsew")
    retFrame.grid_rowconfigure(0, weight = 1)
    retFrame.grid_columnconfigure(0, weight = 1)
    retFrame.grid()
    retFrame.tkraise()
    return retFrame

def getResX(scrX,scrAsp,percentTakenUp):
    if (scrAsp > 1.68 and scrAsp < 1.8): #Looking for 1.77
        return int(16 * (percentTakenUp*(scrX/16)))
    elif (scrAsp > 1.58 and scrAsp < 1.70): #Looking for 1.6
        return int(16 * (percentTakenUp*(scrX/16)))
    else: #Resolution for peasents or people with weird tastes
        return 640