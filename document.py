from docx import Document

class DocumentGenerator:
    def save(self, content):
        doc = Document()
        doc.add_heading("AI Generated Report",1)
        doc.add_paragraph(content)
        # path=""
        path = r"C:\Users\katra\OneDrive\Desktop\ai_agent\output\rerts.docx"
        doc.save(path)
        return path
