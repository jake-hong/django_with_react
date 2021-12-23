from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'message', 'message_length','is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at','is_public']
    search_fields = ['message']

    # def message_length(self, post):
    #     return len(post.message)