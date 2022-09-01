from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render
import logging
from django.contrib.auth import login
from django.middleware.csrf import get_token
logger = logging.getLogger(__name__)
def get_modal_content(request, **kwargs):
    try:
        if request.user.is_staff:
            template_name = request.GET.get('template_name', '')
            context = {}
            if template_name == 'switch_user':
                context['staff_users'] = User.objects.filter(is_staff=True, is_superuser=False).order_by('first_name')
            if template_name == 'log_communication':
                context['communication_type'] = kwargs.get('param1')
            return render(request, f"results/{template_name}.html", context)   
    except Exception as e:
        logger.debug("get_modal_content Error "+str(e))
        return HttpResponse(e, status=500)

def switch_user(request, **kwargs):
    logger.debug(str(request.user))
    try:
        if request.user.is_staff:
            user_pk = request.POST.get('user_pk')
            if type(user_pk) == list:
                user_pk = user_pk[0]
            logger.debug(f"TEST {str(user_pk)}")
            login(request, User.objects.get(pk=user_pk, is_superuser=False))
            return render(request, f"results/profile_dropdown.html", {})   
    except Exception as e:
        logger.debug("switch_user Error "+str(e))
        return HttpResponse(e, status=500)

def mark_done(request, **kwargs):
    logger.debug(str(request.user))
    try:
        if request.user.is_staff:
            return HttpResponse("", "text", 200)
    except Exception as e:
        logger.debug("switch_user Error "+str(e))
        return HttpResponse(e, status=500)

