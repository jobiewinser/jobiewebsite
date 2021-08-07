from django.views.generic import TemplateView
from core.models import Technology, TechnologyType, Project, ProjectImage
from django.views import View
from django.http import HttpResponse
import os
class HomeView(TemplateView):
    template_name='core/home.html'

    def get_context_data(self, **kwargs):

        context = super(TemplateView, self).get_context_data(**kwargs)
        context['technologies'] = Technology.objects.all().order_by('priority')
        temp = context['technologies'].first()
        return context

class ProjectListView(TemplateView):
    template_name='core/projectlist.html'

    def get_context_data(self, **kwargs):

        context = super(TemplateView, self).get_context_data(**kwargs)
        context['projectlist'] = Project.objects.all() 
        return context

class ProjectView(TemplateView):
    template_name='core/project.html'

    def get_context_data(self, **kwargs):

        context = super(TemplateView, self).get_context_data(**kwargs)
        context['project'] = Project.objects.filter(pk=kwargs['project_id']).first() 
        return context

class CareerView(TemplateView):
    template_name='core/career.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        return context

class SiteView(TemplateView):
    template_name='core/site.html'

    def get_context_data(self, **kwargs):
        context = super(TemplateView, self).get_context_data(**kwargs)
        return context

class Project_Image_Download(View):
    def get(self, request, **kwargs):
        projectimage = ProjectImage.objects.filter(pk=kwargs['projectimage_id']).first()
        if projectimage:
            httpresponse = HttpResponse(projectimage.image.file, content_type='application/force-download')
            httpresponse['Content-Disposition'] = 'attachment; filename="'+projectimage.project.name+' Screenshot'+os.path.splitext(projectimage.image.file.name)[1]+'"'
            return httpresponse

