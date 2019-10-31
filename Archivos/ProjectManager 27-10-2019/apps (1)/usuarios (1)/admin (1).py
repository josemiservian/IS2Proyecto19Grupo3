"""User admin classes."""
# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from apps.usuarios.models import Perfil

#Clases
@admin.register(Perfil)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'usuario', 'estado', 'telefono', 'direccion','picture', 'proyecto_involucrado')
    list_display_links = ('pk', 'usuario',)
    list_editable = ('estado', 'telefono', 'direccion', 'picture')

    search_fields = (
        'usuario__email',
        'usuario__username',
        'usuario__first_name',
        'usuario__last_name',
        'estado',
        'telefono',
        'direccion'
    )

    list_filter = (
        'usuario__is_active',
        'usuario__is_staff',
        'created',
        'modified',
    )

    fieldsets = (
        ('Perfil', {
            'fields': (('usuario', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('estado', 'telefono'),
                ('direccion')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)


class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff',
        
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#admin.site.register(Perfil)