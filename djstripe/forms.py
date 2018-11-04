# -*- coding: utf-8 -*-
"""
.. module:: djstripe.forms
   :synopsis: dj-stripe Forms.

.. moduleauthor:: Daniel Greenfeld (@pydanny)

"""

from django import forms

from .models import Plan


class PlanForm(forms.Form):
    plan = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        super(PlanForm, self).__init__(*args, **kwargs)
        plan = Plan.objects.last()
        if not plan:
            raise Exception('No any plan')
        self.fields['plan'].choices = (
            (plan.stripe_id, plan.name),
        )


class CancelSubscriptionForm(forms.Form):
    pass
