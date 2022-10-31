from django.http import JsonResponse

from apiendpoint.models import Bio

def home(request):
    queryset = Bio.objects.all()
    context = {
        'queryset': queryset
    }
    return JsonResponse(context, safe=False)