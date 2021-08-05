from django.views.generic import TemplateView
from core.models import Technology, TechnologyType
class Home(TemplateView):
    template_name='core/home.html'

    def get_context_data(self, **kwargs):

        context = super(TemplateView, self).get_context_data(**kwargs)
        context['technologies'] = Technology.objects.all()

        return context
