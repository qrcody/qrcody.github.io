import os
import shutil
import sys
sys.path.insert(1, '../python-qrcode')
import qrcode
from PIL import Image
import PIL

def main():
    global url
    global root_folder
    if len(sys.argv) < 2:
        print("Invalid arguments! Use python3 <name>")

    root_folder = sys.argv[1]
    folders = ['style', 'images', 'pages', 'icons']

    for dir in folders:
        try:
            os.makedirs(os.path.join(root_folder, dir))
            print('Created dir ' + root_folder + '/' + dir)
            if dir == 'style':
                file = open(root_folder + '/' + dir + '/' + 'style.css', 'w+')
                print('Created file ' + root_folder + '/' + dir + '/' + 'style.css')
                file = open(root_folder + '/' + 'index.html', 'w+')
                print('Created file ' + root_folder + '/' + 'index.html')
            if dir == 'pages':
                shutil.copy2('menu_template.html', root_folder + '/pages/menu.html') # complete target filename given
            	#file = open(root_folder + '/pages/menu.html', 'w+')

        except OSError:
            pass
    url = 'https://www.codinha.dev/' + root_folder + '/pages/menu.html'

def createQRCode():
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    print("Created qrcode to url: " + url)

    img = qr.make_image(fill_color="black", back_color="white")
    img = img.save(root_folder + "_qrcode.png")

if __name__ == "__main__":
    main()
    createQRCode()
