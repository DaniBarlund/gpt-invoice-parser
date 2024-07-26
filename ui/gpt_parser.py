# TODO: Gpt-4o-mini client,
#       markdown prompt for parsing,
#       streaming answer generation.

from openai import OpenAI
from langchain_community.document_loaders import PyMuPDFLoader

client = OpenAI()
prompt = "Extract only the invoice items and summary data from the pdf file into a table."

def get_answer(content:str) -> str:
    stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": content}],
    stream=True
    )
    return stream

def read_pdf(invoice_name: str) -> str:
    loader = PyMuPDFLoader(invoice_name)
    pdf = loader.load()
    content = " ".join([page.page_content for page in pdf])
    return content