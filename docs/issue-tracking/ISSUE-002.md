### 🆔 ID: ISSUE-002
**Titre :** Erreur de connexion à la base de données SQLite (Threading)
**Date :** 2026-10-15
**Sévérité :** Majeur
**Statut :** Résolu

#### 📝 Description
Le serveur plantait aléatoirement avec une erreur `sqlite3.ProgrammingError: SQLite objects created in a thread can only be used in that same thread` lors de requêtes simultanées.

#### 🔍 Analyse
FastAPI utilise des threads asynchrones. Par défaut, SQLite interdit l'utilisation d'une même connexion sur plusieurs threads pour éviter la corruption des données.

#### ✅ Résolution
Modification de la fonction de connexion en ajoutant le paramètre `check_same_thread=False`. Initialement, j'avais tenté d'utiliser un verrou (lock), mais cela ralentissait trop l'API. La solution `check_same_thread=False` est la méthode recommandée pour FastAPI avec SQLite.
Lien utile : [FastAPI Docs - SQL Databases](https://fastapi.tiangolo.com/tutorial/sql-databases/)

#### 💡 Leçons apprises
L'asynchronisme change la gestion des ressources. Il faut vérifier la compatibilité multi-thread des pilotes de base de données.
---
