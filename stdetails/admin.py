from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    pass
admin.site.resiter(Post,PostAdmin)
# Register your models here.
