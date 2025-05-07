from PIL import Image

def jpeg(path):
    img = Image.open(path)
    img.save(f"{path}.jpeg")