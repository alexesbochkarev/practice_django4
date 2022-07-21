from django.contrib import admin
from blog.models import Post

#admin.site.register(Post)

@admin.register(Post)
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'data_updated', 'author']
    prepopulated_fields = {'slug': ("title",)}