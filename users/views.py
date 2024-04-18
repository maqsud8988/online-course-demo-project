from django.shortcuts import render
from django.views import View
from course.models import Course, Speciality, Teacher
from blog.models import Blog

class LandingPageView(View):
    def get(self, request):
        specialitys = Speciality.objects.all()
        course = Course.objects.all()
        Teachers = Teacher.objects.all()
        blogs = Blog.objects.all()

        context = {
            "specialitys": specialitys,
            "course": course,
            "teachers": Teachers,
            "blogs": Blog,
        }
        return render(request, "main/index.html", context)