import pandas as pd


data = {
    "Patient_ID": [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008],
    "Nom": ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"],
    "Prenom": ["John", "Emily", "Michael", "Sarah", "David", "Sophia", "James", "Emma"],
    "Age": [45, 32, 28, 60, 50, 39, 42, 25],
    "Sexe": ["M", "F", "M", "F", "M", "F", "M", "F"],
    "Service": ["Cardiology", "Neurology", "Orthopedics", "Pediatrics",
                "Cardiology", "Neurology", "Orthopedics", "Pediatrics"],
    "Date_Admission": ["2026-01-10", "2026-01-12", "2026-01-15", "2026-01-08",
                       "2026-01-11", "2026-01-14", "2026-01-13", "2026-01-16"],
    "Date_Sortie": ["2026-01-15", "2026-01-18", "2026-01-20", "2026-01-12",
                    "2026-01-16", "2026-01-19", "2026-01-17", "2026-01-22"],
    "Durée_Jours": [5, 6, 5, 4, 5, 5, 4, 6],
    "Médecin": ["Dr. Lee", "Dr. Kim", "Dr. Patel", "Dr. Chen", "Dr. Lee", "Dr. Kim", "Dr. Patel", "Dr. Chen"],
    "Frais_USD": [2500, 3200, 2800, 1800, 2600, 3100, 2700, 1900]
}


df = pd.DataFrame(data)


df.to_excel("hospital_data.xlsx", index=False)
print("✅ Fichier 'hospital_data.xlsx' créé avec succès !")
