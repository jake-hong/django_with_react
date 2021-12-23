from django.contrib import admin
from .models import Post


# 등록법1
# admin.site.register(Post)

# 등록법2
# class PostAdmin(admin.ModelAdmin):
#    pass

# 등록법3
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
