import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from mock_sensor_library import MockTemperatureSensor, MockFlowSensor, MockColorSensor
import time
import os

# Initialize mock sensor objects
temperature_sensor = MockTemperatureSensor()
flow_sensor = MockFlowSensor()
color_sensor = MockColorSensor()

# Main window configuration
root = tk.Tk()
root.geometry("800x480")
root.title("Minimalist Login")

# Japanese minimalist color scheme
background_color = "#F5F5F5"
text_color = "#2E2E2E"
button_color = "#D1CBC7"
highlight_color = "#A1A1A1"

root.configure(bg=background_color)

# Font configuration
font_large = ("Helvetica", 20, "bold")
font_small = ("Helvetica", 16)

# Dictionary to store user credentials
credentials = {}

def save_credentials(user_id, password):
    with open("credentials.txt", "a") as file:
        file.write(f"{user_id}:{password}\n")

def load_credentials():
    try:
        with open("credentials.txt", "r") as file:
            for line in file:
                user_id, password = line.strip().split(":", 1)
                credentials[user_id] = password
    except FileNotFoundError:
        pass

current_entry = None
keyboard_window = None

def show_keyboard(entry):
    global current_entry, keyboard_window
    current_entry = entry

    if keyboard_window and keyboard_window.winfo_exists():
        keyboard_window.lift()
        return

    keyboard_window = tk.Toplevel(root)
    keyboard_window.geometry("600x200")
    keyboard_window.configure(bg=background_color)
    keyboard_window.title("On-Screen Keyboard")

    keys = [
        '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P',
        'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
        'Z', 'X', 'C', 'V', 'B', 'N', 'M',
        'Backspace', 'Space', 'Enter'
    ]

    def add_char(key):
        if key == "Backspace":
            current_entry.delete(len(current_entry.get())-1, tk.END)
        elif key == "Space":
            current_entry.insert(tk.END, ' ')
        elif key == "Enter":
            keyboard_window.destroy()
            move_focus()
        else:
            current_entry.insert(tk.END, key)
    
    row = 0
    col = 0
    for key in keys:
        btn = tk.Button(keyboard_window, text=key, width=4, height=2, font=("Helvetica", 12),
                        bg=button_color, fg=text_color, bd=1, highlightbackground=highlight_color,
                        command=lambda k=key: add_char(k))
        btn.grid(row=row, column=col, padx=5, pady=5)
        col += 1
        if col > 9:
            col = 0
            row += 1

    keyboard_window.protocol("WM_DELETE_WINDOW", lambda: None)

def move_focus():
    widget_list = [entry_user, entry_password, entry_reg_user, entry_reg_password, entry_reg_confirm_password]
    if current_entry in widget_list:
        next_index = (widget_list.index(current_entry) + 1) % len(widget_list)
        next_widget = widget_list[next_index]
        next_widget.focus_set()

def validate_credentials(user_id, password):
    return bool(user_id) and bool(password)

def show_registration():
    def register():
        user_id = entry_reg_user.get()
        password = entry_reg_password.get()
        confirm_password = entry_reg_confirm_password.get()
        
        if validate_credentials(user_id, password) and password == confirm_password:
            save_credentials(user_id, password)
            registration_label.config(text="Registration successful! Please log in.", fg="green")
            root.after(2000, show_login)
        else:
            registration_label.config(text="Invalid input or passwords do not match.", fg="red")

    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Create User ID:", font=font_large, bg=background_color, fg=text_color).pack(pady=20)
    entry_reg_user = tk.Entry(root, font=font_small, width=20)
    entry_reg_user.pack(pady=10)
    entry_reg_user.bind("<FocusIn>", lambda event: show_keyboard(entry_reg_user))

    tk.Label(root, text="Create Password:", font=font_large, bg=background_color, fg=text_color).pack(pady=20)
    entry_reg_password = tk.Entry(root, show="*", font=font_small, width=20)
    entry_reg_password.pack(pady=10)
    entry_reg_password.bind("<FocusIn>", lambda event: show_keyboard(entry_reg_password))

    tk.Label(root, text="Confirm Password:", font=font_large, bg=background_color, fg=text_color).pack(pady=20)
    entry_reg_confirm_password = tk.Entry(root, show="*", font=font_small, width=20)
    entry_reg_confirm_password.pack(pady=10)
    entry_reg_confirm_password.bind("<FocusIn>", lambda event: show_keyboard(entry_reg_confirm_password))

    registration_label = tk.Label(root, text="", font=font_small, bg=background_color, fg=text_color)
    registration_label.pack(pady=10)

    register_button = tk.Button(root, text="Register", font=font_small, width=10, height=2,
                               bg=button_color, fg=text_color, bd=1, highlightbackground=highlight_color,
                               command=register)
    register_button.pack(pady=30)

