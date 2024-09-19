from django.http import HttpResponse
from django.contrib.auth import get_user_model


def create_superuser(request):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )
        return HttpResponse("Superuser created successfully.")
    else:
        return HttpResponse("Superuser already exists.")