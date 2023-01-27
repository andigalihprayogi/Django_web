from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Skill, Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name':'Name',
            'email': 'Email',
            
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'email', 'username', 'location',
                'bio','short_intro', 'profile_image', 'social_github',
                'social_twitter', 'social_linkedin', 'social_youtube',
                'social_website']
        labels = {
            'name':'Name',
            'email': 'Email',
            'username': 'UserName',
            'location' : 'Location',
            'short_intro' : 'intro',
            'profile_image' :'Image',
            'social_github' : 'Github',
            'social_twitter' : 'Twitter',
            'social_linkedin' : 'Linkedin',
            'social_youtube' : 'YouTube',
            'social_website' : 'Website',
            
        }

        
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class skillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']
        labels = {
            'name': 'Name',
            'description' : 'Description'
        }

    
    def __init__(self, *args, **kwargs):
        super(skillForm, self).__init__(*args, **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']


    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        for name , field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

