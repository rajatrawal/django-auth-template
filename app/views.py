from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetCompleteView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetView
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site

from account import settings
from . forms import UserCreationForm
from . tokens import account_activation_token


def index(request):
    return render(request, 'app/index.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('signin')
    template_name = 'app/signup.html'

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        try:
            user = User.objects.get(username=username)
            if user.is_active == False:
                user.delete()
        except:
            pass

        response = super().post(request, *args, **kwargs)

        if response.status_code == 302:
            user = User.objects.get(username=username)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string(
                'app/email/account_activate_email.html',
                {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                }
            )
            mail_subject = 'Activate your account.'
            form = self.get_form()
            try:
                send_mail(
                    subject=mail_subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[username],
                    fail_silently=False,
                )
                messages.success(
                    request,
                    'Account activation link has been sent to your email id. please check your inbox and if it is not there check your spam as well.'
                )
            except Exception as e:
                message.error(
                    request, "An error occured in sending message.Please try again.")
            return self.render_to_response({'form': form})
        else:
            return response


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, 'Signed In Successfully!')
        return redirect(reverse_lazy('index'))
    else:
        return HttpResponse('Activation link has been expired or invalid. Please try to signup or signin.')


class SignInView(LoginView):
    template_name = 'app/signin.html'
    next_page = reverse_lazy('index')


class SignOutView(LogoutView):
    next_page = reverse_lazy('index')


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'app/change_password.html'
    success_url = "reset_password_complete"


class MyPasswordResetView(PasswordResetView):
    template_name = 'app/password_reset_form.html'
    email_template_name = 'app/email/password_reset_email.html'


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'app/password_reset_done.html'


class MyPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'app/password_reset_confirm.html'


class MyPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'app/password_reset_complete.html'
