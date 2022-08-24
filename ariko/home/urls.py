from django.urls import path
from home.views import WorkList, WorkDetail, WorkVideo, VideoList, about_view, contact_view, TagDetailWork
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic.base import RedirectView


urlpatterns = [

    path('works/video_list/', VideoList.as_view(), name='video_list'),
    path('works/<slug:slug>/', WorkDetail.as_view(), name='works_detail'),
    path('works/single_video/<slug:video_slug>/', WorkVideo.as_view(), name='single_video'),
    path('works/', WorkList.as_view(), name='home_page'),
    path('about/', about_view, name='about_page'),
    path('contact/', contact_view, name='contact_page'),
    path('work/tag/<str:slug>', TagDetailWork.as_view(), name='tag_detail'),
    path('', lambda request: redirect(reverse('home_page'))),

]
