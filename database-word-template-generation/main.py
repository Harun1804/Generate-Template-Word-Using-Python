# main.py

from generator import generate_doc
from queries import (tables_data)

if __name__ == "__main__":
    generate_doc(tables_data, output_file="laporan.docx")