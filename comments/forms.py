from captcha.fields import CaptchaField
from django import forms
from mptt.forms import TreeNodeChoiceField

from comments.form_validator import validator_allowed_tags, validator_closed_tags
from comments.models import Comment  # , User


class CommentForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Comment.objects.all())
    text = forms.CharField(
        validators=[validator_allowed_tags, validator_closed_tags],
        widget=forms.Textarea(attrs={"cols": 36, "rows": 7, "class": "m-2"}),
    )
    url = forms.URLField(
        required=False, widget=forms.URLInput(attrs={"size": 36, "class": "m-2"})
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields["parent"].widget.attrs.update({"class": "d-none"})
        self.fields["parent"].label = ""
        self.fields["parent"].required = False


class AnonimCommentForm(CommentForm):
    captcha = CaptchaField(
        label="Enter captcha", error_messages={"invalid": "Uncorrect text captcha"}
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"size": 36, "class": "m-2"})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"size": 36, "class": "m-2"})
    )

    class Meta:
        model = Comment
        fields = ("username", "email", "parent", "text", "url", "captcha")


class AuthCommentForm(CommentForm):
    class Meta:
        model = Comment
        fields = ("parent", "text", "url")