def show_login():
    def login():
        user_id = entry_user.get()
        password = entry_password.get()
        
        if user_id in credentials and credentials[user_id] == password:
            messagebox.showinfo("Login", "Login successful!")
            root.after(1000, show_dashboard)
        else:
            error_label.config(text="Invalid credentials. Please try again.", fg="red")

    for widget in root.winfo_children():
        widget.destroy()

    # Load and display the logo
    logo_path = os.path.join("assets", "logo.jpg")
    if os.path.exists(logo_path):
        logo_image = Image.open(logo_path)
        logo_image = logo_image.resize((200, 100), Image.Resampling.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_image)
        logo_label = tk.Label(root, image=logo_photo, bg=background_color)
        logo_label.image = logo_photo
        logo_label.pack(pady=20)

    tk.Label(root, text="User ID:", font=font_large, bg=background_color, fg=text_color).pack(pady=20)
    entry_user = tk.Entry(root, font=font_small, width=20)
    entry_user.pack(pady=10)
    entry_user.bind("<FocusIn>", lambda event: show_keyboard(entry_user))

    tk.Label(root, text="Password:", font=font_large, bg=background_color, fg=text_color).pack(pady=20)
    entry_password = tk.Entry(root, show="*", font=font_small, width=20)
    entry_password.pack(pady=10)
    entry_password.bind("<FocusIn>", lambda event: show_keyboard(entry_password))

    error_label = tk.Label(root, text="", font=font_small, bg=background_color, fg=text_color)
    error_label.pack(pady=10)

    login_button = tk.Button(root, text="Login", font=font_small, width=10, height=2,
                             bg=button_color, fg=text_color, bd=1, highlightbackground=highlight_color,
                             command=login)
    login_button.pack(pady=30)

    register_button = tk.Button(root, text="Register", font=font_small, width=10, height=2,
                                bg=button_color, fg=text_color, bd=1, highlightbackground=highlight_color,
                                command=show_registration)
    register_button.pack(pady=20)

def show_dashboard():
    def logout():
        show_login()

    for widget in root.winfo_children():
        widget.destroy()

    # Display sensor data
    tk.Label(root, text="Temperature: " + get_temperature(), font=font_large, bg=background_color, fg=text_color).pack(pady=20)
    tk.Label(root, text="Flow Rate: " + get_flow_rate(), font=font_large, bg=background_color, fg=text_color).pack(pady=20)
    tk.Label(root, text="Color Sensor: " + get_color_sensor(), font=font_large, bg=background_color, fg=text_color).pack(pady=20)
    tk.Label(root, text="Current Time: " + get_current_time(), font=font_large, bg=background_color, fg=text_color).pack(pady=20)

    logout_button = tk.Button(root, text="Logout", font=font_small, width=10, height=2,
                             bg=button_color, fg=text_color, bd=1, highlightbackground=highlight_color,
                             command=logout)
    logout_button.pack(pady=30)

def get_temperature():
    return "25°C"

def get_flow_rate():
    return "5 L/min"

def get_color_sensor():
    return "Red"

def get_current_time():
    return time.strftime("%I:%M %p")

# Load saved credentials
load_credentials()

# Start with the login screen
show_login()

root.mainloop()