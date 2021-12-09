from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account
# Register your models here.

class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'last_login', 'date_joined', 'is_active')
    list_display_links = ('email', 'username', 'first_name', 'last_name')   # Campos con enlaces a páginas de detalles trang
    readonly_fields = ('last_login', 'date_joined')     # Permitir solo lectura
    ordering = ('-date_joined',)     # Ordenar al revés

    #Requerido para declarar
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
admin.site.register(Account,AccountAdmin)
