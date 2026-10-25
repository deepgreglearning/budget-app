### 🆔 ID: ISSUE-005
**Titre :** Conflit de types de données sur les montants financiers
**Date :** 2026-10-21
**Sévérité :** Majeur
**Statut :** Résolu

#### 📝 Description
Erreurs de calculs arrondis lors de l'addition de transactions (ex: 0.1 + 0.2 = 0.30000000000000004).

#### 🔍 Analyse
Utilisation du type `float` pour les montants financiers. Les nombres à virgule flottante en informatique causent des erreurs de précision binaire.

#### ✅ Résolution
Migration vers le type `Decimal` pour tous les calculs financiers et stockage sous forme de chaîne ou d'entiers (centimes) pour garantir une précision absolue.
Lien utile : [Python Decimal documentation](https://docs.python.org/3/library/decimal.html)

#### 💡 Leçons apprises
Ne jamais utiliser de float pour de l'argent.
---
