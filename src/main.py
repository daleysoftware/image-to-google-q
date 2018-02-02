import pytesseract
import sys
from PIL import Image, ImageEnhance, ImageFilter


TMP_IMG = '/tmp/image-to-google-q.png'


def main(image_filename):
    im = Image.open(image_filename)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save(TMP_IMG)
    text = pytesseract.image_to_string(Image.open(TMP_IMG))
    print(text)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <image_filename>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])




