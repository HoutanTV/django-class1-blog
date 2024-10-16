from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm
from django import http
# Create your views here.


# @login_required()
def post_list_view(request):
    queryset = Post.objects.select_related('author')
    # we convert the queryset to list for caching the queryset
    # objects_list = list(queryset)
    # output= []
    #
    # for object in objects_list:
    #     if object.title == "jfoiwjeofmiowm":
    #         output.append(object)
    return render(request, 'posts.html', {"objects_list": queryset})


class PostListView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 3


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'PostCreate.html'
    success_url = reverse_lazy('posts_list')  # Redirect to the book list view on success

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super().form_valid(form)


def post_view(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'Post.html', {'post': post})


def post_search_view(request):
    title = request.GET.get('title')
    description = request.GET.get('desc')
    category = request.GET.get('category')
    fields = {}

    if title:
        fields['title__icontains'] = title
    if description:
        fields['description__icontains'] = description
    if category:
        fields['category__title'] = category

    queryset = Post.objects.filter(**fields)
    return render(request, 'postsearch.html', {"posts": queryset})
