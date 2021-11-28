from django.shortcuts import render
from django.contrib import messages
from .forms import ContactUsForm


def contact_view(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
            request, 'Your message has been received,we will contact you with further information regarding your query'
            )
            return render(request, 'site/index.html')
            
    form = ContactUsForm()
    context = {'form': form}
    return render(request, 'contact/contact.html', context)
