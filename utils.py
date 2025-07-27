# ---------- utils.py ----------
import os
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer, util

# Load a small model for offline, CPU use
model = SentenceTransformer('all-MiniLM-L6-v2')


def extract_all_text(pdf_path):
    """Extract all text from a PDF as a list of (page_num, text)"""
    doc = fitz.open(pdf_path)
    text_pages = []
    for page_num, page in enumerate(doc, start=1):
        text = page.get_text().strip()
        if text:
            text_pages.append((page_num, text))
    return text_pages


def process_documents(input_data, pdf_folder):
    persona = input_data["persona"]["role"]
    job = input_data["job_to_be_done"]["task"]
    query = f"{persona} needs to: {job}"

    query_embedding = model.encode(query, convert_to_tensor=True)

    extracted_sections = []
    subsection_analysis = []

    for doc in input_data["documents"]:
        pdf_filename = doc["filename"]
        pdf_path = os.path.join(pdf_folder, pdf_filename)

        if not os.path.exists(pdf_path):
            continue

        pages = extract_all_text(pdf_path)
        scored_pages = []

        for page_num, text in pages:
            page_embedding = model.encode(text, convert_to_tensor=True)
            score = util.cos_sim(query_embedding, page_embedding).item()
            scored_pages.append((score, page_num, text))

        # Sort by similarity score, pick top 1–2 pages
        top_pages = sorted(scored_pages, reverse=True)[:2]

        for i, (score, page_num, text) in enumerate(top_pages):
            if i == 0:
                extracted_sections.append({
                    "document": pdf_filename,
                    "section_title": text.split("\n")[0][:100],  # First line as title
                    "importance_rank": len(extracted_sections) + 1,
                    "page_number": page_num
                })

            subsection_analysis.append({
                "document": pdf_filename,
                "refined_text": text[:1000],  # Trim to 1000 chars for safety
                "page_number": page_num
            })

    return {
        "metadata": {
            "input_documents": [d["filename"] for d in input_data["documents"]],
            "persona": persona,
            "job_to_be_done": job
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }
