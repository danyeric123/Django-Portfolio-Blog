from django.contrib import admin
from blog.models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
  pass

class CategoryAdim(admin.ModelAdmin):
  pass

admin.site.register(Post, PostAdmin)
admin.site.register(Category,CategoryAdim)