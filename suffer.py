#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 14:58:44 2017

@author: Nick
"""

#!/usr/bin/python

import Tkinter as tk
import tkMessageBox
import datetime
import math
#datetime.datetime.now()
#import os

#os.system('''/usr/bin/osascript -e 
#'tell app "Finder" to set frontmost of process "Python" to true' ''')

"""
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Left to survive', 'Survived'
sizes = [9, 91]
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode = explode, labels = labels, autopct='%1.1f%%',
        shadow = True, startangle = 90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()
"""
    
class Work(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        # create a prompt, an input box, an output label,
        # and a button to do the computation
        self.prompt1 = tk.Label(self, text = "Suffer begins at:", anchor = "w")
        self.entry1 = tk.Entry(self)
        self.entry1.insert(1, "08:00:00")
        self.prompt2 = tk.Label(self, text = "Suffer ends at:", anchor = "w")
        self.entry2 = tk.Entry(self)
        self.entry2.insert(1, "16:45:00")
        self.prompt3 = tk.Label(self, text = "Lunch begins at:", anchor = "w")
        self.entry3 = tk.Entry(self)
        self.entry3.insert(1, "12:45:00")
        self.prompt4 = tk.Label(self, text = "Lunch ends at:", anchor = "w")
        self.entry4 = tk.Entry(self)
        self.entry4.insert(1, "13:30:00")

        self.submit = tk.Button(self, text = "Enter", command = self.calculate)
        self.output = tk.Label(self, text = "")
        
        # create pie chart canvas
        side = 600
        self.canvas = tk.Canvas(self, bg = "white", height = side, width = side)
        
        # lay the widgets out on the screen. 
        self.prompt1.pack(side="top", fill="x")
        self.entry1.pack(side="top", fill="x", padx=20)
        self.prompt2.pack(side="top", fill="x")
        self.entry2.pack(side="top", fill="x", padx=20)
        self.prompt3.pack(side="top", fill="x")
        self.entry3.pack(side="top", fill="x", padx=20)
        self.prompt4.pack(side="top", fill="x")
        self.entry4.pack(side="top", fill="x", padx=20)


        self.output.pack(side="top", fill="x", expand=True)
        
        self.submit.pack(side="top")
        self.canvas.pack(side="top", fill="x")
        
        #self.attributes("-topmost", True)
    def update_clock(self):
        self.after(1000, self.update_clock)
                
    def calculate(self):
        # get the value from the input widget, convert
        # it to an int, and do a calculation
        try:            
            self.canvas.delete("all")
            start = str(self.entry1.get())
            end = str(self.entry2.get())
            startL = str(self.entry3.get())
            endL = str(self.entry4.get())

            now = datetime.datetime.now()
            tm = str(datetime.time(now.hour, now.minute, now.second))
            
            # Pie chart, where the slices will be ordered and plotted counter-clockwise:
                
            start = int(start.split(":")[0])*3600 + int(start.split(":")[1])*60 + int(start.split(":")[2])
            end = int(end.split(":")[0])*3600 + int(end.split(":")[1])*60 + int(end.split(":")[2])
            
            startL = int(startL.split(":")[0])*3600 + int(startL.split(":")[1])*60 + int(startL.split(":")[2])
            endL = int(endL.split(":")[0])*3600 + int(endL.split(":")[1])*60 + int(endL.split(":")[2])

            
            tm = int(tm.split(":")[0])*3600 + int(tm.split(":")[1])*60 + int(tm.split(":")[2])
            
            def frac(n): 
                return 360. * n / (end - start)
            
            if (end - tm > 0):
                
                self.canvas.create_arc((155,155,445,445), fill="#875928", start=frac(0), extent = frac(end - tm))
                self.canvas.create_arc((155,155,445,445), fill="green", start=frac(end - tm), extent = frac(tm - start))
                self.canvas.create_arc((155,155,445,445), start=frac(end - endL), extent = frac(endL - startL))

                deltax = 200*math.cos(math.pi*(tm - start)/(end - start))
                deltay = 200*math.sin(math.pi*(tm - start)/(end - start))
                x = 300 + deltax
                y = 300 + deltay
                xrev = 300 - deltax
                yrev = 300 - deltay
                
                survivedSeconds = tm - start
                survivedM, survivedS = divmod(survivedSeconds, 60)
                survivedH, survivedM = divmod(survivedM, 60)
                survivedTotal = "%d:%02d:%02d" % (survivedH, survivedM, survivedS)
                
                leftSeconds = end - tm
                leftM, leftS = divmod(leftSeconds, 60)
                leftH, leftM = divmod(leftM, 60)
                leftTotal = "%d:%02d:%02d" % (leftH, leftM, leftS)
                
                survivedPersent = 100 * survivedSeconds/(end - start)
                leftPersent = 100 - survivedPersent
                
                self.canvas.create_text((x,y), text = "Survived \n"+str(survivedTotal)+"\n"+str(survivedPersent)+"%")
                self.canvas.create_text((xrev,yrev), text = "Left to survive \n"+str(leftTotal)+"\n"+str(leftPersent)+"%")
                
                tillLunchSeconds = startL - tm
                tillLunchM, tillLunchS = divmod(tillLunchSeconds, 60)
                tillLunchH, tillLunchM = divmod(tillLunchM, 60)
                tillLunchTotal = "%d:%02d:%02d" % (tillLunchH, tillLunchM, tillLunchS)
                
                #self.canvas.pack()
                if (tillLunchSeconds > 0):
                    result = "Time till lunch: " + str(tillLunchTotal)
                else:
                    result = "Time till lunch: tomorrow"
                
            else:
                self.canvas.create_oval((155,155,445,445), fill="green")
                result = "You fucking did it!"
                self.canvas.create_text((300,50), text = "Survived \n"+"100%")

        except ValueError:
            result = "Please enter time only"
                
        self.output.configure(text = result)
        self.update_clock
        self.mainloop()
        
        

# if this is run as a program (versus being imported),
# create a root window and an instance of our example,
# then start the event loop

def callback():
    if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("WorkFree")
    
    root.protocol("WM_DELETE_WINDOW", callback)
    
    Work(root).pack(fill="both", expand=True)
    root.lift()
    root.attributes('-topmost',True)
    root.after_idle(root.attributes,'-topmost',False)
    root.resizable(False, False)
                
    root.mainloop()
    
    