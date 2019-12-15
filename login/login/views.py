from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

#menggunakan function based view

def index(request):
	context = {
		'page_title': 'Home',
	}
	template_name = None
 
	#cek session / internal permission checks
	if request.user.is_authenticated():
		#bila ada session
		template_name = 'index_user.html'
	else:
		#tidak ada session
		template_name = 'index.html'
	
	return render(request, template_name, context)


def loginView(request):
	context = {
		'page_title':'Login',
	}
	user = None
 
	#ketika halaman dipanggil / method GET
	if request.method == "GET":
		#cek session / internal permission checks
		if request.user.is_authenticated():
			#bila ada sesssion
			return redirect('index')
		else:
			#tidak ada session
			return render(request, 'login.html', context)

	#proses login / method POST untuk menagkap data dari form login
	if request.method == "POST":
		
		username = request.POST['username']
		password = request.POST['password']
		
		user = authenticate(request, username=username, password=password)

		if user is not None:
			#user tersedia
			login(request, user)
			return redirect('index')
		else:
			#user tidak tersedia
			return redirect('login')
	
#tidak dapat diakses oleh non-user
@login_required
def logoutView(request):
	logout(request)
	return redirect('index')

#tidak dapat diakses oleh non-user
@login_required
def profileView(request):
    context = {
		'page_title':'Profile',
	}
    return render(request, 'profile.html', context)
