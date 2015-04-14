from django import forms
from tagging.forms import TagField
from tagging_autocomplete.widgets import TagAutocomplete

class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, label='')
    #search = TagField(widget=TagAutocomplete())