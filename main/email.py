# -*- coding: utf-8 -*-
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import render_to_response, render, redirect, get_object_or_404
from django.template.loader import get_template
from django.template import Context

from usuarios.models import Usuario
from db.models import Etapa



def mail_comentario(coment, proyecto):
    # user es el usuario logueado 
    subject        = "Nuevo comentario en proyecto %s" % proyecto.nombre_proyecto
    #message        = coment.descripcion+' /n /n  por favor no responda a esta correo'
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
    

    d = Context({ 'nombre_proyecto':proyecto.nombre_proyecto, 'text':'a Recibido un nuevo Comentario' })
    htmly = get_template('main/email_template.html')
    html_content = htmly.render(d)

    msg = EmailMessage(subject, html_content, from_email, recipient_list)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()   
    #return send_mail(subject, message, from_email, recipient_list, fail_silently=True)


def mail_change_etapa(proyecto, request_user):
    # user es el usuario logueado 
    subject        = u"Proyecto %s cambió a %s" %(proyecto.nombre_proyecto, proyecto.get_etapa_actual_display())    
    from_email     = settings.EMAIL_HOST_USER    
   
    if proyecto.etapa_actual == Etapa.CONS_P1: #Construccion Inicia dedicacion calculada
       message        = u"cambió a etapa de %s y se Calcula la fecha de Dedicacion el %s, Como Departamento de Comunicaciones deben tener esta Fecha Presente para Agendar este Compromiso" %(proyecto.get_etapa_actual_display(),proyecto.fecha_aprox_dedicacion.strftime('%Y-%m-%d'))
       d = Context({ 'nombre_proyecto':proyecto.nombre_proyecto, 'text':message  })
       htmly = get_template('main/email_template.html')
       html_content = htmly.render(d)

       msg = EmailMessage(subject, html_content, from_email, [settings.EMAIL_COMUNICACIONES,settings.EMAIL_DEVELOPER])
       msg.content_subtype = "html"  # Main content is now text/html
       msg.send()  

    recipient_list = [proyecto.usuario.email]
    recipient_list.append(settings.EMAIL_DEVELOPER)      
    message = u"cambió a etapa de %s" %(proyecto.get_etapa_actual_display())   
    # componer la lista de destinatarios
    for user in Usuario.objects.filter(tipo=Usuario.NACIONAL):
        recipient_list.append(user.email)   
    # esto porque el user_padre puede ser tambien en Nacional
    if proyecto.usuario.user_padre:
        if proyecto.usuario.user_padre.tipo != Usuario.NACIONAL:
            #regional
            recipient_list.append(proyecto.usuario.user_padre.email)

    if request_user.email in recipient_list:
        # sacamos de la lista de envio al usuario que esta logueado
        recipient_list.remove(request_user.email)

    d = Context({ 'nombre_proyecto':proyecto.nombre_proyecto, 'text':message })
    htmly = get_template('main/email_template.html')
    html_content = htmly.render(d)

    msg = EmailMessage(subject, html_content, from_email, recipient_list)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()    


def mail_change_foto(proyecto, request_user):
    # user es el usuario logueado 
    subject        = u"Proyecto %s adjunto fotos %s" %(proyecto.nombre_proyecto, proyecto.get_etapa_actual_display())
    message        = u"a adjuntado fotos %s" %(proyecto.get_etapa_actual_display())
    from_email     = settings.EMAIL_HOST_USER
    recipient_list = [proyecto.usuario.email]
    recipient_list.append(settings.EMAIL_DEVELOPER)   

    # componer la lista de destinatarios
    for user in Usuario.objects.filter(tipo=Usuario.NACIONAL):
        recipient_list.append(user.email)   
    # esto porque el user_padre puede ser tambien en Nacional
    if proyecto.usuario.user_padre:
        if proyecto.usuario.user_padre.tipo != Usuario.NACIONAL:
            #regional
            recipient_list.append(proyecto.usuario.user_padre.email)

    if request_user.email in recipient_list:
        # sacamos de la lista de envio al usuario que esta logueado
        recipient_list.remove(request_user.email)

    
    d = Context({ 'nombre_proyecto':proyecto.nombre_proyecto, 'text':message })
    htmly = get_template('main/email_template.html')
    html_content = htmly.render(d)

    msg = EmailMessage(subject, html_content, from_email, recipient_list)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()    


def mail_change_sub_etapa(proyecto, request_user, text):
    # user es el usuario logueado 
    subject        = u"Proyecto %s %s " %(proyecto.nombre_proyecto,text)
    message        = u"notifica que %s " %(text)
    from_email     = settings.EMAIL_HOST_USER
    recipient_list = [proyecto.usuario.email]
    recipient_list.append(settings.EMAIL_DEVELOPER)   
    
    # componer la lista de destinatarios
    for user in Usuario.objects.filter(tipo=Usuario.NACIONAL):
        recipient_list.append(user.email)   
    # esto porque el user_padre puede ser tambien en Nacional
    if proyecto.usuario.user_padre:
        if proyecto.usuario.user_padre.tipo != Usuario.NACIONAL:
            #regional
            recipient_list.append(proyecto.usuario.user_padre.email)

    if request_user.email in recipient_list:
        # sacamos de la lista de envio al usuario que esta logueado
        recipient_list.remove(request_user.email)

    d = Context({ 'nombre_proyecto':proyecto.nombre_proyecto, 'text':message })
    htmly = get_template('main/email_template.html')
    html_content = htmly.render(d)

    msg = EmailMessage(subject, html_content, from_email, recipient_list)
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()    


def mail_prueba(): 
  
    subject, from_email, to = 'Hola Prueba', 'soporte@laalianzacristiana.co', 'felipe.valencia@laalianzacristiana.co'
    d = Context({ 'nombre_proyecto': 'Templo Popayan', 'text':'a Cambiado de etapa y espera la aprobacion Nacional' })
    htmly = get_template('main/email_template.html')
    html_content = htmly.render(d)

    msg = EmailMessage(subject, html_content, from_email, [to])
    msg.content_subtype = "html"  # Main content is now text/html
    return msg.send()