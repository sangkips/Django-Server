
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Bio

def django_models_json(request):
    obj = Bio.objects.all()
    data = serialize("json", fields=('slackUsername', 'backend', 'age', 'bio'))
    return HttpResponse(data, content_type="application/json")