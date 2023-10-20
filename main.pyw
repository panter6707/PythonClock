from tkinter import Label, Tk
import time

# Defining the window
app_window = Tk()
app_window.title("MKYLisans Digital Clock")
app_window.geometry("400x200")
app_window.resizable(1,1)

# Label design
text_font = ("Boulder", 68, 'bold')
background = "#070bf2"
foreground = "#ff0505"
border_width = 20

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label.grid(row=0, column=1)
def MKYLisans_text():
    yazi = Label(app_window, text="MKYLisans Ürünüdür", font="Verdana 12 bold", bg="#05ff2a", fg="#0505ff")
    yazi.place(x=100, y=150, width=200, height=50)
    return

# Clock function
def digital_clock_MKYLisans():
    time_live = time.strftime("%H:%M:%S")
    label.config(text=time_live)
    label.after(200, digital_clock_MKYLisans)

# Running the application

digital_clock_MKYLisans()
MKYLisans_text()
app_window.mainloop()