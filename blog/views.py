from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import UpdateView, DeleteView,CreateView 
from django.urls import reverse_lazy 
from .models import Post


class BlogListView(ListView):
    model = Post
    template_name = 'post_list.html'

class BlogDetailView(DetailView): 
    model = Post
    template_name = 'post_detail.html'

class BlogUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView): 
    model = Post
    fields = ('title','body',)
    template_name = 'post_edit.html'
    success_url = reverse_lazy('post_list')

class BlogDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView): 
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

class BlogCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView): 
    model = Post
    template_name = 'post_new.html'
    fields = ('title','body',)
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


