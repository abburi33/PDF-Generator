from fpdf import FPDF
import glob
from pathlib import Path

# create a pdf file
pdf = FPDF(orientation="P", format="A4", unit="mm")
pdf.set_auto_page_break(auto=False, margin=0)

# create a list of text filepaths
filepaths = glob.glob("text_files/*.txt")

for filepath in filepaths:
    pdf.add_page()

    filename = Path(filepath).stem
    name = filename.title()

    # Add header
    pdf.set_font(family="Helvetica", style="B", size=16)
    pdf.cell(w=50, h=8, txt=name, align="L", ln=1)

    # Add content
    with open(filepath) as file:
        content = file.read()

    pdf.set_font(family="Helvetica", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)

pdf.output("outputs/merged_pdf.pdf")
