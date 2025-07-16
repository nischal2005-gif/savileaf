from django.shortcuts import render,get_object_or_404,redirect
from .models import *
import requests
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .tasks import send_contact_emails


# Main pages views
def home_view(request):
    return render(request, 'index.html')

# def contact_view(request):      
#     if request.method == 'POST':
#         recaptcha_response = request.POST.get('g-recaptcha-response')
#         secret_key = '6LfIjXorAAAAAMGK5XwY3wAOwbD89BVvn5UgyyEm'
#         data = {
#             'secret': secret_key,
#             'response': recaptcha_response
#         }
#         r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
#         result = r.json()

#         if result.get('success'):
#             name = request.POST.get('fullname')
#             email = request.POST.get('email')
#             message = request.POST.get('message')
#             uploaded_file = request.FILES.get('attachment')
            
#             abstract_api_key = 'fb8d8ec26246441d9dfe9e6bed15ce9b'  # Your Abstract API key
#             abstract_url = f'https://emailvalidation.abstractapi.com/v1/?api_key={abstract_api_key}&email={email}'
#             response = requests.get(abstract_url,timeout=3)
#             email_validation_result = response.json()

#             if email_validation_result.get('deliverability') == 'DELIVERABLE':
#                 # Email to site admin
#                 subject = f'Contact Form Submission from {name}'
#                 body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'

#                 email_message = EmailMessage(
#                     subject,
#                     body,
#                     settings.EMAIL_HOST_USER,
#                     ['nischalgautam9866@gmail.com'],
#                 )

#                 if uploaded_file:
#                     email_message.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)

#                 email_message.send(fail_silently=False)

#                 # Email confirmation to user
#                 confirmation_subject = "We have received your message"
#                 confirmation_body = (
#                     f"Dear {name},\n\n"
#                     "Thank you for contacting us. We have received your message and will get back to you shortly.\n\n"
#                     f"Your message:\n{message}\n\n"
#                     "Best regards,\nSavileaf"
#                 )
#                 confirmation_email = EmailMessage(
#                     confirmation_subject,
#                     confirmation_body,
#                     settings.EMAIL_HOST_USER,
#                     [email]
#                 )

#                 if uploaded_file:
#                     uploaded_file.seek(0)  # reset file pointer to start before attaching again
#                     confirmation_email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)

#                 confirmation_email.send(fail_silently=False)

#                 messages.success(request, 'Your message has been sent successfully. A confirmation email has been sent to your address.')
#                 return redirect('contact')
#             else:
#                 messages.error(request, 'The email address you entered is not valid or deliverable. Please check and try again.')
#                 return redirect('contact')
#         else:
#             messages.error(request, 'Invalid reCAPTCHA. Please try again.')
#             return redirect('contact')

#     return render(request, 'contact.html')
def contact_view(request):      
    if request.method == 'POST':
        recaptcha_response = request.POST.get('g-recaptcha-response')
        secret_key = '6LfIjXorAAAAAMGK5XwY3wAOwbD89BVvn5UgyyEm'
        data = {
            'secret': secret_key,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        if result.get('success'):
            name = request.POST.get('fullname')
            email = request.POST.get('email')
            message = request.POST.get('message')
            uploaded_file = request.FILES.get('attachment')
            
            abstract_api_key = 'fb8d8ec26246441d9dfe9e6bed15ce9b'  # Your Abstract API key
            abstract_url = f'https://emailvalidation.abstractapi.com/v1/?api_key={abstract_api_key}&email={email}'
            response = requests.get(abstract_url,timeout=3)
            email_validation_result = response.json()

            if email_validation_result.get('deliverability') == 'DELIVERABLE':
                # Email to site admin
                subject = f'Contact Form Submission from {name}'
                body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
                file_data = uploaded_file.read() if uploaded_file else None
                file_name = uploaded_file.name if uploaded_file else None
                file_type = uploaded_file.content_type if uploaded_file else None
                send_contact_emails.delay(name, email, message, file_data, file_name, file_type)


                messages.success(request, 'Your message has been sent successfully. A confirmation email has been sent to your address.')
                return redirect('contact')
            else:
                messages.error(request, 'The email address you entered is not valid or deliverable. Please check and try again.')
                return redirect('contact')
        else:
            messages.error(request, 'Invalid reCAPTCHA. Please try again.')
            return redirect('contact')

    return render(request, 'contact.html')

def process_view(request):
    return render(request, 'process.html')

def solution_view(request):
    return render(request, 'solution.html')

def case_studies_view(request):
    return render(request, 'caseStudies.html')

# Case study detail views
def global_retailer_view(request):
    return render(request, 'casestudyDetailPage/global-retailer.html')

def techcorp_innovations_view(request):
    return render(request, 'casestudyDetailPage/techCorp-innovations.html')

def innovatetech_view(request):
    return render(request, 'casestudyDetailPage/innovatetech.html')

# Services views
def website_development_view(request):
    return render(request, 'services/website-developement.html')

def website_redesign_view(request):
    return render(request, 'services/website-redesign-modernisation.html')

def web_app_development_view(request):
    return render(request, 'services/web-app-development.html')

def mobile_app_development_view(request):
    return render(request, 'services/mobile-app-development.html')

def payment_gateway_view(request):
    return render(request, 'services/payment-gateway-integration.html')

def ai_solutions_view(request):
    return render(request, 'services/ai-business-solutions.html')

# Additional services views (from your image)
def cloud_computing_view(request):
    return render(request, 'services/cloud-computing.html')

def cloud_migration_view(request):
    return render(request, 'services/cloud-migration.html')

def corporate_software_view(request):
    return render(request, 'services/corporate-software.html')

def enterprise_hosting_view(request):
    return render(request, 'services/enterprise-hosting.html')

def enterprise_software_view(request):
    return render(request, 'services/enterprise-software.html')


def service_detail(request, slug):
    service = get_object_or_404(DropdownMenuItem, url_name=slug, active=True)
    return render(request, 'services/service_detail.html', {'service': service, 'page_title': service.section_title 
})

