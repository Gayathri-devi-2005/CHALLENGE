# Approach Explanation

## Problem
Given multiple PDFs, a persona, and a goal, we extract the most relevant sections and summarize key content to support decision-making.

## Method
We:
- Read documents from each collection
- Use simple placeholder logic (or embedding-based scoring in real case) to rank sections
- Format output in required JSON with metadata, ranked sections, and summaries

## Features
- CPU-only, offline, fast execution
- Scalable to 3+ collections
- Dockerized for consistent deployment

Future work: Replace dummy logic with semantic scoring using sentence transformers.
