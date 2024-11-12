from django.urls import path, include

from . import views

urlpatterns = [
    path('',views.Home,name='Home'),
    path('printpagecall/',views.printpagecall,name='printpagecall'),
    path('printpagelogic/',views.printpagelogic,name='printpagelogic'),
    path('exceptionpagecall/',views.exceptionpagecall,name='exceptionpagecall'),
    path('exceptionpagelogic/',views.exceptionpagelogic,name='exceptionpagelogic'),
    path('randompagecall/', views.randompagecall, name='randompagecall'),
    path('randomlogic/', views.randomlogic, name='randomlogic'),
    path('calculatorlogic/', views.calculatorlogic, name='calculatorlogic'),
    path('Login/',views.Login,name='Login'),
    path('Register/', views.Register, name='Register'),
    path('UserRegisterPageCall/',views.UserRegisterPageCall,name='UserRegisterCall'),
    path('UserRegisterLogic/',views.UserRegisterLogic,name='UserRegisterLogic'),
    path('daytimepagelogic/', views.daytimepagelogic, name='daytimepagelogic'),
    path('UserLoginPageCall/',views.UserLoginPageCall,name='UserLoginPageCall'),
    path('UserLoginLogic/', views.UserLoginLogic, name='UserLoginLogic'),
    path('logot/',views.logot,name='logot'),
    path('add_task/',views.add_task,name = 'add_task'),
    path('<int:pk>/delete/',views.delete_task,name = 'delete_task'),
    path('Add_Student/',views.Add_Student,name='Add_Student'),
    path('Feedback/',views.Feedback,name='Feedback')
]
