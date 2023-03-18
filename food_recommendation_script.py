#!/usr/bin/env python
# coding: utf-8




###...Script for Prefixing food based on their categories and storing them in a list...###


#importing required modules- numpy, pandas, openpyxl- of pandas should be installed, as its needed to handle excel files
import sys
import numpy as np
import pandas as pd

#importing the required excel file named- "function_script.xlsx"
input_file = sys.argv[1]
output_file = sys.argv[2]
main_file = pd.ExcelFile(input_file)

#storing each of the excel sheets from the excel workbook into separate dataframes
SCFA = pd.read_excel(main_file,'SCFA')
Carbohydrate = pd.read_excel(main_file,'Carbohydrate')
Protein = pd.read_excel(main_file,'Protein')
Lipid = pd.read_excel(main_file,'Lipid')
Vitamin = pd.read_excel(main_file,'Vitamin')
Gas_Production = pd.read_excel(main_file,'Gas Production')
Gut_Brain_Axis = pd.read_excel(main_file,'Gut Brain Axis')

#1)-Working on 'SCFA' sheet first

#CATEGORY and PREFIX-
#For each food name in the 'Food' Column, we add a prefix to the food name based on the category in the 'Category' column and make a new column called 'prefix_SCFA_food'- 
#Category	Prefix
#Fruits	F
#Dryfruits and Nuts	N
#Vegetables	V
#Cereals	C
#Pulses and Legumes	P
#Herbs and Spices	H
#Miscellaneous	Mi
#Dairy Products	D
#Seeds	S
#Poultry, Meat and Seafood	M
#Probiotics	B
#Fats and Oils	O 

#creating a new column 'prefix_SCFA_food' containing the foods from 'Food' column with a prefix added to them, after comparison with the 'Catgeory colummn'
SCFA.loc[(SCFA['Category'] == 'Fruits'), 'Prefix_SCFA_food'] = 'F_' + SCFA['Food']
SCFA.loc[(SCFA['Category'] == 'Dryfruits and Nuts'), 'Prefix_SCFA_food'] = 'N_' + SCFA['Food']
SCFA.loc[(SCFA['Category'] == 'Vegetables'), 'Prefix_SCFA_food'] = 'V_' + SCFA['Food']
SCFA.loc[(SCFA['Category'] == 'Cereals'), 'Prefix_SCFA_food'] = 'C_' + SCFA['Food']
SCFA.loc[(SCFA['Category'] == 'Pulses and Legumes'), 'Prefix_SCFA_food'] = 'P_' + SCFA['Food']
SCFA.loc[(SCFA['Category'] == 'Herbs and Spices'), 'Prefix_SCFA_food'] = 'H_' + SCFA['Food']
SCFA.loc[(SCFA['Category'] == 'Miscellaneous'), 'Prefix_SCFA_food'] = 'Mi_' + SCFA['Food']
SCFA.loc[(SCFA['Category'] == 'Dairy Products'), 'Prefix_SCFA_food'] = 'D_' + SCFA['Food']
SCFA.loc[(SCFA['Category'] == 'Seeds'), 'Prefix_SCFA_food'] = 'S_' + SCFA['Food']
SCFA.loc[(SCFA['Category'] == 'Poultry, Meat and Seafood'), 'Prefix_SCFA_food'] = 'M_' + SCFA['Food']
SCFA.loc[(SCFA['Category'] == 'Probiotics'), 'Prefix_SCFA_food'] = 'B_' + SCFA['Food']
SCFA.loc[(SCFA['Category'] == 'Fats and Oils'), 'Prefix_SCFA_food'] = 'F_' + SCFA['Food']

