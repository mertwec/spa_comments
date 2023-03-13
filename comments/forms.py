from comments.models import Comment #, User
from django import forms
from mptt.forms import TreeNodeChoiceField


class NewCommentForm(forms.ModelForm):

    parent = TreeNodeChoiceField(queryset=Comment.objects.all())

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields['parent'].widget.attrs.update({'class':'d-none'})
        self.fields['parent'].label = ''
        self.fields['parent'].required = False

    class Meta:
        model = Comment
        fields = ("username", "email", 'parent', 'text', 'url')
        widgets = {
            "username":forms.TextInput(attrs={"size":36, "class": "m-2"}),
            "email": forms.EmailInput(attrs={"size":36, "class": "m-2"}),
            'text': forms.Textarea(attrs={"cols":36, "rows":7, "class": "m-2"}), 
            'url':forms.URLInput(attrs={"size":36, "class": "m-2"}),
        }
