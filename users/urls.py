from django.urls import path
from .views import deleteSkill, logoutUser, profiles, \
    userProfile, loginUser, registerUser,\
    userAccount, editAccount, createSkill,\
    updateSkill, deleteSkill, inbox, viewMessage, \
    createMassage


urlpatterns = [
    path('login/', loginUser, name="login"),
    path('logout/', logoutUser, name="logout"),
    path('register/', registerUser, name="register"),

    path('', profiles, name='profiles'),
    path('profile/<str:pk>/', userProfile, name='user-profile'),
    path('account/', userAccount, name='account'),
    path('edit-account/', editAccount, name='edit-account'),
    path('create-skill/', createSkill, name='create-skill'),
    path('update-skill/<str:pk>/', updateSkill, name='update-skill'),
    path('delete-skill/<str:pk>/', deleteSkill, name='delete-skill'),
    path('inbox/', inbox, name='inbox'),
    path('message/<str:pk>', viewMessage, name='message'),
    path('create-message/<str:pk>', createMassage, name='create-message'),
]