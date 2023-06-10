from django.contrib import admin
from .models import Conta

class ContaInline(admin.TabularInline):
    model = Conta

@admin.register(Conta)
class ContaAdmin(admin.ModelAdmin):
    pass 


