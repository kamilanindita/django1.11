from django.shortcuts import render, redirect
from .models import Mahasiswa
from .forms import MahasiswaForm

# Create your views here.

def list(request):
    Semua_mahasiswa=Mahasiswa.objects.all()
    context={
        'page_title':'Daftar Mahasiswa',
        'semua_mahasiswa':Semua_mahasiswa,
    }
    return render(request,'mahasiswa/list.html',context)

def create(request):
	mahasiswa_form = MahasiswaForm(request.POST or None)

	if request.method == 'POST':
		if mahasiswa_form.is_valid():
			mahasiswa_form.save()

		return redirect('mahasiswa:list')

	context = {
		"page_title":"Tambah Mahasiswa",
		"mahasiswa_form":mahasiswa_form,
	}

	return render(request,'mahasiswa/create.html',context)

def update(request,update_id):
	mahasiswa_update = Mahasiswa.objects.get(id=update_id)
	
	data = {
        'nim'	        : mahasiswa_update.nim,
		'nama_depan'	: mahasiswa_update.nama_depan,
		'nama_belakang'	: mahasiswa_update.nama_belakang,
		'prodi'		    : mahasiswa_update.prodi,
        'alamat'	    : mahasiswa_update.alamat,
	}
	mahasiswa_form = MahasiswaForm(request.POST or None, initial=data, instance=mahasiswa_update)

	if request.method == 'POST':
		if mahasiswa_form.is_valid():
			mahasiswa_form.save()

		return redirect('mahasiswa:list')

	context = {
		"page_title":"Update Mahasiswa",
		"mahasiswa_form":mahasiswa_form,
	}

	return render(request,'mahasiswa/create.html',context)


def delete(request,delete_id):
	Mahasiswa.objects.filter(id=delete_id).delete()
	return redirect('mahasiswa:list')