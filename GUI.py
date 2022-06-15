from asyncio.windows_events import NULL
from time import strftime
from email.mime import image
from operator import index
from pathlib import Path
from tkinter import *
from tkinter import ttk
from datetime import date
from datetime import datetime
from time import strftime
import os
from turtle import hideturtle
from PIL import ImageTk, Image
from tkinter import messagebox
import black

splashscreen=Tk()
splashscreen.geometry("840x630")
splashscreen.wm_title("RECORDFY")
photo = PhotoImage(file ="database.png")
splashscreen.iconphoto(False,photo)

img = ImageTk.PhotoImage(Image.open("Project 1.jpg"))
label = Label(splashscreen, image = img)
label.place(x=0,y=0,height=630,width=840)
def main():
    splashscreen.destroy()
    window=Tk()
    window.geometry("700x550")
    window.wm_title("DASHBOARD")
    photo = PhotoImage(file ="database.png")
    window.iconphoto(False,photo)
    window.resizable(False,False)
    smark=StringVar()
    sname=StringVar()
    susn=StringVar()
    slab=StringVar()
    sname.set("NAME")
    slab.set("LAB NAME")
    smark.set("MARK")
    susn.set("USN")
    ssusn=StringVar()
    ssusn.set("USN")
    upmark=StringVar()

    # ----------Methods--------->
    def insertData():
        name=sname.get().upper()
        mark=smark.get().upper()
        lab=slab.get().upper()
        usn=susn.get().upper()
        if name=="":
            messagebox.showwarning("showwarning", "Field Is Empty")
        elif mark=="":
            messagebox.showwarning("showwarning", "Field Is Empty")
        elif lab=="":
            messagebox.showwarning("showwarning", "Field Is Empty")
        elif usn=="":
            messagebox.showwarning("showwarning", "Field Is Empty")
        else:
            print("Details Entered:"+name+"|"+usn+"|"+lab+"|"+mark)
            filereader=open("studentRecord.txt","a")
            filereader.write("\n"+usn+"|"+name+"|"+lab+"|"+mark+"\n")
            messagebox.showinfo("STATUS", "RECORD ADDED TO DATABASE")

        
    def searchdata():
        usn=ssusn.get().upper()
        print(usn)
        for record in treev.get_children():
                treev.delete(record)
        sfilereader=open("studentRecord.txt","r")
        lines=sfilereader.readlines()
        print(lines)
        match=[]
        for line in lines:
            print(line)
            if line.startswith(usn):
                print(line)
                nnl=line.split("|")
                match.append(nnl)
                print(nnl)
                print(match)
        for i in range(0,len(match)):
            if match[i][0]==usn:
                treev.insert("", 'end', text ="L"+str(i),values =(match[i][0],match[i][1],match[i][2],match[i][3])) 
        sfilereader.close()

    def removeData():
        record=treev.focus()
        temp=treev.item(record,'values')
        temp_list=list(temp)
        fileReader=open("studentRecord.txt","r")
        messagebox.askokcancel("askokcancel", "Want to continue?")
        lines=fileReader.readlines()
        for line in lines:
            del_list=line.split("|")
            if del_list==temp_list:
                print(del_list)
                del lines[lines.index(line)]
                break
        fileReader2=open("studentRecord.txt","w+")
        for i in lines:
            fileReader2.write(i)
        selected_item=treev.selection()[0]
        treev.delete(selected_item)
    def clicked_up(e):
        set_value()
    def set_value():
            
            record=treev.focus()
            temp=treev.item(record,'values')
            temp_list=list(temp)
            
            upmark.set(temp_list[3])
        
            return temp_list
    def updateData():

    

        mark=upmark.get()
        print(mark)
        temp_list=set_value()
        print(temp_list[0])
        filereader=open("studentRecord.txt","r")
        lines=filereader.readlines()
        
        for line in lines:
            if line.startswith(temp_list[0]):
                nlu=line.split("|")
                index=lines.index(line)
                print(nlu)
        up=[]
        up.append(nlu[0])
        up.append(nlu[1])
        up.append(nlu[2])
        up.append(mark+'\n')
        update_file="|".join(up)
        lines[index]=update_file
        filereader2=open("studentRecord.txt","w+")
        for i in lines:
            filereader2.write(i)
        messagebox.showinfo("STATUS", "MARK IS UPDATED")
        upmark.set("")
        filereader.close()
        filereader2.close()


    upmark.set("UPDATE MARK")
    mark = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=smark,
        border=0,
        borderwidth=1
        
    )
    mark.place(
        x=20,
        y=20,
        height=50,
        width=50.00
    )
    studentname= Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=sname,
        border=0,
        borderwidth=1
        
    )
    studentname.place(
        x=120.0,
        y=20.0,
    height=50,
        width=120.00
    )
    studentusn = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=susn,
        border=0,
        borderwidth=1
        
    )
    studentusn.place(
    x=270.0,
        y=20.0,
    height=50,
        width=120.00
    )
    lab = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=slab,
        border=0,
        borderwidth=1
        
    )
    lab.place(
        x=450.0,
        y=20.0,
    height=50,
        width=120.00
    )
    searchusn = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=ssusn,
        border=0,
        borderwidth=1
        
    )
    searchusn.place(
        x=20.0,
        y=120.0,
    height=50,
        width=120.00
    )
    addbtn= Button ( 
        bg="blue",
        text="ADD",
    
        highlightthickness=0,
        command=insertData,
        relief="flat",
        fg="white"
    )
    addbtn.place(
        x=600.0,
        y=20.0,
        width=100.0,
        height=50.0
    )


    treev = ttk.Treeview(window, selectmode ='browse')
    treev.place(x=20,y=220)
        

                        
    treev["columns"] = ("1", "2", "3","4")
    treev['show'] = 'headings'
    treev.column("1", width = 100, anchor ='c')
    treev.column("2", width = 100, anchor ='se')
    treev.column("3", width = 100, anchor ='se')
    treev.column("4", width = 100, anchor ='se')

    treev.bind('<ButtonRelease-1>',clicked_up)                    
    treev.heading("1", text ="USN")
    treev.heading("2", text ="NAME")
    treev.heading("3", text ="Lab")
    treev.heading("4", text ="MARK")

    searchbtn= Button ( 
        bg="blue",
        text="SEARCH DATA",
    
        highlightthickness=0,
        command=searchdata,
        relief="flat",
        fg="white"
    )
    searchbtn.place(
        x=150.0,
        y=120.0,
        width=100.0,
        height=50.0
    )
    removebtn= Button ( 
        bg="blue",
        text="REMOVE DATA",
        highlightthickness=0,
        command=removeData,
        relief="flat",
        fg="white"
    )
    removebtn.place(
        x=270.0,
        y=120.0,
        width=100.0,
        height=50.0
    )
    updatemark = Entry(
        bd=0,
        bg="#C4C4C4",
        highlightthickness=0,
        textvariable=upmark,
        border=0,
        borderwidth=1
        
    )
    updatemark.place(
    x=20.0,
        y=470.0,
    height=50,
        width=120.00
    )
    updatebtn= Button ( 
        bg="blue",
        text="UPDATE DATA",
        highlightthickness=0,
        command=updateData,
        relief="flat",
        fg="white"
    )
    updatebtn.place(
        x=180.0,
        y=470.0,
        width=100.0,
        height=50.0
    )






















    window.mainloop()
splashscreen.after(3000,main)
splashscreen.mainloop()