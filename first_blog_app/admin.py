from django.contrib import admin
from .models import Category, Post



### Configuration of Category Admin.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)

### Register your category models here.
admin.site.register(Category,CategoryAdmin)


### Configuration of Category Admin.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 10

    class Media:
        js=("https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js", 'js/script.js',)

### Register your post models here.
admin.site.register(Post, PostAdmin)
