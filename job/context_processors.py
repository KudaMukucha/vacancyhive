from .models import JobCategory

def category_list(request):
    return {
        'categories':JobCategory.objects.all()
    }