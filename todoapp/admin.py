from django.contrib import admin


from todoapp.models import Task

# from .models import Task

# Register your models here.


@admin.register(Task)
class Taskadmin(admin.ModelAdmin):
    list_display = (
        "title",
        "description",
        "due_date",
        "user",
        "create_time",
        "edit_time",
    )
    readonly_fields = ("create_time", "edit_time", "user")
    search_fields = ("title", "create_time", "edit_time")


# admin.site.register(Task)
