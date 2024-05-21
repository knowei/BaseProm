import pandas as pd


file_path = r'./demo.xlsx'
df = pd.read_excel(file_path, sheet_name="Sheet1")


assert 'PR' in df.columns and 'CITY' in df.columns and 'COUNTY' in df.columns and 'TOWN' in df.columns and '2022' in df.columns


grouped = df.groupby(['CITY', 'COUNTY']).apply(lambda x: list(zip(x['TOWN'], x['2022'])))

output_file = r'./output.txt'
with open(output_file, 'w') as f:
    for (city, county), data in grouped.items():
        town_2022_pairs = [(town, year) for town, year in data]
        f.write(f"CITY: {city}, COUNTY: {county}\n")
        for pair in town_2022_pairs:
            f.write(f" {pair[0]} {pair[1]}\n")
        f.write("\n")

