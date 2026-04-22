from django import forms


class CommentForm(forms.Form):
  name = forms.CharField(label="Tu nombre")
  web_page = forms.URLField(label="Tu página web", required=False, initial="https://")
  comment = forms.CharField(label="Tu comentario", widget=forms.Textarea)