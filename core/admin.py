from django.contrib import admin
from core.models import *

# Register your models here.

admin.site.register(Setting)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Testimonial)
admin.site.register(Contact)
admin.site.register(Advertising)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','like','dislike','views','created_at','updated_at')
    search_fields = ('title','content','created_at','updated_at')
    list_filter = ('created_at','updated_at')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    readonly_fields = ('like','dislike','views','created_at','updated_at')
    

    # fieldsets = (
    #     (None,{
    #         'fields': ('title','content','category','image')
    #     }),
    #     ('Advanced options', {
    #         'classes': ('collapse',),
    #         'fields':('like','dislike','views','created_at','updated_at')

    #     }),
    # )

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.site_header = "P-806"
admin.site.site_title = "P-806"