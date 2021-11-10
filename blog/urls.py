"""django_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from blog import views
from django.conf import settings
from django.conf.urls.static import static
from .views import PostList, PostCreate, PostDetails, PostUpdate


staff_patterns = [
    path('dashboard', views.dashboard, name="dashboard"),
    path('feedback', views.showFeedback, name="feedback"),
    path('categories', views.showCategories, name="categories"),
    path('category/form', views.categoryForm, name="add_category"),
    path('store/category', views.storeCategory, name="store_category"),
    path('delete/category/<id>', views.deleteCategory, name="delete_category"),
    path('posts', PostList.as_view(), name="posts"),
    path('create/post', PostCreate.as_view(), name="add_post"),
    path('view/posts/<pk>', PostDetails.as_view(), name="view_post"),
    path('update/posts/<pk>', PostUpdate.as_view(), name="update_post"),
    path('send/mail', views.sendMail, name="send_mail")




]


urlpatterns = [
    path('', views.home, name="home" ),
    path('contact', views.contact, name="contact"),
    path('all/posts', views.blog, name="blog"),
    path('staff/', include(staff_patterns)),
    path('save/feedback', views.saveFeedback, name="save_feedback"),
    path('posts/details/<id>', views.getPostDetails, name="post_details"),
    path('save/comment/<id>', views.saveComment, name="save_comment"),
    path('posts/category/<id>', views.getCategoryPosts, name="category_posts"),
    path('search', views.searchPosts, name="search")
    
]

