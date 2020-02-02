from django.contrib import admin
from rango.models import Category, Page


class TabPages(admin.TabularInline):
    model = Page
    fields = ["title", "url", "views"]
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
#    fields = ["likes", "name", "views"]
    prepopulated_fields = {"slug": ('name',)}
    inlines = [TabPages]
    list_display = ("name", "likes", "views")

class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "url", "views")

# Register the models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
