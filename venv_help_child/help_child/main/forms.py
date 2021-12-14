from django import forms

Mood = (
    ('good', '良'),
    ('usually', '普'),
    ('bad', '悪'),
)

Hardness = (
    ('water', '水'),
    ('soft', '軟'),
    ('usually', '普'),
    ('hard', '硬'),
)

Number = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

Presence_Or_Absence = (
    ('y', '有'),
    ('n', '無'),
)

Temperature_Int = (
    ('34', '34'),
    ('35', '35'),
    ('36', '36'),
    ('37', '37'),
    ('38', '38'),
    ('39', '39'),
    ('40', '40'),
)

Temperature_Dec = (
    ('0', '0'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
)

Pick_up_List = (
    ('father', '父'),
    ('mother', '母'),
    ('Brother', '兄'),
    ('sister', '姉'),
    ('grandfather', '祖父'),
    ('grandmother', '祖母'),
    ('bus', 'バス'),
)


class HomeContactForm(forms.Form):
    dinner_time = forms.DateTimeField(input_formats=['%H/%M'])
    dinner_text = forms.CharField(widget=forms.Textarea)
    breakfast_time = forms.DateTimeField(input_formats=['%H/%M'])
    breakfast_text = forms.CharField(widget=forms.Textarea)
    home_inbed = forms.DateTimeField(input_formats=['%H/%M'])
    home_outbed = forms.DateTimeField(input_formats=['%H/%M'])
    home_mood = forms.fields.ChoiceField(
        choices=Mood,
        widget=forms.widgets.RadioSelect
    )
    home_hardness = forms.fields.ChoiceField(
        choices=Hardness,
        widget=forms.widgets.RadioSelect
    )
    home_defecate_num = forms.fields.ChoiceField(
        choices=Number,
        widget=forms.Select
    )
    home_bathe = forms.fields.ChoiceField(
        choices=Presence_Or_Absence,
        widget=forms.widgets.RadioSelect
    )
    home_temp_time = forms.DateTimeField(input_formats=['%H/%M'])
    home_temperature_int = forms.fields.ChoiceField(
        choices=Temperature_Int,
        widget=forms.Select
    )
    home_temperature_dec = forms.fields.ChoiceField(
        choices=Temperature_Dec,
        widget=forms.Select
    )
    home_information = forms.CharField(widget=forms.Textarea)
    pickup = forms.fields.ChoiceField(
        choices=Pick_up_List,
        widget=forms.Select
    )
    pickup_time = forms.DateTimeField(input_formats=['%H/%M'])


class SchoolContactForm(forms.Form):
    lunch_time = forms.DateTimeField(input_formats=['%H/%M'])
    lunch_text = forms.CharField(widget=forms.Textarea)
    school_inbed = forms.DateTimeField(input_formats=['%H/%M'])
    school_outbed = forms.DateTimeField(input_formats=['%H/%M'])
    school_mood = forms.fields.ChoiceField(
        choices=Mood,
        widget=forms.widgets.RadioSelect
    )
    school_hardness = forms.fields.ChoiceField(
        choices=Hardness,
        widget=forms.widgets.RadioSelect
    )
    school_defecate_num = forms.fields.ChoiceField(
        choices=Number,
        widget=forms.Select
    )
    school_bathe = forms.fields.ChoiceField(
        choices=Presence_Or_Absence,
        widget=forms.widgets.RadioSelect
    )
    school_temp_time = forms.DateTimeField(input_formats=['%H/%M'])
    school_temperature_int = forms.fields.ChoiceField(
        choices=Temperature_Int,
        widget=forms.Select
    )
    school_temperature_dec = forms.fields.ChoiceField(
        choices=Temperature_Dec,
        widget=forms.Select
    )
    school_information = forms.CharField(widget=forms.Textarea)
    filler_name = forms.CharField(max_length=20)
