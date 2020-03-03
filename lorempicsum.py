import requests
def lorem_picsum(img_name):
    img_url = 'https://picsum.photos/536/354'
    img_bytes = requests.get(img_url).content
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

