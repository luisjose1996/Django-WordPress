from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.views.generic import list_detail, date_based
from wordpress.models import Post
import urllib

PER_PAGE = getattr(settings, 'WP_PER_PAGE', 10)

TAXONOMIES = {
    'term': 'post_tag',
    'category': 'category',
    'link_category': 'link_category',
}
 
def object_detail(request, year, month, day, slug):
    slug = urllib.quote(slug.encode('utf-8')).lower()
    return date_based.object_detail(request, queryset=Post.objects.published(),
        date_field='post_date', year=year, month=month, month_format="%m",
        day=day, slug=slug, template_object_name='post', allow_future=True,
        extra_context={'post_url': request.build_absolute_uri(request.path)})
    
def archive_day(request, year, month, day):
    return date_based.archive_day(request, queryset=Post.objects.published(),
        date_field='post_date', year=year, month=month, month_format="%m",
        day=day, template_object_name='post')
    
def archive_month(request, year, month):
    return date_based.archive_month(request, queryset=Post.objects.published(),
        date_field='post_date', year=year, month=month, month_format="%m",
        template_object_name='post')

def archive_year(request, year):
    return date_based.archive_year(request, queryset=Post.objects.published(),
        date_field='post_date', year=year)
    
def archive_index(request):
    p = request.GET.get('p', None)
    if p:
        post = Post.objects.get(pk=p)
        return render_to_response('wordpress/post_detail.html', {'post': post})
    posts = Post.objects.published().select_related()
    return list_detail.object_list(request, queryset=posts,
        paginate_by=10, template_name='wordpress/post_archive.html',
        template_object_name='post', allow_empty=True)

def taxonomy(request, taxonomy, term):
    taxonomy = TAXONOMIES.get(taxonomy, None)
    if taxonomy:
        posts = Post.objects.term(term, taxonomy=taxonomy).select_related()
        return list_detail.object_list(request, queryset=posts,
            paginate_by=10, template_name='wordpress/post_term.html',
            template_object_name='post', allow_empty=True,
            extra_context={'term': term})