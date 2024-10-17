#!/usr/bin/env python3
"""
Author - Abhishek Singh Chauhan 
Date -  8 June 2024
Purpose - having problem in eyes so made this kind of reminder to keep myself healthy..


------------------------------------------------------------------------------------------------------






--------------------------------------------------------------------------------------------------------------o
chanellogs.. 

** [ 2 oct 2024 ]:
      -  v.2 - *** added  music pausing and playing feature... on 
** [ ]:
        



"""

import playsound
from datetime import datetime
import time
import sys
import termios
import subprocess
from os import system

def timestamp():

    """ it give the timestamp """
    return datetime.now()

def watertime():

    start = time.time() # time counter for watertime action ...
    
    print("Yeah ! it's Water Time ...")
    try:
        stopplayingMedia()
        notify("Time take some Water buddy !")
        playsound.playsound("./healthyprogrammer/water_time.mp3")
    except Exception as e:
        print(f"Error Playing media file ..{e}")
    flush_input()
    message = input("Enter status :")
    with open ("./healthyprogrammer/Water_drank_log.txt","a") as f:
        f.write(f"{str(timestamp())} -: {message}\n")
        print("Entrey added Successfully!")
    return time.time()-start

def eyetime():

    start = time.time() # time counter for eyetime action to take...
    print("It's time to exercise your Eye ...!!!")

    try:
        stopplayingMedia()
        notify("Time to Move your Eye Out of the \n\tSCREEN ! ")
        playsound.playsound("./healthyprogrammer/take_a_look_in_eyes.mp3")
    except Exception as e:
        print(f"Error Playing media file ..{e}")
    flush_input()

    message = input("Enter status :")
    with open("./healthyprogrammer/eyetime_log.txt","a") as f:
        f.write(f"{str(timestamp())} -:{message}\n")
        print("Entrey added Successfully!")

    return time.time()-start

def physical_activity():

    start = time.time() # time counter for physical activity to take place..

    print("Time for Physical activity....")

    try:
        stopplayingMedia()
        notify("Time for some Physical Exercise man!")
        playsound.playsound("./healthyprogrammer/time_to_exercise.mp3")
    except Exception as e:
        print(f"Error Playing media file ..{e}")
    flush_input()
    message = input("Enter status :")
    with open("./healthyprogrammer/physical_data.txt","a") as f:
        f.write(f"{str(timestamp())} -:{message}\n")
        print("Entrey added Successfully!")
        
    return time.time()-start

def notify(message, title="Notification"):
    """
    Display a notification on the system screen.

    Parameters:
    message (str): The message to display in the notification.
    title (str): The title of the notification (default is "Notification").
    """
    subprocess.run(['notify-send', title, message])
    

# The following function is taken from the chatgpt to flush all the uninteded inputs before the user prompt ..

def flush_input():
    """it flush the terminal whatevert we type on that before an input prompt.."""
    termios.tcflush(sys.stdin, termios.TCIFLUSH)
    


# def is_muted():
#     """Check if the system is already muted."""
#     try:
#         result = subprocess.run(['pactl', 'get-sink-mute', '@DEFAULT_SINK@'], 
#                                 stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         if 'yes' in result.stdout:
#             return True
#         return False
#     except Exception as e:
#         print(f"Error checking mute status: {e}")
#         return False


def stopplayingMedia():
    """stop the song that is being playing - with playerctl"""
    try:
        system("playerctl pause")
        print("Music has been paused ")
    except Exception as e:
        print(f"Error in playerctl ...: {e}")

def startplayingMedia():
    """Playing the songs that was playing - with playerctl."""
    try:
        system("playerctl play")
        print(" Music is back . ...")
    except Exception as e:
        print(f"Error in playerctl .... : {e}")


def main():

    print("The Program has started !!!\n You will be notified time to time to keep you Healthy")
    # print("\n\n\tNOTE : Enter the values  \n\t eg - 25 .. for 25 minuts\n\t 2.5 for 2.5 minutes etc...\n")
    
    # eyetime_interval = float(input("Enter after how many minute \n YOU want An Healthy eyetime reminder ->"))*60#25*60 # 25 min in seconds
    # watertime_interval = float(input("Ener your water time Intervale"))*60 #45*60 # 45 min in seconds
    # exercisetime_interval = float(input("Enter the exercise interval time ->"))*60 #60*60 # 60 min or 1 hour in seconds

    eyetime_interval = 25*60 # 25 min in seconds
    watertime_interval =  45*60 # 45 min in seconds
    exercisetime_interval =  60*60 # 60 min or 1 hour in seconds

    last_time_of_exercise = time.time() # catch current time to use in the loop as a base time
    last_time_of_water = time.time()
    last_time_of_eye =time.time()


    while True:

        currentime = time.time()
        # Now checking water time , exercise time and eye time
        
        

        timetaken = 0  
            
        if  currentime - last_time_of_eye >= eyetime_interval :
            timetaken = eyetime()
            startplayingMedia()
            last_time_of_eye = time.time()



        if currentime - last_time_of_exercise >= exercisetime_interval :
            timetaken = physical_activity()
            startplayingMedia()
            last_time_of_exercise = time.time()


        if currentime - last_time_of_water >= watertime_interval:
            timetaken = watertime()
            startplayingMedia()
            last_time_of_water = time.time()


        time.sleep(abs(500-timetaken))



if __name__ == '__main__':
    main()



