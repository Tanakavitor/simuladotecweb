from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .models import Fact

# Create your views here.
from django.http import HttpResponse

def index(request):
      if request.method == 'POST':
            description = request.POST.get('descricao')
            fact = Fact(descricao=description)
            fact.save()
            return HttpResponseRedirect('/')
      else:
            all_facts = Fact.objects.all()
            return render(request, 'notes/index.html', {'facts': all_facts})
def curtir(request, id):
      fact = Fact.objects.get(id=id)
      fact.curtidas += 1
      fact.save()
      return HttpResponseRedirect('/')



            
      
            