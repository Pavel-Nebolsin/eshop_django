from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.dispatch import receiver
from allauth.account.signals import password_set, password_changed

from order.models import Order
from .forms import ProfileForm
def user_contact_view(request):
    return render(request, 'user_account_contact.html',
                 # {'form': form}
                  )


@login_required
def user_account_view(request):
    initial_data = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
        'email': request.user.emailaddress_set.first(),
        'phone_number': request.user.profile.phone_number,
        'address': request.user.profile.address,
    }

    if request.method == 'POST':
        form = ProfileForm(request.POST, initial=initial_data)
        if form.is_valid():
            update_profile(request, initial_data, form.cleaned_data)
            return redirect('user-account')
        else:
            show_form_errors(form)

    else:
        form = ProfileForm(initial=initial_data)

    return render(request, 'user_account_main.html', {'form': form})


class UserOrdersListView(ListView):
    model = Order
    template_name = 'user_account_orders.html'
    context_object_name = 'orders'

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter(user=user,status=Order.STATUS_WAITING_FOR_PAYMENT,total_amount__gt=0)




def update_profile(request, initial_data, new_data):

    user = request.user

    if str(initial_data['email']) != new_data['email']:
        initial_data['email'].change(request, new_data['email'], confirm=False)

    if initial_data['phone_number'] != new_data['phone_number']:
        user.profile.phone_number = new_data['phone_number']
        user.profile.phone_number_is_confirmed = False

    user.first_name = new_data['first_name']
    user.last_name = new_data['last_name']
    user.profile.address = new_data['address']

    user.save()
    user.profile.save()

def show_form_errors(form):
    for field_name, field in form.fields.items():
        if field_name in form.errors:
            field.widget.attrs['class'] += ' is-invalid'
        else:
            field.widget.attrs['class'] += ' is-valid'
