from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from django.views import View
from django.views.generic.edit import FormView
from django.contrib.auth import login as auth_login, logout as logout_auth, \
    authenticate
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import RegistrationForm


class LoginAuth(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            redirectpath = request.META.get('HTTP_REFERER') + '#ret'
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect(redirectpath)
            else:
                if not username and not password:
                    return HttpResponseRedirect(redirectpath)
                else:
                    '''Передача ссобщения в шаблон путём `messages`,
                        использование куки (либо сесий),
                        также следует выставить переменную
                        `MESSAGE_STORAGE` в settings.py'''
                    messages.add_message(
                        request, messages.ERROR,
                        'Проверьте корректность полей <br> логин и пароль.',
                        extra_tags='login')
                    return HttpResponseRedirect(redirectpath)
        return super(LoginAuth).dispatch(request, *args, **kwargs)


class LogoutUser(RedirectView):
    def get(self, request, *args, **kwargs):
        logout_auth(request)
        self.url = request.META.get('HTTP_REFERER')
        return super(LogoutUser, self).get(request, *args, **kwargs)


class Registration(FormView):
    template_name = 'loginsys/registration.html'
    form_class = RegistrationForm

    def form_valid(self, form):
        form.save()
        self.success_url = self.request.META.get('HTTP_REFERER')
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'])
        # Передача сообщения через сессию в `request`
        self.request.session['success_message'] = \
            'Регистрация прошла успешно'
        self.request.session.set_expiry(0)
        auth_login(self.request, user)
        return super(Registration, self).form_valid(form)
