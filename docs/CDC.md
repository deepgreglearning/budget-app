# 📄 Cahier des Charges : Application de Gestion de Budget (Budget Master)

## 1. Présentation du Projet
**Budget Master** est une application de gestion financière personnelle conçue pour permettre à plusieurs utilisateurs de suivre leurs revenus et dépenses de manière sécurisée et centralisée. L'application adopte une architecture client-serveur pour permettre l'accès aux données à distance.

## 2. Objectifs Principaux
- **Centralisation** : Accéder à ses données financières depuis n'importe quel poste client.
- **Multi-utilisateurs** : Gestion isolée et sécurisée des données pour chaque compte utilisateur.
- **Simplicité d'utilisation** : Interface moderne et intuitive pour une saisie rapide.
- **Analyse** : Outils de suivi pour optimiser la gestion budgétaire.

## 3. Spécifications Fonctionnelles

### 3.1 Gestion des Utilisateurs (Authentification)
- **Inscription** : Création de compte avec nom d'utilisateur, email et mot de passe.
- **Connexion** : Accès sécurisé via identifiants.
- **Sécurité** : Hachage des mots de passe côté serveur et gestion de sessions (Tokens).

### 3.2 Gestion du Budget
- **Saisie des Transactions** : 
    - Ajout de transactions (Montant, Catégorie, Date, Description).
    - Distinction entre Revenus et Dépenses.
- **Suivi et Modification** : 
    - Consultation de l'historique des transactions.
    - Modification ou suppression d'une opération.
- **Catégorisation** : Gestion de catégories personnalisées pour mieux segmenter les dépenses.

### 3.3 Outils et Fonctionnalités Avancées
- **Tableau de Bord (Dashboard)** : 
    - Affichage du solde total actuel.
    - Visualisation des dépenses totales vs revenus totaux.
- **Analyse et Rapports** : 
    - Calcul automatique du budget restant par catégorie.
    - (Évolution future) Graphiques de répartition des dépenses.

## 4. Spécifications Techniques

### 4.1 Architecture
- **Type** : Architecture Client-Serveur.
- **Client** : Application Desktop développée en **Python** avec la bibliothèque **CustomTkinter** (Interface moderne).
- **Serveur (Backend)** : API REST développée en **Python** (FastAPI ou Flask).
- **Base de Données** : Base de données distante (PostgreSQL ou MongoDB) pour le stockage centralisé.

### 4.2 Flux de Données
- Le client communique avec le serveur via des requêtes HTTP (JSON).
- L'authentification est gérée par un système de tokens pour sécuriser les échanges.

## 5. Contraintes et Exigences
- **Confidentialité** : Les données d'un utilisateur ne doivent en aucun cas être accessibles par un autre utilisateur.
- **Disponibilité** : Le serveur doit être accessible à distance.
- **Ergonomie** : L'interface doit être responsive et intuitive.

## 6. Livrables attendus
- Code source du serveur (API).
- Code source de l'application client (CustomTkinter).
- Documentation technique et guide d'installation.
- Fiches de suivi des problèmes rencontrés et résolus.
