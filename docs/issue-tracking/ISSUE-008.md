### 🆔 ID: ISSUE-008
**Titre :** Erreur de synchronisation des dates (Fuseau horaire)
**Date :** 2026-10-24
**Sévérité :** Mineur
**Statut :** Résolu

#### 📝 Description
Les transactions enregistrées à minuit apparaissaient la veille sur certains postes clients.

#### 🔍 Analyse
L'application utilisait `datetime.now()` qui récupère l'heure locale du serveur. Lors du transfert vers le client, le décalage horaire provoquait un décalage de date.

#### ✅ Résolution
Standardisation de toutes les dates en format UTC (Coordinated Universal Time) côté serveur et conversion en heure locale uniquement lors de l'affichage final côté client.
Lien utile : [Python datetime UTC documentation](https://docs.python.org/3/library/datetime.html#datetime.datetime.utcnow)

#### 💡 Leçons apprises
Toujours stocker les dates en UTC dans une base de données pour garantir la cohérence multi-zone.
---
