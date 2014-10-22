# -*- coding: utf-8 -*-
from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext, ugettext_lazy as _
from django.utils.datastructures import MultiValueDict, MergeDict  # para que select retorne una lista
from django.db.models import Q

from usuarios.models import Usuario


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repita su contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email', 'nombre', 'apellidos', 'tipo', 'password1', 'password2',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden")
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
        # widgets = {
        #     'groups': admin.widgets.FilteredSelectMultiple('Permisos', False)
        # }

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]




class UsuarioAdmin(UserAdmin):

    form      = UserChangeForm
    add_form  = UserCreationForm
    
    list_display = ('email', 'nombre', 'apellidos', 'tipo', 'is_active', 'is_admin', 'is_superuser')
    list_filter  = ('is_admin', 'tipo',)
    
    fieldsets = [      
        ('Información personal', {'fields': ['nombre', 'apellidos', 'email', 'tipo','user_creador', 'user_padre']}),
        ('Permisos',             {'fields': ['is_active', 'is_admin', 'is_superuser', 'groups']}),
        ('Cambiar Contraseña',   {'fields': ['last_login', 'password']}),
    ]

    add_fieldsets = (
        ('Crear Nuevo Usuario', {
            'classes': ('wide',),
            'fields': add_form.Meta.fields }
        ),
    )


    search_fields = ('email',)
    ordering = ('email',)
    readonly_fields = ('last_login', 'user_creador',)#'is_superuser', 'is_admin', 'is_active')


    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []

        if request.user.is_superuser:
            self.exclude.append('user_padre')
            self.fieldsets[0][1]["fields"] = ('nombre', 'apellidos', 'email', 'tipo', 'user_creador')
            #self.fieldsets[1][1]["fields"] = ('is_active', 'is_admin')
            self.readonly_fields = self.readonly_fields + ('groups',) 

        return super(UsuarioAdmin, self).get_form(request, obj, **kwargs)



    def save_model(self, request, obj, form, change):

        obj.user_creador = request.user   
        obj.is_admin     = True
        obj.is_superuser = False
        
        if obj.tipo == Usuario.SUPER:
            obj.is_superuser = True 
            obj.groups.clear()

        if not change:
            
            if request.user.is_superuser:  
                pass                              
            obj.save()
            
        
        if change:
            obj.save()

        if obj.tipo != Usuario.SUPER:
            obj.groups.clear()
            g = Group.objects.get(name=obj.tipo)
            obj.groups.add(g) 



    def formfield_for_choice_field(self, db_field, request, **kwargs):
        
        if db_field.name == "tipo":

            if request.user.is_superuser:    # solo le permito ver tipo super nacional
                kwargs['choices'] = db_field.choices[0:2]

            elif request.user.tipo == Usuario.NACIONAL:    # solo le permito ver tipo nacional, regional, local, ingeniero y tesorero
                kwargs['choices'] = db_field.choices[1:6] 

            elif request.user.tipo == Usuario.REGIONAL:    # solo le permito ver tipo  local
                kwargs['choices'] = db_field.choices[3:4] 

            else:   # si usuario es de tipo LOCAL, INGENIERO O TESORERO solo le permito ver tipo igual a si mismo
                kwargs['choices'] = ((request.user.tipo, request.user.tipo),)  

        return super(UsuarioAdmin, self).formfield_for_choice_field(db_field, request, **kwargs)    


    def get_queryset(self, request):
        
        qs = super(UsuarioAdmin, self).get_queryset(request)
        
        if request.user.is_superuser:
            return qs

        elif request.user.tipo == Usuario.NACIONAL: # puede ver usuarios regionales y locales y a si mismo
            return qs.filter(Q(pk=request.user.pk) | Q(tipo=Usuario.REGIONAL) | Q(tipo=Usuario.LOCAL) | Q(tipo=Usuario.INGENIERO) | Q(tipo=Usuario.TESORERO))

        elif request.user.tipo == Usuario.REGIONAL:  # puede ver usuarios locales y a si mismo
            return qs.filter(Q(pk=request.user.pk) | Q(user_padre=request.user.pk))

        return qs.filter(pk=request.user.pk)  # los demas usuarios solo pueden verse a si mismos





# Esta funcion permite pasarle al campo "name" del modelo "Group", la tupla con las variables estáticas 
# de los tipos de usuarios en el modelo "Usuario", para garantizar consistencia de la aplicación
class GroupAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        
        if db_field.name == 'name':
            kwargs['widget'] = forms.Select(choices=Usuario.TIPO_USUARIO)

        if db_field.name == 'permissions':
            kwargs['widget'] = admin.widgets.FilteredSelectMultiple('Permisos', False)

        return super(GroupAdmin,self).formfield_for_dbfield(db_field,**kwargs)



admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(Usuario, UsuarioAdmin)
