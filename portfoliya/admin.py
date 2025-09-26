from django.contrib import admin
from .models import AboutMe, Skills,Experiences,Portfolio

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)

@admin.register(Experiences)
class ExperiencesAdmin(admin.ModelAdmin):
        list_display = ('id', 'title')
        search_fields = ('title',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'github_link')
    search_fields = ('title',)

#
# from django.contrib import admin
# from .models import Student
#
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ("email", "is_verified", "created_at")
#     readonly_fields = ("is_verified", "created_at", "code")  # 🔒 admin o‘zgartira olmaydi
