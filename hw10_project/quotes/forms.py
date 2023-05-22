from django.forms import ModelForm, CharField, DateField, TextInput, DateInput, ModelMultipleChoiceField, Select , SelectMultiple, ModelChoiceField


from .models import Author, Quote, Tag


class AuthorForm(ModelForm):
    fullname = CharField(max_length=200, required=True,
                         widget=TextInput(attrs={"class": "form-control"}))
    born_date = DateField(required=True, widget=DateInput(
        attrs={"class": "form-control"}))
    born_location = CharField(required=True, widget=TextInput(
        attrs={"class": "form-control"}))
    description = CharField(required=True, widget=TextInput(
        attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = ["fullname", "born_date", "born_location", "description"]


class QuoteForm(ModelForm):
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(
    ).order_by("name"), required=True, widget=SelectMultiple(attrs={"class": "form-control"}))
    author = ModelChoiceField(queryset=Author.objects.all().order_by("fullname"), required=True, widget=Select(
        attrs={"class": "form-control"}))
    quote = CharField(required=True, widget=TextInput(
        attrs={"class": "form-control"}))

    class Meta:
        model = Quote
        fields = ["tags", "author", "quote"]
        # exclude = ["tags"]


class TagForm(ModelForm):
    name = CharField(required=True,
                     widget=TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Tag
        fields = ["name"]
