from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import socket

hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="  ╱|、").grid(column=0, row=0)
ttk.Label(frm, text="(˚ˎ 。7").grid(column=0, row=1)
ttk.Label(frm, text="|、˜〵").grid(column=0, row=2)
ttk.Label(frm, text=" じしˍ,)ノ").grid(column=0, row=3)
ttk.Label(frm, text="Dɪsᴄʟᴀɪᴍᴇʀ: ᴡᴇ ᴅᴏɴ'ᴛ ʟᴏɢ ᴛʜɪs ɪɴғᴏ ᴛʜɪs ɪs ᴊᴜsᴛ ᴀ ᴘʀᴀɴᴋ").grid(column=0, row=5)
#Define a function for opening the Dialog box


def kill_prompt():
   messagebox.showinfo("Message", "How dare you")
   messagebox.showinfo("Message", "why would you ever do this")
   messagebox.showinfo("Message", "You know what will happen now")
   messagebox.showinfo("Message", "Do you know what youve gotten yourself into")
   messagebox.showinfo("Message", "I have the controls to your device")
   messagebox.showinfo("Message", "ᎩᎧᏬᏒ ᏖᏒᏗᎮᎮᏋᎴ ᏂᏋᏒᏋ ᏇᎥᏖᏂ ᎷᏋ ᏁᎧᏇ")
   messagebox.showinfo("Message", "H҉A҉ ҉H҉A҉ ҉H҉A҉ ҉H҉A҉ ҉H҉A҉ ҉H҉A҉")
   messagebox.showinfo("Message", "Your OS Name is:" + hostname)
   messagebox.showinfo("Message", "Your IP address:" + IPAddr)
   messagebox.showinfo("Message", "All your files will be gone now")
   messagebox.showinfo("Message", "So now")
   messagebox.showinfo("Message", "/ᐠ - ˕ -マ may he rest in peace")
   messagebox.showinfo("Message", "And you, you will die for this /ᐠﹷ ‸ ﹷ ᐟ\ﾉ")
   os.system('shutdown -s')
   
   
   
   
def leave_prompt():
    messagebox.showinfo("Message", "You truly disgust me")
    messagebox.showinfo("Message", "I don't get why you wouldnt help him")
    messagebox.showinfo("Message", "Just look at him")
    messagebox.showinfo("Message", "/ᐠ - ˕ -マ like seriosly")
    messagebox.showinfo("Message", "whatever man ig you do you")
    messagebox.showinfo("Message", "If you enjoyed join the discord : https://discord.gg/MGc5PAunEH")
    
    
def adopt_prompt():
    messagebox.showinfo("Message", "Yippe you took him in ฅᨐฅ₎")
    messagebox.showinfo("Message", "Please join my server or else")
    messagebox.showinfo("Message", "Thx for playing : https://discord.gg/MGc5PAunEH")
    root.destroy()
   

   

#Create a Button for opening a dialog Box
ttk.Button(frm, text= "Put him down", command= kill_prompt).grid(column=0, row=7)
ttk.Button(frm, text= "Leave", command= leave_prompt).grid(column=0, row=9)
ttk.Button(frm, text= "Adopt", command= adopt_prompt).grid(column=0, row=11)

def on_closing():
    if messagebox.askokcancel("Quit", "Why would you want to leave the kitten - ˕ •マ "):
        messagebox.showinfo("Quit", "You will pay the price for this")
        messagebox.showinfo("Quit", "₍^.  ̫.^₎ just look at him")
        messagebox.showinfo("Quit", "Your now my opp kid")
        messagebox.showinfo("Quit", "I will find you someday ₍^ >ヮ<^₎ .ᐟ.ᐟ")
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()