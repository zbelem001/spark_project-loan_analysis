# Description des Datasets - Projet Spark Analytics

## 📋 Vue d'ensemble

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

## 📊 Dataset 1 : `borrower_profile.csv`

### Description
Profil socio-économique et historique de crédit des emprunteurs. Ce dataset permet de comprendre **QUI emprunte** mais ne contient aucune information sur la performance du prêt.

### Dimensions
- **466 285 lignes**
- **20 colonnes**
- **71 MB**

### Colonnes détaillées

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| **id** | INT | 🔑 Identifiant unique du prêt (CLÉ DE JOINTURE) | 1077501 |
| **member_id** | INT | Identifiant unique de l'emprunteur | 1296599 |
| **annual_inc** | FLOAT | Revenu annuel déclaré par l'emprunteur (USD) | 24000.0 |
| **emp_title** | STRING | Intitulé du poste occupé | "Software Engineer", "Teacher" |
| **emp_length** | STRING | Ancienneté dans l'emploi actuel | "10+ years", "< 1 year", "2 years" |
| **home_ownership** | STRING | Statut de propriété du logement | RENT, OWN, MORTGAGE, OTHER |
| **addr_state** | STRING | État de résidence (code à 2 lettres) | CA, NY, TX, FL |
| **zip_code** | STRING | Code postal (3 premiers chiffres) | 945xx, 100xx |
| **dti** | FLOAT | Debt-to-Income ratio : ratio dette/revenu mensuel (%) | 27.65 |
| **delinq_2yrs** | INT | Nombre de retards de paiement (+30 jours) sur 2 ans | 0, 1, 2 |
| **earliest_cr_line** | STRING | Date d'ouverture de la première ligne de crédit | "Jan-1990" |
| **inq_last_6mths** | INT | Nombre de demandes de crédit sur les 6 derniers mois | 1, 0, 3 |
| **open_acc** | INT | Nombre de comptes de crédit ouverts | 3, 10, 24 |
| **pub_rec** | INT | Nombre de registres publics défavorables (faillites, etc.) | 0, 1 |
| **revol_bal** | INT | Solde total du crédit revolving (USD) | 13648 |
| **revol_util** | FLOAT | Taux d'utilisation du crédit revolving (%) | 83.7 |
| **total_acc** | INT | Nombre total de lignes de crédit dans l'historique | 9, 25, 37 |
| **verification_status** | STRING | Statut de vérification du revenu | Verified, Source Verified, Not Verified |
| **purpose** | STRING | Objectif du prêt | debt_consolidation, credit_card, home_improvement |
| **title** | STRING | Titre descriptif du prêt fourni par l'emprunteur | "Debt consolidation", "Car financing" |

---

## 💰 Dataset 2 : `loan_performance.csv`

### Description
Caractéristiques du prêt et historique de performance. Ce dataset décrit le **PRÊT** et son **évolution** mais ne contient pas le profil complet de l'emprunteur.

### Dimensions
- **466 285 lignes**
- **25 colonnes**
- **72 MB**

### Colonnes détaillées

| Colonne | Type | Description | Exemple |
|---------|------|-------------|---------|
| **id** | INT | 🔑 Identifiant unique du prêt (CLÉ DE JOINTURE) | 1077501 |
| **loan_amnt** | INT | Montant du prêt demandé (USD) | 5000, 10000, 35000 |
| **funded_amnt** | INT | Montant total financé (USD) | 5000 |
| **funded_amnt_inv** | FLOAT | Montant financé par les investisseurs (USD) | 4975.0 |
| **term** | STRING | Durée du prêt (mois) | " 36 months", " 60 months" |
| **int_rate** | FLOAT | Taux d'intérêt annuel (%) | 10.65, 15.27 |
| **installment** | FLOAT | Mensualité à payer (USD) | 162.87, 339.31 |
| **grade** | STRING | Note de crédit attribuée (A=meilleur, G=pire) | A, B, C, D, E, F, G |
| **sub_grade** | STRING | Sous-note de crédit | A1, A2, B1, B2, C3, C4 |
| **issue_d** | STRING | Date d'émission du prêt | "Dec-2011", "Jan-2012" |
| **loan_status** | STRING | **⭐ Statut actuel du prêt** | Fully Paid, Charged Off, Current, Default |
| **pymnt_plan** | STRING | Indique si un plan de paiement est en place | n (non), y (oui) |
| **out_prncp** | FLOAT | Principal restant à rembourser (USD) | 0.0, 1523.45 |
| **out_prncp_inv** | FLOAT | Principal restant dû aux investisseurs (USD) | 0.0 |
| **total_pymnt** | FLOAT | **Total payé à ce jour** (USD) | 5863.15 |
| **total_pymnt_inv** | FLOAT | Total payé aux investisseurs (USD) | 5833.84 |
| **total_rec_prncp** | FLOAT | Principal récupéré à ce jour (USD) | 5000.0 |
| **total_rec_int** | FLOAT | **Intérêts récupérés** à ce jour (USD) | 863.16 |
| **total_rec_late_fee** | FLOAT | Frais de retard récupérés (USD) | 0.0, 16.97 |
| **recoveries** | FLOAT | Montants récupérés après défaut (USD) | 0.0 |
| **collection_recovery_fee** | FLOAT | Frais de recouvrement après défaut (USD) | 0.0 |
| **last_pymnt_d** | STRING | Date du dernier paiement reçu | "Jan-2015" |
| **last_pymnt_amnt** | FLOAT | Montant du dernier paiement (USD) | 171.62 |
| **last_credit_pull_d** | STRING | Date de la dernière vérification de crédit | "Jan-2016" |
| **issue_period** | STRING | Période d'émission (même valeur que issue_d) | "Dec-2011" |

