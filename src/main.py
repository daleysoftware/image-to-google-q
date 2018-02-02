import pytesseract
import sys
from PIL import Image, ImageEnhance, ImageFilter
from googleapiclient.discovery import build
import pprint


API_KEY = "<redacted>"
CSE_ID = "<redacted>"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    results = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return results['items'][0]


TMP_IMG = '/tmp/image-to-google-q.png'


def main(image_filename):
    # Parse text
    im = Image.open(image_filename)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save(TMP_IMG)
    text = pytesseract.image_to_string(Image.open(TMP_IMG))
    print('Parsed text: ' + text)

    # Query google
    results = google_search(text, API_KEY, CSE_ID, num=10)
    pprint.pprint(results)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: %s <image_filename>" % sys.argv[0])
        sys.exit(1)
    main(sys.argv[1])




