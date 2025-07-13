from django.shortcuts import render,get_object_or_404
from .models import *
from django.core.mail import send_mail
from django.conf import settings
import openai,os,json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
openai.api_key=settings.OPENAI_API_KEY
client = OpenAI()

def get_context():
    file_path = os.path.join(os.path.dirname(__file__), 'site_info.txt')
    with open(file_path, 'r') as file:
        return file.read()

@csrf_exempt
def chat_view(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "").strip()

            if not user_message:
                return JsonResponse({"error": "Empty message"}, status=400)

            context = get_context()

            system_prompt = (
                "You are an AI assistant for Savileaf. "
                "You have the following knowledge:\n" + context +
                "\nOnly answer questions directly related to Savileaf's services. "
                "If the user asks about anything else, politely decline."
            )

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_message}
                ],
                temperature=0.7,
                max_tokens=400
            )

            reply = response.choices[0].message.content.strip()
            return JsonResponse({"reply": reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "POST request required"}, status=405)

# Main pages views
def home_view(request):
    return render(request, 'index.html')

def contact_view(request):
     if request.method == 'POST':
        name = request.POST.get('fullname')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        subject = f'Contact Form Submission from {name}'
        body = f'Email: {email}\n\nMessage:\n{message}'

        send_mail(
            subject,
            body,
            settings.EMAIL_HOST_USER,  
            ['nischalgautam9866@gmail.com'],  
            fail_silently=False
        )
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

# def service_detail(request, slug):
#     service = get_object_or_404(Service, slug=slug)
#     features = service.features.all()
#     return render(request, 'services/service_detail.html', {
#         'service': service,
#         'features': features,
#     })
def service_detail(request, slug):
    service = get_object_or_404(DropdownMenuItem, url_name=slug, active=True)
    return render(request, 'services/service_detail.html', {'service': service, 'page_title': service.section_title 
})

