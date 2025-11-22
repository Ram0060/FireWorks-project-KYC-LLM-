# app/utils/errors.py


class KYCError(Exception):
    """Base KYC exception."""


class ClassificationError(KYCError):
    pass


class OCRCallError(KYCError):
    pass


class ExtractionError(KYCError):
    pass


class ValidationError(KYCError):
    pass


class UnsupportedDocumentError(KYCError):
    pass
