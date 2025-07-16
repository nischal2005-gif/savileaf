# # yourapp/tasks.py

# # from celery import shared_task
# # from django.core.mail import EmailMessage
# # from django.conf import settings
# # import base64
# # @shared_task
# # def send_contact_emails(name, email, message, file_data=None, file_name=None, file_type=None):
# #     # Email to admin
# #     subject = f'Contact Form Submission from {name}'
# #     body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'
# #     admin_email = EmailMessage(subject, body, settings.EMAIL_HOST_USER, ['nischalgautam9866@gmail.com'])
    
# #     if file_data:
# #         decoded_file = base64.b64decode(file_data)  # ✅ Decode before attaching
# #         admin_email.attach(file_name, decoded_file, file_type)
# #     admin_email.send(fail_silently=False)

# #     # Confirmation email to user
# #     confirmation_subject = "We have received your message"
# #     confirmation_body = (
# #         f"Dear {name},\n\n"
# #         "Thank you for contacting us. We have received your message and will get back to you shortly.\n\n"
# #         f"Your message:\n{message}\n\n"
# #         "Best regards,\nSavileaf"
# #     )
# #     user_email = EmailMessage(confirmation_subject, confirmation_body, settings.EMAIL_HOST_USER, [email])
    
# #     if file_data:
# #         decoded_file = base64.b64decode(file_data)  # ✅ Decode again
# #         user_email.attach(file_name, decoded_file, file_type)
# #     user_email.send(fail_silently=False)

# from celery import shared_task
# from django.core.mail import EmailMessage
# from django.conf import settings
# import requests

# @shared_task
# def send_contact_emails(name, email, message, uploaded_file_data=None, uploaded_file_name=None, uploaded_file_type=None):
#     # Email to site admin
#     subject = f'Contact Form Submission from {name}'
#     body = f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}'

#     admin_email = EmailMessage(
#         subject,
#         body,
#         settings.EMAIL_HOST_USER,
#         ['nischalgautam9866@gmail.com'],
#     )

#     if uploaded_file_data:
#         admin_email.attach(uploaded_file_name, uploaded_file_data, uploaded_file_type)

#     admin_email.send(fail_silently=False)

#     # Confirmation email to user
#     confirmation_subject = "We have received your message"
#     confirmation_body = (
#         f"Dear {name},\n\n"
#         "Thank you for contacting us. We have received your message and will get back to you shortly.\n\n"
#         f"Your message:\n{message}\n\n"
#         "Best regards,\nSavileaf"
#     )

#     confirmation_email = EmailMessage(
#         confirmation_subject,
#         confirmation_body,
#         settings.EMAIL_HOST_USER,
#         [email]
#     )

#     if uploaded_file_data:
#         confirmation_email.attach(uploaded_file_name, uploaded_file_data, uploaded_file_type)

#     confirmation_email.send(fail_silently=False)
