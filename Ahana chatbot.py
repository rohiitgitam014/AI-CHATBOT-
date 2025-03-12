import tkinter as tk
from tkinter import ttk, scrolledtext
from PIL import Image, ImageTk
import time
import webbrowser
import os
import pyttsx3  # Text-to-Speech Library

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speed
engine.setProperty("volume", 1.0)  # Max volume
global user_name
user_name = ""


# Function to ask for the user's name
def ask_name(event=None):
    global user_name
    user_name = entry.get().strip()
    if user_name:
        chat_history.insert(tk.END, f"Ahana Bot : Nice to meet you, {user_name}! How can I assist you today?\n")
        entry.delete(0, tk.END)
        entry.config(state="normal")
        send_button.config(command=chatbot_response)
        entry.bind("<Return>", chatbot_response)  # Enable Enter key for chatting
    else:
        chat_history.insert(tk.END, "Ahana Bot: Please enter a valid name.\n")


# Function to delay opening a website
def delayed_open(url, message):
    def open_url():
        webbrowser.open(url)

    root.after(1500, open_url)
    return message

#  Functions to Open Web Pages
def open_jobs():
    webbrowser.open("https://ahanait.com//career/")
    return "Opening the job listings page..."

def open_info():
    webbrowser.open("https://ahanait.com/")
    return "Opening the Ahana page..."

def open_hrms():
    webbrowser.open("https://hr.hwtpl.com/Ahana/login.aspx?ReturnUrl=%2fAhana%2f")
    return "Opening HRMS page..."

def open_myahana():
    webbrowser.open("https://myahana.ahanait.com/")
    return "Opening MyAhana page..."

def open_timesheet():
    webbrowser.open("https://hr.hwtpl.com/Ahana/hrms/pages/ListTimesheetCreationP.aspx")
    return "Opening Timesheet page..."

def open_checklist():
    webbrowser.open("https://myahana1.ahanait.com:5002/login")
    return "Opening Checklist page..."

def open_support():
    webbrowser.open("https://support.ahanait.com/ahana/WorkOrder.do?woMode=viewWO&woID=144881&PORTALID=1")
    return "Opening Ahana Support page..."

#  Dictionary of Responses
responses = {
    "hi": lambda: "Hello! Welcome to Ahana Chatbot. How can I assist you?",
    "hello": lambda: "Hi there! How can I help you today?",
    "how are you": lambda: "I'm just a bot, but I'm doing great! How about you?",
    "bye": lambda: "Goodbye! Have a great day!",
    "help": lambda: "You can ask me about Ahana Systems, job listings, or anything else.",
    "good morning" : lambda : "Good morning I am ahana chatbot . How can i help you ?",
    "good afternoon" : lambda : "Good evening  I am ahana chatbot . How can i help you ?",
    "good evening" : lambda : "Good evening I am ahana chatbot. How can i help you ?",
    "jobs": open_jobs,  
    "info": open_info,  
    "hrms": open_hrms,
    "myahana": open_myahana,
    "checklist": open_checklist,
    "timesheet": open_timesheet,
    "support": open_support,
    "thanks": lambda: "You're welcome! Let me know if you need more help."
}

# 🗣 Function to Process User Input
def chatbot_response():
    user_input = entry.get().strip().lower()  # Clean input
    chat_history.insert(tk.END, f"\n You: {user_input}\n", "user_msg")

     # Check if user input matches any keyword
    response = "Sorry, I don't understand. Can you rephrase?"
    for keyword in responses:
        if keyword in user_input:
            response = responses[keyword]()  # Call function if it exists
            break


    # Simulate typing effect
    chat_history.insert(tk.END, " Ahana chatbot: Typing...\n", "bot_typing")
    root.update_idletasks()
    time.sleep(0.5)

    # Update response
    chat_history.delete("end-2l", "end-1l")
    chat_history.insert(tk.END, f"Ahana  Bot: {response}\n", "bot_msg")

    # Speak the response
    speak(response)

    entry.delete(0, tk.END)  # Clear input field

#  Function to Speak Bot's Response
def speak(text):
    engine.say(text)
    engine.runAndWait()

#  GUI Setup
root = tk.Tk()
root.title("Ahana Chatbot ")
root.geometry("500x600")
root.configure(bg="#E3F2FD")  # Light blue background

# 🖼 Load Ahana Logo (with error handling)
logo_path = r"C:\Users\skj_h\OneDrive\Desktop\Ahana chatbot\static\ahana_logo.png"

if os.path.exists(logo_path):
    logo_img = Image.open(logo_path)
    logo_img = logo_img.resize((120, 120))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(root, image=logo_photo, bg="#E3F2FD")
    logo_label.pack(pady=10)
else:
    logo_label = tk.Label(root, text="Ahana Chatbot", font=("Arial", 16, "bold"), bg="#E3F2FD", fg="#1565C0")
    logo_label.pack(pady=10)

# 📝 Chat History Display (Styled)
chat_frame = tk.Frame(root)
chat_frame.pack(pady=10)

chat_history = scrolledtext.ScrolledText(chat_frame, width=55, height=20, wrap=tk.WORD, font=("Arial", 12), bg="white", fg="black", borderwidth=2, relief="solid")
chat_history.pack()

#  Chat Styling
chat_history.tag_config("user_msg", foreground="#1565C0", font=("Arial", 12, "bold"))
chat_history.tag_config("bot_msg", foreground="#1B5E20", font=("Arial", 12, "bold"))
chat_history.tag_config("bot_typing", foreground="#9E9E9E", font=("Arial", 12, "italic"))

#  Input Frame
input_frame = tk.Frame(root, bg="#E3F2FD")
input_frame.pack(pady=10)
entry = ttk.Entry(input_frame, width=40, font=("Arial", 12))
entry.grid(row=0, column=0, padx=5)
entry.bind("<Return>", ask_name)
entry = ttk.Entry(input_frame, width=40, font=("Arial", 12), style="TEntry")
entry.grid(row=0, column=0, padx=5, pady=5)

#  Styled Send Button
send_button = ttk.Button(input_frame, text="Send", command=ask_name)
send_button.grid(row=0, column=1, padx=5)
send_button = ttk.Button(input_frame, text="Send", command=chatbot_response, style="TButton")
send_button.grid(row=0, column=1, padx=5)
style = ttk.Style()
style.configure("TButton", font=("Arial", 12), padding=5)
style.configure("TEntry", padding=5)

chat_history.insert(tk.END, " Ahana Bot: Hi! What's your name?\n")

#  Speak Button (Microphone Icon)
speak_icon = "Speak"  # Unicode microphone emoji
speak_button = ttk.Button(input_frame, text=speak_icon, command=lambda: speak(chat_history.get("end-3l", "end-2l")), style="TButton")
speak_button.grid(row=0, column=2, padx=5)

#  Apply Styling
style = ttk.Style()
style.configure("TButton", font=("Arial", 12, "bold"), padding=5, background="#1976D2", foreground="white")
style.configure("TEntry", padding=5)

#  Add Button Hover Effect
def on_enter(e):
    send_button.config(style="Hover.TButton")
    speak_button.config(style="Hover.TButton")

def on_leave(e):
    send_button.config(style="TButton")
    speak_button.config(style="TButton")

style.configure("Hover.TButton", font=("Arial", 12, "bold"), padding=5, background="#0D47A1", foreground="white")

send_button.bind("<Enter>", on_enter)
send_button.bind("<Leave>", on_leave)
speak_button.bind("<Enter>", on_enter)
speak_button.bind("<Leave>", on_leave)

#  Run GUI
root.mainloop()

