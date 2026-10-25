### 🆔 ID: ISSUE-007
**Titre :** Deadlock lors de l'insertion massive de transactions
**Date :** 2026-10-23
**Sévérité :** Majeur
**Statut :** Résolu

#### 📝 Description
Le serveur se bloquait complètement lors de l'importation d'un fichier CSV de transactions.

#### 🔍 Analyse
Tentative d'ouverture de multiples connexions en écriture simultanées sur SQLite, provoquant un verrouillage global de la base de données (database is locked).

#### ✅ Résolution
Optimisation des insertions via l'utilisation de `executemany` pour regrouper les transactions en une seule transaction SQL, réduisant le nombre de verrous.
Lien utile : [SQLite Locking documentation](https://www.sqlite.org/lock.html)

#### 💡 Leçons apprises
Le traitement par lots (batching) est essentiel pour les opérations d'écriture massives.
---
