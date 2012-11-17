from django.template.loader import get_template
from django.template import Context
from django.http import Http404, HttpResponse
import datetime

def hello(request):
	return HttpResponse("Hello")

def current_datetime(request):
	now = datetime.datetime.now()
	# set the template
	t = get_template('current_datetime.html')
	# create the web page
	html = t.render(Context({'current_date': now}))

	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	t = get_template('hours_ahead.html')
	html = t.render(Context({'hour_offset': offset, 'next_time': dt}))	

	return HttpResponse(html)


