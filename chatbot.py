import tkinter as tk
from datetime import datetime

# Function to handle user input and provide chatbot responses
def chatbot_response():
    user_input = entry.get().strip().lower()
    if user_input == "":
        response = "Please type something to chat with me!"
    elif user_input == "exit" or user_input == "bye":
        response = "Goodbye! Have a great day!"
        window.destroy()
    elif "hello" in user_input or "hi" in user_input:
        response = "Hello there! How can I assist you today?"
    elif "your name" in user_input or "who are you" in user_input:
        response = "I'm Chatpy, your friendly chatbot!"
    elif "how are you" in user_input:
        response = "I'm just code, but I'm feeling great! How about you?"
    elif "help" in user_input:
        response = "I can help you with general queries like time, date, or small talk. Ask me anything!"
    elif "time" in user_input:
        current_time = datetime.now().strftime("%H:%M:%S")
        response = f"The current time is {current_time}."
    elif "date" in user_input:
        current_date = datetime.now().strftime("%Y-%m-%d")
        response = f"Today's date is {current_date}."
    elif "weather" in user_input:
        response = "I can't check the weather, but you can use weather apps for that!"
    elif "joke" in user_input:
        response = "Why don't scientists trust atoms? Because they make up everything!"
    else:
        response = "I'm sorry, I didn't understand that. Can you try asking in a different way?"
    
    # Display chatbot response in the chat window
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n", "user")
    chat_window.insert(tk.END, f"Chatpy: {response}\n\n", "chatbot")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)
    entry.delete(0, tk.END)

# Function to toggle between light and dark themes
def toggle_theme():
    global theme
    if theme == "light":
        theme = "dark"
        apply_theme(dark_theme)
    else:
        theme = "light"
        apply_theme(light_theme)

# Function to apply a theme to the UI
def apply_theme(theme_config):
    window.config(bg=theme_config["bg"])
    chat_window.config(bg=theme_config["chat_bg"], fg=theme_config["chat_fg"])
    entry.config(bg=theme_config["entry_bg"], fg=theme_config["entry_fg"])
    send_button.config(bg=theme_config["button_bg"], fg=theme_config["button_fg"])
    toggle_button.config(bg=theme_config["button_bg"], fg=theme_config["button_fg"])
    footer_label.config(bg=theme_config["bg"], fg=theme_config["footer_fg"])

# Theme configurations
light_theme = {
    "bg": "#f0f8ff",
    "chat_bg": "#ffffff",
    "chat_fg": "#333333",
    "entry_bg": "#e6f7ff",
    "entry_fg": "#333333",
    "button_bg": "#0059b3",
    "button_fg": "white",
    "footer_fg": "#666666",
}

dark_theme = {
    "bg": "#1e1e1e",
    "chat_bg": "#2e2e2e",
    "chat_fg": "#e6e6e6",
    "entry_bg": "#3c3c3c",
    "entry_fg": "#e6e6e6",
    "button_bg": "#444444",
    "button_fg": "#ffffff",
    "footer_fg": "#bbbbbb",
}

# Initialize the main window
window = tk.Tk()
window.title("Chatpy - Your Friendly Chatbot")
window.geometry("500x600")
window.resizable(False, False)

# Chat display area
chat_window = tk.Text(
    window, 
    height=25, 
    width=60, 
    state=tk.DISABLED, 
    font=("Arial", 12), 
    wrap=tk.WORD
)
chat_window.tag_config("user", foreground="#0059b3")  # User text in blue
chat_window.tag_config("chatbot", foreground="#228b22")  # Chatbot text in green
chat_window.pack(pady=10, padx=10)

# User input area
entry_frame = tk.Frame(window)
entry_frame.pack(pady=10)

entry = tk.Entry(entry_frame, width=40, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=5)

send_button = tk.Button(
    entry_frame, 
    text="Send", 
    command=chatbot_response, 
    font=("Arial", 12), 
    relief="flat"
)
send_button.pack(side=tk.RIGHT)

# Theme toggle button
toggle_button = tk.Button(
    window, 
    text="Toggle Theme", 
    command=toggle_theme, 
    font=("Arial", 10), 
    relief="flat"
)
toggle_button.pack(pady=5)

# Footer label
footer_label = tk.Label(
    window, 
    text="Chatpy - Your Friendly Chatbot", 
    font=("Arial", 10, "italic")
)
footer_label.pack(side=tk.BOTTOM, pady=10)

# Set default theme
theme = "light"
apply_theme(light_theme)

# Run the application
window.mainloop()
