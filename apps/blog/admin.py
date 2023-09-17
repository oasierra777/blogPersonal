from django.contrib import admin

from apps.blog.models import Post
from apps.blog.models import ViewCount

admin.site.register(Post)
admin.site.register(ViewCount)
