from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

import sweetify

# Create your views here.

def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']

		user = auth.authenticate(username=username, email=email)

		if user is not None:
			auth.login(request, user)
			sweetify.info(request, 
				'You did it', 
				text='Good job! You successfully Logged In', 
				persistent='Thanks')
			return render(request, 'users/index.html')
		else:
			sweetify.info(request, 
				'Opps!!', 
				text='Wrong Information MayB', 
				persistent='Try Again') 
			return render(request, 'users/index.html')

	else:
		return render(request, 'users/index.html')


def register(request):
	if request.method == 'POST':
		username = request.POST['username']
		email = request.POST['email']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if User.objects.filter(username=username).exists():
			sweetify.info(request, 'Opps!', text='This Username is taken', persistent='Try Again')
			print('username has already been taken' )
			return render(request, 'users/index.html')
		elif User.objects.filter(email=email).exists():
			sweetify.info(request, 'Opps!', text='This email is already been used', persistent='Try Again')
			print('email has already been used')
			return render(request, 'users/index.html')
		elif password2 != password1:
			sweetify.info(request, 'Opps!', text='Your Passwords are not matching!', persistent='Try Again')
			return render(request, 'users/index.html')
		else:
			userObj = User.objects.create_user(username=username, password=password2, email=email)
			userObj.save()
			messages.success(request, 'Successfully Created!')
			print('created!')
			sweetify.sweetalert(request, 'Westworld is awesome', text='Really... if you have the chance - watch it!', persistent='I agree!')
			sweetify.info(request, 'You did it', text='Good job! You successfully showed a SweetAlert message', persistent='Hell yeah')
			return render(request, 'users/index.html')

	
		# return render(request, 'users/index.html')

	else:
		return render(request, 'users/index.html')
