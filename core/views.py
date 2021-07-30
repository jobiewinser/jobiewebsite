from django.views.generic import TemplateView

class Home(TemplateView):
    template_name='core/home.html'
    def get(self, request):
        return 1/0
