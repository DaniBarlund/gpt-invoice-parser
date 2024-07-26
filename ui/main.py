# TODO: write simple UI which takes in invoice as pdf and returns the extracted data in a table
import streamlit as st
import random
import base64

def init_state():
    if "invoice" not in st.session_state:
        st.session_state.invoice = ""
    if "markdown_string" not in st.session_state:
        st.session_state.markdown_string = ""

def get_random_invoice():
    invoice_number = random.randint(0, 99)
    char_number = invoice_number + 1
    invoice_name = f"data/invoice_{invoice_number}_charspace_{char_number}.pdf"
    st.session_state["invoice"] = invoice_name

def show_pdf():
    get_random_invoice()
    encoded_string = None
    with open(st.session_state["invoice"], "rb") as file:
        encoded_string = base64.b64encode(file.read())
    markdown_string = f'<embed src="data:application/pdf;base64,{encoded_string.decode()}" width="700" height="1000" type="application/pdf">'
    st.session_state["markdown_string"]  = markdown_string

def extract_data():
    #TODO: extract data from pdf using gpt-4o-mini
    # and stream as table to user
    pass

def main():
    init_state()
    st.title("Invoice Data Extractor")

    st.button("get random invoice file", on_click=show_pdf)

    st.markdown(st.session_state["markdown_string"], unsafe_allow_html=True)

    st.button("extract data to table with gpt", on_click=extract_data)

if __name__ == "__main__":
    main()