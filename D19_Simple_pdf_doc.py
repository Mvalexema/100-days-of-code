from fpdf import FPDF 
pdf = FPDF('P','mm','A4') # default values: pages are in portrait with the measure unit millimeter and A4 format
# L - landscape, measure units (pt,cm,in), formates (Letter and Legal)

pdf.add_page() #adding new page with the current position is by default places at 1 cm from the borders

pdf.set_margins(0,0,0)

# Adding first line in pdf

pdf.set_font('Arial', 'B', 14)
#pdf.cell(w = 40, h = 10, "New pdf document - check the features!", border = 0, ln = 1, align = '', fill = False, link='')
pdf.cell(w = 40, h = 10, border = 0, ln = 1, align = '', fill = False, link='')
# Adding new line

pdf.set_font('Times', '', 9)
pdf.cell(210, 10, 'Powered by FPDF.', 0, 0, 'C')

# Managing text position

pdf.set_font('Arial', '', 10)
pdf.ln(80)
pdf.cell(70)
pdf.cell(0, 0, 'First pdf document.', 0)

# Add image

#pdf.image('715052-Glasses 4-01.jpg', x = 85, y = 32.5, w = 40, h = 0, type = '', link = '')

# Draw a line

pdf.line(x1 = 85, y1 = 27.5, x2 = 125, y2 = 27.5)

# Drawing a rectangle or Ellipse

pdf.rect(x = 80, y = 20, w = 70, h = 55, style = '')

# Setting colour

pdf.set_fill_color(207, 227, 209)
pdf.set_draw_color(41, 53, 50)
pdf.rect(80, 115, 50, 10, 'DF')

pdf.set_text_color(32, 39, 186) # Text colour
pdf.ln(50)
pdf.cell(70)
pdf.cell(70, 0, 'The picture should be here. Next time it will be better.', 0, 0, 'C')

pdf.output('sample.pdf', 'F')

