from django.shortcuts import render
from .models import AboutMe, Skills, Experiences, Portfolio

def home(request):
    about_me = AboutMe.objects.all()
    skills = Skills.objects.all()
    experiences = Experiences.objects.all()
    portfolio = Portfolio.objects.all()

    context = {
        'about_me': about_me,
        'skills': skills,
        'experiences': experiences,
        'portfolio': portfolio,
    }
    return render(request, 'home.html', context)


