import tkinter as tk
from tkinter import ttk
import sys, os
import libuvk5


if len(sys.argv)!=3: print(f'Usage: {os.path.basename(sys.argv[0])} <COMx> <pooling>') ; exit(1)


class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Quansheng UV-K5 RSSI Window')
        self.root.geometry('420x240')

        s = ttk.Style()
        s.configure('My.TFrame', background='black')

        self.mainWindow = ttk.Frame(self.root, width=420, height=240, style='My.TFrame')
        self.mainWindow.grid(column=0, row=0, sticky = "nsew")  # to fill whole window

        #RSSI
        self.Label1 = ttk.Label(self.mainWindow, text="RSSI (Register 0x67) = ", font=('Consolas',10), justify=tk.LEFT, foreground='#FFF', background='#000')
        self.Label1.place(x=10, y=10)
        self.ProgressBar1 = ttk.Progressbar(self.mainWindow, orient='horizontal', mode='determinate', maximum=0x1FF/2)
        self.ProgressBar1.place(x=10, y=30, width=400, height=20)
        self.ProgressBar1['value'] = 0


        #NOISE
        self.Label2 = ttk.Label(self.mainWindow, text="Ex-noiseindicator, dB/step. (Register 0x65) = ", font=('Consolas',10), justify=tk.LEFT, foreground='#FFF', background='#000')
        self.Label2.place(x=10, y=60)
        self.ProgressBar2 = ttk.Progressbar(self.mainWindow, orient='horizontal', mode='determinate', maximum=0x7F)
        self.ProgressBar2.place(x=10, y=80, width=400, height=20)
        self.ProgressBar2['value'] = 0


        #GLITCH
        self.Label3 = ttk.Label(self.mainWindow, text="Glitch indicator (Register 0x63) = ", font=('Consolas',10), justify=tk.LEFT, foreground='#FFF', background='#000')
        self.Label3.place(x=10, y=110)
        self.ProgressBar3 = ttk.Progressbar(self.mainWindow, orient='horizontal', mode='determinate', maximum=0xFF)
        self.ProgressBar3.place(x=10, y=130, width=400, height=20)
        self.ProgressBar3['value'] = 0


        #RAW BYTES
        self.Label4 = ttk.Label(self.mainWindow, text="RAW = ", font=('Consolas',10), justify=tk.LEFT, foreground='#FFF', background='#000')
        self.Label4.place(x=10, y=160)
        
        #Refresh info
        self.Label5 = ttk.Label(self.mainWindow, text="Refresh rate = ", font=('Consolas',10), justify=tk.LEFT, foreground='#FFF', background='#000')
        self.Label5.place(x=10, y=180)


        #---- CONNECT WITH RADIO -----
        self.radio = libuvk5.uvk5(sys.argv[1])
        self.radio.debug=False
        if self.radio.connect():
            self.root.title('Quansheng UV-K5 RSSI Window - '+sys.argv[1])
            self.refresh_rate = int(sys.argv[2]) #ms

        self.update()
        self.root.mainloop()

    def update(self):
        data = self.radio.get_rssi()
        #print(data)
        self.Label1.config(text="RSSI (Register 0x67) = {} dBm".format(data['rssi']))
        self.ProgressBar1['value'] = data['rssi']+160
        
        self.Label2.config(text="Ex-noiseindicator, dB/step. (Register 0x65) = {}".format(data['noise']))
        self.ProgressBar2['value'] = data['noise']
                
        self.Label3.config(text="Glitch indicator (Register 0x63) = {}".format(data['glitch']))
        self.ProgressBar3['value'] = data['glitch']
        
        self.Label4.config(text="RAW = {}".format(data['raw']))
        self.Label5.config(text="Refresh rate = {} ms".format(self.refresh_rate))
        
        
        self.root.after(self.refresh_rate, self.update)

app=App()

