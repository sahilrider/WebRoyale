from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect

from .models import Post,Comment
from .forms import CommentForm
'''from .forms import CommentForm'''
def index(request):
    return render(request,'blog/index.html',{'posts':Post.objects.all()})

def view_post(request, post_id):
	post=get_object_or_404(Post,pk=post_id)
	if request.method=='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			comment=form.save(commit=False)
			comment.post=post
			comment.save()
			return redirect('blog:view_post',post_id=post_id)
	else:
		form=CommentForm()
	return render(request,'blog/view_post.html',{'post':post,'form':form})




