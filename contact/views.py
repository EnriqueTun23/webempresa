from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.


def contact(request):
    contact_form = ContactForm()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # Enviamos el correo y redireccionamos
            email = EmailMessage(
                    "La Caffettiera nuevo mensaje de contacto", #<---- asunto,
                    "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content), #<---- cuerpo,
                    "no-contestar@imbox.mailtrap.io", #<----email_origen,
                    ["quiquejesus23@hotmail.com"], #<---- email_destino,
                    reply_to=[email]
            )
            try:
                    email.send()
                    #si salio bien el envio
                    return redirect(reverse('contact')+"?ok")
            except:
                    # algo no a salido bien          
                    return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html", {'form':contact_form})
