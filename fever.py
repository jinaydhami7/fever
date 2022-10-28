# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 16:21:30 2022

@author: Nirav
"""

from tkinter import *
root = Tk()
root.title("Fever_Report")
root.geometry("600x600")





question1_radioButton=StringVar(value="0")
Question1=Label(root, text ="Do you have pain in your heart ?")
Question1.pack()
question1_r1=Radiobutton(root, text = "yes", variable=question1_radioButton, value="yes")
question1_r1.pack()
question1_r2=Radiobutton(root, text = "no", variable=question1_radioButton, value="no")
question1_r2.pack()

question2_radioButton=StringVar(value="0")
Question2=Label(root, text =" Can you  ?")
Question2.pack()
question2_r3=Radiobutton(root, text = "yes", variable=question2_radioButton, value="yes")
question2_r3.pack()
question2_r4=Radiobutton(root, text = "no", variable=question2_radioButton, value="no")
question2_r4.pack()

question3_radioButton=StringVar(value="0")
Question3=Label(root, text ="If you feel like doing nagin dance then you should definetly visit docter?")
Question3.pack()
question3_r3=Radiobutton(root, text = "yes", variable=question3_radioButton, value="yes")
question3_r3.pack()
question3_r4=Radiobutton(root, text = "no", variable=question3_radioButton, value="no")
question3_r4.pack()

def fever_score():
    score = 0
    if question1_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question2_radioButton.get()=="yes":
        score = score+20
        print(score)
    if question3_radioButton.get()=="yes":
        score = score+20
        print(score)
        
  
        
    if score <= 20:
        messagebox.showinfo("Report","You don't need to visit a doctor.")
    elif score > 20 and score <= 40: 
          messagebox.showinfo("Report","You might perhaps have to visit a doctor")
    else :
        messagebox.showinfo("Report","I strongly advise you to visit a doctor")
        
        
    root.mainloop()