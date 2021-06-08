from .models import Categories



def menu_links(request):
    link = Categories.objects.all()
    return dict(links=link)
