# TODO: Gpt-4o-mini client,
#       markdown prompt for parsing,
#       streaming answer generation.

from openai import OpenAI
from langchain_community.document_loaders import PyMuPDFLoader

client = OpenAI()

def get_answer(prompt: str,content:str) -> str:
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

def main():
    prompt = "Extract the invoice data from the pdf file"
    invoice_name = "data/invoice_1_charspace_2.pdf"
    content = read_pdf(invoice_name)
    answer = get_answer(prompt, content)
    print(answer)

if __name__ == "__main__":
    main()