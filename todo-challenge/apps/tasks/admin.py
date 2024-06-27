from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task, Label

class LabelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status', 'priority', 'created_at', 'updated_at', 'parent_task')
    list_filter = ('status', 'priority', 'created_at')
    search_fields = ('title', 'description')
    autocomplete_fields = ['labels', 'parent_task']
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'status', 'priority', 'parent_task')
        }),
        ('Labels', {
            'fields': ('labels',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Task, TaskAdmin)
admin.site.register(Label, LabelAdmin)
