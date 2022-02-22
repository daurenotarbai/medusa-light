from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView
from rest_framework.generics import ListAPIView
from .forms import ArticleForm
from .models import Article
from .serializers import ArticleSerializer


def main_view(request):
    return redirect('/login')


class ArticleView(LoginRequiredMixin, CreateView):
    """Создание и получения публикаций"""
    model = Article
    template_name = 'news/article_list.html'
    form_class = ArticleForm
    success_url = 'admin'

    def get_context_data(self, **kwargs):
        kwargs['article_list'] = Article.objects.order_by('-date')
        return super(ArticleView, self).get_context_data(**kwargs)


class ArticleAPIView(ListAPIView):
    """API для получения списка публикаций"""
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


def logout_view(request):
    logout(request)
    return redirect('/login')


@csrf_exempt
def login_view(request):
    logout(request)
    next = request.GET.get('next')
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if next:
                    return redirect(next)
                else:
                    return redirect('/news/admin')
    return render(request, "login.html")
