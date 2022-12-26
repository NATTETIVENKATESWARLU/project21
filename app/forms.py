from django import forms
from app.models import *

class Topic_forms(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'



class web_forms(forms.ModelForm):
    class Meta:
        model=webpages
        fields='__all__'
        #fields=['topic_name','name']
        #exclude=['name']
        help_texts={'name':'enter only name'}
        widgets={'name':forms.PasswordInput,'url':forms.Textarea,'topic_name':forms.RadioSelect}


class A_R_forms(forms.ModelForm):
    class Meta:
        model=A_R
        fields='__all__'
            