import csv
import json
import os

csv_file_path = "E:\Intern_Vissoft\Week_1\pokemon.csv"
output_folder = "E:\Intern_Vissoft\Week_1\pokemon_json_files"

os.makedirs(output_folder, exist_ok=True)

def create_pokemon_json():

    try:
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pokemon_id = row['id']
                pokemon_name = row['Name']
                json_file_name = os.path.join(output_folder, f"{pokemon_id}_{pokemon_name}.json")
                
                with open(json_file_name, 'w', encoding='utf-8') as json_file:
                    json.dump(row, json_file, indent=4, ensure_ascii=False)

        print(f"JSON files have been created in the folder: {output_folder}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    create_pokemon_json()