from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from application.models import ProductList



def contactpage(request):
    template_name = "application\\fview.html"
    product_list = ProductList.objects.all()
    context= {'info':'Smart Phones', 'product_list' : product_list }
    return render (request,template_name,context)
    

class contactpg(TemplateView):
    template_name = "application\cview.html"

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = 'Full Specification'
        try:
            cdata = ProductList.objects.get(pk = kwargs ['id'])
            context ['cdata'] = cdata
        except ProductList.DoesNotExist:
            context['cdata'] = None
            raise Http404 ("Contact ID not found")
        return context
   
