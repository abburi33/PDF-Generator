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

    pdf.set_font(family="Helvetica", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=50, h=8, txt=name, align="L", ln=1)

pdf.output("outputs/merged_pdf.pdf")
