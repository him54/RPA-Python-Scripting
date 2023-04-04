import PyPDF2

def pdfmerge(p, o):

    pdfmerger = PyPDF2.PdfMerger()

    for pdf in p:
        pdfmerger.append(pdf)

    with open(o, "wb") as f:
        pdfmerger.write(f)

pdffile=["Seminar Topics.pdf", "pd1.pdf"]
output = "mergedout.pdf"
pdfmerge(p=pdffile, o=output)
