from .models import DropdownMenuItem,FooterService

def dropdown_items(request):
    items = DropdownMenuItem.objects.filter(active=True).order_by('order')
    return {
        'dropdown_items': items
    }



def footer_services(request):
    return {
        'footer_services': FooterService.objects.all()
    }