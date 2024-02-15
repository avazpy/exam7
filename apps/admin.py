from django.contrib import admin

from apps.models import Person, Category


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
