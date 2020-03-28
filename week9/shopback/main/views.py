from django.http.request import HttpRequest
from django.http.response import JsonResponse

import random

products=[]
categories=[]

for i in range(1,5):
    n = random.randrange(1, 10)
    products.append(
        {
            'id': n,
            'category id': i,
            'product name': f'product {i}',
            'price': f'{i*n} dollars'
        }
    )
    categories.append(
        {
            'category id': i,
            'category name': f'category {i}'
        }
    )

def product_list(request):
    return JsonResponse(products, safe=False)

def product_id(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product)

    return JsonResponse({'error' : 'product does not exists'})

def category(request):
    return JsonResponse(categories, safe=False)

def cat_id(request, cat_id):
    for categori in categories:
        if categori['category id'] == cat_id:
            return JsonResponse(categori)

    return JsonResponse({'error' : 'product does not exists'})

def cat_prod_id(request, cat_id):
    for product in products:
        for category in categories:
            if product['category id'] == category['category id']:
                return JsonResponse(product)
    return JsonResponse({'error' : 'product does not exists'})