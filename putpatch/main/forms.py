from django import forms
from .models import IssueTickets


class ticketForm(forms.ModelForm):
    class Meta:
        model = IssueTickets
        fields = ("ticketNumber","createdBy","issueDetial","status","assignedTo")