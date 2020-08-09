from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from students.models import Student


def regStudent(request):
	return render(request, 'students/registerStudent.html')


def regConStudent(request):
	name = request.POST['name']
	major = request.POST['major']
	age = request.POST['age']
	grade = request.POST['grade']
	gender = request.POST['gender']
	
	qs = Student(s_name=name, s_major=major, s_age=age, s_grade=grade, s_gender=gender)
	qs.save()
	
	return HttpResponseRedirect(reverse('students:stuAll'))


def reaStudentAll(request):
	qs = Student.objects.all()
	context = {'student_list': qs}
	print(context)
	return render(request, 'students/readStudents.html', context)


def detStudent(request, name):
	qs = Student.objects.get(s_name=name)
	context = {'student_info': qs}
	return render(request, 'students/detailStudent.html', context)


def reaStudentOne(request, name):
	qs = Student.objects.get(s_name=name)
	context = {'student_info': qs}
	return render(request, 'students/modifyStudent.html', context)


def modConStudent(request):
	name = request.POST['name']
	major = request.POST['major']
	age = request.POST['age']
	grade = request.POST['grade']
	gender = request.POST['gender']
	
	s_qs = Student.objects.get(s_name=name)
	
	s_qs.s_name = name
	s_qs.s_major = major
	s_qs.s_age = age
	s_qs.s_grade = grade
	s_qs.s_gender = gender
	s_qs.save()
	
	return HttpResponseRedirect(reverse('students:stuAll'))


def delConStudent(request, name):
	s_qs = Student.objects.get(s_name=name)
	s_qs.delete()
	
	return HttpResponseRedirect(reverse('students:stuAll'))


def ejealgetda(request):
	qsa = Student.objects.all()
	context = {'student_list': qsa}
	
	return render(request, 'students/readStudents.html', context)
