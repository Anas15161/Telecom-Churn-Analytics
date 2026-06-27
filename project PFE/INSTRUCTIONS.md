# 🚀 Guide de Test et de Lancement du Projet PFE

Ce document contient toutes les instructions nécessaires pour installer, lancer et tester l'application de prédiction du Churn Client de Maroc Telecom sur votre machine.

---

## 📋 Prérequis

Avant de commencer, assurez-vous d'avoir installé sur votre système :
* **Python** (version 3.10, 3.11 ou supérieure)
* **pip** (gestionnaire de paquets Python)

---

## 🛠️ Étape 1 : Préparation de l'environnement virtuel

Pour éviter tout conflit avec d'autres paquets Python installés sur votre ordinateur, il est fortement recommandé de créer un nouvel environnement virtuel.

1. Ouvrez un terminal dans le dossier racine du projet (`project PFE`).
2. Créez un environnement virtuel nommé `env` :
   ```bash
   # Sur Linux/macOS
   python3 -m venv env

   # Sur Windows
   python -m venv env
   ```
3. Activez l'environnement virtuel :
   ```bash
   # Sur Linux/macOS
   source env/bin/activate

   # Sur Windows (Command Prompt)
   env\Scripts\activate

   # Sur Windows (PowerShell)
   .\env\Scripts\Activate.ps1
   ```

---

## 📦 Étape 2 : Installation des dépendances

Une fois l'environnement activé, installez toutes les bibliothèques requises répertoriées dans le fichier `requirements.txt` :
```bash
pip install -r requirements.txt
```

---

## 🚀 Étape 3 : Lancement de l'application Flask

Démarrez le serveur de développement local :
```bash
python app.py
```

L'application est maintenant en ligne ! Ouvrez votre navigateur Web et accédez à l'adresse suivante :
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 🧪 Étape 4 : Guide de test de l'application

Une fois sur l'interface de l'application, voici les deux méthodes pour tester la prédiction :

### 1. Test Individuel (Formulaire interactif)
* Sur la page d'accueil, sous l'onglet **Individuel**, remplissez les champs concernant le client (ancienneté, services souscrits comme l'assistance technique, charges mensuelles, type de contrat, etc.).
* Cliquez sur **Prédire**.
* Le système affichera immédiatement si le client est susceptible de résilier (**Churn**) ou s'il restera fidèle.
* *Astuce : Vous pouvez utiliser les profils d'exemples dans la barre latérale pour pré-remplir le formulaire en un clic.*

### 2. Test par Lot (Batch Prediction)
* Allez sur l'onglet **Batch (CSV/Excel)**.
* Cliquez sur la zone de téléchargement et sélectionnez un fichier CSV contenant des données clients (vous pouvez utiliser le fichier d'exemple disponible dans le projet sous : `data/data-predect.csv`).
* Cliquez sur **Lancer l'analyse batch**.
* L'application affichera un tableau de résultats contenant une nouvelle colonne **Churn Prediction** pour chaque client (avec des badges de couleur vert/rouge).
* Vous pouvez télécharger les résultats de la prédiction en cliquant sur le bouton **Télécharger CSV**.

---

## 📁 Structure des dossiers clés du Projet

* `app.py` : Script principal contenant les routes de l'application Flask et le traitement des prédictions.
* `models/` : Contient le modèle entraîné (`random_forest_model.pkl`) et les encodeurs (`label_encoders_and_scaler.pkl`).
* `data/` : Contient le fichier de données d'exemple pour tester la prédiction en lot (`data-predect.csv`).
* `templates/` & `static/` : Code de l'interface utilisateur (HTML, CSS, images).
