from django.shortcuts import *
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import hashlib, random, datetime
from surl.models import Surl

def get(request,_surl):
	try:
		s=Surl.objects.get(surl__exact=_surl)
	except Surl.DoesNotExist:
		return render_to_response('404.html')
	return HttpResponseRedirect(s.lurl)

def test(request,_surl):
	return HttpResponse(_surl)

def putindex(request):
	l=Surl.objects.all().order_by('-add_date')[:5]
	return render_to_response('surl/index.html',{'the_list':l})

def __gensurl(lurl):
	RANDSEED = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	surl=''
	for i in range(6):
		surl+=random.choice(RANDSEED)
	return surl

def __procurl(lurl):
	if lurl.find('://')==-1:
		lurl='http://'+lurl
	return lurl

@csrf_exempt
def add(request):
	try:
		_lurl=request.POST['url']
	except(KeyError):
		return HttpResponse('post something to me!')

	#lurl
	_lurl=__procurl(_lurl)
	s = Surl(lurl=_lurl)
	#fingerprint
	m=hashlib.md5(_lurl)
	s.fingerprint=m.hexdigest()
	#add_date
	s.add_date=datetime.datetime.now()
	#surl=pk
	_surl=__gensurl(_lurl)
	while Surl.objects.get(surl__exact=_surl):
		_surl=__gensurl(_lurl)
	s.surl=_surl
	
	#res='success<br />long url: '+s.lurl+'<br />fingerprint: '+s.fingerprint+'<br />short url: http://192.168.1.200:7788/'+s.surl
	res=_surl
	s.save()
	return HttpResponse(res)
