import qrcode
import os

from django.conf import settings


def make_qr_code(phone_number):
    path_to_qr_code = os.path.join(settings.MEDIA_ROOT, "qr_codes", phone_number)
    img = qrcode.make(phone_number)
    img.save(path_to_qr_code)
    return f"qr_codes/{phone_number}"
