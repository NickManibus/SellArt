from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DetailView, FormView
from user.forms import RegisterForm, LoginForm, UpdateUserForm, UserFormWorks, ImageForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin, messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
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
    success_url = reverse_lazy('users_profile')

    def get_context_data(self, **kwargs):
        context = super(Profile, self).get_context_data(**kwargs)
        context['user_form'] = UpdateUserForm(instance=self.request.user)
        context['works'] = Work.objects.filter(author=self.request.user)
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.save()
        return HttpResponseRedirect(reverse('users_profile', kwargs={'slug': self.get_object().slug}))


class PostCreateView(LoginRequiredMixin, FormView):
    model = Work
    form_class = UserFormWorks
    template_name = 'profile/create_project.html'
    success_url = reverse_lazy('users_profile')

    def get_context_data(self, **kwargs):
        context = super(PostCreateView, self).get_context_data(**kwargs)
        context['form'] = UserFormWorks(instance=self.request.user)
        context['works'] = Work.objects.all()
        return context

    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        images = request.FILES.getlist('Images')
        if form.is_valid():
            form.save()
            for img in images:
                file = Images(images=img)
                file.save()
            messages.success(request, 'New Project Added')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

# def post_create_view(request):
    #     if request.method == 'POST':
    #         form = UserFormWorks(request.POST, request.FILES)
    #         if form.is_valid():
    #
    #             form.save()
    #             return HttpResponseRedirect('users_profile')
    #     else:
    #         form = UserFormWorks()
    #     return render(request, 'profile/create_project.html', {'form': form})
