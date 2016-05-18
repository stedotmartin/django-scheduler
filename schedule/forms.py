from django import forms
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from schedule.models import Event, Occurrence, Rule
from schedule.widgets import SpectrumColorPicker
from django.template.loader import render_to_string



class SpanForm(forms.ModelForm):
    start = forms.SplitDateTimeField(label=_("start"))
    end = forms.SplitDateTimeField(label=_("end"),
                                   help_text=_(u"The end time must be later than start time."))

    def clean(self):
        if 'end' in self.cleaned_data and 'start' in self.cleaned_data:
            if self.cleaned_data['end'] <= self.cleaned_data['start']:
                raise forms.ValidationError(_(u"The end time must be later than start time."))
        return self.cleaned_data

class RuleWidget(forms.Widget):
	template_name = 'schedule/rule_creator.html'
	def render(self, name, value, attrs=None):
		context = {
		'url': '/'
		}
		return mark_safe(render_to_string(self.template_name, context))
		

class RuleForm(forms.ModelForm):
	params = forms.CharField(widget=RuleWidget)
	class Meta:
		model = Rule
		exclude = []


		

class EventForm(SpanForm):
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)

    end_recurring_period = forms.DateTimeField(label=_(u"End recurring period"),
                                               help_text=_(u"This date is ignored for one time only events."),
                                               required=False)

    class Meta(object):
        model = Event
        exclude = ('creator', 'created_on', 'calendar')


class OccurrenceForm(SpanForm):
    class Meta(object):
        model = Occurrence
        exclude = ('original_start', 'original_end', 'event', 'cancelled')


class EventAdminForm(forms.ModelForm):
    class Meta:
        exclude = []
        
        model = Event
        widgets = {
          'color_event': SpectrumColorPicker,
        }


