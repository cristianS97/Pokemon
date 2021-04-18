from pathlib import Path
import json

ruta = Path(__file__).resolve().parent

def write_types(types):
    with open(ruta.joinpath('archivos').joinpath('types.json'), 'w') as json_file:
        json.dump(types, json_file, indent=4)