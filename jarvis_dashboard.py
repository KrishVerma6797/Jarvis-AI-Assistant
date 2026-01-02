import tkinter as tk
from tkinter import scrolledtext, filedialog
import threading
import time
from tkinter import messagebox
from takeCommand import takeCommand
from speak import speak
from llama import ask_llama
from wish import wishMe
import datetime
import os
import json
from wish import wishMe
class JarvisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jarvis AI Assistant")
        self.root.geometry("700x600")
        self.root.configure(bg="black")

        self.create_widgets()
        self.model_start_time = time.time()

        threading.Thread(target=self.startup_greeting).start()

    def create_widgets(self):
        # Title
        title = tk.Label(self.root, text="🧠 Jarvis AI", font=("Segoe UI", 20, "bold"),
                         bg="black", fg="cyan")
        title.pack(pady=10)

        # Scrollable output
        self.output = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Segoe UI", 12),
                                                bg="#111111", fg="white", height=20)
        self.output.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        # Input field
        input_frame = tk.Frame(self.root, bg="black")
        input_frame.pack(pady=5)

        self.input_text = tk.Entry(input_frame, font=("Segoe UI", 14), width=50, bg="#222222", fg="white")
        self.input_text.pack(side=tk.LEFT, padx=10)

        send_btn = tk.Button(input_frame, text="Send", font=("Segoe UI", 12), command=self.handle_text_input,
                             bg="cyan", fg="black")
        send_btn.pack(side=tk.LEFT)

        mic_button = tk.Button(self.root, text="🎤 Speak", font=("Segoe UI", 14),
                               command=self.listen_and_respond,
                               bg="cyan", fg="black", width=10)
        mic_button.pack(pady=5)

        save_btn = tk.Button(self.root, text="🔖 Save Log", font=("Segoe UI", 12), command=self.save_chat,
                             bg="#444444", fg="white")
        save_btn.pack(pady=5)

        time_btn = tk.Button(self.root, text="⏱ Model Load Time", font=("Segoe UI", 12), command=self.show_load_time,
                             bg="#444444", fg="white")
        time_btn.pack(pady=5)

    def startup_greeting(self):
        
        speak("Hey! I am Jarvis. How can I assist you today?")
        
        self.log_response("Jarvis", "Hey! I am Jarvis. How can I assist you today?")

    def listen_and_respond(self):
        threading.Thread(target=self.handle_voice_query).start()

    def handle_voice_query(self):
        self.log_response("System", "🎤 Listening...")
        query = takeCommand()
        if query == "none":
            self.log_response("System", "❌ Didn't catch that.")
            return
        self.process_query(query)

    def handle_text_input(self):
        query = self.input_text.get().strip()
        self.input_text.delete(0, tk.END)
        if query:
            self.process_query(query)

    def process_query(self, query):
        self.log_response("You", query)
        response = ask_llama(query)
        self.log_response("Jarvis", response)
        speak(response)

    def log_response(self, sender, message):
        timestamp = datetime.datetime.now().strftime("%H:%M")
        self.output.insert(tk.END, f"[{timestamp}] {sender}: {message}\n")
        self.output.see(tk.END)

    def save_chat(self):
        log_text = self.output.get("1.0", tk.END).strip()
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(log_text)

    def show_load_time(self):
        load_time = time.time() - self.model_start_time
        messagebox.showinfo("Model Load Time", f"LLaMA initialized in {load_time:.2f} seconds.")


# Main launcher
if __name__ == "__main__":
    root = tk.Tk()
    app = JarvisApp(root)
    root.mainloop()
