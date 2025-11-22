# tests/test_pipeline.py
from app.services.pipeline import run_kyc_pipeline
from app.utils.image_utils import encode_image_to_base64


def test_pipeline_smoke():
    # TODO: replace with a real sample image
    sample_path = "Images/sample_passport.jpg"
    image_b64 = encode_image_to_base64(sample_path)

    result, debug = run_kyc_pipeline(image_b64)

    assert result.document_type is not None
