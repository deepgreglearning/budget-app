import customtkinter as ctk
import requests
from tkinter import messagebox, ttk
from datetime import datetime

# Configuration du thème
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class BudgetApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Budget Master - Gestion Financière")
        self.geometry("1100x700")

        # URL du serveur API
        self.API_URL = "http://127.0.0.1:8000"
        self.current_user_id = None

        self.show_login_screen()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    # --- ÉCRANS D'AUTHENTIFICATION ---

    def show_login_screen(self):
        self.clear_screen()
        self.frame = ctk.CTkFrame(self, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.4, relheight=0.6)

        self.label = ctk.CTkLabel(self.frame, text="Budget Master", font=("Roboto", 28, "bold"))
        self.label.pack(pady=(40, 30))

        self.username_entry = ctk.CTkEntry(self.frame, placeholder_text="Nom d'utilisateur", width=280, height=40)
        self.username_entry.pack(pady=10)

        self.password_entry = ctk.CTkEntry(self.frame, placeholder_text="Mot de passe", show="*", width=280, height=40)
        self.password_entry.pack(pady=10)

        self.login_button = ctk.CTkButton(self.frame, text="Se connecter", command=self.handle_login, width=280, height=40, font=("Roboto", 14, "bold"))
        self.login_button.pack(pady=25)

        self.register_link = ctk.CTkButton(self.frame, text="Créer un compte", fg_color="transparent",
                                           text_color="#3b82f6", hover_color="#2563eb",
                                           command=self.show_register_screen)
        self.register_link.pack(pady=10)

    def show_register_screen(self):
        self.clear_screen()
        self.frame = ctk.CTkFrame(self, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.4, relheight=0.7)

        self.label = ctk.CTkLabel(self.frame, text="Inscription", font=("Roboto", 28, "bold"))
        self.label.pack(pady=(40, 30))

        self.reg_username = ctk.CTkEntry(self.frame, placeholder_text="Nom d'utilisateur", width=280, height=40)
        self.reg_username.pack(pady=10)

        self.reg_email = ctk.CTkEntry(self.frame, placeholder_text="Email", width=280, height=40)
        self.reg_email.pack(pady=10)

        self.reg_password = ctk.CTkEntry(self.frame, placeholder_text="Mot de passe", show="*", width=280, height=40)
        self.reg_password.pack(pady=10)

        self.reg_button = ctk.CTkButton(self.frame, text="S'inscrire", command=self.handle_register, width=280, height=40, font=("Roboto", 14, "bold"))
        self.reg_button.pack(pady=25)

        self.back_button = ctk.CTkButton(self.frame, text="Retour à la connexion", fg_color="transparent",
                                         text_color="#3b82f6", hover_color="#2563eb",
                                         command=self.show_login_screen)
        self.back_button.pack(pady=10)
    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs")
            return
        try:
            response = requests.post(f"{self.API_URL}/login", json={"username": username, "password": password}, timeout=5)
            if response.status_code == 200:
                data = response.json()
                self.current_user_id = data['user_id']
                self.show_dashboard()
            else:
                messagebox.showerror("Erreur", response.json().get("detail", "Erreur de connexion"))
        except Exception as e:
            messagebox.showerror("Erreur Réseau", f"Impossible de contacter le serveur : {e}")

    def handle_register(self):
        username = self.reg_username.get()
        email = self.reg_email.get()
        password = self.reg_password.get()
        if not username or not email or not password:
            messagebox.showwarning("Attention", "Veuillez remplir tous les champs")
            return
        try:
            response = requests.post(f"{self.API_URL}/register", json={"username": username, "email": email, "password": password}, timeout=5)
            if response.status_code == 201:
                messagebox.showinfo("Succès", "Compte créé avec succès !")
                self.show_login_screen()
            else:
                messagebox.showerror("Erreur", response.json().get("detail", "Erreur lors de l'inscription"))
        except Exception as e:
            messagebox.showerror("Erreur Réseau", f"Le serveur est injoignable : {e}")
    def create_stat_card(self, parent, title, value, color):
        card = ctk.CTkFrame(parent, fg_color="#1e293b", corner_radius=10, width=250, height=100)
        card.pack(side="left", padx=10, expand=True, fill="both")
        lbl_title = ctk.CTkLabel(card, text=title, font=("Roboto", 14), text_color="#94a3b8")
        lbl_title.pack(pady=(15, 0))
        lbl_val = ctk.CTkLabel(card, text=value, font=("Roboto", 24, "bold"), text_color=color)
        lbl_val.pack(pady=(0, 15))
        return lbl_val

    def show_dashboard(self):
        self.clear_screen()
        # Top Bar
        self.top_bar = ctk.CTkFrame(self, height=60, fg_color="#0b2545", corner_radius=0)
        self.top_bar.pack(side="top", fill="x")
        ctk.CTkLabel(self.top_bar, text="Budget Master", font=("Roboto", 20, "bold"), text_color="white").pack(side="left", padx=20, pady=15)
        ctk.CTkButton(self.top_bar, text="Déconnexion", width=100, height=30, command=self.show_login_screen, fg_color="#ef4444", hover_color="#dc2626").pack(side="right", padx=20, pady=15)

        # Main Container
        self.main_container = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.main_container.pack(fill="both", expand=True, padx=30, pady=30)

        # 1. Statistics Cards
        self.stats_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.stats_frame.pack(fill="x", pady=(0, 30))
        self.lbl_balance = self.create_stat_card(self.stats_frame, "Solde Total", "0.00 €", "#3b82f6")
        self.lbl_income = self.create_stat_card(self.stats_frame, "Total Revenus", "0.00 €", "#10b981")
        self.lbl_expense = self.create_stat_card(self.stats_frame, "Total Dépenses", "0.00 €", "#ef4444")