#Creating a new column- 'Actetate_low_yes' for storing those foods from 'Prefix_SCFA_Food' column who have a 'Yes' in the 'Acetate_low' column-
SCFA["Acetate_low_yes"]= SCFA.query('Acetate_low =="Yes"')["Prefix_SCFA_food"]
#Creating a new column- 'Actetate_high_yes' for storing those foods from 'Prefix_SCFA_Food' column who have a 'Yes' in the 'Acetate_high' column-
SCFA["Acetate_high_yes"]= SCFA.query('Acetate_high == "Yes"')["Prefix_SCFA_food"]
#Creating a new column- 'Butyrate_low_yes' for storing those foods from 'Prefix_SCFA_Food' column who have a 'Yes' in the 'Butyrate_low' column-
SCFA["Butyrate_low_yes"]= SCFA.query('Butyrate_low =="Yes"')["Prefix_SCFA_food"]
#Creating a new column- 'Butyrate_high_yes' for storing those foods from 'Prefix_SCFA_Food' column who have a 'Yes' in the 'Butyrate_high' column-
SCFA["Butyrate_high_yes"]= SCFA.query('Butyrate_high =="Yes"')["Prefix_SCFA_food"]
#Creating a new column- 'Propionate_low_yes' for storing those foods from 'Prefix_SCFA_Food' column who have a 'Yes' in the 'Propionate_low' column-
SCFA["Propionate_low_yes"]= SCFA.query('Propionate_low =="Yes"')["Prefix_SCFA_food"]
#Creating a new column- 'Propionate_high_yes' for storing those foods from 'Prefix_SCFA_Food' column who have a 'Yes' in the 'Propionate_high' column-
SCFA["Propionate_high_yes"]= SCFA.query('Propionate_high =="Yes"')["Prefix_SCFA_food"]

#storing the items from 'Acetate_low_yes' into a variable called "ALY"
ALY = SCFA['Acetate_low_yes'].str.cat(sep=',')
#storing the items from 'Acetate_high_yes' into a variable called "AHY"
AHY = SCFA['Acetate_high_yes'].str.cat(sep= ',')
#storing the items from 'Butyrate_low_yes' into a variable called "BLY"
BLY = SCFA['Butyrate_low_yes'].str.cat(sep=',')
#storing the items from 'Butyrate_high_yes' into a variable called "BHY"
BHY = SCFA['Butyrate_high_yes'].str.cat(sep= ',')
#storing the items from 'Propionate_low_yes' into a variable called "PLY"
PLY = SCFA['Propionate_low_yes'].str.cat(sep=',')
#storing the items from 'Propionate_high_yes' into a variable called "PHY"
PHY = SCFA['Propionate_high_yes'].str.cat(sep= ',')

#Storing the 'ALY' variable into the first cell of a new column named 'Acetate_low_Y'
SCFA.loc[0,'Acetate_low_Y'] = ALY
#Storing the 'AHY' variable into the first cell of a new column named 'Acetate_high_Y'
SCFA.loc[0,'Acetate_high_Y']= AHY
#Storing the 'BLY' variable into the first cell of a new column named 'Butyrate_low_Y'
SCFA.loc[0,'Butyrate_low_Y'] = BLY
#Storing the 'BHY' variable into the first cell of a new column named 'Butyrate_high_Y'
SCFA.loc[0,'Butyrate_high_Y']= BHY
#Storing the 'PLY' variable into the first cell of a new column named 'Propionate_low_Y'
SCFA.loc[0,'Propionate_low_Y'] = PLY
#Storing the 'PHY' variable into the first cell of a new column named 'Propionate_high_Y'
SCFA.loc[0,'Propionate_high_Y']= PHY

#2)-Working on 'Protein' sheet

#creating a new column 'prefix_SCFA_food' containing the foods from 'Food' column with a prefix added to them, after comparison with the 'Catgeory colummn'
Protein.loc[(Protein['Category'] == 'Fruits'), 'Prefix_Protein_food'] = 'F_' + Protein['Food']
Protein.loc[(Protein['Category'] == 'Dryfruits and Nuts'), 'Prefix_Protein_food'] = 'N_' + Protein['Food']
Protein.loc[(Protein['Category'] == 'Vegetables'), 'Prefix_Protein_food'] = 'V_' + Protein['Food']
Protein.loc[(Protein['Category'] == 'Cereals'), 'Prefix_Protein_food'] = 'C_' + Protein['Food']
Protein.loc[(Protein['Category'] == 'Pulses and Legumes'), 'Prefix_Protein_food'] = 'P_' + Protein['Food']
Protein.loc[(Protein['Category'] == 'Herbs and Spices'), 'Prefix_Protein_food'] = 'H_' + Protein['Food']
Protein.loc[(Protein['Category'] == 'Miscellaneous'), 'Prefix_Protein_food'] = 'Mi_' + Protein['Food']
Protein.loc[(Protein['Category'] == 'Dairy Products'), 'Prefix_Protein_food'] = 'D_' + Protein['Food']
Protein.loc[(Protein['Category'] == 'Seeds'), 'Prefix_Protein_food'] = 'S_' + Protein['Food']
Protein.loc[(Protein['Category'] == 'Poultry, Meat and Seafood'), 'Prefix_Protein_food'] = 'M_' + Protein['Food']
Protein.loc[(Protein['Category'] == 'Probiotics'), 'Prefix_Protein_food'] = 'B_' + Protein['Food']
Protein.loc[(Protein['Category'] == 'Fats and Oils'), 'Prefix_Protein_food'] = 'F_' + Protein['Food']

