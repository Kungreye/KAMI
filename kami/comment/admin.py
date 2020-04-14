from django.contrib import admin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')

    def save_model(self, request, obj, form, change):
        return super(CommentAdmin, self).save_model(request, obj, form, change)
