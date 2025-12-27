#!/usr/bin/env python3
"""
Script pour diviser le dataset de prêts en deux datasets complémentaires.
Les insights clés ne seront visibles qu'après jointure sur 'id'.
"""

import pandas as pd
import numpy as np
from datetime import datetime

print("=" * 80)
print("SPLIT STRATÉGIQUE DU DATASET PAR COLONNES")
print("=" * 80)

# Chargement du dataset
print("\n[1/5] Chargement du dataset...")
df = pd.read_csv('loan_data_2007_2014.csv', low_memory=False)
print(f"   ✓ {len(df):,} lignes chargées")
print(f"   ✓ {len(df.columns)} colonnes")

# Vérification de la colonne id
if 'id' not in df.columns:
    print("   ⚠ Colonne 'id' manquante, création d'un index...")
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'id'}, inplace=True)

print(f"\n[2/5] Analyse des colonnes...")

# DATASET 1 : PROFIL EMPRUNTEUR (qui est l'emprunteur ?)
# Ces colonnes décrivent QUI emprunte mais pas la PERFORMANCE du prêt
borrower_columns = [
    'id',                    # CLÉ COMMUNE
    'member_id',
    'annual_inc',            # Revenu annuel
    'emp_title',             # Titre d'emploi
    'emp_length',            # Ancienneté emploi
    'home_ownership',        # Statut propriétaire/locataire
    'addr_state',            # État
    'zip_code',              # Code postal
    'dti',                   # Ratio dette/revenu
    'delinq_2yrs',           # Retards de paiement passés
    'earliest_cr_line',      # Première ligne de crédit
    'inq_last_6mths',        # Demandes de crédit récentes
    'open_acc',              # Comptes ouverts
    'pub_rec',               # Enregistrements publics
    'revol_bal',             # Solde crédit revolving
    'revol_util',            # Utilisation crédit revolving
    'total_acc',             # Total comptes crédit
    'verification_status',   # Statut vérification revenu
    'purpose',               # Objectif du prêt
    'title',                 # Titre du prêt
]

# DATASET 2 : CARACTÉRISTIQUES & PERFORMANCE DU PRÊT
# Ces colonnes décrivent le PRÊT et sa PERFORMANCE mais pas le profil complet de l'emprunteur
loan_columns = [
    'id',                    # CLÉ COMMUNE
    'loan_amnt',             # Montant du prêt
    'funded_amnt',           # Montant financé
    'funded_amnt_inv',       # Montant financé par investisseurs
    'term',                  # Durée (36 ou 60 mois)
    'int_rate',              # Taux d'intérêt
    'installment',           # Mensualité
    'grade',                 # Note de crédit (A-G)
    'sub_grade',             # Sous-note
    'issue_d',               # Date d'émission
    'loan_status',           # Statut du prêt (Payé, Défaut, En cours...)
    'pymnt_plan',            # Plan de paiement
    'out_prncp',             # Principal restant
    'out_prncp_inv',         # Principal restant investisseurs
    'total_pymnt',           # Total payé
    'total_pymnt_inv',       # Total payé aux investisseurs
    'total_rec_prncp',       # Principal reçu
    'total_rec_int',         # Intérêts reçus
    'total_rec_late_fee',    # Frais de retard reçus
    'recoveries',            # Récupérations post-défaut
    'collection_recovery_fee', # Frais de recouvrement
    'last_pymnt_d',          # Date dernier paiement
    'last_pymnt_amnt',       # Montant dernier paiement
    'last_credit_pull_d',    # Dernière vérification crédit
]

# Filtrer les colonnes existantes
borrower_columns = [col for col in borrower_columns if col in df.columns]
loan_columns = [col for col in loan_columns if col in df.columns]

print(f"   ✓ Dataset 1 (Profil Emprunteur) : {len(borrower_columns)} colonnes")
print(f"   ✓ Dataset 2 (Prêt & Performance) : {len(loan_columns)} colonnes")

# Création des deux datasets
print(f"\n[3/5] Création des deux datasets...")
df_borrower = df[borrower_columns].copy()
df_loan = df[loan_columns].copy()

print(f"   ✓ df_borrower : {len(df_borrower):,} lignes × {len(df_borrower.columns)} colonnes")
print(f"   ✓ df_loan : {len(df_loan):,} lignes × {len(df_loan.columns)} colonnes")

# Ajout d'une dimension temporelle pour rendre la jointure plus intéressante
print(f"\n[4/5] Ajout d'une clé secondaire temporelle...")
if 'issue_d' in df_loan.columns:
    # Extraire l'année-mois pour créer une dimension temporelle
    df_loan['issue_period'] = df_loan['issue_d']
    print("   ✓ Colonne 'issue_period' ajoutée au dataset prêts")

# Statistiques de validation
print(f"\n[5/5] Export des datasets...")

# Export
df_borrower.to_csv('borrower_profile.csv', index=False)
df_loan.to_csv('loan_performance.csv', index=False)

print(f"   ✓ borrower_profile.csv créé ({len(df_borrower):,} lignes)")
print(f"   ✓ loan_performance.csv créé ({len(df_loan):,} lignes)")

# Résumé des insights possibles uniquement après jointure
print("\n" + "=" * 80)
print("INSIGHTS IMPOSSIBLES SANS JOINTURE :")
print("=" * 80)
print("""
Sans jointure, vous ne pouvez PAS analyser :
  
  ✗ Corrélation entre REVENU (borrower) et TAUX DE DÉFAUT (loan)
  ✗ Impact du DTI (borrower) sur la PERFORMANCE de remboursement (loan)
  ✗ Relation entre STABILITÉ EMPLOI (borrower) et GRADE du prêt (loan)
  ✗ Influence du STATUT PROPRIÉTAIRE (borrower) sur le TAUX D'INTÉRÊT (loan)
  ✗ Prédiction du RISQUE DE DÉFAUT selon profil emprunteur
  ✗ Segmentation des emprunteurs par performance de prêt
  
Après jointure sur 'id', ces analyses deviennent possibles ! 🔑
""")

print("=" * 80)
print("SPLIT TERMINÉ AVEC SUCCÈS !")
print("=" * 80)
print(f"\nClé de jointure : 'id'")
print(f"Type de jointure recommandé : INNER JOIN")
print(f"\nCommande Spark exemple :")
print("  df_joined = df_borrower.join(df_loan, on='id', how='inner')")
