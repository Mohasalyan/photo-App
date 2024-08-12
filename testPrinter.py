# from PIL import Image
# from reportlab.lib.pagesizes import letter
# from reportlab.lib.units import inch
# from reportlab.pdfgen import canvas

# def create_pdf_with_image(image_path, output_pdf_path, width_in_inches, height_in_inches, dpi=96):
#     # Open the image using PIL
#     image = Image.open(image_path)

#     # Calculate the image size in pixels
#     width_in_pixels = int(width_in_inches * dpi)
#     height_in_pixels = int(height_in_inches * dpi)

#     # Resize the image to the target size
#     image = image.resize((width_in_pixels, height_in_pixels))

#     # Create a PDF with ReportLab
#     c = canvas.Canvas(output_pdf_path, pagesize=(width_in_inches * inch, height_in_inches * inch))

#     # Draw the image on the PDF
#     c.drawInlineImage(image, 0, 0, width_in_inches * inch, height_in_inches * inch)

#     # Save the PDF
#     c.showPage()
#     c.save()

# # Example usage:
# image_path = "test4.jpg"  # Path to your image file
# output_pdf_path = "output_image.pdf"  # Path where you want to save the PDF
# width_in_inches = 4 # Width in inches
# height_in_inches = 3  # Height in inches

# # create_pdf_with_image(image_path, output_pdf_path, width_in_inches, height_in_inches)

# # # print(f"PDF created: {output_pdf_path}")
# # # import os
# # print(inch)
# # # # Command to open the PDF with the default PDF viewer (which can then print)
# # # os.startfile("output_image.pdf", "print")




import win32print
import win32ui
from PIL import Image, ImageWin
HORZRES = 8
VERTRES = 10
PHYSICALWIDTH = 110
PHYSICALHEIGHT = 111
PHYSICALOFFSETX = 112
PHYSICALOFFSETY = 113
LOGPIXELSX = 88
LOGPIXELSY = 90



def print_image(path,width,height,rotate=False ,offset_x=0,offset_y=0):  
    printer_name = win32print.GetDefaultPrinter ()
    file_name = path
    hDC = win32ui.CreateDC ()
    hDC.CreatePrinterDC (printer_name)
    dpi_printer = hDC.GetDeviceCaps (LOGPIXELSX), hDC.GetDeviceCaps (LOGPIXELSY)
    print(dpi_printer)
    bmp = Image.open (file_name)
    if rotate:
        bmp = bmp.rotate (90)
        
    hDC.StartDoc(file_name)
    hDC.StartPage ()

    dib = ImageWin.Dib (bmp)
    print((int((dpi_printer[0]*offset_x)/2.54),int((dpi_printer[1]*offset_y)/2.54),int((dpi_printer[0]*width)/2.54),int((dpi_printer[1]*height)/2.54)))
    dib.draw (hDC.GetHandleOutput (), (int((dpi_printer[0]*offset_x)/2.54),int((dpi_printer[1]*offset_y)/2.54),int((dpi_printer[0]*width)/2.54),int((dpi_printer[1]*height)/2.54)))
    
    hDC.EndPage ()
    hDC.EndDoc ()
    hDC.DeleteDC ()
    


width_in_cm =2
height_in_cm =2
path_image ="test2.jpg"
rotate_img=False
offset_x_cm =1
offset_y_cm =0

print_image(path_image,width_in_cm,height_in_cm,rotate_img ,offset_x_cm,offset_y_cm)