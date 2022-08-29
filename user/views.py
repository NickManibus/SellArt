from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, FormView, DeleteView
from user.forms import RegisterForm, LoginForm, UpdateUserForm, UserFormWorks
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from home.models import Work, User, Images

from django.shortcuts import HttpResponseRedirect


class LogLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
        return super(LogLoginView, self).form_valid(form)


class RegisterView(SuccessMessageMixin, CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login_page')
    form_class = RegisterForm


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home_page')


def log_out(request):
    logout(request)
    return redirect(reverse("login_page"))


class Profile(UpdateView, DetailView):
    model = User
    template_name = 'profile/profile.html'
    form_class = UpdateUserForm

    def get_context_data(self, *args, **kwargs):
        context = super(Profile, self).get_context_data(*args, **kwargs)
        context['user_form'] = UpdateUserForm( instance=self.request.user)
        context['works'] = Work.objects.filter(author=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return HttpResponseRedirect(reverse('users_profile', kwargs={'slug': self.get_object().slug}))


class CreateWorkView(LoginRequiredMixin, CreateView):
    model = Work
    form_class = UserFormWorks
    template_name = 'profile/create_project.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserFormWorks(instance=self.request.user)
        context['works'] = Work.objects.all()
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.save()
        return HttpResponseRedirect(self.request.path)


class UpdateWorkView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Work
    form_class = UserFormWorks
    template_name = 'profile/create_project.html'
    success_url = reverse_lazy('home_page')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        work = self.get_object()
        if self.request.user == work.author:
            return True
        return False

class DeleteWorkView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Work
    template_name = 'profile/work_delete.html'
    success_url = reverse_lazy('home_page')

    def test_func(self):
        work = self.get_object()
        if self.request.user == work.author:
            return True
        return False
