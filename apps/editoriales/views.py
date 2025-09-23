from django.shortcuts import render
from apps.editoriales.models import Editorial

# Create your views here.
def lista_editoriales(request):
    return render(request=request,
                  template_name='editoriales.html',
                  context={"editoriales":Editorial.objects.all()})