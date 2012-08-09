from django.template.response import TemplateResponse

def view(request):
    return TemplateResponse(request, '.html', {})
