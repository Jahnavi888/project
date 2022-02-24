import tkinter as tk
import tkinter.font as font
#from in_out import in_out
#from motion import noise
#from rect_noise import rect_noise
#from record import record
from PIL import Image, ImageTk

window = tk.Tk()
window.title("Smart cctv")
window.iconphoto(False, tk.PhotoImage(file='bg.png'))
window.geometry('1080x760')


frame1 = tk.Frame(window)

label_title = tk.Label(frame1, text="SMART GUARD")
label_font = font.Font(size=30, weight='bold',family='Algerian')
label_title['font'] = label_font
label_title.grid(pady=(10,10), column=2)


icon = Image.open('new icons/smart guard.png')
icon = icon.resize((50,50), Image.ANTIALIAS)
icon = ImageTk.PhotoImage(icon)
label_icon = tk.Label(frame1, image=icon)
label_icon.grid(row=1, pady=(5,10), column=2)

btn1_image = Image.open('new icons/identify.png')
btn1_image = btn1_image.resize((50,50), Image.ANTIALIAS)
btn1_image = ImageTk.PhotoImage(btn1_image)

btn2_image = Image.open('new icons/motion.png')
btn2_image = btn2_image.resize((50,50), Image.ANTIALIAS)
btn2_image = ImageTk.PhotoImage(btn2_image)

btn3_image = Image.open('new icons/motion direction.png')
btn3_image = btn3_image.resize((50,50), Image.ANTIALIAS)
btn3_image = ImageTk.PhotoImage(btn3_image)

btn4_image = Image.open('new icons/motion distance.png')
btn4_image = btn4_image.resize((50,50), Image.ANTIALIAS)
btn4_image = ImageTk.PhotoImage(btn4_image)

btn5_image = Image.open('new icons/record.png')
btn5_image = btn5_image.resize((50,50), Image.ANTIALIAS)
btn5_image = ImageTk.PhotoImage(btn5_image)

btn6_image = Image.open('new icons/track object.png')
btn6_image = btn6_image.resize((50,50), Image.ANTIALIAS)
btn6_image = ImageTk.PhotoImage(btn6_image)

btn7_image = Image.open('new icons/track time.png')
btn7_image = btn7_image.resize((50,50), Image.ANTIALIAS)
btn7_image = ImageTk.PhotoImage(btn7_image)

btn8_image = Image.open('new icons/count.png')
btn8_image = btn8_image.resize((50,50), Image.ANTIALIAS)
btn8_image = ImageTk.PhotoImage(btn8_image)

btn9_image = Image.open('new icons/dwell time.png')
btn9_image = btn9_image.resize((50,50), Image.ANTIALIAS)
btn9_image = ImageTk.PhotoImage(btn9_image)

btn10_image = Image.open('new icons/exit.png')
btn10_image = btn10_image.resize((50,50), Image.ANTIALIAS)
btn10_image = ImageTk.PhotoImage(btn10_image)

# --------------- Button -------------------#
btn_font = font.Font(size=15)
btn1 = tk.Button(frame1, text='Identify', height=90, width=180, fg='green', image=btn1_image, compound='left')
btn1['font'] = btn_font
btn1.grid(row=3, pady=(0,10))

btn_font = font.Font(size=15)
btn2 = tk.Button(frame1, text='Motion', height=90, width=180, fg='green', image=btn2_image, compound='left')
btn2['font'] = btn_font
btn2.grid(row=3, pady=(0,10),column=2)

btn_font = font.Font(size=15)
btn3 = tk.Button(frame1, text='Direction', height=90, width=180, fg='orange',image=btn3_image, compound='left')
btn3['font'] = btn_font
btn3.grid(row=3, pady=(0,10), column=3)

btn_font = font.Font(size=15)
btn4 = tk.Button(frame1, text='Distance', height=90, width=180, fg='orange',image=btn4_image, compound='left')
btn4['font'] = btn_font
btn4.grid(row=4, pady=(0,10))

btn_font = font.Font(size=15)
btn5 = tk.Button(frame1, text='Record', height=90, width=180, fg='orange',image=btn5_image, compound='left')
btn5['font'] = btn_font
btn5.grid(row=4, pady=(0,10), column=2)

btn_font = font.Font(size=15)
btn6 = tk.Button(frame1, text='Track Object', height=90, width=180, fg='green',image=btn6_image, compound='left')
btn6['font'] = btn_font
btn6.grid(row=4, pady=(0,10), column=3)

btn_font = font.Font(size=15)
btn7 = tk.Button(frame1, text='Track Time', height=90, width=180, fg='orange',image=btn7_image, compound='left')
btn7['font'] = btn_font
btn7.grid(row=5, pady=(0,10))

btn_font = font.Font(size=15)
btn8 = tk.Button(frame1, text='Count', height=90, width=180, fg='orange',image=btn8_image, compound='left')
btn8['font'] = btn_font
btn8.grid(row=5, pady=(0,10), column=2)

btn_font = font.Font(size=15)
btn9 = tk.Button(frame1, text='Dwell Time', height=90, width=180, fg='green',image=btn9_image, compound='left')
btn9['font'] = btn_font
btn9.grid(row=5, pady=(0,10), column=3)

btn10 = tk.Button(frame1, text='Exit', height=90, width=180, fg='red',image=btn10_image,compount='left')
btn10['font'] = btn_font
btn10.grid(row=6, pady=(0,10), column=2)

frame1.pack()
window.mainloop()
