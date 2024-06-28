import customtkinter
import datetime
from customtkinter import *
from tkinter import *
import tkinter
from PIL import Image
import pywhatkit

exercises = {
    "Day 1": ["Flat bench press", "Incline Bench Press", "Cable Cross Over (Lower Chest)", "Butter Fly", "Fly", "Chest Press", "Dumble Pull Over"],
    "Day 2": ["Seated Cable Rows", "Lat Pulldown", "Chest Supported Row", "Behind-The-Neck Lat Pulldown", "Barbell Bent Over Row", "One-Arm Dumbbell Row", "Dumbell Shrug"],
    "Day 3": ["Cable Pushdown", "Barbell Bicep Curl", "Dumbbell Overhead Extension", "Dumbbell Bicep Curl", "Dips", "Machine Preacher Curl", "Wrist lift"],
    "Day 4": ["Shoulder Press Machine", "Lateral Raise", "Cable Front Raise", "Face Pull", "Reverse Machine Fly", "Dumble Shurgg"],
    "Day 5": ["Body Weight Squat", "Weighted Squat", "Leg Press", "Lunges", "Leg Extension", "Sumo Squat", "Calf Raise"],
}
day_completed=1
now = datetime.datetime.now()
printed=False
# command=input("Enter=").lower
message=""
while(True):

    if not printed:

        for i in exercises[f"Day {day_completed}"]:


            message=message+f"[.]{i}\n"
            pywhatkit.sendwhatmsg_instantly("+92 3288754547",message,tab_close=True)

            printed=True

        #     # if command=="completed":
        #         print("Great")
        # if now.hour == 0 and command=="completed":
        #     day_completed=day_completed+1
        #     printed=False
        # if day_completed>=6:
        #     day_completed=0



