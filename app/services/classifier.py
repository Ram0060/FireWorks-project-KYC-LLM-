# app/services/classifier.py
from core.fireworks_client import client
from core.config import settings
from app.models.enums import DocumentType
from app.models.prompts import CLASSIFICATION_PROMPT
from app.models.schemas import ClassificationResult
from app.utils.errors import ClassificationError
from app.utils.image_utils import normalize_data_url


def classify_document(image_b64: str) -> ClassificationResult:
    data_url = normalize_data_url(image_b64)

    try:
        response = client.responses.create(
            model=settings.CLASSIFICATION_MODEL,
            input=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": CLASSIFICATION_PROMPT},
                        {"type": "image", "image_url": data_url},
                    ],
                }
            ],
            max_output_tokens=16,
        )
        text = response.output_text.strip().lower()
    except Exception as e:
        raise ClassificationError(str(e))

    if "passport" in text:
        doc_type = DocumentType.PASSPORT
    elif "driver" in text:
        doc_type = DocumentType.DRIVERS_LICENSE
    else:
        doc_type = DocumentType.OTHER

    # TODO: You can compute a confidence based on logprobs if available.
    return ClassificationResult(document_type=doc_type, confidence=0.9)
