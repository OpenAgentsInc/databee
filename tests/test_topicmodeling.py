"""Testing topic modeling"""

from databee.ingest import ingest_pdf

def test_topic_modeling():
    """Test return topics from PDF"""
    pages = ingest_pdf("docs/Seasteading-Implementation-Plan.pdf")
    print("-------")
    print(pages[9])
    print("-------")
