from django.shortcuts import render, redirect
from home.forms import FormContact
from home.models import Work, Video, FeedBackContact, Images, Tags
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.core.mail import send_mail
from django.template.loader import render_to_string


class WorkList(ListView):  # Home_page
    model = Work
    template_name = 'works.html'
    context_object_name = 'works'
    paginate_by = 3


class WorkDetail(DetailView):
    model = Work
    template_name = 'works/works_single.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = Work.objects.all()
        return context


class VideoList(ListView):
    model = Video
    template_name = 'works/video_list.html'
    context_object_name = 'video'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = Video.objects.all()
        return context


class WorkVideo(DetailView):
    model = Video
    template_name = 'works/single_video.html'
    context_object_name = 'video'
    slug_url_kwarg = 'video_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = Video.objects.all()
        return context


def contact_view(request):
    if request.method == 'POST':
        form = FormContact(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            html = render_to_string('contact/contact_message.html', {
                'full_name': full_name,
                'email': email,
                'message': message
            })

            send_mail('The contact form subject', 'This is the message', 'nickmanibus@gmail.com',
                      ['nickmanibus@gmail.com'], html_message=html)
            return render(request, 'contact.html')
    else:
        form = FormContact()
    return render(request, 'contact.html', {'form': form})


def about_view(request):
    return render(request, 'about.html', {})


class TagDetailWork(DetailView):
    queryset = Tags.objects.all()
    template_name = 'works/tag_detail.html'
    context_object_name = 'tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = Work.objects.all()
        return context