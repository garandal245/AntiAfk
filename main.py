import pyautogui
import random
import time
import keyboard


current_cords = pyautogui.position()
afktimer = 0

#user inputed variables defaults
user_time = 600
user_Zone_X_Min = 0
user_Zone_X_Max = 100
user_Zone_Y_Min = 0
user_Zone_Y_Max = 100

user_Zone_X_Min = int(input("enter min x value you would like it to right click in: "))
user_Zone_X_Max = int(input("enter max x value you would like it to right click in: "))
user_Zone_Y_Max = int(input("enter min y value you would like it to right click in: "))
user_Zone_Y_Max = int(input("enter max y value you would like it to right click in: "))
user_time = int(input("enter time in seconds you would like it to wait to activate: "))


#appends key to keypressed array if key is pressed
def on_press_callback(e):
    keypressed.append(e.name)

while True:
    keypressed = []
    keyboard.on_press(on_press_callback)



    while True:
        time.sleep(1)

    #checks if keyboard has pressed any keys as recorded by keyboard.onrelease
        if (len(keypressed) == 0):
            afktimer += .5 
            print(afktimer)
            keyboard.unhook_all()
            pass
        else:
            afktimer = 0
            print(afktimer)
            break #breaks to re run on press and reset keypressed
    
    
    #checks if mouse is in same position as last recorded by pyautogui

        if current_cords == pyautogui.position() :
            afktimer += .5 
            print(afktimer)
            keyboard.unhook_all()
            break
        else:
            afktimer = 0
            current_cords = pyautogui.position()            
            print(afktimer)
            break #breaks to re run on press and reset keypressed


    

        

    #checks if time afk is the defined time and preforms random rightclick in zone 
    if afktimer >= user_time:
        x = random.randint(user_Zone_X_Min, user_Zone_X_Max)
        y = random.randint(user_Zone_Y_Min, user_Zone_Y_Max)
        print("afk doing movement")
        pyautogui.moveTo(x, y, 0.5)
        pyautogui.click(button='right')
        afktimer = 0
        
    

