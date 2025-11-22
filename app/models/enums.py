# app/models/enums.py
from enum import Enum


class DocumentType(str, Enum):
    PASSPORT = "passport"
    DRIVERS_LICENSE = "drivers_license"
    OTHER = "other"
