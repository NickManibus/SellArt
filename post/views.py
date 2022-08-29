from django.views.generic import DetailView, ListView, FormView
from post.models import Post, Comment, Tags
from post.forms import CommentForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from home.models import Work
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

class BlogView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    paginate_by = 2
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = Post.objects.all()
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_single.html'
    slug_url_kwarg = 'post_slug'
    success_url = reverse_lazy('post_single')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.all()
        context['comment_form'] = CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        new_comment = Comment(text=request.POST.get('text'),
                              name=request.POST.get('name'),
                              email=request.POST.get('email'),
                              parent=request.POST.get('parent'),
                              post=self.get_object())

        new_comment.save()
        return HttpResponseRedirect(self.request.path_info)


class TagDetail(DetailView):
    queryset = Tags.objects.all()
    template_name = 'post/detail_tag.html'
    context_object_name = 'detail_tag'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['works'] = Work.objects.all()
        return context
