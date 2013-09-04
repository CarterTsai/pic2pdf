from reportlab.pdfgen import canvas

# A4
pdfWidht = 595
pdfHeight = 842

picWidth = (595 / 2) - (10 * 2)
picHeight = 280
picInteval = 15

# create canvas
c = canvas.Canvas("picture.pdf")

imageLen = 6
#for v in range(6):
#c.rect(0 + (v * 100), 750, picWidth, picHeight)
c.rect(0 + picInteval, 500, picWidth, picHeight)
c.rect(306, 500, picWidth, picHeight)


c.drawString(100, 750, "Welcome to Reportlab!")


c.save()
