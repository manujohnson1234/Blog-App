from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Category
from .forms import PostForm, EditForm
# Create your views here.


class HomeView(generic.ListView):
    model = Post
    template_name = 'blogsite/home.html'
    context_object_name = 'blogs'
    ordering = ['-posted']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class DetailHome(generic.DetailView):
    model = Post
    template_name = 'blogsite/detail.html'
    context_object_name = 'blog'

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DetailHome, self).get_context_data(**kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['cat_menu'] = cat_menu
        context['total_likes'] = total_likes
        context['liked'] = liked

        return context


class CreatePost(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'blogsite/create.html'
    form_class = PostForm
    # fields = ['title', 'title_tag', 'author', 'body']
    success_url = reverse_lazy('blogs')

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(CreatePost, self).get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super(CreatePost, self).form_valid(form)


class UpdatePost(LoginRequiredMixin, generic.UpdateView):
    model = Post
    template_name = 'blogsite/update.html'
    form_class = EditForm

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(UpdatePost, self).get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context


class DeletePost(LoginRequiredMixin, generic.DeleteView):
    model = Post
    template_name = 'blogsite/delete.html'
    success_url = reverse_lazy('blogs')

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(DeletePost, self).get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context


class AddCategoryView(LoginRequiredMixin, generic.CreateView):
    model = Category
    template_name = 'blogsite/category.html'
    # form_class = PostForm
    fields = "__all__"
    success_url = reverse_lazy('add_category')

    def get_context_data(self, **kwargs):
        cat_menu = Category.objects.all()
        context = super(AddCategoryView, self).get_context_data(**kwargs)
        context['cat_menu'] = cat_menu
        return context


def categoryView(request, cats):
    category_post = Post.objects.filter(category=cats.replace('-', ' '))
    category = Category.objects.all()
    return render(request, 'blogsite/catView.html', {'category_post': category_post, 'cats': cats.replace('-', ' '),
                                                     'category': category})


def likeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('blog', args=[str(pk)]))

