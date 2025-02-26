import os, shutil
from pathlib import Path
from zipfile import ZipFile

ROOT_PATH = Path(__file__).parent
PATH_DIR_ZIP = ROOT_PATH / 'aula121_dir_zip'
PATH_ZIP_FILE = ROOT_PATH / 'aula121_compressed.zip'
PATH_UNCOMPRESSED_FILE = ROOT_PATH / 'aula121_uncompressed'

shutil.rmtree(PATH_DIR_ZIP, ignore_errors=True)
Path.unlink(PATH_ZIP_FILE, missing_ok=True)
shutil.rmtree(str(PATH_ZIP_FILE).replace('.zip', ''), ignore_errors=True)
shutil.rmtree(PATH_UNCOMPRESSED_FILE, ignore_errors=True)

PATH_DIR_ZIP.mkdir(exist_ok=True)

def make_files(amt: int, zip_dir: Path):
    for i in range(amt):
        text = f'file_{i}'
        with open(zip_dir / f'{text}.txt', 'w', encoding='utf-8') as file:
            file.write(text)

make_files(10, PATH_DIR_ZIP)

with ZipFile(PATH_ZIP_FILE, 'w') as zip:
    for root, dirs, files in os.walk(PATH_DIR_ZIP):
        for file in files:
            zip.write(os.path.join(root, file), file)

with ZipFile(PATH_ZIP_FILE, 'r') as zip:
    for file in zip.namelist():
        print(file)
        print('    ',zip.read(file))

with ZipFile(PATH_ZIP_FILE, 'r') as zip:
    zip.extractall(PATH_UNCOMPRESSED_FILE)