"""Testing topic modeling"""

from databee.ingest import ingest_pdf
from databee.topics import extract_topics_from_documents

def test_topic_modeling():
    """Test return topics from PDF"""
    pages = ingest_pdf("docs/Seasteading-Implementation-Plan.pdf")
    topics = extract_topics_from_documents(pages)
    print("-------")
    print(topics)
    print("-------")
