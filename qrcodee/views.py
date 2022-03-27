from django.shortcuts import render

# Create your views here.
import qrcode
from qrcode.image.svg import SvgFillImage
from io import BytesIO


def index(request):
    context = {}
    if request.method == "POST":
        factory = SvgFillImage
        img = qrcode.make(request.POST.get("qr_text","") , image_factory=factory)
        stream = BytesIO()
        img.save(stream)
        context["svg"] = stream.getvalue().decode()

    return render(request, "index.html", context=context)