from django.views.generic import CreateView

from .models import CustomUser
from .forms import CustomUserForm


class UserCreateView(CreateView):
    model = CustomUser
    form_class = CustomUserForm
    context_object_name = "create_user"
    success_url = "/"
    template_name = "registration/register.html"


