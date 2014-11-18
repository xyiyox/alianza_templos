from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin, Group
)


class UsuarioManager(BaseUserManager):

    def create_user(self, email, nombre, apellidos, password=None):
 
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            nombre=nombre,
            apellidos=apellidos
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nombre, apellidos, password):

        user = self.create_user(email,
            password=password,
            nombre=nombre,
            apellidos=apellidos
        )
        user.is_admin = True
        user.is_superuser = True
        user.tipo = user.SUPERADMIN
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):

    SUPERADMIN      = "superadmin"
    NACIONAL        = "nacional" 
    REGIONAL        = "regional" 
    LOCAL           = "local" 
    
    INGENIERO       = "ingeniero"
    ARQUITECTO      = "arquitecto"
    TESORERO        = "tesorero"

    TIPO_USUARIO = (
        (SUPERADMIN,"Superadmin"),
        (NACIONAL,  "Nacional"),
        (REGIONAL,  "Regional"),
        (LOCAL,     "Local"),

        (INGENIERO, "Ingeniero"),
        (ARQUITECTO, "Arquitecto"),
        (TESORERO,  "Tesorero"),
    )

    email           = models.EmailField(max_length=255, unique=True)
    nombre          = models.CharField(max_length=50)
    apellidos       = models.CharField(max_length=50)
    tipo            = models.CharField(max_length=10, choices=TIPO_USUARIO, help_text='Escoja bien el tipo de usuario que desea crear')

    is_active       = models.BooleanField(default=True)
    is_admin        = models.BooleanField(default=False)

    user_creador    = models.ForeignKey('self', null=True, blank=True, verbose_name="Creado por", 
                        related_name='creador')
    user_padre      = models.ForeignKey('self', null=True, blank=True, related_name='padre', 
                        verbose_name='Asignado a', help_text='Asigne este usuario a un usuario regional')

    objects         = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellidos']

    def get_full_name(self):
        if self.nombre:
        	return "%s %s" %(self.nombre, self.apellidos)
        return self.email

    def get_short_name(self):
        if self.nombre:
        	return "%s %s" %(self.nombre, self.apellidos)
        return self.email

    # On Python 3: def __str__(self):
    def __unicode__(self):
    	if self.nombre:
        	return "%s %s" %(self.nombre, self.apellidos)
        return self.email

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property 
    def username(self):
        if self.nombre:
            return self.nombre
        return self.email