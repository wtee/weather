from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from datetime import date

from cancellations.models import Cancellation
from cancellations.models import Organization

# Views
class IndexView(generic.ListView):
  template_name = 'cancellations/index.html'
  context_object_name = 'cancel_list'

  def get_queryset(self):
    """Return cancellations from today or later."""
    return filter(lambda x: x.cancel_date >= date.today(), Cancellation.objects.order_by('-cancel_date').reverse())

class DetailView(generic.DetailView):
  template_name = 'cancellations/event.html'
  context_object_name = 'cancel_detail'

#  def get_queryset(self):
#    """Return only the desired result"""
#    return Cancellation.objects.get_object()




#def index(request):
#  cancellation_list = Cancellation.objects.order_by('-cancel_date')
#  context = {'cancellation_list':cancellation_list}
#  return render(request, 'cancel/index.html', context)