# 2. Formulaire d'ajout
        self.form_frame = ctk.CTkFrame(self.main_container, corner_radius=15)
        self.form_frame.pack(fill="x", pady=(0, 30), padx=10)

        ctk.CTkLabel(self.form_frame, text="Ajouter une transaction", font=("Roboto", 18, "bold")).pack(pady=15)

        self.entry_amount = ctk.CTkEntry(self.form_frame, placeholder_text="Montant (ex: 50.5)", width=200)
        self.entry_amount.pack(pady=5)

        self.entry_cat = ctk.CTkComboBox(self.form_frame, values=["Alimentation", "Loyer", "Loisirs", "Salaire", "Transport", "Santé"], width=200)
        self.entry_cat.pack(pady=5)

        self.entry_type = ctk.CTkSegmentedButton(self.form_frame, values=["expense", "income"], width=200)
        self.entry_type.set("expense")
        self.entry_type.pack(pady=5)

        self.entry_desc = ctk.CTkEntry(self.form_frame, placeholder_text="Description", width=200)
        self.entry_desc.pack(pady=5)

        self.add_btn = ctk.CTkButton(self.form_frame, text="Ajouter", command=self.handle_add_transaction, width=200, height=40, font=("Roboto", 14, "bold"))
        self.add_btn.pack(pady=20)
# 3. Historique des Transactions
        self.list_frame = ctk.CTkFrame(self.main_container, corner_radius=15)
        self.list_frame.pack(fill="both", expand=True, padx=10)

        ctk.CTkLabel(self.list_frame, text="Historique des opérations", font=("Roboto", 18, "bold")).pack(pady=15)

        # Configuration du tableau (Treeview)
        columns = ("id", "date", "category", "amount", "type", "desc")
        self.tree = ttk.Treeview(self.list_frame, columns=columns, show="headings")

        # Style pour le tableau
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b", borderwidth=0)
        style.map("Treeview", background=[('selected', '#3b82f6')])

        self.tree.heading("id", text="ID")
        self.tree.heading("date", text="Date")
        self.tree.heading("category", text="Catégorie")
        self.tree.heading("amount", text="Montant")
        self.tree.heading("type", text="Type")
        self.tree.heading("desc", text="Description")

        self.tree.column("id", width=50, anchor="center")
        self.tree.column("date", width=100, anchor="center")
        self.tree.column("category", width=150, anchor="center")
        self.tree.column("amount", width=100, anchor="center")
        self.tree.column("type", width=100, anchor="center")
        self.tree.column("desc", width=300, anchor="w")

        self.tree.pack(pady=10, padx=10, fill="both", expand=True)

        self.del_btn = ctk.CTkButton(self.list_frame, text="Supprimer sélection", fg_color="#ef4444", hover_color="#dc2626", command=self.delete_selected)
        self.del_btn.pack(pady=15)

        # Charger les données initiales
        self.update_stats()
        self.update_transaction_list()

    # --- LOGIQUE METIER ---

    def update_stats(self):
        try:
            response = requests.get(f"{self.API_URL}/stats/{self.current_user_id}", timeout=5)
            if response.status_code == 200:
                stats = response.json()
                self.lbl_balance.configure(text=f"{stats['balance']:.2f} €")
                self.lbl_income.configure(text=f"{stats['total_income']:.2f} €")
                self.lbl_expense.configure(text=f"{stats['total_expense']:.2f} €")
        except: pass

    def update_transaction_list(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        try:
            response = requests.get(f"{self.API_URL}/transactions/{self.current_user_id}", timeout=5)
            if response.status_code == 200:
                for t in response.json():
                    self.tree.insert("", "end", values=(t['id'], t['date'], t['category'], t['amount'], t['type'], t['description']))
        except: pass

    def handle_add_transaction(self):
        amount = self.entry_amount.get()
        category = self.entry_cat.get()
        trans_type = self.entry_type.get()
        description = self.entry_desc.get()
        date = datetime.now().strftime("%Y-%m-%d")

        if not amount or not category:
            messagebox.showwarning("Attention", "Le montant et la catégorie sont obligatoires")
            return

        try:
            payload = {"amount": float(amount), "category": category, "date": date, "description": description, "type": trans_type}
            response = requests.post(f"{self.API_URL}/transactions", json=payload, params={"user_id": self.current_user_id}, timeout=5)
            if response.status_code == 200:
                messagebox.showinfo("Succès", "Transaction ajoutée !")
                self.entry_amount.delete(0, 'end')
                self.entry_desc.delete(0, 'end')
                self.update_stats()
                self.update_transaction_list()
            else:
                messagebox.showerror("Erreur", "Erreur lors de l'ajout")
        except ValueError:
            messagebox.showerror("Erreur", "Le montant doit être un nombre")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur : {e}")

    def delete_selected(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Attention", "Veuillez sélectionner une transaction")
            return
        trans_id = self.tree.item(selected[0])['values'][0]
        try:
            response = requests.delete(f"{self.API_URL}/transactions/{trans_id}", params={"user_id": self.current_user_id}, timeout=5)
            if response.status_code == 200:
                self.update_stats()
                self.update_transaction_list()
                messagebox.showinfo("Succès", "Transaction supprimée")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur : {e}")

if __name__ == "__main__":
    app = BudgetApp()
    app.mainloop()