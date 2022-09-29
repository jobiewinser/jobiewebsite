from django.template.defaulttags import register
from django import template
register = template.Library()
import logging
logger = logging.getLogger(__name__)
@register.filter
def time_to_time_input_prefill(time):
    try:
        return time.strftime('%H:%M')
    except:
        return time