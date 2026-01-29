from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Product


def send_product_email(request, pk):
    product = get_object_or_404(Product, pk=pk)

    subject = f"New Product: {product.name}"
    from_email = "user123@gmail.com"
    recipient_list = ["your_mailtrap_inbox@mailtrap.io"]

    html_message = render_to_string(
        'product_email.html',
        {'product': product}
    )

    plain_message = strip_tags(html_message)

    send_mail(
        subject,
        plain_message,
        from_email,
        recipient_list,
        html_message=html_message
    )

    return HttpResponse("Email sent successfully")
