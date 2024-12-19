import streamlit as st
import base64
from time import sleep
from pypdf import PdfWriter, PdfReader
import os

def Compress_pdf(bin_value):
    """after compression return the path"""

    writer = PdfWriter(PdfReader(bin_value))

    if os.path.exists("compress"):
        pass
    else:
        os.mkdir("compress")

    for page in writer.pages:
        page.compress_content_streams()  # This is CPU intensive!

    path = os.path.join("compress", "compressed.pdf")
    writer.write(path)
    return path


main_title = "PDF Operation"
pdf_files = st.file_uploader("PDF HERE", type=['pdf'], accept_multiple_files=True)
st.subheader(main_title)

def displayPDF(file):
    # Opening file from file path
    with open(file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')

    # Embedding PDF in HTML
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

    # Displaying File
    st.markdown(pdf_display, unsafe_allow_html=True)


if st.button("Compress"):
    if pdf_files:
        total_size = 0
        for pdf in pdf_files:
            size = len(pdf.getvalue())
            total_size += size

        total_size = total_size / (1024 * 1024)
        print("Total (MB) : " + str(total_size))

        out_path = Compress_pdf(pdf_files[0])

        st.write("Merge complete at : ", out_path)
        with st.spinner("Compressing..."):
            sleep(total_size + 0.5)
        displayPDF(out_path)


