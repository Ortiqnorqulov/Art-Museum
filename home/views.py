from django.shortcuts import render, redirect
from django.contrib import messages
from home.forms import ContactForm
from home.models import Exponat, Blog, Contact, ContactMessage


def index(request):
    exponat = Exponat.objects.all()
    blog = Blog.objects.all()
    context = {
        'exponat': exponat,
        'blog': blog,
    }
    return render(request, 'index.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = ContactMessage()
            data.name = form.cleaned_data['name']
            data.surname = form.cleaned_data['surname']
            data.subject = form.cleaned_data['subject']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Your message has been sent! Thank you")
            return redirect('home')
    form = ContactForm
    contact = Contact.objects.all()
    context = {
        'contact': contact,
        'form': form,
    }
    return render(request, 'contact.html', context)


def about(request):
    return render(request, 'about.html')



def event(request):
    exponat = Exponat.objects.all()
    blog = Blog.objects.all()
    context = {
        'exponat': exponat,
        'blog': blog,
    }
    return render(request, 'event.html', context)
