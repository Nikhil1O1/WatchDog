import tkinter as tk
import tkinter.font as font
from in_out import in_out
from motion import noise
from rect_noise import rect_noise
from record import record
from PIL import Image, ImageTk
from find_motion import find_motion
from identify import maincall



window = tk.Tk()
window.title("WATCHDOG")
window.iconphoto(False, tk.PhotoImage(file='mn.png'))
window.geometry('1080x700')
window.config(bg='blue')

frame1 = tk.Frame(window)
frame1.config(bg="green")



label_title = tk.Label(frame1, text="WATCHDOG")
label_title.config(bg="yellow")
label_title.configure(foreground="#00ff1e")
label_font = font.Font(size=35, weight='bold',family='Helvetica')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('icons/watchdog.png')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.config(bg="#000000")
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('icons/lamp.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('icons/rectangle-of-cutted-line-geometrical-shape.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn5_image = Image.open('icons/exit.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn3_image = Image.open('icons/security-camera.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn6_image = Image.open('icons/incognito.png')
btn6_image = btn6_image.resize((50,50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn4_image = Image.open('icons/record.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn7_image = Image.open('icons/recording.png')
btn7_image = btn7_image.resize((50,50), Image.ANTIALIAS)
btn7_image = ImageTk.PhotoImage(btn7_image)

bg = tk.PhotoImage(file = "icons/background.png")
icon = Image.open('icons/watchdog.png')
icon = icon.resize((150,150), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
canvas1 = tk.Canvas( window, width = 1080,height = 720) 
canvas1.pack(fill = "both", expand = True)  
canvas1.create_image( 0, 0, image = bg,anchor = "nw")
canvas1.create_image(600,90,image = icon,anchor = "nw")
canvas1.create_text( 653, 70,text = "Watch",fill= '#31a8f7',font=('Helvetica','30','bold'))
canvas1.create_text( 750, 70,text = "Dog",fill= 'white',font=('Helvetica','30','bold'))
#label_font = font.Font(size=35, weight='bold',family='Helvetica')
#label_title['font'] = label_font

#button1 = tk.Button( window, text = "Exit", height=90, width=200, fg='green',command = find_motion, image=btn1_image, compound='left')
#button3 = tk.Button( window, text = "Start")
#button2 = tk.Button( window, text = "Reset")
#btn_font = font.Font(size=25)
#button1['font'] = btn_font
#button1.grid(row = 3,  pady =(20,10))
#button1_canvas = canvas1.create_window( 500, 10, anchor = "nw",window = button1)
#button2_canvas = canvas1.create_window( 100, 40,anchor = "nw",window = button2)
#button3_canvas = canvas1.create_window( 100, 70, anchor = "nw",window = button3)


# --------------- Button -------------------#
btn_font = font.Font(size=25)
btn1 = tk.Button(window, text='Monitor', height=90, width=200, fg='green',command = find_motion, image=btn1_image, compound='left')
btn1['font'] = btn_font
button1_canvas = canvas1.create_window( 350,270, anchor = "nw",window = btn1)

btn2 = tk.Button(window, text='Rectangle', height=90, width=200, fg='orange', command=rect_noise, compound='left', image=btn2_image)
btn2['font'] = btn_font
button1_canvas = canvas1.create_window( 560,270, anchor = "nw",window = btn2)

btn3 = tk.Button(window, text='Noise', height=90, width=200, fg='green', command=noise, image=btn3_image, compound='left')
btn3['font'] = btn_font
button1_canvas = canvas1.create_window( 770,270, anchor = "nw",window = btn3)

btn4 = tk.Button(window, text='Record', height=90, width=200, fg='orange', command=record, image=btn4_image, compound='left')
btn4['font'] = btn_font
button1_canvas = canvas1.create_window( 350,380, anchor = "nw",window = btn4)

btn6 = tk.Button(window, text='In Out', height=90, width=200, fg='green', command=in_out, image=btn6_image, compound='left')
btn6['font'] = btn_font
button1_canvas = canvas1.create_window( 560,380, anchor = "nw",window = btn6)

btn5 = tk.Button(window, height=90, width=200, fg='red', command=window.destroy, image=btn5_image)
btn5['font'] = btn_font
button1_canvas = canvas1.create_window( 560,490, anchor = "nw",window = btn5)

btn7 = tk.Button(window, text="identify", height=90, width=200, fg="orange",command=maincall, compound='left', image=btn7_image)
btn7['font'] = btn_font
button1_canvas = canvas1.create_window( 770,380, anchor = "nw",window = btn7)

frame1.pack()
window.mainloop()


