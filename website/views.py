from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def home(request):
	if request.method == "POST":
		name = request.POST['name']
		email = request.POST['email']
		message = request.POST['message']

		data = {
			'name':name,
			'email':email,
			'message':message
		}
		message = '''
		New message: {}
		From: {}
		'''.format(data['message'], data['email'])
		send_mail(data['email'], message, '', ['i.nyamu5@gmail.com'])
		
		# send an email
		'''
		send_mail(
			name, # name
			message, # message
			email, # from email
			['i.nyamu5@gmail.com'], # to email
			)
		'''
		return render(request, 'home.html', {'name': name})
	else:	
		return render(request, 'home.html', {})