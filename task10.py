import csv

def export_pokemon_csv(file_csv, keyword):

    try:
        with open(file_csv, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            matched_pokemons = [row for row in reader if keyword.lower() in row["Name"].lower()]

        if matched_pokemons:
            output_file = f"matched_pokemons_{keyword}.csv"
            with open(output_file, 'w', encoding='utf-8', newline='') as out_file:
                writer = csv.DictWriter(out_file, fieldnames=matched_pokemons[0].keys())
                writer.writeheader()
                writer.writerows(matched_pokemons)
            print(f"Pokemon data has been exported to: {output_file}")
        else:
            print("No Pokemon matched the search.")

    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    file_csv = "E:\Intern_Vissoft\Week_1\pokemon.csv"
    keyword = input("Enter the search keyword: ")
    export_pokemon_csv(file_csv, keyword)