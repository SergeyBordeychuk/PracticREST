import os

import stripe


def create_product(request):
    stripe.api_key = os.getenv("STRIPE_API")
    product = stripe.Product.create(name=request.data['name'])
    return product

def create_price_product(request, product):
    stripe.api_key = os.getenv("STRIPE_API")
    price = stripe.Price.create(
        currency="rub",
        unit_amount=request.data['price'],
        recurring={"interval": "year"},
        product=product['id'],
    )
    return price

def create_session(request, price):
    stripe.api_key = os.getenv("STRIPE_API")
    session = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": price['id'], "quantity": 2}],
        mode="payment",
    )
    return session.json()