from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class AccessMixin(LoginRequiredMixin):
    """
    Миксин для ограничения доступа на основе ролей.
    Если роль не разрешена, выполняется перенаправление на указанную страницу.
    """

    allowed_roles:list = []
    redirect_url:str = '/'


    def handle_no_permission(self):
        """
        Метод, вызываемый, если доступ запрещен.
        """
        return redirect(self.redirect_url)
    
    def dispatch(self, request, *args, **kwargs):
        """
        Проверяет, соответствует ли пользователь разрешенным ролям перед выполнением представления.
        """
        # Проверяем, авторизован ли пользователь (обрабатывается LoginRequiredMixin)
        if not request.user.is_authenticated:
            return super().handle_no_permission()

        user_role = getattr(request.user, 'role', None)

        # Проверяется роль пользователя добавленая во view с ролью текущего пользователя
        if user_role not in self.allowed_roles:
            return self.handle_no_permission()

        # Если все проверки пройдены, вызываем метод dispatch родительского класса
        return super().dispatch(request, *args, **kwargs)