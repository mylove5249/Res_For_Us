from django.shortcuts import render
from django.views.generic.base import TemplateView, View
from django.views.generic import CreateView, DetailView
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import AccessMixin
from forum.models import Forum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse



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

class ForumDV(DetailView):
    model = Forum 
    template_name = "forum/forum_detail.html"
    context_object_name = 'object'

class SearchView(View):
    def get(self, request):

        search_type = request.GET['type']
        search_name = request.GET['name']

        connection_info = { 'host': 'localhost', 'db': 'res_for_us', 'user': 'root', 'password': 'Kweondh123!', 'charset': 'utf8' }
        import pymysql

        conn = pymysql.connect(**connection_info)
        cursor = conn.cursor()
        sql = "select subject, address, DATE_FORMAT(last_updated, \"%Y년 %m월 "+"%"+"d일\"), slug, owner_id from forum_forum where "+ search_type + " like \"%" + search_name + "%\""
        cursor.execute(sql)
        row = cursor.fetchall()
        keys = ["subject", "address", "last_updated", "slug", "owner"]
        result = []
        for row_idx in row:
            result.append(dict(zip(keys, row_idx)))

        conn.close()

        import json

        json_result = json.dumps(result, ensure_ascii=False)
        return HttpResponse(json_result, content_type="application/json") 

