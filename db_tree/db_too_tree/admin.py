from django.contrib import admin

from db_too_tree.models import Dir


@admin.register(Dir)
class DirAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'parent',
    )
    list_editable = ('parent',)
    search_fields = ('title',)
    list_filter = ('create_date',)
    empty_value_display = '-'