#Creating a new column- 'Protein_high_yes' for storing those foods from 'Prefix_Protein_Food' column who have a 'Yes' in the 'High_Quality_Protein' column-
Protein["Protein_high_yes"]= Protein.query('High_Quality_Protein=="Yes"')["Prefix_Protein_food"]
#Creating a new column- 'Protein_low_yes' for storing those foods from 'Prefix_Protein_Food' column who have a 'Low' in the 'Low_Quality_Protein' column-
Protein["Protein_low_yes"]= Protein.query('Low_Quality_Protein== "Low"')["Prefix_Protein_food"]

#storing the items from 'Protein_high_yes' into a variable called "P_H"
P_H= Protein['Protein_high_yes'].str.cat(sep=',')
#storing the items from 'Protein_low_yes' into a variable called "P_L"
P_L= Protein['Protein_low_yes'].str.cat(sep= ',')
#Storing the 'P_H' variable into the first cell of a new column named 'Protein_High_Quality_Y'
Protein.loc[0,'Protein_High_Quality_Y'] = P_H
#Storing the 'P_L' variable into the first cell of a new column named 'Protein_Low_Quality_Y'
Protein.loc[0,'Protein_Low_Quality_Y']= P_L

#3)-Working on 'Carbohydrate' sheet

#creating a new column 'prefix_Starch_food' containing the foods from 'Food' column with a prefix added to them, after comparison with the 'Catgeory colummn'
Carbohydrate.loc[(Carbohydrate['Category'] == 'Fruits'), 'Prefix_Starch_food'] = 'F_' + Carbohydrate['Food']
Carbohydrate.loc[(Carbohydrate['Category'] == 'Dryfruits and Nuts'), 'Prefix_Starch_food'] = 'N_' + Carbohydrate['Food']
Carbohydrate.loc[(Carbohydrate['Category'] == 'Vegetables'), 'Prefix_Starch_food'] = 'V_' + Carbohydrate['Food']
Carbohydrate.loc[(Carbohydrate['Category'] == 'Cereals'), 'Prefix_Starch_food'] = 'C_' + Carbohydrate['Food']
Carbohydrate.loc[(Carbohydrate['Category'] == 'Pulses and Legumes'), 'Prefix_Starch_food'] = 'P_' + Carbohydrate['Food']
Carbohydrate.loc[(Carbohydrate['Category'] == 'Herbs and Spices'), 'Prefix_Starch_food'] = 'H_' + Carbohydrate['Food']
Carbohydrate.loc[(Carbohydrate['Category'] == 'Miscellaneous'), 'Prefix_Starch_food'] = 'Mi_' + Carbohydrate['Food']
Carbohydrate.loc[(Carbohydrate['Category'] == 'Dairy Products'), 'Prefix_Starch_food'] = 'D_' + Carbohydrate['Food']
Carbohydrate.loc[(Carbohydrate['Category'] == 'Seeds'), 'Prefix_Starch_food'] = 'S_' + Carbohydrate['Food']
Carbohydrate.loc[(Carbohydrate['Category'] == 'Poultry, Meat and Seafood'), 'Prefix_Starch_food'] = 'M_' + Carbohydrate['Food']
Carbohydrate.loc[(Carbohydrate['Category'] == 'Probiotics'), 'Prefix_Starch_food'] = 'B_' + Carbohydrate['Food']
Carbohydrate.loc[(Carbohydrate['Category'] == 'Fats and Oils'), 'Prefix_Starch_food'] = 'F_' + Carbohydrate['Food']

