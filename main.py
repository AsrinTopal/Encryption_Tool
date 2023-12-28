from tkinter import *
from tkinter import messagebox
import base64
import os

# Function to handle decryption
def decrypt():
    password = code.get()
    
    if password == "1234":
        # Create a new window for decryption
        screen2 = Toplevel(screen)
        screen2.title("Decryption")
        
        # Set window dimensions and configure background color
        screen2.geometry("400x200")
        screen2.minsize(400, 200)
        screen2.maxsize(400, 200)
        screen2.configure(bg="#00bd56")
        
        # Get the input text for decryption
        message = text1.get(1.0, END)
        
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")
        
        # Display decryption result in a new window
        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Rpbote 10", fg="black", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        text2.insert(END, decrypt)
    elif password == "":
        messagebox.showerror("Decryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("Decryption", "Invalid Password")

# Function to handle encryption
def encrypt():
    password = code.get()
    
    if password == "1234":
        # Create a new window for encryption
        screen1 = Toplevel(screen)
        screen1.title("Encryption")
        
        # Set window dimensions and configure background color
        screen1.geometry("400x200")
        screen1.minsize(400, 200)
        screen1.maxsize(400, 200)
        screen1.configure(bg="#ed3833")
        
        # Get the input text for encryption
        message = text1.get(1.0, END)
        
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")
        
        # Display encryption result in a new window
        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y=0)
        text2 = Text(screen1, font="Rpbote 10", fg="black", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)
        
        text2.insert(END, encrypt)
    elif password == "":
        messagebox.showerror("Encryption", "Input Password")
    elif password != "1234":
        messagebox.showerror("Encryption", "Invalid Password")

# Function to create the main GUI screen
def main_screen():
    global screen
    global code
    global text1
    
    screen = Tk()
    screen.geometry("375x398")
    screen.minsize(375, 398)
    screen.maxsize(375, 398)
    
    # Set window icon
    image_icon = PhotoImage(file="Keys.png")
    screen.iconphoto(False, image_icon)
    screen.title("Encryption Decryption Tool")
    
    # Function to reset input fields
    def reset():
        code.set("")
        text1.delete(1.0, END)
    
    # Label for text input
    Label(text="Enter text for encryption or decryption", fg="black", font=("calbri", 13)).place(x=10, y=10)
    text1 = Text(font="Robote 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
    text1.place(x=10, y=50, width=355, height=100)
    
    # Label for key input
    Label(text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10, y=170)
    
    # Entry field for key
    code = StringVar()
    Entry(textvariable=code, width=19, bd=0, font=("arial", 25), show="*").place(x=10, y=200)
    
    # Buttons for encryption, decryption, and reset
    Button(text="ENCRYPT", height="2", width=23, bg="#ed3833", fg="white", bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2", width=23, bg="#00bd56", fg="white", bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width=50, bg="#1089ff", fg="white", bd=0, command=reset).place(x=10, y=300)
    
    screen.mainloop()

# Launch the main screen
main_screen()