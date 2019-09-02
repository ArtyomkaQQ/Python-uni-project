from tkinter import *
from pygame import mixer

def left_click(event):
    global bg, nupp2, tulede_i
    global magnet_oli_kasutusel, flashlight_oli_kasutusel, battery_oli_kasutusel, key_oli_kasutusel
    global kapp_avatud, kast_avatud, lukk_avatud, uks_avatud
    global magnet, flashlight, battery, flashwithlight, key
    #TUBA
    if event.x >= 346 and event.x <= 372 and event.y >= 110 and event.y <= 130 and tulede_i % 2 != 0 and magnet_oli_kasutusel == False and kapp_avatud == False and kast_avatud == False and lukk_avatud == False and uks_avatud == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/room.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        tulede_i += 1
        raam.mainloop()
    if event.x >= 346 and event.x <= 372 and event.y >= 110 and event.y <= 130 and tulede_i % 2 == 0 and magnet_oli_kasutusel == False and kapp_avatud == False and kast_avatud == False and lukk_avatud == False and uks_avatud == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no light.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        tulede_i += 1
        raam.mainloop()
    if event.x >= 346 and event.x <= 372 and event.y >= 110 and event.y <= 130 and tulede_i % 2 != 0 and magnet_oli_kasutusel == True and kapp_avatud == False and kast_avatud == False and lukk_avatud == False and uks_avatud == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no magnet.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        tulede_i += 1
        raam.mainloop()
    if event.x >= 346 and event.x <= 372 and event.y >= 110 and event.y <= 130 and tulede_i % 2 == 0 and magnet_oli_kasutusel == True and kapp_avatud == False and kast_avatud == False and lukk_avatud == False and uks_avatud == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no light no magnet.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        tulede_i += 1
        raam.mainloop()
    if event.x >= 274 and event.x <= 288 and event.y >= 312 and event.y <= 328 and tulede_i % 2 == 0 and magnet_oli_kasutusel == False and kapp_avatud == False and kast_avatud == False and lukk_avatud == False and uks_avatud == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no magnet.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        image_magnet = PhotoImage(file = "Pictures/magnet.png")
        magnet = Button(raam, image = image_magnet)
        magnet.pack(side = BOTTOM)
        magnet_oli_kasutusel = True
        raam.mainloop()
    if event.x >= 274 and event.x <= 288 and event.y >= 312 and event.y <= 328 and tulede_i % 2 != 0 and magnet_oli_kasutusel == False and kapp_avatud == False and kast_avatud == False and lukk_avatud == False and uks_avatud == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no light no magnet.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        image_magnet = PhotoImage(file = "Pictures/magnet.png")
        magnet = Button(raam, image = image_magnet)
        magnet.pack(side = BOTTOM)
        magnet_oli_kasutusel = True
        raam.mainloop()
    #KAPP
    if event.x >= 682 and event.x <= 720 and event.y >= 310 and event.y <= 356 and tulede_i % 2 == 0 and magnet_oli_kasutusel == False and flashlight_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/kapp.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kapp_avatud = True
        raam.mainloop()
    if event.x >= 682 and event.x <= 720 and event.y >= 310 and event.y <= 356 and tulede_i % 2 != 0 and magnet_oli_kasutusel == False and flashlight_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/kapp no light.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kapp_avatud = True
        raam.mainloop()
    if event.x >= 682 and event.x <= 720 and event.y >= 310 and event.y <= 356 and tulede_i % 2 == 0 and magnet_oli_kasutusel == True and flashlight_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/kapp.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kapp_avatud = True
        raam.mainloop()
    if event.x >= 682 and event.x <= 720 and event.y >= 310 and event.y <= 356 and tulede_i % 2 != 0 and magnet_oli_kasutusel == True and flashlight_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/kapp no light.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kapp_avatud = True
        raam.mainloop()
    if event.x >= 682 and event.x <= 720 and event.y >= 310 and event.y <= 356 and tulede_i % 2 == 0 and magnet_oli_kasutusel == False and flashlight_oli_kasutusel == True:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no flashlight.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kapp_avatud = True
        raam.mainloop()
    if event.x >= 682 and event.x <= 720 and event.y >= 310 and event.y <= 356 and tulede_i % 2 != 0 and magnet_oli_kasutusel == False and flashlight_oli_kasutusel == True:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no light no flashlight.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kapp_avatud = True
        raam.mainloop()
    if event.x >= 682 and event.x <= 720 and event.y >= 310 and event.y <= 356 and tulede_i % 2 == 0 and magnet_oli_kasutusel == True and flashlight_oli_kasutusel == True:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no flashlight.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kapp_avatud = True
        raam.mainloop()
    if event.x >= 682 and event.x <= 720 and event.y >= 310 and event.y <= 356 and tulede_i % 2 != 0 and magnet_oli_kasutusel == True and flashlight_oli_kasutusel == True:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no light no flashlight.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kapp_avatud = True
        raam.mainloop()
    if event.x >= 300 and event.x <= 398 and event.y >= 280 and event.y <= 300 and tulede_i % 2 == 0 and kapp_avatud == True and flashlight_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no flashlight.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        image_flashlight = PhotoImage(file = "Pictures/flashlight.png")
        flashlight = Button(raam, image = image_flashlight, command = check)
        flashlight.pack(side = BOTTOM)
        flashlight_oli_kasutusel = True
        raam.mainloop()
    if event.x >= 300 and event.x <= 398 and event.y >= 280 and event.y <= 300 and tulede_i % 2 != 0 and kapp_avatud == True and flashlight_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no flashlight.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        image_flashlight = PhotoImage(file = "Pictures/flashlight.png")
        flashlight = Button(raam, image = image_flashlight, command = check)
        flashlight.pack(side = BOTTOM)
        flashlight_oli_kasutusel = True
        raam.mainloop()
    #KAST
    if event.x >= 542 and event.x <= 618 and event.y >= 214 and event.y <= 298 and tulede_i % 2 == 0 and battery_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/box.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kast_avatud = True
        raam.mainloop()
    if event.x >= 542 and event.x <= 618 and event.y >= 214 and event.y <= 298 and tulede_i % 2 != 0 and battery_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/box no light.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kast_avatud = True
        raam.mainloop()
    if event.x >= 542 and event.x <= 618 and event.y >= 214 and event.y <= 298 and tulede_i % 2 == 0 and battery_oli_kasutusel == True:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no battery.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kast_avatud = True
        raam.mainloop()
    if event.x >= 542 and event.x <= 618 and event.y >= 214 and event.y <= 298 and tulede_i % 2 != 0 and battery_oli_kasutusel == True:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no light no battery.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        kast_avatud = True
        raam.mainloop()
    if event.x >= 222 and event.x <= 294 and event.y >= 284 and event.y <= 354 and tulede_i % 2 == 0 and kast_avatud == True and battery_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no battery.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        image_battery = PhotoImage(file = "Pictures/battery.png")
        battery = Button(raam, image = image_battery, command = check)
        battery.pack(side = BOTTOM)
        battery_oli_kasutusel = True
        kast_avatud = True
        raam.mainloop()
    if event.x >= 222 and event.x <= 294 and event.y >= 284 and event.y <= 354 and tulede_i % 2 != 0 and kast_avatud == True and battery_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no light no battery.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        image_battery = PhotoImage(file = "Pictures/battery.png")
        battery = Button(raam, image = image_battery, command = check)
        battery.pack(side = BOTTOM)
        battery_oli_kasutusel = True
        kast_avatud = True
        raam.mainloop()
    #LUKK
    if event.x >= 414 and event.x <= 472 and event.y >= 516 and event.y <= 530 and kapp_avatud == False and kast_avatud == False and flashlight_ready == False and key_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/no light lukk.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        lukk_avatud = True
        raam.mainloop()
    if event.x >= 414 and event.x <= 472 and event.y >= 516 and event.y <= 530 and kapp_avatud == False and kast_avatud == False and flashlight_ready == True and key_oli_kasutusel == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/lukk.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        lukk_avatud = True
        raam.mainloop()
    if event.x >= 214 and event.x <= 284 and event.y >= 458 and event.y <= 482 and kapp_avatud == False and kast_avatud == False and lukk_avatud == True  and flashlight_ready == True and magnet_oli_kasutusel == True and key_oli_kasutusel == False:
        bg.destroy()
        magnet.destroy()
        image_introduction = PhotoImage(file = "Pictures/lukk no key.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        image_key = PhotoImage(file = "Pictures/key.png")
        key = Button(raam, image = image_key, command = check)
        key.pack(side = BOTTOM)
        key_oli_kasutusel = True
        raam.mainloop()
    if event.x >= 414 and event.x <= 472 and event.y >= 516 and event.y <= 530 and kapp_avatud == False and kast_avatud == False and key_oli_kasutusel == True:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/lukk no key.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        lukk_avatud = True
        raam.mainloop()
    #UKS
    if event.x >= 408 and event.x <= 438 and event.y >= 264 and event.y <= 274 and kapp_avatud == False and kast_avatud == False and lukk_avatud == False:
        bg.destroy()
        image_introduction = PhotoImage(file = "Pictures/uks.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        back = PhotoImage(file = "Pictures/back.png")
        nupp2 = Button(raam, image = back, command = tagasi)
        nupp2.place(x = 675, y = 400, width = 100)
        uks_avatud = True
        raam.mainloop()
    if event.x >= 104 and event.x <= 270 and event.y >= 250 and event.y <= 316 and uks_avatud == True and key_oli_kasutusel == True:
        bg.destroy()
        key.destroy()
        flashwithlight.destroy()
        image_done = PhotoImage(file = "Pictures/escaped.png")
        bg = Label(raam, image = image_done)
        bg.pack()
        raam.mainloop()

def tagasi():
    global bg
    global kapp_avatud
    global kast_avatud
    global lukk_avatud
    global uks_avatud
    bg.destroy()
    nupp2.destroy()  
    lukk_avatud = False
    uks_avatud = False
    
    if tulede_i % 2 == 0 and magnet_oli_kasutusel == False:
        image_introduction = PhotoImage(file = "Pictures/room.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        kapp_avatud = False
        kast_avatud = False
        raam.mainloop()
    if tulede_i % 2 != 0 and magnet_oli_kasutusel == False:
        image_introduction = PhotoImage(file = "Pictures/no light.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        kapp_avatud = False
        kast_avatud = False
        raam.mainloop()
    if tulede_i % 2 == 0 and magnet_oli_kasutusel == True:
        image_introduction = PhotoImage(file = "Pictures/no magnet.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        kapp_avatud = False
        kast_avatud = False
        raam.mainloop()
    if tulede_i % 2 != 0 and magnet_oli_kasutusel == True:
        image_introduction = PhotoImage(file = "Pictures/no light no magnet.png")
        bg = Label(raam, image = image_introduction)
        bg.pack()
        kapp_avatud = False
        kast_avatud = False
        nupp2.destroy()
        flashwithlight.destroy()
        key.destroy()
        raam.mainloop()
        
def mängu_alustamine():
    global bg
    bg.destroy()
    nupp1.destroy()
    mixer.init()
    mixer.music.load("Tomb Raider.mp3")
    mixer.music.play()
    image_introduction = PhotoImage(file = "Pictures/room.png")
    bg = Label(raam, image = image_introduction)
    bg.pack()
    raam.bind("<Button-1>", left_click)
    raam.mainloop()
    
def check():
    global flashlight
    global battery
    global flashlight_ready
    global flashwithlight
    
    if flashlight_oli_kasutusel == True and battery_oli_kasutusel == True:
        flashlight.destroy()
        battery.destroy()
        image_flashwithlight = PhotoImage(file = "Pictures/flashwithlight.png")
        flashwithlight = Button(raam, image = image_flashwithlight)
        flashwithlight.pack(side = BOTTOM)
        flashlight_ready = True
        raam.mainloop()
        
raam = Tk()
raam.title("Escape")
raam.geometry("800x660")
raam.wm_iconbitmap("pictures/icon.ico")
raam.resizable(0,0)

image_introduction = PhotoImage(file = "Pictures/escape.png")
bg = Label(raam, image = image_introduction)
bg.pack()

nupp1 = Button(raam, text = "Alusta", command = mängu_alustamine)
nupp1.place(x = 325, y = 360, width = 150)

tulede_i = 0
magnet_oli_kasutusel = False
flashlight_oli_kasutusel = False
battery_oli_kasutusel = False
key_oli_kasutusel = False
kapp_avatud = False
kast_avatud = False
lukk_avatud = False
uks_avatud = False
flashlight_ready = False

raam.mainloop()