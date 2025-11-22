# app/models/prompts.py

CLASSIFICATION_PROMPT = """
You are a KYC document classifier.
Return ONE WORD ONLY: passport, drivers_license, or other.
"""

OCR_PROMPT = """
You are an OCR assistant for KYC identity documents.
Extract all text faithfully from the given image.
Return ONLY the plain text, no explanations.
"""

PASSPORT_EXTRACTION_SYSTEM_PROMPT = """
You are an expert KYC extraction model.
Extract all passport identity fields into the provided JSON schema.
Be strict with dates (YYYY-MM-DD) and return null if unknown.
"""

DL_EXTRACTION_SYSTEM_PROMPT = """
You are an expert KYC extraction model.
Extract all driver’s license identity fields into the provided JSON schema.
Be strict with dates (YYYY-MM-DD) and return null if unknown.
"""
