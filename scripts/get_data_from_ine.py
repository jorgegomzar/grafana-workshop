import csv
import requests
from pathlib import Path
from tqdm import tqdm

INE_MONTH_MAPPINGS = {
    "enero": 1,
    "febrero": 2,
    "marzo": 3,
    "abril": 4,
    "mayo": 5,
    "junio": 6,
    "julio": 7,
    "agosto": 8,
    "septiembre": 9,
    "octubre": 10,
    "noviembre": 11,
    "diciembre": 12,
}
INE_URL = "https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/56934.csv?nocab=1"
DATE_COLUMN = "Periodo"
NUMBER_COLUMN = "Total"

data_csv_path = Path(__file__).parent.parent / "nginx/data.csv"
data_csv_tmp_path = Path(str(data_csv_path.absolute()) + ".tmp")

# Download the CSV into a temp file
data_csv_text = requests.get(INE_URL).text
with data_csv_tmp_path.open(mode="wt") as f:
    f.write(data_csv_text.replace("ï»¿", ""))

# Clean data
with (
    data_csv_tmp_path.open() as f,
    data_csv_path.open(mode="wt") as f2
):
    reader = csv.DictReader(f, delimiter=";")
    writer = csv.DictWriter(
        f2,
        delimiter=";",
        fieldnames=[
            "Edad simple", "Sexo", "Periodo", "Total"
        ],
    )
    writer.writeheader()

    for row in tqdm(reader):
        # we don't want rows with empty numbers
        if not (ine_number := row[NUMBER_COLUMN]):
            continue

        # we clean spanish dates + spanish integers
        ine_date = row[DATE_COLUMN]
        date_parts = [
            part
            for part in ine_date.split()
            if part != "de"
        ]
        ok_date = f"{date_parts[2]}-{INE_MONTH_MAPPINGS[date_parts[1]]:02d}-{int(date_parts[0]):02d}"
        ok_number = ine_number.replace(".", "")

        row[DATE_COLUMN] = ok_date
        row[NUMBER_COLUMN] = ok_number

        writer.writerow(row)

data_csv_tmp_path.unlink(missing_ok=True)
print("Done")
