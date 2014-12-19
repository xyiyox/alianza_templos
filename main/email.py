# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail

from usuarios.models import Usuario



def mail_comentario(coment, proyecto):
    # user es el usuario logueado 
    subject        = "Nuevo comentario en proyecto %s" % proyecto.nombre_proyecto
    message        = coment.descripcion+' /n /n  por favor no responda a esta correo'
    from_email     = settings.EMAIL_HOST_USER
    recipient_list = [proyecto.usuario.email]  #local
    
    # componer la lista de destinatarios
    for user in Usuario.objects.filter(tipo=Usuario.NACIONAL):
        recipient_list.append(user.email)   

    # esto porque el user_padre puede ser tambien en Nacional
    if proyecto.usuario.user_padre.tipo != Usuario.NACIONAL:
        recipient_list.append(proyecto.usuario.user_padre.email) #regional

    # le enviamos a los siguentes usuarios solo si les contestaron un comentario
    if coment.comentario_padre:
        
        if coment.comentario_padre.commenter.tipo == Usuario.ARQUITECTO:
            recipient_list.append(coment.comentario_padre.commenter.email)
        
        if coment.comentario_padre.commenter.tipo == Usuario.INGENIERO:
            recipient_list.append(coment.comentario_padre.commenter.email)
        
        if coment.comentario_padre.commenter.tipo == Usuario.TESORERO:
            recipient_list.append(coment.comentario_padre.commenter.email)

    if coment.commenter.email in recipient_list:
        # no le enviamos email al que comento
        recipient_list.remove(coment.commenter.email)

    return send_mail(subject, message, from_email, recipient_list, fail_silently=True)


def mail_change_etapa(proyecto, request_user):
    # user es el usuario logueado 
    subject        = u"Proyecto %s cambió a %s" %(proyecto.nombre_proyecto, proyecto.get_etapa_actual_display())
    message        = subject
    #local
    recipient_list = [proyecto.usuario.email]
    
    # componer la lista de destinatarios
    for user in Usuario.objects.filter(tipo=Usuario.NACIONAL):
        recipient_list.append(user.email)   
    # esto porque el user_padre puede ser tambien en Nacional
    if proyecto.usuario.user_padre.tipo != Usuario.NACIONAL:
        #regional
        recipient_list.append(proyecto.usuario.user_padre.email)

    if request_user.email in recipient_list:
        recipient_list.remove(request_user.email)

    return send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)