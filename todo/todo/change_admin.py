from django.contrib.auth import get_user_model

# User = get_user_model()
# User.objects.create_superuser("admin", "dev@email.io", "admin")
user = get_user_model().objects.get(username="admin")
user.set_password("admin")
user.save()
