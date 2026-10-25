### 🆔 ID: ISSUE-001
**Titre :** Erreur de module non trouvé lors du lancement du serveur FastAPI
**Date :** 2026-10-12
**Sévérité :** Bloquant
**Statut :** Résolu

#### 📝 Description
Lancement du serveur via `main.py` entraînant une erreur `ModuleNotFoundError: No module named 'fastapi'`. Le problème persistait malgré l'exécution de la commande `pip install`.

#### 🔍 Analyse
Le système possédait plusieurs installations de Python. La commande `pip` installait les modules pour une version différente de celle utilisée pour exécuter le script.

#### ✅ Résolution
Remplacement de la commande `pip install` par `python -m pip install`. Cela garantit que les modules sont installés pour l'interpréteur Python actif.
Lien utile : [Stack Overflow - Pip install not working](https://stackoverflow.com/questions/14142161/how-to-install-python-packages-for-a-specific-python-version)

#### 💡 Leçons apprises
Toujours utiliser `python -m pip` pour éviter les conflits de versions d'environnement sur Windows.
---
