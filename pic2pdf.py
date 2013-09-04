from reportlab.pdfgen import canvas

# A4
pdfWidht = 595
pdfHeight = 842

pitch = 2
picWidth = (595 / 2) - (10 * 2)
picHeight = 270
picInteval = 15


# create canvas
c = canvas.Canvas("picture.pdf")

imageLen = 6
picX = 0
picY = 560
for v in range(1, imageLen + 1):
    c.rect(picX + picInteval + ((v % 2) * picWidth), picY, picWidth, picHeight)
    if((v % 2) == 0):
        picY -= picHeight
        picX = 0

c.drawString(100, 750, "Welcome to Reportlab!")


c.save()
