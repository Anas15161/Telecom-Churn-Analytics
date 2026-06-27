# 📊 Présentation : Prédiction du Churn Telecom
**Horizon Telecom - Projet de Fin d'Études**

---

## 🖥️ Slide 1 : Titre & Introduction
- **Sujet :** Système Intelligent de Prédiction de Résiliation Client.
- **Client :** Horizon Telecom.
- **Réalisé par :** Mohamed Maiski & Amine Tayek.
- **Domaine :** Data Science & Machine Learning.

---

## 🎯 Slide 2 : Contexte & Problématique
- **Le Churn :** Perte de clients au profit de la concurrence.
- **Impact :** Perte directe de revenus et coût d'acquisition élevé.
- **Défi :** Comment identifier proactivement les clients sur le départ ?

---

## 🏁 Slide 3 : Objectifs du Projet
- Développer un modèle prédictif **fiable** et **performant**.
- Fournir une interface **professionnelle** pour les décideurs.
- Permettre des analyses **individuelles** et **en masse** (Batch).

---

## 📊 Slide 4 : Analyse des Données (EDA)
- **Source :** Dataset Telecom (7 043 clients).
- **Variables :** Tenure, Monthly Charges, Contract Type, etc.
- **Observation :** Déséquilibre des classes (74% vs 26%).

---

## 🛠️ Slide 5 : Préparation & Nettoyage
- **Conversion :** Transformation des charges en format numérique.
- **Encodage :** Label Encoding pour les variables catégorielles.
- **Normalisation :** StandardScaler pour uniformiser les échelles.

---

## ⚖️ Slide 6 : Gestion du Déséquilibre
- **Technique :** Utilisation de **SMOTEENN**.
- **Méthode :** Suréchantillonnage (SMOTE) + Nettoyage (ENN).
- **Résultat :** Amélioration radicale de la détection de la classe "Churn".

---

## 🧠 Slide 7 : Modélisation
- **Algorithmes testés :** 
  - Logistic Regression (Baseline).
  - Decision Tree.
  - **Random Forest (Champion).**
  - Gradient Boosting.

---

## 📈 Slide 8 : Résultats & Performances
- **Précision globale :** ~93%.
- **F1-Score :** ~94%.
- **ROC AUC :** 0.96.
- Modèle robuste et généralisable.

---

## 🚀 Slide 9 : Démo - Fonctionnalités Web
- **Interface :** Design moderne Rouge & Blanc (IAM).
- **Sidebar :** 15 exemples pour test immédiat.
- **Analyse Batch :** Import CSV/Excel + Exportation des résultats.
- **Documentation :** Page technique intégrée.

---

## 🏁 Slide 10 : Conclusion
- **Apport :** Outil d'aide à la décision stratégique.
- **Futur :** Intégration de modèles de Deep Learning ou NLP.
- **Fin :** Merci pour votre attention !
