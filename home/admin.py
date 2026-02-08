from django.contrib import admin
from .models import Person

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'college', 'dob', 'marital_status', 'employed')
    search_fields = ('name', 'college')
    list_filter = ('marital_status', 'employed')