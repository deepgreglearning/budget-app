### 🆔 ID: ISSUE-006
**Titre :** Erreur de validation d'email lors de l'inscription
**Date :** 2026-10-22
**Sévérité :** Mineur
**Statut : Résolu**

#### 📝 Description
L'application acceptait des adresses email invalides (ex: "test@test") sans erreur.

#### 🔍 Analyse
La validation était faite via une simple vérification de la présence du caractère @, ce qui était insuffisant.

#### ✅ Résolution
Intégration de `Pydantic` avec le type `EmailStr` pour forcer une validation RFC stricte des adresses email dès la réception de la requête.
Lien utile : [Pydantic EmailStr documentation](https://docs.pydantic.dev/latest/usage/types/emails/)

#### 💡 Leçons apprises
Utiliser des bibliothèques de validation éprouvées plutôt que de créer ses propres expressions régulières.
---
