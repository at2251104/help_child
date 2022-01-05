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

Temperature = (
    ('34.0', '34.0'),
    ('34.1', '34.1'),
    ('34.2', '34.2'),
    ('34.3', '34.3'),
    ('34.4', '34.4'),
    ('34.5', '34.5'),
    ('34.6', '34.6'),
    ('34.7', '34.7'),
    ('34.8', '34.8'),
    ('34.9', '34.9'),
    ('35.0', '35.0'),
    ('35.1', '35.1'),
    ('35.2', '35.2'),
    ('35.3', '35.3'),
    ('35.4', '35.4'),
    ('35.5', '35.5'),
    ('35.6', '35.6'),
    ('35.7', '35.7'),
    ('35.8', '35.8'),
    ('35.9', '35.9'),
    ('36.0', '36.0'),
    ('36.1', '36.1'),
    ('36.2', '36.2'),
    ('36.3', '36.3'),
    ('36.4', '36.4'),
    ('36.5', '36.5'),
    ('36.6', '36.6'),
    ('36.7', '36.7'),
    ('36.8', '36.8'),
    ('36.9', '36.9'),
    ('37.0', '37.0'),
    ('37.1', '37.1'),
    ('37.2', '37.2'),
    ('37.3', '37.3'),
    ('37.4', '37.4'),
    ('37.5', '37.5'),
    ('37.6', '37.6'),
    ('37.7', '37.7'),
    ('37.8', '37.8'),
    ('37.9', '37.9'),
    ('38.0', '38.0'),
    ('38.1', '38.1'),
    ('38.2', '38.2'),
    ('38.3', '38.3'),
    ('38.4', '38.4'),
    ('38.5', '38.5'),
    ('38.6', '38.6'),
    ('38.7', '38.7'),
    ('38.8', '38.8'),
    ('38.9', '38.9'),
    ('39.0', '39.0'),
    ('39.1', '39.1'),
    ('39.2', '39.2'),
    ('39.3', '39.3'),
    ('39.4', '39.4'),
    ('39.5', '39.5'),
    ('39.6', '39.6'),
    ('39.7', '39.7'),
    ('39.8', '39.8'),
    ('39.9', '39.9'),
    ('40', '40'),
)

Pick_up_List = (
    ('父', '父'),
    ('母', '母'),
    ('兄', '兄'),
    ('姉', '姉'),
    ('祖父', '祖父'),
    ('祖母', '祖母'),
    ('バス', 'バス'),
)


class HomeContactForm(forms.Form):
    t007_fd03_meal_time = forms.DateTimeField(input_formats=['%H/%M'])
    t007_fd04_meal_contents = forms.CharField(
        widget=forms.Textarea,
        max_length=100,
    )
    t007_fd14_breakfast_time = forms.DateTimeField(input_formats=['%H/%M'])
    t007_fd13_breakfast_contents = forms.CharField(
        widget=forms.Textarea,
        max_length=100,
    )
    t007_fd05_bed_time = forms.DateTimeField(input_formats=['%H/%M'])
    t007_fd06_wakeup_time = forms.DateTimeField(input_formats=['%H/%M'])
    t007_fd07_mood = forms.fields.ChoiceField(
        choices=Mood,
        widget=forms.widgets.RadioSelect,
    )
    t007_fd08_defecation_status = forms.fields.ChoiceField(
        choices=Hardness,
        widget=forms.widgets.RadioSelect,
    )
    t007_fd09_defecation_times = forms.fields.ChoiceField(
        choices=Number,
        widget=forms.Select,
    )
    t007_fd10_bathing = forms.fields.ChoiceField(
        choices=Presence_Or_Absence,
        widget=forms.widgets.RadioSelect,
    )
    t007_fd11_temperature_time = forms.DateTimeField(input_formats=['%H/%M'])
    t007_fd12_temperature = forms.fields.ChoiceField(
        choices=Temperature,
        widget=forms.Select,
    )
    t007_fd02_infomation = forms.CharField(
        widget=forms.Textarea,
        max_length=200,
    )
    t007_fd25_pickup_person = forms.fields.ChoiceField(
        choices=Pick_up_List,
        widget=forms.Select,
        
    )
    t007_fd26_pickup_time = forms.DateTimeField(input_formats=['%H/%M'])


class SchoolContactForm(forms.Form):
    t007_fd16_lunch_time = forms.DateTimeField(input_formats=['%H/%M'])
    t007_fd15_lunch_contents = forms.CharField(
        widget=forms.Textarea,
        max_length=100,
    )
    t007_fd27_bed_time = forms.DateTimeField(input_formats=['%H/%M'])
    t007_fd17_wakeup_time = forms.DateTimeField(input_formats=['%H/%M'])
    t007_fd18_mood = forms.fields.ChoiceField(
        choices=Mood,
        widget=forms.widgets.RadioSelect,
    )
    t007_fd20_defecation_status = forms.fields.ChoiceField(
        choices=Hardness,
        widget=forms.widgets.RadioSelect
    )
    t007_fd19_defecation_times = forms.fields.ChoiceField(
        choices=Number,
        widget=forms.Select,
    )
    t007_fd21_bathing = forms.fields.ChoiceField(
        choices=Presence_Or_Absence,
        widget=forms.widgets.RadioSelect,
    )
    t007_fd23_temperature_time = forms.DateTimeField(input_formats=['%H/%M'])
    t007_fd22_temperature = forms.fields.ChoiceField(
        choices=Temperature,
        widget=forms.Select,
    )
    t007_fd24_infomation = forms.CharField(
        widget=forms.Textarea,
        max_length=200,
    )
    t007_fk02_childminder_id = forms.CharField(max_length=20)
