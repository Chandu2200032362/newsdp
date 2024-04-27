from django.urls import path
from .views import signup,signup1,form1, form2,educational,edform1,login_view, logout_view,fhome, home, survey_create,survey_types,customers,customersurvey,websitefeedback,navbar,secondnavbar
urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('fhome/', fhome, name='fhome'),
    path('',navbar,name='navbar'),
    path('signup/', signup, name='signup'),
    path('signup1/', signup1, name='signup1'),
    path('logout/', logout_view, name='logout'),
    path('customers/', customers, name='customers'),
    path('form1/', form1, name='form1'),
    path('form2/', form2, name='form2'),
    path('education/', educational, name='educational'),
    path('edform1/', edform1, name='edform1'),


    # path('/home', home, name='home'),
    path('survey_create/', survey_create, name='survey_create'),
    path('survey-types/', survey_types, name='survey_types'),
    path('customersurvey/', customersurvey, name='customersurvey'),
    path('websitefeedback/', websitefeedback, name='websitefeedback'),

]
