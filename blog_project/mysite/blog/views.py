from datetime import timezone
from typing import List
from django.shortcuts import render
from django.views.generic import(TemplateView,ListView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post 

    def get_queryset(self):
        return Post.objects.filter(published_date_lte = timezone.now().order_by('-published_date')) 