#Creating a new column- 'Low_Starch_Yes' for storing those foods from 'Prefix_Starch_Food' column who have a 'Yes' in the 'Low_Starch' column-
Carbohydrate["Low_Starch_Yes"]= Carbohydrate.query('Low_Starch=="Yes"')["Prefix_Starch_food"]
#Creating a new column- 'High_Starch_yes' for storing those foods from 'Prefix_Starch_Food' column who have a 'Yes' in the 'High_Starch' column-
Carbohydrate["High_Starch_Yes"]= Carbohydrate.query('High_Starch== "Yes"')["Prefix_Starch_food"]

#storing the items from 'Low_Starch' into a variable called "L_S"
L_S= Carbohydrate['Low_Starch_Yes'].str.cat(sep=',')
#storing the items from 'High_Starch' into a variable called "H_S"
H_S= Carbohydrate['High_Starch_Yes'].str.cat(sep= ',')
#Storing the 'P_H' variable into the first cell of a new column named 'Protein_High_Quality_Y'
Carbohydrate.loc[0,'Carbohydrate_Low_Starch'] = L_S
#Storing the 'P_L' variable into the first cell of a new column named 'Protein_Low_Quality_Y'
Carbohydrate.loc[0,'Carbohydrate_High_Starch']= H_S

#4)-Working on 'Lipid' sheet

#creating a new column 'prefix_Lipid_food' containing the foods from 'Food' column with a prefix added to them, after comparison with the 'Catgeory colummn'
Lipid.loc[(Lipid['Category'] == 'Fruits'), 'Prefix_Lipid_food'] = 'F_' + Lipid['Food']
Lipid.loc[(Lipid['Category'] == 'Dryfruits and Nuts'), 'Prefix_Lipid_food'] = 'N_' + Lipid['Food']
Lipid.loc[(Lipid['Category'] == 'Vegetables'), 'Prefix_Lipid_food'] = 'V_' + Lipid['Food']
Lipid.loc[(Lipid['Category'] == 'Cereals'), 'Prefix_Lipid_food'] = 'C_' + Lipid['Food']
Lipid.loc[(Lipid['Category'] == 'Pulses and Legumes'), 'Prefix_Lipid_food'] = 'P_' + Lipid['Food']
Lipid.loc[(Lipid['Category'] == 'Herbs and Spices'), 'Prefix_Lipid_food'] = 'H_' + Lipid['Food']
Lipid.loc[(Lipid['Category'] == 'Miscellaneous'), 'Prefix_Lipid_food'] = 'Mi_' + Lipid['Food']
Lipid.loc[(Lipid['Category'] == 'Dairy Products'), 'Prefix_Lipid_food'] = 'D_' + Lipid['Food']
Lipid.loc[(Lipid['Category'] == 'Seeds'), 'Prefix_Lipid_food'] = 'S_' + Lipid['Food']
Lipid.loc[(Lipid['Category'] == 'Poultry, Meat and Seafood'), 'Prefix_Lipid_food'] = 'M_' + Lipid['Food']
Lipid.loc[(Lipid['Category'] == 'Probiotics'), 'Prefix_Lipid_food'] = 'B_' + Lipid['Food']
Lipid.loc[(Lipid['Category'] == 'Fats and Oils'), 'Prefix_Lipid_food'] = 'F_' + Lipid['Food']

#Creating a new column- 'Phospholipid_yes' for storing those foods from 'Prefix_Lipid_Food' column who have a 'Yes' in the 'Phospholipid' column-
Lipid["Phospholipid_Yes"]= Lipid.query('Phospholipid=="Yes"')["Prefix_Lipid_food"]
#Creating a new column- 'Triglyceride_yes' for storing those foods from 'Prefix_Lipid_Food' column who have a 'Yes' in the 'Triglyceride' column-
Lipid["Triglyceride_Yes"]= Lipid.query('Triglyceride== "Yes"')["Prefix_Lipid_food"]
#Creating a new column- 'Cholesterol_yes' for storing those foods from 'Prefix_Lipid_Food' column who have a 'Yes' in the 'Cholesterol' column-
Lipid["Cholesterol_Yes"]= Lipid.query('Cholesterol== "Yes"')["Prefix_Lipid_food"]

