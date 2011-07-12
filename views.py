# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from SOS.models import SOSuser

class LoginForm( forms.Form ):
	username = forms.CharField( max_length = 25 )
	password = forms.CharField( max_length = 25, widget=forms.PasswordInput )
	
def login_view( request, session_action ):
	if request.method == 'POST': # If the form has been submitted...
		form = LoginForm( request.POST ) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
		    # Process the data in form.cleaned_data
		    user = authenticate( username = form.cleaned_data['username'], 
		    					 password = form.cleaned_data['password'] )
		    if user is not None:
		        if user.is_active:
		        	login(  request, user  )
		        	return HttpResponseRedirect( '/sos/' )
		        else:
		            return HttpResponse( "Your account has been disabled!" )
		    else:
		        return HttpResponse( "Your username and/or password were incorrect." )
	 
	if session_action == 'logout':
		logout( request )
		form = LoginForm()
			
	else:
		form = LoginForm() # An unbound form

	return render_to_response(	
		'login.html', 
		{'form': form,}, 
		context_instance = RequestContext( request )
	)

def index( request ):
	if request.user.is_authenticated():
		return render_to_response( 'home.html', context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect( 'login/' )
		
def user_info( request ):
	'''context processor that loads user info into the template'''
	if request.user.is_authenticated():
		user_id = request.user.id
		s = SOSuser.objects.get(pk=user_id)
		l = s.location.all()
		return { 'SOSuser' : s, 'location' : l }
	else:
		return { 'none' : None }