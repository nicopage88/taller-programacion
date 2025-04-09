from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import green
import os

def create_folio_overlay(folio_number, output_file, width, height):
    c = canvas.Canvas(output_file, pagesize=(width, height))
    c.setFillColor(green)  # Cambia el color del texto a verde
    c.setFont("Helvetica-Bold", 12)  # Cambia la fuente a Arial Bold Narrow (Helvetica-Bold en ReportLab)
    
    # Ajusta la posición del folio
    offset_x = 56.692  # 2 cm en puntos
    offset_y = 85.039  # 3 cm en puntos
    c.drawString(width - 100 - offset_x, height - 50 - offset_y, f"Folio: {folio_number:05d}")
    c.save()

def add_folio_to_pdf(input_pdf, overlay_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    overlay_reader = PdfReader(overlay_pdf)
    writer = PdfWriter()

    for i in range(len(reader.pages)):
        page = reader.pages[i]
        overlay_page = overlay_reader.pages[0]
        page.merge_page(overlay_page)
        writer.add_page(page)

    with open(output_pdf, "wb") as f_out:
        writer.write(f_out)

input_pdf = "archivo_base.pdf"
output_dir = "output_pdfs"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Leer el tamaño de la primera página del PDF base
reader = PdfReader(input_pdf)
page = reader.pages[0]
width = float(page.mediabox.width)
height = float(page.mediabox.height)

for i in range(1, 701):
    folio_overlay = f"folio_{i:05d}.pdf"
    output_pdf = os.path.join(output_dir, f"documento_{i:05d}.pdf")

    create_folio_overlay(i, folio_overlay, width, height)
    add_folio_to_pdf(input_pdf, folio_overlay, output_pdf)

    os.remove(folio_overlay)

print("PDFs generados exitosamente.")
