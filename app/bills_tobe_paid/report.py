# TODO EM DESENVOLVIMENTO

from django.shortcuts import render

from order.models import Order


def bills_tobe_received_report(request):

    if request == 'GET':
        orders = list(Order.objects.filter(is_active=True))

        context = {
            'order_form': orders
        }

        return render(request, 'bills_tobe_paid/report.html')
