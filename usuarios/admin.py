# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.datastructures import MultiValueDict, MergeDict  # para que select retorne una lista

from usuarios.models import Usuario


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email', 'nombre', 'apellidos', 'password1', 'password2',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user




# class SelectSingleAsList(forms.Select):
#     def value_from_datadict(self, data, files, name):
#         if isinstance(data, (MultiValueDict, MergeDict)):
#             return data.getlist(name)  # NOTE this returns a list rather than a single value.
#         return data.get(name, None)


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField(label=_("Password"),
        help_text=_("Raw passwords are not stored, so there is no way to see "
                    "this user's password, but you can change the password "
                    "using <a href=\"password/\">this form</a>."))

    class Meta:
        model = Usuario
        widgets = {
            'groups': admin.widgets.FilteredSelectMultiple('Permisos', False)
        }

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UsuarioAdmin(UserAdmin):

    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm
    
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'nombre', 'apellidos', 'tipo', 'is_active', 'is_admin', 'is_superuser')
    list_filter = ('is_admin',)
    fieldsets = (
        
        ('Información personal', {'fields': ('nombre', 'apellidos', 'email', 'tipo', 'user_creador')}),
        ('Permisos', {'fields': ('is_active', 'is_admin', 'groups')}),
        ('Cambiar Contraseña', {'fields': ('last_login', 'password')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        ('Crear Nuevo Usuario', {
            'classes': ('wide',),
            'fields': add_form.Meta.fields }
        ),
    )

    def save_model(self, request, obj, form, change):

        if change:
            obj.save()

        elif request.user.is_superuser:
            obj.tipo = Usuario.NACIONAL
            obj.is_admin = True
            obj.user_creador = request.user
            obj.save()
            print obj.is_superuser

            g = Group.objects.get(name="nacional")
            obj.groups.add(g)

        elif request.user.tipo == Usuario.NACIONAL:
            obj.tipo = Usuario.LOCAL
            obj.is_admin = True
            obj.user_creador = request.user
            obj.save()

            g = Group.objects.get(name="local")
            obj.groups.add(g)

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    readonly_fields = ('last_login', 'is_superuser', 'user_creador')

    #Muestra en el admin solo los modelos creados por el usuario y al usuario mismo
    def queryset(self, request): 
        qs = super(UsuarioAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        elif request.user.tipo == Usuario.NACIONAL:
            return qs.filter(tipo=Usuario.LOCAL)
        return qs.filter(user_creador=request.user.id)

# Now register the new UserAdmin...
admin.site.register(Usuario, UsuarioAdmin)
