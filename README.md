# Adobe Hackathon – Round 1B  
## Persona-Driven Document Intelligence (Backend)

This repository contains a backend-only solution for Round 1B of the Adobe “Connecting the Dots” Hackathon. The system identifies and ranks relevant sections and sub-sections from multiple PDFs based on a user persona and a specific task.

---

## 🧠 Problem Statement

You are given:
- A collection of 3–10 PDFs per test case
- A JSON file describing the **persona** and **job-to-be-done**

Your task is to:
- Extract the most relevant sections/subsections from the documents
- Rank them in order of importance
- Output the result in a structured `challenge1b_output.json` format

---

## 📁 Folder Structure

```
CHALLENGE_1B/
├── Collection1/
│   ├── PDFs/
│   ├── challenge1b_input.json
│   └── challenge1b_output.json
├── Collection2/
│   └── ...
├── Collection3/
│   └── ...
├── main.py
├── utils.py
├── Dockerfile
├── requirements.txt
└── approach_explanation.md
```

- Each `CollectionX/` contains its own documents and task
- Output JSON is automatically generated by the system

---

## ⚙️ Running the Solution (Docker)

Build the Docker image:
```bash
docker build --platform linux/amd64 -t adobe1b:final .
```

Run the container:
```bash
docker run --rm -v $(pwd)/CHALLENGE_1B:/app --network none adobe1b:final
```

---

## 📤 Output Format

Each `challenge1b_output.json` will contain:
- Metadata (documents, persona, job, timestamp)
- Extracted sections ranked by importance
- Refined sub-section summaries

---

## ✅ Features

- CPU-only, offline inference
- Modular codebase for easy extension
- Automatically handles multiple collections

---

## 📄 License

This project is intended solely for submission to Adobe's India Hackathon 2025. All rights reserved.