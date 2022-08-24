from django.views.generic import DetailView, ListView, FormView
from post.models import Post, Comment, Tags
from post.forms import CommentForm
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from home.models import Work
from django.shortcuts import get_object_or_404


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


class PostDetail(FormView, DetailView):
    model = Post
    template_name = 'post/post_single.html'
    form_class = CommentForm
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data(**kwargs)
        comments_connected = Comment.objects.filter(post=self.get_object())
        context['comments'] = comments_connected
        context['comment_form'] = CommentForm()
        context['works'] = Post.objects.all()
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


