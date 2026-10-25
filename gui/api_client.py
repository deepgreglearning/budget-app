import requests

class APIClient:
    def __init__(self):
        self.base_url = "http://127.0.0.1:8000"

    def register(self, username, email, password):
        try:
            response = requests.post(f"{self.base_url}/register",
                                     json={"username": username, "email": email, "password": password},
                                     timeout=5)
            return response.status_code == 201, response.json().get("detail", "Erreur") if response.status_code != 201 else "Succès"
        except requests.exceptions.ConnectionError:
            return False, "Le serveur est injoignable."
        except Exception as e:
            return False, str(e)

    def login(self, username, password):
        try:
            response = requests.post(f"{self.base_url}/login",
                                     json={"username": username, "password": password},
                                     timeout=5)
            if response.status_code == 200:
                return True, response.json()
            return False, response.json().get("detail", "Erreur de connexion")
        except requests.exceptions.ConnectionError:
            return False, "Le serveur est injoignable."
        except Exception as e:
            return False, str(e)

    def get_stats(self, user_id):
        try:
            response = requests.get(f"{self.base_url}/stats/{user_id}", timeout=5)
            return response.json() if response.status_code == 200 else None
        except:
            return None

    def add_transaction(self, user_id, amount, category, date, description, type):
        try:
            response = requests.post(f"{self.base_url}/transactions",
                                     json={"amount": amount, "category": category, "date": date, "description": description, "type": type},
                                     params={"user_id": user_id}, timeout=5)
            return response.status_code == 200, response.json().get("message", "Erreur")
        except:
            return False, "Erreur de connexion"

    def get_transactions(self, user_id):
        try:
            response = requests.get(f"{self.base_url}/transactions/{user_id}", timeout=5)
            return response.json() if response.status_code == 200 else []
        except:
            return []

    def delete_transaction(self, transaction_id, user_id):
        try:
            response = requests.delete(f"{self.base_url}/transactions/{transaction_id}",
                                      params={"user_id": user_id}, timeout=5)
            return response.status_code == 200, response.json().get("message", "Erreur")
        except:
            return False, "Erreur de connexion"
