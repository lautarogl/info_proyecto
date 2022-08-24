from django import newforms as forms

from apps.comentarios.models import Comentario

TOPIC_CHOICES = (
    ('general', 'General enquiry'),
    ('bug', 'Bug report'),
    ('suggestion', 'Suggestion'),
)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comentario
        fields = ('noticia', 'comentario')