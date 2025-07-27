# ---------- main.py ----------
import os
import json
from datetime import datetime
from utils import process_documents
from langdetect import detect

BASE_DIR = "/app"

def detect_language_from_first_pdf_text(pages):
    if pages:
        try:
            return detect(pages[0][1])
        except:
            return "unknown"
    return "unknown"

def process_collection(collection_path):
    input_path = os.path.join(collection_path, "challenge1b_input.json")
    output_path = os.path.join(collection_path, "challenge1b_output.json")
    pdf_folder = os.path.join(collection_path, "PDFs")

    with open(input_path, 'r', encoding='utf-8') as f:
        input_data = json.load(f)

    # Run document processing
    output = process_documents(input_data, pdf_folder)

    # Try to detect language from the first document (optional)
    first_doc_path = os.path.join(pdf_folder, input_data["documents"][0]["filename"])
    if os.path.exists(first_doc_path):
        import fitz  # PyMuPDF
        doc = fitz.open(first_doc_path)
        first_page = doc[0].get_text() if len(doc) > 0 else ""
        lang = detect(first_page) if first_page.strip() else "unknown"
    else:
        lang = "unknown"

    output["metadata"]["language"] = lang
    output["metadata"]["processing_timestamp"] = str(datetime.utcnow())

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=4)

def main():
    for folder in os.listdir(BASE_DIR):
        path = os.path.join(BASE_DIR, folder)
        if os.path.isdir(path) and folder.lower().startswith("collection"):
            print(f"Processing {folder}...")
            process_collection(path)

if __name__ == "__main__":
    main()
