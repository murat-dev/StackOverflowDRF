from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


class ImageInline(admin.TabularInline):
    model = CodeImage
    max_num = 7
    min_num = 1


@admin.register(Problem)
class ProblemAdmin(TranslationAdmin):
    inlines = [ImageInline,]
    list_display = ('title',)


admin.site.register(Reply)
admin.site.register(Comment)