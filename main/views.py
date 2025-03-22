from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render,redirect


def index(request):
    return render(request, 'main/home.html')


@csrf_exempt  # Remove this if CSRF protection is needed
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if not (name and email and message):
            return JsonResponse({'status': 'error', 'message': 'All fields are required'}, status=400)

        subject = f"New Contact Form Submission from {name}"
        email_body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        try:
            send_mail(
                "Contact Form Submission",
                email_body,
                
                settings.EMAIL_HOST_USER,  # Sender email (configured in settings.py)
                ['lieo50672@gmail.com'],  # Send a copy to user
                fail_silently=False
            )

            return redirect('index')
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)
