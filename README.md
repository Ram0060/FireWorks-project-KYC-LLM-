# 🔍 Identity Document KYC Pipeline — Fireworks AI (PoC)

This project is an end-to-end KYC (Know Your Customer) identity-document processing pipeline built entirely using **Fireworks AI’s multimodal LLMs**.  
It takes an image of an identity document (Passport or Driver’s License) and produces a **clean, validated JSON output** containing all structured identity fields.


##  Features

### ✔️ Document Classification  
Uses Fireworks vision-language models to classify the input as:
- `passport`
- `drivers_license`
- `other`

###  OCR / Text Extraction  
Vision-LLM based OCR using **qwen2p5-vl / qwen2-vl models** to extract raw text.

###  Structured Field Extraction  
A strict JSON schema–based extraction for:
- **Passport Schema**
- **Driver’s License Schema**

Each document type has its own set of fields:
- Name  
- DOB  
- Issuing Country / State  
- Document Number  
- Gender  
- Nationality  
- Address (if applicable)  
- Issue/Expiry dates  
- Fireworks-model confidence score  
- Raw OCR text  

###  Data Validation Layer  
After extraction, the output is validated using **Pydantic models**, ensuring:
- Required fields are present  
- Dates are normalized  
- Strings cleaned  
- Schema-safe output  

###  Modular Pipeline  
The system is broken into clean services:




Data Ingestion ((Image Upload / API)) -->  Preprocessing Service(Image utils, rotation,resizing, base64) 

--> Document Classification Service (LLM Inference) ---> Handler MicroServices image+text → JSON

[Possiblity for EXtension for clean Extension ] --> Validation Service  --> Final Structured Output
