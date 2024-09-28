from django.shortcuts import render
from .models import Post
# Create your views here.


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
