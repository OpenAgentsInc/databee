"""Testing ingestion"""

from databee.ingest import ingest_pdf

def test_pdf_ingest():
    """Test ingest a PDF"""
    ingest_pdf("docs/Seasteading-Implementation-Plan.pdf")
