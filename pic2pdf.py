from reportlab.pdfgen import canvas
import glob

# A4
pdfWidht = 595
pdfHeight = 842

pitch = 2
picWidth = (595 / 2) - (10 * 2)
picHeight = 270
picInteval = 15

# get all of picture from
imgs = glob.glob('./img/*')
imageLen = len(imgs)

# create canvas
c = canvas.Canvas("picture.pdf")

picX = 0
picY = 560

# draw form
for v in range(1, imageLen + 1):
    offsetX = picX + picInteval + ((v % 2) * picWidth)
    offsetY = picY
    c.rect(offsetX, offsetY, picWidth, picHeight)
    # draw image
    c.drawImage(imgs[v-1], offsetX, offsetY, picWidth, picHeight)
    if((v % 2) == 0):
        picY -= picHeight
        picX = 0

c.drawString(100, 750, "Welcome to Reportlab!")
c.save()
