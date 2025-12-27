# 🚀 Spark Project - Loan Analysis

## 📋 Description du Projet

Pipeline complet d'analyse de données avec Apache Spark et MLlib sur les prêts bancaires Lending Club (2007-2014).

### Objectifs
- ✅ Analyse de données volumineuses avec PySpark
- ✅ Jointure de datasets complémentaires
- ✅ Sécurisation des données sensibles
- ✅ Agrégations pour reporting métier
- ✅ Machine Learning avec MLlib
- ✅ Visualisations et insights

## 📊 Datasets

### Source
**Lending Club** - Plateforme américaine de prêts peer-to-peer

### Volume
- **466 285 prêts** (2007-2014)
- **Split en 2 datasets** complémentaires

### Fichiers
1. `borrower_profile.csv` (71 MB) - Profil des emprunteurs
2. `loan_performance.csv` (72 MB) - Performance des prêts

**Clé de jointure** : `id`

Voir [DATA_DESCRIPTION.md](DATA_DESCRIPTION.md) pour détails complets.

## 🛠️ Technologies

- **Apache Spark** (PySpark)
- **MLlib** (Machine Learning)
- **Python 3.13+**
- **Jupyter Notebook**
- **Matplotlib / Seaborn** (Visualisations)

## 📁 Structure du Projet

```
.
├── README.md                    # Ce fichier
├── DATA_DESCRIPTION.md          # Description détaillée des données
├── data/                        # Datasets
│   ├── borrower_profile.csv
│   ├── loan_performance.csv
│   └── split_datasets.py
├── notebooks/                   # Notebooks d'analyse
│   └── spark_loan_analysis.ipynb
└── requirements.txt             # Dépendances Python
```

## 🚀 Installation

```bash
# Cloner le repository
git clone https://github.com/zbelem001/spark_project-loan_analysis.git
cd spark_project-loan_analysis

# Créer un environnement virtuel
python3 -m venv .venv
source .venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## 📓 Workflow du Projet

### 1️⃣ Chargement des données
- Import des 2 CSV dans Spark DataFrames
- Exploration initiale (schema, statistiques)

### 2️⃣ Nettoyage
- Traitement valeurs manquantes
- Conversion des types
- Validation des données

### 3️⃣ Jointure
- Inner join sur `id`
- Dataset unifié pour analyses avancées

### 4️⃣ Sécurisation
- Hashage SHA-256 des identifiants
- Masquage des données sensibles
- Généralisation des revenus

### 5️⃣ Agrégations
- Indicateurs par État
- Taux de défaut par grade
- Tendances temporelles

### 6️⃣ Machine Learning
- Classification : Prédiction des défauts
- Features engineering
- Évaluation du modèle

### 7️⃣ Visualisations
- Distributions et corrélations
- Insights métier
- Graphiques interactifs

## 📈 Analyses Réalisées

- 🎯 Taux de défaut par profil emprunteur
- 📍 Performance géographique (par État)
- 💰 Impact du DTI sur la performance
- 📊 Segmentation des emprunteurs
- 🤖 Prédiction du risque de défaut
- 📉 Analyse de la crise 2008

## 👥 Auteurs

Projet réalisé en binôme - Master Data Analytics Spark  
**2IE** - Semestre 7

## 📅 Date

Décembre 2025

## 📝 Licence

Projet académique - 2IE
