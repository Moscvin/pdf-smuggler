import sys
from pypdf import PdfReader, PdfWriter
from pypdf.generic import (
    NameObject, TextStringObject, DictionaryObject, ArrayObject
)

def add_open_url(inputpdf, url, outputpdf):
    reader = PdfReader(inputpdf)
    writer = PdfWriter()
    writer.append(reader)

    # Varianta 1: actiune JavaScript care lanseaza URL-ul
    # (app.launchURL -> deschide URL-ul in browserul implicit)
    js = DictionaryObject()
    js[NameObject("/S")]  = NameObject("/JavaScript")
    js[NameObject("/JS")] = TextStringObject(
        'app.launchURL("%s", true);' % url
    )
    writer._root_object[NameObject("/OpenAction")] = js

    with open(outputpdf, "wb") as f:
        writer.write(f)
    print('Gata! "%s" se va deschide la %s cand e deschis PDF-ul.' % (outputpdf, url))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python pdf-open-url.py <input.pdf> <url> <output.pdf>")
        sys.exit(1)
    add_open_url(sys.argv[1], sys.argv[2], sys.argv[3])
