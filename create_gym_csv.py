import pandas as pd


data = {
    "ID_Membre": [101, 102, 103, 104, 105, 106, 107, 108],
    "Nom": ["El Amrani", "Benali", "Kadiri", "Chraibi", "Saidi", "El Idrissi", "Bouaziz", "Hafidi"],
    "Prenom": ["Hajar", "Omar", "Sara", "Mehdi", "Imane", "Youssef", "Ali", "Salma"],
    "Age": [20, 28, 24, 35, 31, 22, 27, 30],
    "Sexe": ["F", "M", "F", "M", "F", "M", "M", "F"],
    "Abonnement": ["Premium", "Standard", "Premium", "Basic", "Standard", "Premium", "Standard", "Basic"],
    "Date_Inscription": ["2024-06-12", "2023-11-03", "2024-01-20", "2022-09-15",
                         "2023-05-27", "2024-03-02", "2023-07-10", "2024-01-05"],
    "Seances_Mois": [18, 12, 20, 6, 10, 22, 14, 8],
    "Poids_kg": [58, 82, 65, 90, 70, 75, 68, 62],
    "Taille_cm": [165, 178, 170, 180, 168, 175, 172, 167],
    "Calories_Brulees": [4200, 3100, 4600, 1800, 2900, 5100, 3500, 2700],
    "Coach": ["Yassine", "Amina", "Yassine", "Karim", "Amina", "Karim", "Yassine", "Amina"]
}


df = pd.DataFrame(data)


df.to_csv("gym_data.csv", index=False, encoding="utf-8")
print("✅ Fichier 'gym_data.csv' créé avec succès !")
