# app/services/validator.py
from datetime import datetime
from app.models.schemas import KYCResult
from app.utils.errors import ValidationError


def _parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None


def validate_kyc(result: KYCResult) -> KYCResult:
    # Example checks – extend as needed

    # 1. Expiry date is in the future
    if result.expiry_date:
        exp = _parse_date(result.expiry_date)
        if exp is None:
            raise ValidationError(f"Invalid expiry_date format: {result.expiry_date}")
        if exp < datetime.utcnow():
            raise ValidationError("Document is expired")

    # 2. DOB is not in the future
    if result.date_of_birth:
        dob = _parse_date(result.date_of_birth)
        if dob is None:
            raise ValidationError(f"Invalid date_of_birth: {result.date_of_birth}")
        if dob > datetime.utcnow():
            raise ValidationError("date_of_birth cannot be in the future")

    # Add more checks: nationality vs issuing_country, etc.

    return result
