# Spark Project - Loan Analysis

## Description du Projet

Pipeline complet d'analyse de données avec Apache Spark et MLlib sur les prêts bancaires Lending Club (2007-2014).

### Objectifs
- Analyse de données volumineuses avec PySpark
- Jointure de datasets complémentaires
- Sécurisation des données sensibles
- Agrégations pour reporting métier
- Machine Learning avec MLlib
- Visualisations et insights

## Vue d'ensemble des Données

### Source des données
**Lending Club** - Plateforme américaine de prêts peer-to-peer (P2P lending)

### Période couverte
**2007 - 2014** (incluant la crise financière de 2008)

### Zone géographique
**États-Unis** - Tous les états américains
- Dataset couvre l'ensemble du territoire américain
- Colonne `addr_state` contient les codes d'états (CA, NY, TX, FL, etc.)
- Colonne `zip_code` pour la granularité par code postal

### Volume des données
- **466 285 prêts** (lignes)
- **Split en 2 datasets complémentaires** nécessitant une jointure pour analyses complètes

---

## Dataset 1 : borrower_profile.csv

### Description
Profil socio-économique et historique de crédit des emprunteurs. Ce dataset permet de comprendre **QUI emprunte** mais ne contient aucune information sur la performance du prêt.

### Dimensions
- **466 285 lignes**
- **20 colonnes**
- **71 MB**

### Colonnes principales

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| **id** | INT | Identifiant unique du prêt (CLE DE JOINTURE) | 1077501 |
| **member_id** | INT | Identifiant unique de l'emprunteur | 1296599 |
| **annual_inc** | FLOAT | Revenu annuel déclaré par l'emprunteur (USD) | 24000.0 |
| **emp_title** | STRING | Intitulé du poste occupé | "Software Engineer", "Teacher" |
| **emp_length** | STRING | Ancienneté dans l'emploi actuel | "10+ years", "< 1 year" |
| **home_ownership** | STRING | Statut de propriété du logement | RENT, OWN, MORTGAGE |
| **addr_state** | STRING | État de résidence (code à 2 lettres) | CA, NY, TX, FL |
| **zip_code** | STRING | Code postal (3 premiers chiffres) | 945xx, 100xx |
| **dti** | FLOAT | Debt-to-Income ratio : ratio dette/revenu (%) | 27.65 |
| **delinq_2yrs** | INT | Nombre de retards de paiement (+30j) sur 2 ans | 0, 1, 2 |
| **inq_last_6mths** | INT | Demandes de crédit sur les 6 derniers mois | 1, 0, 3 |
| **open_acc** | INT | Nombre de comptes de crédit ouverts | 3, 10, 24 |
| **pub_rec** | INT | Registres publics défavorables (faillites) | 0, 1 |
| **revol_bal** | INT | Solde total du crédit revolving (USD) | 13648 |
| **revol_util** | FLOAT | Taux d'utilisation du crédit revolving (%) | 83.7 |
| **total_acc** | INT | Nombre total de lignes de crédit | 9, 25, 37 |
| **verification_status** | STRING | Statut de vérification du revenu | Verified, Not Verified |
| **purpose** | STRING | Objectif du prêt | debt_consolidation, credit_card |
| **title** | STRING | Titre descriptif du prêt | "Debt consolidation" |

---

## Dataset 2 : loan_performance.csv

### Description
Caractéristiques du prêt et historique de performance. Ce dataset décrit le **PRET** et son **évolution** mais ne contient pas le profil complet de l'emprunteur.

### Dimensions
- **466 285 lignes**
- **25 colonnes**
- **72 MB**

### Colonnes principales

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| **id** | INT | Identifiant unique du prêt (CLE DE JOINTURE) | 1077501 |
| **loan_amnt** | INT | Montant du prêt demandé (USD) | 5000, 10000 |
| **funded_amnt** | INT | Montant total financé (USD) | 5000 |
| **term** | STRING | Durée du prêt (mois) | " 36 months", " 60 months" |
| **int_rate** | FLOAT | Taux d'intérêt annuel (%) | 10.65, 15.27 |
| **installment** | FLOAT | Mensualité à payer (USD) | 162.87 |
| **grade** | STRING | Note de crédit (A=meilleur, G=pire) | A, B, C, D, E, F, G |
| **sub_grade** | STRING | Sous-note de crédit | A1, B2, C3 |
| **issue_d** | STRING | Date d'émission du prêt | "Dec-2011" |
| **loan_status** | STRING | Statut actuel du prêt | Fully Paid, Charged Off, Default |
| **pymnt_plan** | STRING | Plan de paiement en place | n (non), y (oui) |
| **total_pymnt** | FLOAT | Total payé à ce jour (USD) | 5863.15 |
| **total_rec_prncp** | FLOAT | Principal récupéré (USD) | 5000.0 |
| **total_rec_int** | FLOAT | Intérêts récupérés (USD) | 863.16 |
| **total_rec_late_fee** | FLOAT | Frais de retard récupérés (USD) | 0.0, 16.97 |
| **recoveries** | FLOAT | Montants récupérés après défaut (USD) | 0.0 |
| **last_pymnt_d** | STRING | Date du dernier paiement reçu | "Jan-2015" |

