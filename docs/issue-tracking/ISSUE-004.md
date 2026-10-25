### 🆔 ID: ISSUE-004
**Titre :** Fuite de mémoire due à des connexions SQLite non fermées
**Date :** 2026-10-20
**Sévérité :** Majeur
**Statut :** Résolu

#### 📝 Description
Ralentissement progressif du serveur et augmentation de la consommation RAM après plusieurs heures d'utilisation.

#### 🔍 Analyse
Plusieurs fonctions ouvraient des connexions à la base de données sans jamais appeler `.close()`. Les connexions restaient orphelines en mémoire.

#### ✅ Résolution
Mise en place d'un gestionnaire de contexte `with sqlite3.connect()` et création d'un générateur `get_db()` pour garantir la fermeture systématique des connexions, même en cas d'erreur.
Lien utile : [Python SQLite3 documentation](https://docs.python.org/3/library/sqlite3.html)

#### 💡 Leçons apprises
L'utilisation de gestionnaires de contexte est indispensable pour la gestion des ressources externes.
---
