import customtkinter as ctk
from tkinter import messagebox

class AuthScreen(ctk.CTkFrame):
    def __init__(self, master, api_client, on_login_success):
        super().__init__(master, corner_radius=15)
        self.api = api_client
        self.on_login_success = on_// la suite...
