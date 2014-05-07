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
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255, unique=True)
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UsuarioManager()

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

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin