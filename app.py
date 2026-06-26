import streamlit as st
from PyPDF2 import PdfReader
import base64
import os

st.title("PRINTING PRICE CALCULATOR ❤️")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:

    os.makedirs("uploads", exist_ok=True)
    save_path = os.path.join("uploads", uploaded_file.name)

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"PDF saved to: {save_path}")

    pdf = PdfReader(uploaded_file)
    pages = len(pdf.pages)

    st.success("PDF uploaded successfully!")
    st.write(f"Number of pages: {pages}")

    base64_pdf = base64.b64encode(uploaded_file.read()).decode("utf-8")

    pdf_view = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}"
    width="700" height="900"></iframe>
    """

    st.markdown(pdf_view, unsafe_allow_html=True)

    paper = st.selectbox("Choose paper type", ["80 gsm", "100 gsm"])
    colour = st.selectbox("Choose printing type", ["Colour", "Black & White"])
    side = st.selectbox("Choose printing side", ["One-sided", "Two-sided"])

    if paper == "100 gsm":
        if colour == "Colour" and side == "One-sided":
            price = 0.80
        elif colour == "Colour" and side == "Two-sided":
            price = 0.90
        elif colour == "Black & White" and side == "One-sided":
            price = 0.40
        else:
            price = 0.50
    else:
        if colour == "Colour" and side == "One-sided":
            price = 0.50
        elif colour == "Colour" and side == "Two-sided":
            price = 0.60
        elif colour == "Black & White" and side == "One-sided":
            price = 0.30
        else:
            price = 0.40

    printing_price = pages * price

    addon = st.selectbox("Add-on", ["None", "Paper Clip", "Fastener"])

    addon_price = 0
    if addon == "Paper Clip":
        addon_price = 0.10
    elif addon == "Fastener":
        addon_price = 0.30

    final_price = printing_price + addon_price

    st.subheader(f"Final Price: RM {final_price:.2f}")

    receipt = f"""
PRINTING RECEIPT
-----------------------
Pages: {pages}
Paper: {paper}
Colour: {colour}
Side: {side}
Add-on: {addon}

Final Price: RM {final_price:.2f}
"""

    st.download_button("Download Receipt", receipt, file_name="receipt.txt")