#storing the items from 'Phospholipid' into a variable called "P_L"
P_L= Lipid['Phospholipid_Yes'].str.cat(sep=',')
#storing the items from 'Triglyceride_yes' into a variable called "T_l"
T_L= Lipid['Triglyceride_Yes'].str.cat(sep= ',')
#storing the items from 'Cholesterol_yes' into a variable called "C_l"
C_L= Lipid['Cholesterol_Yes'].str.cat(sep= ',')
#Storing the 'P_L' variable into the first cell of a new column named 'Phospholipid_Y'
Lipid.loc[0,'Phospholipid_Y'] = P_L
#Storing the 'T_L' variable into the first cell of a new column named 'Triglyceride_Y'
Lipid.loc[0,'Triglyceride_Y']= T_L
#Storing the 'C_L' variable into the first cell of a new column named 'Cholesterol_Y'
Lipid.loc[0,'Cholesterol_Y']= C_L

#5)-Working on 'Vitamin' sheet

#creating a new column 'prefix_Vitamin_food' containing the foods from 'Food' column with a prefix added to them, after comparison with the 'Catgeory colummn'
Vitamin.loc[(Vitamin['Category'] == 'Fruits'), 'Prefix_Vitamin_food'] = 'F_' + Vitamin['Food']
Vitamin.loc[(Vitamin['Category'] == 'Dryfruits and Nuts'), 'Prefix_Vitamin_food'] = 'N_' + Vitamin['Food']
Vitamin.loc[(Vitamin['Category'] == 'Vegetables'), 'Prefix_Vitamin_food'] = 'V_' + Vitamin['Food']
Vitamin.loc[(Vitamin['Category'] == 'Cereals'), 'Prefix_Vitamin_food'] = 'C_' + Vitamin['Food']
Vitamin.loc[(Vitamin['Category'] == 'Pulses and Legumes'), 'Prefix_Vitamin_food'] = 'P_' + Vitamin['Food']
Vitamin.loc[(Vitamin['Category'] == 'Herbs and Spices'), 'Prefix_Vitamin_food'] = 'H_' + Vitamin['Food']
Vitamin.loc[(Vitamin['Category'] == 'Miscellaneous'), 'Prefix_Vitamin_food'] = 'Mi_' + Vitamin['Food']
Vitamin.loc[(Vitamin['Category'] == 'Dairy Products'), 'Prefix_Vitamin_food'] = 'D_' + Vitamin['Food']
Vitamin.loc[(Vitamin['Category'] == 'Seeds'), 'Prefix_Vitamin_food'] = 'S_' + Vitamin['Food']
Vitamin.loc[(Vitamin['Category'] == 'Poultry, Meat and Seafood'), 'Prefix_Vitamin_food'] = 'M_' + Vitamin['Food']
Vitamin.loc[(Vitamin['Category'] == 'Probiotics'), 'Prefix_Vitamin_food'] = 'B_' + Vitamin['Food']
Vitamin.loc[(Vitamin['Category'] == 'Fats and Oils'), 'Prefix_Vitamin_food'] = 'F_' + Vitamin['Food']

#Creating a new column- 'Vitamin_B2_Yes' for storing those foods from 'Prefix_Vitamin_Food' column who have a 'Yes' in the 'Vitamin_B2' column-
Vitamin["Vitamin_B2_Yes"]= Vitamin.query('Vitamin_B2=="Yes"')["Prefix_Vitamin_food"]
#Creating a new column- 'Vitamin_B7_yes' for storing those foods from 'Prefix_Vitamin_Food' column who have a 'Yes' in the 'Vitamin_B7' column-
Vitamin["Vitamin_B7_Yes"]= Vitamin.query('Vitamin_B7== "Yes"')["Prefix_Vitamin_food"]
#Creating a new column- 'Vitamin_B9_yes' for storing those foods from 'Prefix_Vitamin_Food' column who have a 'Yes' in the 'Vitamin_B9' column-
Vitamin["Vitamin_B9_Yes"]= Vitamin.query('Vitamin_B9== "Yes"')["Prefix_Vitamin_food"]
#Creating a new column- 'Vitamin_B12_yes' for storing those foods from 'Prefix_Vitamin_Food' column who have a 'Yes' in the 'Vitamin_B12' column-
Vitamin["Vitamin_B12_Yes"]= Vitamin.query('Vitamin_B12== "Yes"')["Prefix_Vitamin_food"]
#Creating a new column- 'Vitamin_K_yes' for storing those foods from 'Prefix_Vitamin_Food' column who have a 'Yes' in the 'Vitamin_K' column-
Vitamin["Vitamin_K_Yes"]= Vitamin.query('Vitamin_K== "Yes"')["Prefix_Vitamin_food"]
#storing the items from 'Vitamin_B2_Yes' into a variable called "V_B2"
V_B2= Vitamin['Vitamin_B2_Yes'].str.cat(sep=',')
#storing the items from 'Vitamin_B7_yes' into a variable called "V_B7"
V_B7= Vitamin['Vitamin_B7_Yes'].str.cat(sep= ',')
#storing the items from 'Vitamin_B9_yes' into a variable called "V_B9"
V_B9= Vitamin['Vitamin_B9_Yes'].str.cat(sep= ',')
#storing the items from 'Vitamin_B12_yes' into a variable called "V_B12"
V_B12= Vitamin['Vitamin_B12_Yes'].str.cat(sep= ',')
#storing the items from 'Vitamin_K_yes' into a variable called "V_K"
V_K= Vitamin['Vitamin_K_Yes'].str.cat(sep= ',')

