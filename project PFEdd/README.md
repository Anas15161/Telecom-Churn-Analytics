# 📡 Telecom Customer Churn Prediction - Horizon Telecom

![Horizon Telecom](static/horizon_logo.png)

## 📝 Présentation du Projet
Ce projet de fin d'études (PFE) vise à développer une solution intelligente pour la prédiction de la perte de clients (Churn) pour **Horizon Telecom**. En utilisant des algorithmes d'apprentissage automatique, l'application identifie les clients susceptibles de résilier leur contrat, permettant ainsi à l'entreprise de prendre des mesures préventives.

## 🚀 Fonctionnalités Clés
- **Prédiction Individuelle :** Formulaire interactif pour tester un client spécifique.
- **Analyse par Lot (Batch) :** Importation de fichiers CSV/Excel pour traiter des centaines de clients simultanément.
- **Menu des Exemples :** Sidebar dynamique permettant de charger des profils réels du dataset pour démonstration.
- **Exportation des Résultats :** Téléchargement des prédictions au format CSV.
- **Documentation Intégrée :** Page détaillée expliquant le pipeline Data Science (EDA, SMOTEENN, Modélisation).

## 🛠️ Stack Technique
- **Backend :** Flask (Python 3.14)
- **Machine Learning :** Scikit-Learn (Random Forest, SMOTEENN)
- **Frontend :** HTML5, CSS3 (Flexbox/Animations), JavaScript (Vanilla)
- **Data :** Pandas, NumPy, Pickle

## 📋 Installation et Lancement

1. **Cloner le projet :**
   ```bash
   git clone <url-du-repo>
   cd "project PFE"
   ```

2. **Activer l'environnement virtuel :**
   ```bash
   source venv/bin/activate
   ```

3. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Lancer le serveur :**
   ```bash
   python app.py
   ```
   L'application sera accessible sur `http://127.0.0.1:5000`.

## 🧠 Pipeline de Données
Le projet suit une méthodologie rigoureuse :
1. **Analyse Exploratoire (EDA) :** Visualisation des corrélations et tendances.
2. **Nettoyage :** Gestion des valeurs manquantes et conversion des types.
3. **Ingénierie des caractéristiques :** Sélection des 10 variables les plus influentes.
4. **Équilibrage :** Application de **SMOTEENN** pour gérer le déséquilibre des classes.
5. **Modélisation :** Comparaison de modèles (Logistic Regression, Random Forest, etc.) et sauvegarde du meilleur candidat.

## 👥 Auteurs
- **Anas Haddou**
- **Amine Tayek**

---
*Projet réalisé dans le cadre d'un PFE au département Data Science.*
