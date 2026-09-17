20260917-014149.py



from datetime import date

# Demander les informations
nom = input("Entrez votre nom : ")
annee_naissance = int(input("Entrez votre année de naissance : "))

# Récupérer automatiquement l'année actuelle
annee_actuelle = date.today().year

# Calculer l'âge
age = annee_actuelle - annee_naissance

# Afficher le résultat
print(f"Bonjour {nom}, vous avez {age} ans !")