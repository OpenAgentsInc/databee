"""Testing ingestion"""

from databee.ingest import ingest_pdf

def test_pdf_ingest():
    """Let's see if this works"""
    ingest_pdf("docs/Seasteading-Implementation-Plan.pdf")