#Storing the 'V_B2' variable into the first cell of a new column named 'Vitamin_B2_Y'
Vitamin.loc[0,'Vitamin_B2_Y'] = V_B2
#Storing the 'V_B7' variable into the first cell of a new column named 'Vitamin_B7_Y'
Vitamin.loc[0,'Vitamin_B7_Y']= V_B7
#Storing the 'V_B9' variable into the first cell of a new column named 'Vitamin_B9_Y'
Vitamin.loc[0,'Vitamin_B9_Y']= V_B9
#Storing the 'V_B12' variable into the first cell of a new column named 'Vitamin_B12_Y'
Vitamin.loc[0,'Vitamin_B12_Y']= V_B12
#Storing the 'V_K' variable into the first cell of a new column named 'Vitamin_K_Y'
Vitamin.loc[0,'Vitamin_K_Y']= V_K

#6)-Working on 'Gut_Brain_Axis' sheet

#creating a new column 'prefix_GBA_food' containing the foods from 'Food' column with a prefix added to them, after comparison with the 'Catgeory colummn'
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Fruits'), 'Prefix_GBA_food'] = 'F_' + Gut_Brain_Axis['Food']
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Dryfruits and Nuts'), 'Prefix_GBA_food'] = 'N_' + Gut_Brain_Axis['Food']
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Vegetables'), 'Prefix_GBA_food'] = 'V_' + Gut_Brain_Axis['Food']
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Cereals'), 'Prefix_GBA_food'] = 'C_' + Gut_Brain_Axis['Food']
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Pulses and Legumes'), 'Prefix_GBA_food'] = 'P_' + Gut_Brain_Axis['Food']
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Herbs and Spices'), 'Prefix_GBA_food'] = 'H_' + Gut_Brain_Axis['Food']
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Miscellaneous'), 'Prefix_GBA_food'] = 'Mi_' + Gut_Brain_Axis['Food']
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Dairy Products'), 'Prefix_GBA_food'] = 'D_' + Gut_Brain_Axis['Food']
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Seeds'), 'Prefix_GBA_food'] = 'S_' + Gut_Brain_Axis['Food']
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Poultry, Meat and Seafood'), 'Prefix_GBA_food'] = 'M_' + Gut_Brain_Axis['Food']
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Probiotics'), 'Prefix_GBA_food'] = 'B_' + Gut_Brain_Axis['Food']
Gut_Brain_Axis.loc[(Gut_Brain_Axis['Category'] == 'Fats and Oils'), 'Prefix_GBA_food'] = 'F_' + Gut_Brain_Axis['Food']

#Creating a new column- 'Gamma_Yes' for storing those foods from 'Prefix_GBA_Food' column who have a 'Yes' in the 'Gamma_Aminobutyric_Acid' column-
Gut_Brain_Axis["Gamma_Yes"]= Gut_Brain_Axis.query('Gamma_Aminobutyric_Acid=="Yes"')["Prefix_GBA_food"]
#Creating a new column- 'Dopamine_Yes' for storing those foods from 'Prefix_GBA_Food' column who have a 'Yes' in the 'Dopamine' column-
Gut_Brain_Axis["Dopamine_Yes"]= Gut_Brain_Axis.query('Dopamine== "Yes"')["Prefix_GBA_food"]
#Creating a new column- 'Serotonin_yes' for storing those foods from 'Prefix_GBA_Food' column who have a 'Yes' in the 'Serotonin' column-
Gut_Brain_Axis["Serotonin_Yes"]= Gut_Brain_Axis.query('Serotonin== "Yes"')["Prefix_GBA_food"]

