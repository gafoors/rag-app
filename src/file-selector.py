import streamlit as st
import os
import tkinter as tk
from tkinter import filedialog
import PyPDF2


def document_selector():
    selected_folder_path = st.session_state.get("folder_path", None)
    folder_select_button = st.button("Select Folder")
    if folder_select_button:
        selected_folder_path = select_folder()
        st.session_state.folder_path = selected_folder_path

    st.title("Document Selector")

    # Directory where the documents are stored
    doc_dir = selected_folder_path

    # Fetch list of files in the directory
    try:
        files = os.listdir(doc_dir)
        if not files:
            st.warning("No documents found in the specified directory.")
            return
    except FileNotFoundError:
        st.error("Specified directory not found.")
        return

    # Filter to only show specific document types, e.g., .txt, .pdf
    files = [f for f in files if f.endswith('.txt') or f.endswith('.pdf')]

    # Dropdown to select a document
    selected_file = st.selectbox("Select a document", files)

    if selected_file:
        file_path = os.path.join(doc_dir, selected_file)

        # Read and display the content of the selected document
        if selected_file.endswith('.txt'):
            with open(file_path, 'r') as file:
                content = file.read()
                st.text_area("Document Content", content, height=400)
        elif selected_file.endswith('.pdf'):
            # For PDF files, you might need additional libraries to read content, e.g., PyMuPDF, PyPDF2
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfFileReader(file)
                num_pages = reader.numPages
                pdf_text = ""
                for page_num in range(num_pages):
                    page = reader.getPage(page_num)
                    pdf_text += page.extract_text()
                st.text_area("Document Content", pdf_text, height=400)


def select_folder():
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(master=root)
    root.destroy()
    return folder_path


if __name__ == "__main__":
    document_selector()
