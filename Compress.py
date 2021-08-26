from PDFNetPython3 import PDFDoc, Optimizer, SDFDoc

doc = PDFDoc('./origin.pdf')
doc.InitSecurityHandler()
Optimizer.Optimize(doc)
doc.Save('./origin_compressed.pdf', SDFDoc.e_linearized)
doc.Close()