from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'jsonPage/', views.jsonPage, name='jsonPage'),
	url(r'profilePage/', views.profilePage, name='profilePage'),
	url(r'course/([0-9]+)', views.course, name='course'),
	url(r'professor/([0-9]+)', views.professor, name='professor'),
	url(r'addPage/', views.addPage, name='addPage'),
	url(r'addProfesorPage/', views.addProfesorPage, name='addProfesorPage'),
	url(r'addCoursePage/', views.addCoursePage, name='addCoursePage'),
	url(r'addReviewPage/', views.addReviewPage, name='addReviewPage'),
	url(r'dislikeReview/([0-9]+)', views.dislikeReview, name='dislikeReview'),
	url(r'likeReview/([0-9]+)', views.likeReview, name='likeReview'),
	url(r'searchPage/', views.searchPage, name='searchPage'),
	url(r'professorSearchPage/', views.professorSearchPage, name='professorSearchPage'),
	url(r'courseSearchPage/', views.courseSearchPage, name='courseSearchPage'),
	url(r'highSchoolRecommendedProfessorsPage/', views.highSchoolRecommendedProfessorsPage, name='highSchoolRecommendedProfessorsPage'),
	url(r'highSchoolRecommendedCoursesPage/', views.highSchoolRecommendedCoursesPage, name='highSchoolRecommendedCoursesPage'),
	url(r'interestsRecommendedProfessorsPage/', views.interestsRecommendedProfessorsPage, name='interestsRecommendedProfessorsPage'),
	url(r'interestsRecommendedCoursesPage/', views.interestsRecommendedCoursesPage, name='interestsRecommendedCoursesPage'),
    url(r'^$', views.homepage, name='homepage'),
]