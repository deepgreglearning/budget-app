### 🆔 ID: ISSUE-003
**Titre :** Vulnérabilité de sécurité : Stockage des mots de passe en texte clair
**Date :** 2026-10-18
**Sévérité :** Bloquant
**Statut :** Résolu

#### 📝 Description
Lors de la première version du prototype, les mots de passe étaient enregistrés directement dans la base de données sans aucune transformation.

#### 🔍 Analyse
L'utilisation de texte clair pour les mots de passe est une erreur critique de sécurité. En cas de fuite de la base de données, tous les comptes utilisateurs seraient compromis instantanément.

#### ✅ Résolution
Intégration de la bibliothèque `passlib` avec l'algorithme `bcrypt`. Le système a été modifié pour hacher le mot de passe lors de l'inscription et vérifier le hachage lors de la connexion. L'ancienne table a été purgée pour forcer la création de comptes sécurisés.
Lien utile : [OWASP Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)

#### 💡 Leçons apprises
La sécurité ne doit pas être une option ajoutée à la fin, mais une base dès la première ligne de code.
---
