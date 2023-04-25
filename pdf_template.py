from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("csv_files/topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    # Set the header
    topic = row['Topic']
    pdf.set_font(family="Helvetica", size=20, style="B")
    # gray text
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=topic, border=0, ln=1, align="L")

    for i in range(20, 284, 10):
        pdf.line(x1=10, y1=i, x2=200, y2=i)

    # set the footer
    pdf.ln(265)
    pdf.set_font(family="Helvetica", size=8, style="I")
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=topic, border=0, ln=1, align="R")

    for l in range(row['Pages']-1):
        pdf.add_page()

        # set the footer
        pdf.ln(277)
        pdf.set_font(family="Helvetica", size=8, style="I")
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=topic, border=0, ln=1, align="R")

        for i in range(20, 284, 10):
            pdf.line(x1=10, y1=i, x2=200, y2=i)

pdf.output("outputs/template.pdf")
