#https://github.com/sourcechord/FluentWPF/issues/42#issuecomment-873615119 idea
from tkinter import *
import ctypes
from BlurWindow.blurWindow import blur,Win7Blur,GlobalBlur
from ctypes import windll                                               #new import> windll
root = Tk()
root.config(bg='#202020')                                               #green won't make it blur, I tried a different color, and it seems to work fine.

#root.wm_attributes("-transparent", 'green')                            # This is causing the bugs with this kind of weak approach but then it works
root.geometry('500x400')
root.update()

mainWindow=root                                                         #defining the main window
HWND =    windll.user32.GetParent(mainWindow.winfo_id())                #ctypes.windll.user32.GetForegroundWindow() # this line causes the issue, I've replaced it
dark_mode='#11111199'
light_mode='#30121244'
super_dark_mode='#111111FF'




theme=light_mode

GlobalBlur(HWND,hexColor=theme,Acrylic=True) #Enable Acrylic

global ACRYLIC_ENABLED
ACRYLIC_ENABLED = True

global DRAG
DRAG = False

def dragging(event):
    global DRAG
    if event.widget is root: #if is event Configure of root (Drag,Resize)
        if DRAG == False:#If Drag is disabled (set by stop_drag)
            GlobalBlur(HWND,hexColor=theme,Acrylic=False)
        else:
            root.after_cancel(DRAG) #cancel task \/ (is dragging)
        DRAG = root.after(200, stop_drag) #execute stop_drag after 200ms

def stop_drag():
    global DRAG
    DRAG = False
    GlobalBlur(HWND,hexColor=theme,Acrylic=True) 

root.bind('<Configure>', dragging)

root.mainloop()
