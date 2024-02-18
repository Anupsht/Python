from django import forms

class PostCustomForm(forms.Form):
    title = forms.CharField(
        label="Post Title", widget=forms.TextInput(attrs={"class": "form-control",}),)
    

    content = forms.CharField(
        label="Post Content",
        widget=forms.Textarea(attrs={"class":"form-control"}),
    )

    image = forms.ImageField(required=True) 

from post.models import Post
class PostModeForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 5:
            raise forms.ValidationError("Title field must have atleast 5 letters.")
        return title