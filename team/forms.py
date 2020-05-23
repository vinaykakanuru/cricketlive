from django import forms
from team.models import PlayerHistory, Matches, Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = '__all__'


class PlayerHistoryForm(forms.ModelForm):
    class Meta:
        model = PlayerHistory
        fields = '__all__'


class MatchForm(forms.ModelForm):
    class Meta:
        model = Matches
        fields = '__all__'
