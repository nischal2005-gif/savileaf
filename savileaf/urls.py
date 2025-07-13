from django.urls import path
from . import views

urlpatterns = [
    # Main pages
    path('', views.home_view, name='home'),
    path('contact/', views.contact_view, name='contact'),
    path('process/', views.process_view, name='process'),
    path('solution/', views.solution_view, name='solution'),
    path('case-studies/', views.case_studies_view, name='case_studies'),
    
    # Case study details
    path('casestudy/global-retailer/', views.global_retailer_view, name='global_retailer'),
    path('casestudy/techcorp-innovations/', views.techcorp_innovations_view, name='techcorpinnovations'),
    path('casestudy/innovatetech/', views.innovatetech_view, name='innovatetech'),
    
    # Services
    path('services/website-development/', views.website_development_view, name='website_development'),
    path('services/website-redesign/', views.website_redesign_view, name='website_redesign'),
    path('services/web-app-development/', views.web_app_development_view, name='web_app_development'),
    path('services/mobile-app-development/', views.mobile_app_development_view, name='mobile_app_development'),
    path('services/payment-gateway/', views.payment_gateway_view, name='payment_gateway'),
    path('services/ai-solutions/', views.ai_solutions_view, name='ai_solutions'),
    
    # Additional services
    path('services/cloud-computing/', views.cloud_computing_view, name='cloud_computing'),
    path('services/cloud-migration/', views.cloud_migration_view, name='cloud_migration'),
    path('services/corporate-software/', views.corporate_software_view, name='corporate_software'),
    path('services/enterprise-hosting/', views.enterprise_hosting_view, name='enterprise_hosting'),
    path('services/enterprise-software/', views.enterprise_software_view, name='enterprise_software'),
    path('services/<slug:slug>/', views.service_detail, name='service_detail'),
    path('chat/',views.chat_view,name='chat')
]