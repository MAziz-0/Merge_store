from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import ContactUsForm


def contact(request):
    """ Contact Form """
    contact_form = ContactUsForm
    if request.method == "POST":
        form_data = {
            'name': request.POST.get('name', ''),
            'email': request.POST.get('email', ''),
            'message': request.POST.get('message', '')
        }
        print(f"FORM_DATA: {form_data}")
        form = contact_form(form_data)

        if form.is_valid():
            print("Form is valid")
            send_mail(
                form_data['name'] + " - " + form_data['email'],
                form_data['message'],
                'maastudentacc@gmail.com',
                [settings.DEFAULT_FROM_EMAIL],
                fail_silently=False,
            )
        messages.success(
            request, 'Your message has been received,we will contact you with further information regarding your query'
            )
        return redirect('contact')
    context = {
        'form': contact_form,
    }

    return render(request, 'contact/contact.html', context)
