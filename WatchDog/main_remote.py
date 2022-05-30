from mimetypes import init
import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import rem_noise
from rect_noise import rect_noise
from record import rem_record
from PIL import Image, ImageTk
from find_motion import rem_find_motion
from identify import maincall


#pybot files
from threading import Thread
from turtle import update
from telegram import Update,Bot
from telegram.ext import Updater,MessageHandler,Filters
from telegram.utils.request import Request
import os,json
from threading import Thread

pwd=""

def mesaage_handler(update,context):
    user_message=update.message.text
    user_message,stop_event=user_message.split(" ")
    stop_event = int(stop_event)
    print(stop_event)
    print(user_message)
    if(user_message.lower() == "startrcd"):
        update.message.reply_text(f'Recording Started')
        rem_record(stop_event)
    if(user_message.lower() == "startnoise"):
        update.message.reply_text(f'Noise detection active')
        rem_noise(stop_event)
    if(user_message.lower() == "startmotion"):
        update.message.reply_text(f'Motion detection active')
        rem_find_motion(stop_event = 1)

    else:
        update.message.reply_text(f'you sent the following: {update.message.text}')

    
def tele_intit():
    req=Request(connect_timeout=0.5)
    t_bot=Bot(request=req,token=pwd)
    updater=Updater(bot=t_bot,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(MessageHandler(filters=Filters.all,callback=mesaage_handler))

    updater.start_polling()
    updater.idle()


#tele_intit()