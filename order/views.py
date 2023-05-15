from django.shortcuts import render

def order_details(request,pk):
    return render(request, 'order_details.html', context={'pk': pk})
