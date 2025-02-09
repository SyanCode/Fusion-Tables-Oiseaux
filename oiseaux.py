import csv
import os

def read_csv_table(filename):
    """Safely read a CSV file and return its contents."""
    try:
        with open(
            file     = filename,
            mode     = "r",
            encoding = "utf-8-sig"
        ) as f:
            return list(csv.DictReader(f, delimiter = ","))
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return []
    except Exception as e:
        print(f"Error reading {filename}: {e}")
        return []

def fusionOiseau(ligneA, ligneB):
    '''In : ligneA la table 1 et ligneB de la table 4
    Out : le dictionnaire fusion'''
    return {
        "nom"     : ligneA["nom"],
        "couleur1": ligneA["couleur1"],
        "couleur2": ligneB["couleur2"]
    }

def main():
    # List of input files
    file_names = [
        "Oiseaux1.csv",
        "Oiseaux2.csv",
        "couleur2.csv"
    ]

    # Read all tables
    tables = {}
    for nb, name in enumerate(file_names, start=1):
        tables[nb] = read_csv_table(name)
        if not tables[nb]:
            print(f"Skipping processing due to error in {name}")
            return

    # Combine first two tables
    table12 = tables[1] + tables[2]

    # Write first output file
    with open("Oiseaux3.csv", "w", newline='', encoding='utf-8') as sortie:
        objet = csv.DictWriter(sortie, ['nom', 'couleur1'])
        objet.writeheader()
        objet.writerows(table12)

    # Optimize join using dictionary for faster lookup
    table3_dict = {ligne['nom']: ligne for ligne in tables[3]}
    
    # Perform join
    jointureOiseaux = [
        fusionOiseau(ligneA, table3_dict[ligneA['nom']])
        for ligneA in table12
        if ligneA['nom'] in table3_dict
    ]

    # Write final output file
    with open("bilan_oiseaux.csv", "w", newline='', encoding='utf-8') as sortie:
        objet = csv.DictWriter(sortie, ['nom', 'couleur1', 'couleur2'])
        objet.writeheader()
        objet.writerows(jointureOiseaux)

    print("Processing complete. Check Oiseaux3.csv and bilan_oiseaux.csv")

if __name__ == "__main__":
    main()