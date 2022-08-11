from sys import version
from django.views.generic import TemplateView
from core.models import Technology, TechnologyType, Project, ProjectImage, Language, HomePlug, EnergyDayReading
from django.views import View
from django.http import HttpResponse
import os

import asyncio
# from kasa import SmartPlug
from asgiref.sync import sync_to_async
import datetime
from django.shortcuts import render
from django.db.models import Sum
from django.http import JsonResponse
import logging
logger = logging.getLogger(__name__)


# class IotView(TemplateView):
#     template_name='core/iot.html'

#     def get_context_data(self, **kwargs):
#         context = super(IotView, self).get_context_data(**kwargs)
#         return context

# def energy_chart(request):
#     labels = []
#     data = []

#     queryset = EnergyDayReading.objects.values('nice_date').annotate(homedevice_mac=Sum('energy_wh')).order_by('date')
#     for entry in queryset:
#         labels.append(entry['nice_date'])
#         data.append(entry['homedevice_mac'])
    
#     return JsonResponse(data={
#         'labels': labels,
#         'data': data,
#     })

# async def updateKasa(ip):
#     p = SmartPlug(ip)
    
#     await p.update()
#     await p.turn_off()
#     return p

# def getLastMonth(datetime):
#     month = datetime.month
#     year = datetime.year
#     if month == 1:
#         month = 12
#         year = year - 1
#     return month, year

class HomeView(TemplateView):
    template_name='core/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        
        # try:
            
            # plug = asyncio.run(updateKasa("192.168.0.29"))
            # existing_plug, created = HomePlug.objects.get_or_create(mac=plug.hw_info['mac'])

            # existing_plug.sw_ver=plug.hw_info['sw_ver']
            # existing_plug.hw_ver=plug.hw_info['hw_ver'],
            # existing_plug.hwId=plug.hw_info['hwId'],
            # existing_plug.oemId=plug.hw_info['oemId'],
            # existing_plug.dev_name=plug.hw_info['dev_name'],
            # existing_plug.alias=plug.alias
            # existing_plug.save()

            # month, year = getLastMonth(datetime.datetime.now())
            # temp = asyncio.run(plug.get_emeter_daily(year=year, month=month, kwh=False))
            # for k, v in temp.items():
            #     logger.debug(datetime.datetime(year, month, k))
            #     existing_reading, created = EnergyDayReading.objects.get_or_create(date = datetime.datetime(year, month, k), homeplug=existing_plug)
            #     existing_reading.energy_wh=v
            #     existing_reading.nice_date=existing_reading.date.strftime('%A %d %B %Y')
            #     existing_reading.save()
        # except Exception as e:
        #     logger.debug("ERROR "+str(e))


        # context['kasa'] = plug
        context['technologies'] = Technology.objects.all().order_by('priority')
        return context

class ProjectListView(TemplateView):
    template_name='core/projectlist.html'

    def get_context_data(self, **kwargs):

        context = super(ProjectListView, self).get_context_data(**kwargs)
        context['projectlist'] = Project.objects.all() 
        if 'technology_id' in kwargs:
            filter_technology = Technology.objects.filter(pk=kwargs['technology_id']).first()
            context['projectlist'] = context['projectlist'].filter(technology=filter_technology)
            context['filter_type'] = 'Technology'
            context['filter_parameter'] = filter_technology.name
        if 'language_id' in kwargs:
            filter_language = Language.objects.filter(pk=kwargs['language_id']).first()
            context['projectlist'] = context['projectlist'].filter(technology__language=filter_language)
            context['filter_type'] = 'Language'
            context['filter_parameter'] = filter_language.name
            
        return context

class ProjectView(TemplateView):
    template_name='core/project.html'

    def get_context_data(self, **kwargs):

        context = super(ProjectView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.filter(pk=kwargs['project_id']).first() 
        return context

class CareerView(TemplateView):
    template_name='core/career.html'

    def get_context_data(self, **kwargs):
        context = super(CareerView, self).get_context_data(**kwargs)
        return context

class SiteView(TemplateView):
    template_name='core/site.html'

    def get_context_data(self, **kwargs):
        context = super(SiteView, self).get_context_data(**kwargs)
        return context

class Project_Image_Download(View):
    def get(self, request, **kwargs):
        projectimage = ProjectImage.objects.filter(pk=kwargs['projectimage_id']).first()
        if projectimage:
            httpresponse = HttpResponse(projectimage.image.file, content_type='application/force-download')
            httpresponse['Content-Disposition'] = 'attachment; filename="'+projectimage.project.name+' Screenshot'+os.path.splitext(projectimage.image.file.name)[1]+'"'
            return httpresponse

class EnquiriesView(TemplateView):
    template_name='core/enquiries.html'

    def get_context_data(self, **kwargs):
        context = super(EnquiriesView, self).get_context_data(**kwargs)
        return context



class TestView(TemplateView):
    template_name='core/test.html'

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        return context