#storing the items from 'Gamma_Yes' into a variable called "GBA_Gamma"
GBA_Gamma= Gut_Brain_Axis['Gamma_Yes'].str.cat(sep=',')
#storing the items from 'Dopamine_yes' into a variable called "GBA_Dopamine"
GBA_Dopamine= Gut_Brain_Axis['Dopamine_Yes'].str.cat(sep= ',')
#storing the items from 'Serotonin_yes' into a variable called "GBA_Serotonin"
GBA_Serotonin= Gut_Brain_Axis['Serotonin_Yes'].str.cat(sep= ',')
#Storing the 'GBA_Gamma' variable into the first cell of a new column named 'Gamma_Amniobutyric_Acid_Y'
Gut_Brain_Axis.loc[0,'Gamma_Aminobutyric_Acid_Y'] = GBA_Gamma
#Storing the 'GBA_Dopamine' variable into the first cell of a new column named 'Dopamine_Y'
Gut_Brain_Axis.loc[0,'Dopamine_Y']= GBA_Dopamine
#Storing the 'GBA_Serotonin' variable into the first cell of a new column named 'Serotonin_Y'
Gut_Brain_Axis.loc[0,'Serotonin_Y']= GBA_Serotonin

#Storing all the food Increased column, with respect to 'Ammonia' into a new column named 'Ammonia_Increased'..but this code is hard coded.
#So in the next line of code- '0' indicates cell no '0' of the 'increased' column, and the value from that column is getting copied to cell '0' of a new column - 'Ammonia_Increased'
Gas_Production.at[0,'Ammonia_Increased']=Gas_Production.at[0,'Increased']
Gas_Production.at[0,'Ammonia_Decreased']=Gas_Production.at[0,'Decreased']
Gas_Production.at[0,'Hydrogen_Sulphide_Increased']=Gas_Production.at[1,'Increased']
Gas_Production.at[0,'Hydrogen_Sulphide_Decreased']=Gas_Production.at[1,'Decreased']
Gas_Production.at[0,'Methane_Increased']=Gas_Production.at[2,'Increased']
Gas_Production.at[0,'Methane_Decreased']=Gas_Production.at[2,'Decreased']

#Copying the required columns from the required dataframes into a new excelfile called 'food_recommendation_database', in a sheet named 'food_increase_decrease'
cols_SCFA = ['Acetate_low_Y','Acetate_high_Y','Butyrate_low_Y','Butyrate_high_Y','Propionate_low_Y','Propionate_high_Y']
cols_Protein = ['Protein_High_Quality_Y','Protein_Low_Quality_Y']
cols_Carbohydrate = ['Carbohydrate_Low_Starch','Carbohydrate_High_Starch']
cols_Lipid = ['Phospholipid_Y','Triglyceride_Y','Cholesterol_Y']
cols_Vitamin = ['Vitamin_B2_Y','Vitamin_B7_Y','Vitamin_B9_Y', 'Vitamin_B12_Y','Vitamin_K_Y']
cols_Gut_Brain_Axis = ['Gamma_Aminobutyric_Acid_Y','Dopamine_Y','Serotonin_Y']
cols_Gas_Production = ['Ammonia_Increased','Ammonia_Decreased','Hydrogen_Sulphide_Increased','Hydrogen_Sulphide_Decreased','Methane_Increased','Methane_Decreased']
new_df = pd.concat([SCFA[cols_SCFA],Protein[cols_Protein],Carbohydrate[cols_Carbohydrate],Lipid[cols_Lipid],Vitamin[cols_Vitamin],Gut_Brain_Axis[cols_Gut_Brain_Axis],Gas_Production[cols_Gas_Production]],axis=1)                 
new_df.to_excel(output_file,sheet_name= "food_increase_decrease" ,index=False)

###...Done...###