---

## Clé de jointure

### Colonne commune : `id`
- **Type** : INT
- **Unicité** : Chaque ID est unique (pas de doublons)
- **Type de jointure recommandé** : `INNER JOIN`

### Exemple de jointure Spark
```python
df_joined = df_borrower.join(df_loan, on='id', how='inner')
```

---

## Analyses impossibles SANS jointure

Sans réunir les deux datasets, vous **NE POUVEZ PAS** :

- **Analyser l'impact du revenu sur le taux de défaut**
  - `annual_inc` (borrower) vs `loan_status` (loan)

- **Corréler le DTI avec la performance de remboursement**
  - `dti` (borrower) vs `total_pymnt`, `loan_status` (loan)

- **Étudier la relation stabilité emploi et grade**
  - `emp_length` (borrower) vs `grade`, `int_rate` (loan)

- **Identifier les profils à risque de défaut**
  - Profil complet (borrower) vs `loan_status='Charged Off'` (loan)

- **Prédire le risque de défaut (ML)**
  - Features des deux datasets nécessaires

---

## Analyses possibles APRES jointure

- **Risque de défaut par profil** : Quel profil d'emprunteur est plus susceptible de faire défaut ?
- **Impact géographique** : Quels états ont les meilleures/pires performances ?
- **Scoring prédictif** : ML pour prédire loan_status à partir du profil
- **Optimisation du pricing** : Relation entre profil et taux d'intérêt optimal
- **Segmentation client** : Clustering des emprunteurs selon profil + performance
- **Analyse temporelle** : Impact de la crise 2008 sur les défauts

---

## Données sensibles identifiées

Pour l'étape de sécurisation :

### A hasher (SHA-256)
- `id`, `member_id` - Pseudonymisation
- `zip_code` - Données géographiques précises

### A masquer partiellement
- `emp_title` - Métier (peut révéler identité)
- `title` - Description personnelle

### A agréger/généraliser
- `annual_inc` - Créer des tranches de revenus

---

## Technologies

- **Apache Spark** (PySpark)
- **MLlib** (Machine Learning)
- **Python 3.13+**
- **Jupyter Notebook**
- **Matplotlib / Seaborn** (Visualisations)

## Structure du Projet

```
.
├── README.md                    # Ce fichier
├── data/                        # Datasets
│   ├── borrower_profile.csv
│   └── loan_performance.csv
├── notebooks/                   # Notebooks d'analyse
│   └── spark_loan_analysis.ipynb
├── output/                      # Résultats exportés
└── requirements.txt             # Dépendances Python
```

## Installation

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

## Workflow du Projet

### 1. Chargement des données
- Import des 2 CSV dans Spark DataFrames
- Exploration initiale (schema, statistiques)

### 2. Nettoyage
- Traitement valeurs manquantes
- Conversion des types
- Validation des données

### 3. Jointure
- Inner join sur `id`
- Dataset unifié pour analyses avancées

### 4. Sécurisation
- Hashage SHA-256 des identifiants
- Masquage des données sensibles
- Généralisation des revenus

### 5. Agrégations
- Indicateurs par État
- Taux de défaut par grade
- Tendances temporelles

### 6. Machine Learning
- Classification : Prédiction des défauts
- Features engineering
- Évaluation du modèle

### 7. Visualisations
- Distributions et corrélations
- Insights métier
- Graphiques interactifs

## Analyses Réalisées

- Taux de défaut par profil emprunteur
- Performance géographique (par État)
- Impact du DTI sur la performance
- Segmentation des emprunteurs
- Prédiction du risque de défaut
- Analyse de la crise 2008

## Statistiques clés

### Distribution géographique
Top 5 états : CA (Californie), NY (New York), TX (Texas), FL (Floride), IL (Illinois)

### Période critique
**2008-2009** : Crise financière - taux de défaut élevés

### Grades de crédit
- **A, B** : Emprunteurs premium (faible risque)
- **C, D** : Emprunteurs standard
- **E, F, G** : Emprunteurs à risque élevé

### Statuts de prêt
- **Fully Paid** : Prêt entièrement remboursé
- **Charged Off** : Défaut de paiement
- **Current** : Prêt en cours, paiements à jour
- **Default** : Défaut confirmé

## Auteurs

Projet réalisé en binôme - Master Data Analytics Spark  
**2IE** - Semestre 7

## Date

Décembre 2025

**Source originale** : Lending Club (2007-2014)

## Licence

Projet académique - 2IE
