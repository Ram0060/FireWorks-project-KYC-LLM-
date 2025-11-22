# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health, classify, extract, pipeline


app = FastAPI(
    title="KYC Identity Document Pipeline",
    version="0.1.0",
    description="KYC PoC using Fireworks AI models",
)

# CORS (tweak as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router)
app.include_router(classify.router)
app.include_router(extract.router)
app.include_router(pipeline.router)
