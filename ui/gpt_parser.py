# TODO: Gpt-4o-mini client,
#       markdown prompt for parsing,
#       streaming answer generation.

from openai import OpenAI
import instructor
from pydantic import BaseModel
from typing import List
from langchain_community.document_loaders import PyMuPDFLoader

prompt = "Extract only the invoice items and summary data from the pdf file into a table."

def get_answer(content:str) -> str:
    client = OpenAI()
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

#------------------- INSTRUCTOR -------------------#


class Columns(BaseModel):
    columns : List[str]

def get_columns(content:str) -> list[str]:
    client = instructor.from_openai(OpenAI())
    prompt = "Extract only columns of the invoice"
    columns = client.chat.completions.create(
    model="gpt-4o-mini",
    response_model=Columns,
    messages=[
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": content}]
    )
    return columns

def create_prompt(columns:list[str])->str:
    prompt = "Extract only the invoice items listed into a table. Columns are: "
    for column in columns:
        prompt = f"{prompt} {column},"
    return prompt

def get_table(content:str) -> str:
    client = OpenAI()
    columns = get_columns(content)
    prompt = create_prompt(columns)
    table = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": content}],
    stream=True
    )
    return table