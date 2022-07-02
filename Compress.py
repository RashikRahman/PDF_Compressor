
from PDFNetPython3 import *

PDFNet.Initialize("demo:1656775129318:7a4c316403000000002ded2b9985ddf7cce81ba75d69be5b9fa2a7bccf")
doc = PDFDoc('./origin.pdf')
doc.InitSecurityHandler()
Optimizer.Optimize(doc)
doc.Save('./origin_compressed.pdf', SDFDoc.e_linearized)
doc.Close()