---

## 🔗 Clé de jointure

### Colonne commune : `id`
- **Type** : INT
- **Unicité** : Chaque ID est unique (pas de doublons)
- **Type de jointure recommandé** : `INNER JOIN`

### Exemple de jointure Spark
```python
df_joined = df_borrower.join(df_loan, on='id', how='inner')
```

---

## 🎯 Analyses impossibles SANS jointure

Sans réunir les deux datasets, vous **NE POUVEZ PAS** :

❌ **Analyser l'impact du revenu sur le taux de défaut**
- `annual_inc` (borrower) vs `loan_status` (loan)

❌ **Corréler le DTI avec la performance de remboursement**
- `dti` (borrower) vs `total_pymnt`, `loan_status` (loan)

❌ **Étudier la relation stabilité emploi et grade**
- `emp_length` (borrower) vs `grade`, `int_rate` (loan)

❌ **Identifier les profils à risque de défaut**
- Profil complet (borrower) vs `loan_status='Charged Off'` (loan)

❌ **Segmenter les emprunteurs par performance**
- Clustering nécessitant colonnes des deux datasets

❌ **Prédire le risque de défaut (ML)**
- Features des deux datasets nécessaires

---

## 📈 Analyses possibles APRÈS jointure

✅ **Risque de défaut par profil**
- Quel profil d'emprunteur (revenu, DTI, emploi) est plus susceptible de faire défaut ?

✅ **Impact géographique**
- Quels états (addr_state) ont les meilleures/pires performances ?

✅ **Scoring prédictif**
- ML pour prédire loan_status à partir du profil emprunteur

✅ **Optimisation du pricing**
- Relation entre profil emprunteur et taux d'intérêt optimal

✅ **Segmentation client**
- Clustering des emprunteurs selon profil + performance

✅ **Analyse temporelle**
- Impact de la crise 2008 sur les défauts selon profils

---

## 🔒 Données sensibles identifiées

Pour l'étape de sécurisation, les colonnes suivantes seront à protéger :

### À hasher (SHA-256)
- `id` → Pseudonymisation
- `member_id` → Pseudonymisation
- `zip_code` → Données géographiques précises

### À masquer partiellement
- `emp_title` → Métier (peut révéler identité)
- `title` → Description personnelle

### À agréger/généraliser
- `annual_inc` → Créer des tranches de revenus
- `addr_state` → Peut être conservé (niveau agrégé)

---

## 📊 Statistiques clés

### Distribution géographique
Top 5 états attendus : CA (Californie), NY (New York), TX (Texas), FL (Floride), IL (Illinois)

### Période critique
**2008-2009** : Crise financière → taux de défaut élevés

### Grades de crédit
- **A, B** : Emprunteurs premium (faible risque)
- **C, D** : Emprunteurs standard
- **E, F, G** : Emprunteurs à risque élevé

### Statuts de prêt possibles
- **Fully Paid** : Prêt entièrement remboursé ✅
- **Current** : Prêt en cours, paiements à jour
- **Charged Off** : Défaut de paiement ❌
- **Default** : Défaut confirmé
- **Late** : Retards de paiement
- **In Grace Period** : Période de grâce

---

## 🚀 Utilisation pour le projet

1. **Chargement** : Importer les 2 CSV dans Spark
2. **Exploration** : Analyser chaque dataset séparément
3. **Nettoyage** : Traiter valeurs manquantes, formats
4. **Jointure** : Réunir sur `id`
5. **Sécurisation** : Hasher/masquer données sensibles
6. **Agrégations** : Créer indicateurs métier
7. **MLlib** : Prédiction défauts, clustering
8. **Visualisation** : Graphiques insights

---

**Date de création** : 27 décembre 2025  
**Source originale** : Lending Club (2007-2014)  
**Préparation** : Split stratégique par colonnes pour maximiser l'intérêt de la jointure
