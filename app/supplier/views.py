from django.shortcuts import render

from supplier.models import Supplier


def detail_supplier(request, pk):

    if request.method == 'GET':

        supplier = Supplier.objects.filter(id=pk).first()

        context = {
            'supplier': supplier
        }

        return render(request, 'supplier/detail_supplier.html', context)
