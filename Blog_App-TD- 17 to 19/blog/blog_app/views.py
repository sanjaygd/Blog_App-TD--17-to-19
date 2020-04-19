from django.shortcuts import render,get_object_or_404

from .models import Post

def post_list(request):
    queryset = Post.objects.all()
    context = {
        'object_list' : queryset
    }
    return render(request,'blog_app/post_list.html',context)


def post_details(request,pk=None):
    instance = get_object_or_404(Post,pk=pk)
    context = {
        'obj_details':instance
    }
    return render(request,'blog_app/post_details.html',context)


 