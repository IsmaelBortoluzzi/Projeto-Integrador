from django.shortcuts import render

from product_brand.forms import BrandForm


def create_brand(request):

    if request.method == 'GET':
        context = {
            'brand_form': BrandForm()
        }
        return render(request, 'brand/create_brand.html', context)

    if request.method == 'POST':
        pass
        # TODO fazer igual foi feito no client e address