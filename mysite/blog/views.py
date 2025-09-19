from django.shortcuts import render
from django.http import HttpResponse
from .models import Post,PostCategory,PostSeries

def single_slug(request,single_slug):
	categories = [c.category_slug for c in PostCategory.objects.all()]
	if single_slug in categories:
		matching_series = PostSeries.objects.filter(post_category__category_slug=single_slug)
		series_urls ={}
		for m in matching_series.all():
			part_one = m.post_slug
			series_urls[m] = part_one
		return render(request=request,template_name='blog/category.html',context={"post_series":matching_series,"part_ones":series_urls})
	posts = [p.post_slug for p in Post.objects.all() ]
	if single_slug in posts:
		this_post =  Post.objects.get(post_slug=single_slug)
		return render(request,template_name='blog/post.html',context={'post':this_post})
		#return HttpResponse(f"{single_slug} is a post")
	return HttpResponse(f" {single_slug} does not correspond to anything we know of!")
# Create your views here.
def post_list(request):
    post = PostCategory.objects.all()
    return render(request=request,template_name='post_list.html',context={'categories' : post})
    #return HttpResponse('Hello')
    