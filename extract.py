from PIL import Image
from PIL.ExifTags import TAGS

def exif(path: str) -> dict:
    img = Image.open(path)
    exif_data = img._getexif()
    exif = {}
    for tag_id in exif_data:
        tag = TAGS.get(tag_id, tag_id)
        data = exif_data.get(tag_id)
        if isinstance(data, bytes):
            data = data.decode()
        exif[tag] = data
        # print(f"{tag:25}: {data}")
    return exif


