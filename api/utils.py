from io import BytesIO
from random import shuffle, randint, choice
from string import ascii_letters, digits

from qrcode import QRCode


def hashed_url(url: str) -> str:
    url: str = url.replace('.', '').replace('/', '').replace("\'", '')
    a = list((ascii_letters + digits + url) * 2)
    shuffle(a)
    a = "".join(a)
    rand = randint(4, 6)
    return "".join(choice(a) for _ in range(rand))


def generate_qrcode(url: str):
    qr = QRCode(
        version=1,
        box_size=20,
        border=1
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    buf = BytesIO()
    img.save(buf)
    buf.seek(0)
    return buf
