from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Feedback, Category, Post, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .forms import CommentForm, MailForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_http_methods





# Create your views here.

def home(request):

    num_of_visits = request.session.get("num_of_visits", 0)
    request.session["num_of_visits"] = num_of_visits + 1
    
    context = {
        'heading' : 'My first Blog!',
        'services' : Category.objects.all()[:3],
        'posts' : Post.objects.all()[:6],
        'num_of_visits' : num_of_visits,
    }

    return render(request,"home.html", context )

def getPostDetails(request, id):    

    our_post = Post.objects.get(pk = id)

    our_post.views += 1
    our_post.save()

    our_post.category.views +=1
    our_post.category.save()


    
    context = {
        'post' : our_post,
        'categories' : Category.objects.all(),
        'posts' :  Post.objects.filter(category = our_post.category).exclude(pk = our_post.id),
        'commentForm' : CommentForm(),
        'comments' : Comment.objects.filter(post = our_post.id),
    }

    return render(request, 'blog/post_details.html', context)

def saveComment(request, id):
    form = CommentForm(request.POST)
    redirect_url = "/posts/details/"+id


    if form.is_valid():
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']
        message = form.cleaned_data['message']

        user = User.objects.get(pk = 1)
        post = Post.objects.get(pk = id)

        Comment.objects.create(message = message, user = user, post = post)


        return HttpResponseRedirect(redirect_url)

    else:

        return HttpResponseRedirect(redirect_url)






def contact(request):

    context = {
        'number' : '0707320000',
        'email' : 'briangachiri@gmail.com',
        'address': 'somewhere',
        'services' : ["Future Fridays", "Mondays with You", "Oh the weekend"],

    }

    return render(request,"contact.html", context )

def blog(request):

    context = {
        'posts' : Post.objects.all(),
        'all_categories': Category.objects.all(),
        'title' : "All you can read buffet",            

    }

    return render(request,"blog/blog.html", context )

@login_required
def dashboard(request):

    context= {
        'feedback_list' : Feedback.objects.all(),
        'posts' : Post.objects.all(),
        'categories': Category.objects.all(),

    }

    return render(request, "blog/admin/dashboard.html", context)

def saveFeedback(request):

    myname = request.POST.get("name", None)
    myemail = request.POST.get("email", None)
    no= request.POST.get("number", None)
    themessage = request.POST.get("message", None)

    # print(message)

    Feedback.objects.create(name= myname, email= myemail, phone_number = no, message = themessage)

    data = {}

    return JsonResponse(data)

@login_required
def showFeedback(request):

    context = {}
    context['feedback_list'] = Feedback.objects.all()

    return render(request, "blog/admin/feedback.html", context)

@login_required
def showCategories(request):

    context = {
        'category_list' : Category.objects.all()
    }

    return render(request, "blog/admin/categories.html", context)

@login_required
def categoryForm(request):
    context = {}

    return render(request, "blog/admin/category_form.html", context)

@login_required
def storeCategory(request):

    category_name_from_form = request.POST.get("name")

    Category.objects.create(name = category_name_from_form)

    return HttpResponseRedirect('/staff/categories')

@login_required
def deleteCategory(request, id):

    our_category = Category.objects.get(pk = id)
    our_category.delete()

    return HttpResponseRedirect('/staff/categories')


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = "blog/admin/posts.html"
    
@method_decorator(login_required, name="dispatch")
class PostCreate(CreateView):
    model = Post
    template_name = "blog/admin/post_form.html"
    fields = ['title', 'message', 'slug', 'category', 'user', 'keywords', 'image_url']
    success_url = '/staff/posts'

    

@method_decorator(login_required, name="dispatch")
class PostDetails(DetailView):
    model = Post
    template_name = "blog/admin/post_details.html"
    context_object_name = "post"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comments"] = Comment.objects.filter(post = self.kwargs['pk'])
        return context

@method_decorator(login_required, name="dispatch")
class PostUpdate(UpdateView):
    model = Post
    template_name = "blog/admin/post_form.html"
    fields = ['title', 'message', 'slug', 'category', 'user', 'keywords', 'image_url']
    success_url = '/staff/posts'

def getCategoryPosts(request, id):

    category = Category.objects.get(pk = id)
    posts = Post.objects.filter(category = category.id)

    category.views +=1
    category.save()

    context = {
        'posts' : posts,
        'all_categories': Category.objects.all(),
        'title' : "Posts in the category: "+ category.name,
    }

    return render(request, 'blog/blog.html',context)
    
def searchPosts(request):

    search = request.POST.get('searchInput', None)

    posts = Post.objects.filter(message__icontains= search).values()

    data ={
        'posts' : list(posts)
    }

    return JsonResponse(data)


def sendMail(request):

    if request.method == "POST":
        form = MailForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient = form.cleaned_data['recipient']

            send_mail(
                subject,
                message,
                'admin@gmail.com',
                [recipient],
                fail_silently= False
            )

            
            return HttpResponseRedirect('/staff/feedback')
    else:
        context = {
            'form': MailForm
        }

        return render(request, 'blog/admin/send_mail.html', context)

