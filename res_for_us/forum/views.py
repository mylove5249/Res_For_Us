from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic import CreateView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from forum.models import Forum
from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.

class ForumLV(ListView):
    # 목록 조회
    model = Forum # Post.objects.all()
    # 템플릿(default : blog/post_list.html)에 데이터(default : object_list) 전달
    template_name = "forum/forum_index.html"
    context_object_name = 'forums'
    paginate_by = 10 # 페이징 처리 설정 (한 화면에 2개씩 표시)

class ForumCreateView(LoginRequiredMixin, CreateView):
    model = Forum
    # fields = ['title', 'slug', 'description', 'content', 'tags']
    fields = ['subject', 'slug', 'address', 'cleaned', 'taste', 'kindness', 'message']
    initial = {'slug': 'auto-filling-do-not-input'} 
    #fields = ['title', 'description', 'content', 'tags'] 
    success_url = reverse_lazy('forum:index')
    

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)