from django.shortcuts import render, redirect
from .models import ContactMessage
def home(request):
    return render(request, 'home.html', {})
def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        # Get the form data from the POST request
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')

        # Save the form data to the database
        contact_message = ContactMessage(name=name, email=email, phone=phone, message=message)
        contact_message.save()

        # Redirect the user to a thank you page after successful submission
        return redirect('thank_you')  # Create the 'thank_you' URL and template

    return render(request, 'contact.html')
def thank_you(request):
    return render(request, 'thank_you.html')