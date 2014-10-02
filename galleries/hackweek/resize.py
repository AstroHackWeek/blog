import PIL
import os

def resize_image(filename, max_width=800, max_height=800):
    from PIL import Image
    im = Image.open(filename)
    width, height = im.size

    frac = min(1, # never grow image
               max_width * 1. / width,
               max_height * 1. / height)
    
    final_size = (int(round(frac * width)),
                  int(round(frac * height)))

    im_small = im.resize(final_size, Image.ANTIALIAS)

    root = os.path.splitext(filename)[0]
    outfile = os.path.join('small', root + '.jpg')
    im_small.save(outfile)
    return outfile
    


if __name__ == '__main__':
    for filename in os.listdir('.'):
        if filename.lower().endswith('-small.jpg'):
            continue
        if filename.lower().endswith('.jpg'):
            print(filename)
            print("->", resize_image(filename))
    
