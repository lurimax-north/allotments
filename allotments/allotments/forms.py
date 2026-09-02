from crispy_forms.helper import FormHelper
from crispy_forms.layout import Hidden, Submit

from django import forms
from django.forms import ModelForm
from django.urls import reverse
from allotments.models import Message, Comment
class MessageForm(forms.ModelForm):
    message = forms.CharField()

    class Meta:
        model = Message
        fields = ['message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "message-form"
        self.helper.form_method = "post"
        self.helper.form_action = reverse("message_create")
        self.helper.add_input(Submit("submit", "Post"))

class CommentForm(forms.ModelForm):
    comment = forms.CharField()

    class Meta:
        model = Comment
        fields = ['comment']

