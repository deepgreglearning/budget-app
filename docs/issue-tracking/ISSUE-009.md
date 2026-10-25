### 🆔 ID: ISSUE-009
**Titre :** Injection SQL via le champ de description des transactions
**Date :** 2026-10-25
**Sévérité :** Bloquant
**Statut :** Résolu

#### 📝 Description
Il a été constaté qu'en saisissant certains caractères spéciaux dans le champ description, il était possible de modifier d'autres transactions.

#### 🔍 Analyse
Utilisation de f-strings pour construire les requêtes SQL au lieu de requêtes paramétrées. Cela permettait l'injection de commandes SQL malveillantes.

#### ✅ Résolution
Remplacement systématique de toutes les requêtes formatées par des requêtes paramétrées (utilisation du marqueur `?` avec sqlite3). Cette méthode assure que les entrées utilisateur sont traitées comme des données et non comme du code exécutable.
Lien utile : [SQLite Parameterized Queries](https://www.sqlite.org/lang_value.html)

#### 💡 Leçons apprises
Ne jamais concaténer des entrées utilisateur directement dans une requête SQL.
---
