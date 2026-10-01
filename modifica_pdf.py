#!/usr/bin/env python3
import pikepdf
import os
import sys

# ================= CONFIGURARE =================
# Calea către PDF-ul original (așa cum ai specificat)
input_pdf = "/home/vlad/Downloads/BVB Loads - Freight Management Platform.pdf"

# Calea către PDF-ul modificat (în același folder)
output_pdf = "/home/vlad/Downloads/BVB_modificat.pdf"

# URL-ul care se va deschide în browser
url = "https://chat.deepseek.com"

# Mesajul din pop-up
mesaj = "Acesta este un mesaj pop-up! Se va deschide linkul."
# ===============================================

# Verifică dacă fișierul original există
if not os.path.isfile(input_pdf):
    print(f"Eroare: Fișierul nu a fost găsit: {input_pdf}")
    sys.exit(1)

# 1. Deschide PDF-ul original
try:
    pdf = pikepdf.open(input_pdf)
except Exception as e:
    print(f"Eroare la deschiderea PDF-ului: {e}")
    sys.exit(1)

# 2. Creează codul JavaScript care va rula la deschidere
#    - app.alert() afișează un pop-up
#    - app.launchURL() deschide linkul în browser
js_code = f"""
app.alert('{mesaj}');
app.launchURL('{url}');
"""

# 3. Creează acțiunea JavaScript în PDF
js_action = pikepdf.Dictionary({
    "/S": pikepdf.Name("/JavaScript"),
    "/JS": pikepdf.String(js_code)
})

# 4. Adaugă acțiunea la deschiderea documentului (OpenAction)
pdf.Root["/OpenAction"] = js_action

# 5. Salvează PDF-ul modificat
try:
    pdf.save(output_pdf)
    pdf.close()
    print(f"PDF modificat salvat cu succes: {output_pdf}")
except Exception as e:
    print(f"Eroare la salvarea PDF-ului: {e}")
    sys.exit(1)

# 6. Deschide PDF-ul modificat cu viewerul implicit din Linux
try:
    os.system(f'xdg-open "{output_pdf}"')
except Exception as e:
    print(f"Nu am putut deschide PDF-ul automat: {e}")
    print(f"Îl poți deschide manual: {output_pdf}")