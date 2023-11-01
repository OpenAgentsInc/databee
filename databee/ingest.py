"""Utilities for ingesting PDFs"""

from langchain.document_loaders import PyPDFLoader

def ingest_pdf(path):
    """
    Ingest a PDF and return a list of pages
    https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf#using-pypdf
    """

    loader = PyPDFLoader(path)
    pages = loader.load_and_split()
    return pages
