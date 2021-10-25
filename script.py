import os
import sys


def main():
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

        except OSError:
            pass


if __name__ == "__main__":
    main()