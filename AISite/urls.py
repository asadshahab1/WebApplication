from django.urls import path
from . import views
urlpatterns = [path('Sign-Up/',views.signUp_page, name="SignUp_Page" ),
               path("",views.home_page, name="Home_Page"),
               path('Sign-Up/Sign-Up-Record',views.signUp_details,name="SignUp_Details"),
               path('Sign-In/',views.signIn_page, name="SignIn_Page"),
               path('Sign-In/Sign-In-Details',views.signIn_details, name="SignIn_Details"),
               path('Report/',views.report_gen,name="Report_Generate")]