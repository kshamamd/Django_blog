from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Like, Task
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
import json


def home(request):
    context = {
        'posts': Post.objects.all(),
    }
        # a = get_object_or_404('', pk=pk)
    return render(request, 'template/home.html', context)

#there are classbased views and function based views in FV we have to pass fun explictly and render


class PostListView(ListView):
    model = Post
    template_name = 'template/home.html'#<app>/<model>_<viewtype>.html
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
    template_name = 'template/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'template/post_form.html'
#success url

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


#template inheritance
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):#authenticate user
    model = Post
    fields = ['title', 'content']
    template_name = 'template/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):            #exact current post to update
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'template/post_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


#class PostLikedRedirect(RedirectView):
 #   def get_redirect_url(self, *args, **kwargs):
 #       pk = self.kwargs.get("pk")   #slug ay be a object change the name
  #      print(pk)#see whats printing
   #     obj = get_object_or_404(Post, pk=pk)
    #    return obj.get_absolute_url()


# Create your views here.

#def like(request, pk):
    #    post = get_object_or_404(Post, id=request.POST.get('post_id'))
     #   post.likes.add(request.user)
      #  return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))


def search(request):
    query = request.POST['search']
    posts = Post.objects.filter(title__iexact=query)
    para = {'posts': posts}

    return render(request, 'template/search.html', para)

#redirect and return render are different redirect will redirect you to specific path but
# reverse will specify strng to that route
#i need to create all the class based function as for posts including model as data will stored in the database


def task_com(request):
    task = Task.objects.all()        #filter(post=request.post.id)
    context = {
        'tasks': task,
    }
    print('hello')
    return render(request, 'template/post_detail.html', context)

