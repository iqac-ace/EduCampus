from django import forms
from decimal import Decimal, InvalidOperation
from django.contrib.auth.models import User
from .models import (Department, Student, Subject, SemesterResult, ActivityEvidence, ProgressSubmission, ScoreParameter, Profile,ROLE_CHOICES)
from .progress_rules import PROGRESS_RULES

class DepartmentForm(forms.ModelForm):
    class Meta: model=Department; fields=['code','name','active']
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'register_number',
            'name',
            'department',
            'batch',
            'current_semester',
            'email',
            'phone',
            'class12_board',
            'class12_total',
            'class12_max',
            'active',
        ]

        widgets = {
            'register_number': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Register Number'
                }
            ),

            'name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Student Name'
                }
            ),

            'department': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'batch': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Example: 2025-2029'
                }
            ),

            'current_semester': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'min': 1,
                    'max': 8
                }
            ),

            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Student Email'
                }
            ),

            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Phone Number'
                }
            ),

            'class12_board': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': '12th Board'
                }
            ),

            'class12_total': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),

            'class12_max': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'step': '0.01'
                }
            ),
        }
class SubjectForm(forms.ModelForm):
    class Meta: model=Subject; fields='__all__'
class SemesterResultForm(forms.ModelForm):
    class Meta: model=SemesterResult; exclude=['uploaded_by','status']
class ActivityEvidenceForm(forms.ModelForm):
    class Meta: model=ActivityEvidence; exclude=['created_by','status']
class ActivityForm(forms.ModelForm):

    class Meta:
        model = ActivityEvidence

        fields = [
            'student',
            'parameter',
            'title',
            'activity_date',
            'evidence',
            'remarks',
        ]

        widgets = {

            'student': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'parameter': forms.Select(
                attrs={
                    'class': 'form-select'
                }
            ),

            'title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'activity_date': forms.DateInput(
                attrs={
                    'type': 'date',
                    'class': 'form-control'
                }
            ),

            'evidence': forms.ClearableFileInput(
                attrs={
                    'class': 'form-control'
                }
            ),

            'remarks': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'rows': 3
                }
            ),
        }
class ExcelUploadForm(forms.Form):
    file=forms.FileField(help_text='Upload .xlsx file using the provided template')
class StaffCreateForm(forms.Form):

    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )

    first_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    last_name = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )

    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        widget=forms.Select(
            attrs={'class': 'form-select'}
        )
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.filter(active=True),
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-select'}
        ),
        help_text='Required for HOD accounts.'
    )

    student = forms.ModelChoiceField(
        queryset=Student.objects.filter(
            active=True
        ).select_related('department'),
        required=False,
        widget=forms.Select(
            attrs={'class': 'form-select'}
        ),
        help_text='Select only when creating a Student login.'
    )
class StudentProgressForm(forms.ModelForm):

    title = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    activity_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'})
    )
    subtopic = forms.CharField(
        required=False,
        widget=forms.Select(attrs={'class': 'form-select', 'id': 'id_subtopic'})
    )
    detail_1 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_detail_1'})
    )
    detail_2 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_detail_2'})
    )
    detail_3 = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'id_detail_3'})
    )

    class Meta:
        model = ActivityEvidence
        fields = [
            'student', 'parameter', 'title', 'activity_date',
            'board', 'school', 'academic_year', 'academic_group',
            'marks_obtained', 'maximum_marks', 'remarks',
        ]
        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'parameter': forms.Select(attrs={'class': 'form-select'}),
            'board': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: State Board / CBSE'}),
            'school': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'School name'}),
            'academic_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: 2023-2024'}),
            'academic_group': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Example: Maths Biology'}),
            'marks_obtained': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '0'}),
            'maximum_marks': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01', 'min': '1'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['parameter'].label_from_instance = lambda obj: (
            f"{obj.category_code}. {obj.name} — {obj.max_points} Points"
        )
        if not user:
            return
        current_role = 'IQAC' if user.is_superuser else getattr(
            getattr(user, 'profile', None), 'role', ''
        )
        if current_role == 'STUDENT':
            self.fields['student'].required = False
            self.fields['student'].widget = forms.HiddenInput()
        elif current_role == 'HOD':
            self.fields['student'].queryset = Student.objects.filter(
                department=user.profile.department, active=True
            ).order_by('register_number')
        else:
            self.fields['student'].queryset = Student.objects.filter(
                active=True
            ).select_related('department').order_by(
                'department__code', 'register_number'
            )

    def clean(self):
        cleaned = super().clean()
        parameter = cleaned.get('parameter')
        parameter_text = str(parameter).lower() if parameter else ''
        is_plus2 = '+2 academic performance' in parameter_text

        if is_plus2:
            required_fields = {
                'board': 'Board is required.',
                'school': 'School is required.',
                'academic_year': 'Academic year is required.',
                'academic_group': 'Group is required.',
                'marks_obtained': 'Marks obtained is required.',
                'maximum_marks': 'Maximum marks is required.',
            }
            for field, message in required_fields.items():
                if cleaned.get(field) in (None, ''):
                    self.add_error(field, message)

            obtained = cleaned.get('marks_obtained')
            maximum = cleaned.get('maximum_marks')
            if maximum is not None and maximum <= 0:
                self.add_error('maximum_marks', 'Maximum marks must be greater than zero.')
            elif obtained is not None and maximum is not None and obtained > maximum:
                self.add_error('marks_obtained', 'Marks obtained cannot exceed maximum marks.')
        else:
            if not cleaned.get('title'):
                self.add_error('title', 'Activity title is required.')
            if not cleaned.get('activity_date'):
                self.add_error('activity_date', 'Activity date is required.')

        return cleaned


class ProgressSubmissionForm(
    forms.ModelForm
):

    detail_1 = forms.CharField(required=False)
    detail_2 = forms.CharField(required=False)
    detail_3 = forms.CharField(required=False)
    detail_4 = forms.CharField(required=False)

    # ========================================================
    # ACADEMIC /20
    # ========================================================

    academic_basis = forms.ChoiceField(

        required=False,

        choices=[
            ('', '---------'),
            ('CGPA', 'CGPA'),
            ('SGPA', 'SGPA'),
            (
                'PLUS2',
                '+2 Percentage - First Year Provisional'
            ),
        ],

        widget=forms.Select(
            attrs={
                'class':
                    'form-select'
            }
        )
    )


    academic_value = forms.DecimalField(

        required=False,

        min_value=0,

        max_value=10,

        decimal_places=2,

        widget=forms.NumberInput(
            attrs={
                'class':
                    'form-control',

                'step': '0.01'
            }
        )
    )


    board = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control'
            }
        )
    )


    school = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control'
            }
        )
    )


    plus2_year = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',

                'placeholder':
                    'Example: 2025-2026'
            }
        )
    )


    plus2_group = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control'
            }
        )
    )


    plus2_percentage = forms.DecimalField(

        required=False,

        min_value=0,

        max_value=100,

        decimal_places=2,

        widget=forms.NumberInput(
            attrs={
                'class':
                    'form-control',

                'step': '0.01'
            }
        )
    )


    # ========================================================
    # ATTENDANCE /10
    # ========================================================

    attendance_percentage = forms.DecimalField(

        required=False,

        min_value=0,

        max_value=100,

        decimal_places=2,

        widget=forms.NumberInput(
            attrs={
                'class':
                    'form-control',

                'step': '0.01'
            }
        )
    )


    attendance_period = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',

                'placeholder':
                    'Example: Semester 3'
            }
        )
    )


    # ========================================================
    # LEARNING /10
    # ========================================================

    learning_level = forms.ChoiceField(

        required=False,

        choices=[

            (
                '',
                'Select achievement'
            ),

            (
                'CERT_3_PLUS',
                '3 or more recognized certifications - 10'
            ),

            (
                'CERT_2',
                '2 certifications - 8'
            ),

            (
                'CERT_1',
                '1 certification - 6'
            ),

            (
                'MOOC',
                'MOOC / NPTEL / SWAYAM / ODL - 4'
            ),

            (
                'STRUCTURED',
                'Structured learning programme - 2'
            ),

            (
                'NONE',
                'None - 0'
            ),
        ],

        widget=forms.Select(
            attrs={
                'class':
                    'form-select'
            }
        )
    )


    certificate_name = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',

                'placeholder':
                    'Certificate/course name'
            }
        )
    )


    certificate_provider = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',

                'placeholder':
                    'NPTEL / SWAYAM / Coursera / Company'
            }
        )
    )


    # ========================================================
    # TECHNICAL /15
    # ========================================================

    technical_level = forms.ChoiceField(

        required=False,

        choices=[

            ('', 'Select achievement'),

            (
                'NATIONAL_INTL',
                'National/International achievement '
                '- 15'
            ),

            (
                'MAJOR_ACHIEVEMENT',
                'Major hackathon/competition '
                'achievement - 12'
            ),

            (
                'FUNCTIONAL_PROJECT',
                'Functional industry/technical '
                'project - 10'
            ),

            (
                'ENGINEERING_EXPLORATION',
                'Engineering Exploration / '
                'substantial project - 8'
            ),

            (
                'PARTICIPATION',
                'Hackathon/competition '
                'participation - 5'
            ),

            (
                'BASIC',
                'Basic technical activity - 3'
            ),

            (
                'NONE',
                'None - 0'
            ),
        ],

        widget=forms.Select(
            attrs={
                'class':
                    'form-select'
            }
        )
    )


    technical_title = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',

                'placeholder':
                    'Project / competition / '
                    'hackathon name'
            }
        )
    )


    technology_used = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',

                'placeholder':
                    'Technology / tools used'
            }
        )
    )


    # ========================================================
    # INTERNSHIP /10
    # ========================================================

    internship_level = forms.ChoiceField(

        required=False,

        choices=[

            ('', 'Select achievement'),

            (
                'EXCELLENT_PPO',
                'Internship + excellent evaluation/'
                'PPO - 10'
            ),

            (
                'SIX_PLUS_WEEKS',
                'Internship ≥6 weeks - 8'
            ),

            (
                'FOUR_FIVE_WEEKS',
                'Internship 4-5 weeks - 6'
            ),

            (
                'SHORT_TERM',
                'Short internship / industry '
                'project - 4'
            ),

            (
                'VISIT_INTERACTION',
                'Industrial visit / expert '
                'interaction - 2'
            ),

            (
                'NONE',
                'None - 0'
            ),
        ],

        widget=forms.Select(
            attrs={
                'class':
                    'form-select'
            }
        )
    )


    internship_organization = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control'
            }
        )
    )


    internship_title = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control'
            }
        )
    )


    duration_weeks = forms.DecimalField(

        required=False,

        min_value=0,

        decimal_places=1,

        widget=forms.NumberInput(
            attrs={
                'class':
                    'form-control',

                'step': '0.5'
            }
        )
    )


    # ========================================================
    # RESEARCH /10
    # ========================================================

    research_level = forms.ChoiceField(

        required=False,

        choices=[

            ('', 'Select achievement'),

            (
                'GRANTED_PATENT',
                'Granted patent / major '
                'research - 10'
            ),

            (
                'PATENT_SCOPUS_WOS',
                'Published patent / Scopus / '
                'WoS - 9'
            ),

            (
                'PUBLICATION_PROJECT',
                'Publication / significant '
                'research project - 7'
            ),

            (
                'PAPER_IIC',
                'Paper presentation / '
                'IIC project - 5'
            ),

            (
                'PROTOTYPE_IDEA',
                'Prototype / idea submission - 3'
            ),

            (
                'AWARENESS',
                'Research awareness programme - 1'
            ),

            (
                'NONE',
                'None - 0'
            ),
        ],

        widget=forms.Select(
            attrs={
                'class':
                    'form-select'
            }
        )
    )


    research_title = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control'
            }
        )
    )


    research_reference = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',

                'placeholder':
                    'DOI / Patent No / Conference'
            }
        )
    )


    # ========================================================
    # CAREER /10
    # ========================================================

    career_level = forms.ChoiceField(

        required=False,

        choices=[

            ('', 'Select achievement'),

            (
                'PLACED_HIGHER_STUDIES',
                'Placement/PPO/Higher-study '
                'admission - 10'
            ),

            (
                'ADVANCED_READINESS',
                'Advanced placement readiness - 8'
            ),

            (
                'STRONG_ASSESSMENT',
                'Strong aptitude/coding/interview '
                'performance - 6'
            ),

            (
                'TRAINING_COMPLETED',
                'Completed placement training - 4'
            ),

            (
                'CAREER_PROGRAMME',
                'Career development programme - 2'
            ),

            (
                'NONE',
                'None - 0'
            ),
        ],

        widget=forms.Select(
            attrs={
                'class':
                    'form-select'
            }
        )
    )


    career_activity = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control'
            }
        )
    )


    career_organization = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',

                'placeholder':
                    'Company / Institution / '
                    'Training provider'
            }
        )
    )


    # ========================================================
    # LEADERSHIP /5
    # ========================================================

    leadership_level = forms.ChoiceField(

        required=False,

        choices=[

            ('', 'Select achievement'),

            (
                'MAJOR_LEADER',
                'Student leader / office bearer / '
                'major leadership - 5'
            ),

            (
                'CLUB_LEADER',
                'Domain club / society leader - 4'
            ),

            (
                'REGULAR_PARTICIPATION',
                'Regular club participation - 3'
            ),

            (
                'MENTOR_ACTIVITY',
                'Peer teaching / mentoring / '
                'activity - 2'
            ),

            (
                'MEMBERSHIP',
                'Membership only - 1'
            ),

            (
                'NONE',
                'None - 0'
            ),
        ],

        widget=forms.Select(
            attrs={
                'class':
                    'form-select'
            }
        )
    )


    leadership_role = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control'
            }
        )
    )


    club_body = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',

                'placeholder':
                    'Club / Society / Committee'
            }
        )
    )


    # ========================================================
    # SOCIAL /5
    # ========================================================

    social_level = forms.ChoiceField(

        required=False,

        choices=[

            ('', 'Select achievement'),

            (
                'LED_MAJOR',
                'Led major initiative - 5'
            ),

            (
                'THREE_PLUS',
                '3 or more activities - 4'
            ),

            (
                'TWO_ACTIVITIES',
                '2 activities - 3'
            ),

            (
                'ONE_ACTIVITY',
                '1 activity - 2'
            ),

            (
                'AWARENESS',
                'Awareness programme - 1'
            ),

            (
                'NONE',
                'None - 0'
            ),
        ],

        widget=forms.Select(
            attrs={
                'class':
                    'form-select'
            }
        )
    )


    initiative_name = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',

                'placeholder':
                    'NSS / UBA / SDG / IQAC / Outreach'
            }
        )
    )


    social_activity_count = forms.IntegerField(

        required=False,

        min_value=0,

        widget=forms.NumberInput(
            attrs={
                'class':
                    'form-control'
            }
        )
    )


    # ========================================================
    # SPORTS/CULTURAL /5
    # ========================================================

    sports_level = forms.ChoiceField(

        required=False,

        choices=[

            ('', 'Select achievement'),

            (
                'NATIONAL_INTL',
                'National/International - 5'
            ),

            (
                'STATE_UNIVERSITY',
                'State/University/Inter-Zone - 4'
            ),

            (
                'DISTRICT_REGIONAL',
                'District/Regional - 3'
            ),

            (
                'INSTITUTIONAL',
                'Institutional level - 2'
            ),

            (
                'PARTICIPATION',
                'Participation - 1'
            ),

            (
                'NONE',
                'None - 0'
            ),
        ],

        widget=forms.Select(
            attrs={
                'class':
                    'form-select'
            }
        )
    )


    sports_event = forms.CharField(

        required=False,

        widget=forms.TextInput(
            attrs={
                'class':
                    'form-control',

                'placeholder':
                    'Sport / Cultural Event / Award'
            }
        )
    )


    # ========================================================
    # META
    # ========================================================

    class Meta:

        model = ProgressSubmission

        fields = [

            'parameter',
            'academic_year',
            'subtopic',
            'evidence',
            'remarks',
        ]

        widgets = {

            'parameter':
                forms.Select(
                    attrs={
                        'class':
                            'form-select'
                    }
                ),

            'academic_year':
                forms.TextInput(
                    attrs={
                        'class':
                            'form-control',

                        'placeholder':
                            'Example: 2026-2027'
                    }
                ),

            'evidence':
                forms.ClearableFileInput(
                    attrs={
                        'class':
                            'form-control',

                        'accept':
                            '.pdf,.jpg,.jpeg,.png'
                    }
                ),

            'remarks':
                forms.Textarea(
                    attrs={
                        'class':
                            'form-control',

                        'rows': 3
                    }
                ),
        }


    def __init__(
        self,
        *args,
        **kwargs
    ):

        super().__init__(
            *args,
            **kwargs
        )


        self.fields[
            'parameter'
        ].queryset = (

            ScoreParameter.objects
            .filter(
                active=True
            )
            .order_by(
                'order'
            )
        )


        self.fields[
            'parameter'
        ].label_from_instance = (
            lambda obj:
                f"{obj.order}. "
                f"{obj.name} — "
                f"{obj.max_points} Points"
        )

def clean(self):

    cleaned = super().clean()

    parameter = cleaned.get(
        'parameter'
    )

    if not parameter:
        return cleaned


    parameter_rule = (
        PROGRESS_RULES.get(
            parameter.code
        )
    )

    if not parameter_rule:

        self.add_error(
            'parameter',
            'Invalid performance parameter.'
        )

        return cleaned


    subtopic = (
        cleaned.get('subtopic')
        or
        self.data.get('subtopic')
        or
        ''
    ).strip()


    subtopics = (
        parameter_rule.get(
            'subtopics',
            {}
        )
    )


    if subtopic not in subtopics:

        self.add_error(
            None,
            'Please select a valid '
            'Sub-Parameter / Achievement.'
        )

        return cleaned


    sub_rule = (
        subtopics[
            subtopic
        ]
    )


    requirements = (
        sub_rule.get(
            'requirements',
            []
        )
    )


    submitted_details = {}


    for index, requirement in enumerate(
        requirements,
        start=1
    ):

        value = (
            self.data.get(
                f'detail_{index}',
                ''
            )
            or ''
        ).strip()


        if not value:

            self.add_error(
                None,
                f'{requirement} is required.'
            )


        submitted_details[
            requirement
        ] = value


    details = {

        'subtopic_code':
            subtopic,

        'achievement':
            sub_rule.get(
                'label',
                ''
            ),

        'rule_points':
            sub_rule.get(
                'points'
            ),

        'submitted_details':
            submitted_details,
    }


    # =====================================================
    # ACADEMIC VALIDATION
    # =====================================================

    if parameter.code == 'ACADEMIC':

        if subtopic == 'PLUS2':

            percentage_text = (
                submitted_details.get(
                    '12th Percentage',
                    ''
                )
            )

            try:

                percentage = Decimal(
                    percentage_text
                )

                if (
                    percentage < 0
                    or
                    percentage > 100
                ):

                    raise ValueError

            except (
                InvalidOperation,
                ValueError
            ):

                self.add_error(
                    None,
                    'Enter a valid +2 percentage '
                    'between 0 and 100.'
                )

                percentage = Decimal('0')


            details.update({

                'basis':
                    'PLUS2',

                'board':
                    submitted_details.get(
                        'Board',
                        ''
                    ),

                'school':
                    submitted_details.get(
                        'School',
                        ''
                    ),

                'year':
                    submitted_details.get(
                        'Year of Passing',
                        ''
                    ),

                'group':
                    submitted_details.get(
                        'Group',
                        ''
                    ),

                'plus2_percentage':
                    float(
                        percentage
                    ),
            })


        else:

            basis = (
                submitted_details.get(
                    'Basis (CGPA or SGPA)',
                    ''
                )
                .strip()
                .upper()
            )


            if basis not in [
                'CGPA',
                'SGPA'
            ]:

                self.add_error(
                    None,
                    'Select CGPA or SGPA.'
                )


            value_text = (
                submitted_details.get(
                    'CGPA / SGPA',
                    ''
                )
            )


            try:

                academic_value = Decimal(
                    value_text
                )

                if (
                    academic_value < 0
                    or
                    academic_value > 10
                ):

                    raise ValueError

            except (
                InvalidOperation,
                ValueError
            ):

                self.add_error(
                    None,
                    'Enter a valid CGPA / SGPA '
                    'between 0 and 10.'
                )

                academic_value = Decimal('0')


            valid_range = True


            if subtopic == 'CGPA_9':

                valid_range = (
                    academic_value >= 9
                    and
                    academic_value <= 10
                )


            elif subtopic == 'CGPA_8':

                valid_range = (
                    academic_value >= 8
                    and
                    academic_value < 9
                )


            elif subtopic == 'CGPA_7':

                valid_range = (
                    academic_value >= 7
                    and
                    academic_value < 8
                )


            elif subtopic == 'CGPA_6':

                valid_range = (
                    academic_value >= 6
                    and
                    academic_value < 7
                )


            elif subtopic == 'CGPA_5':

                valid_range = (
                    academic_value >= 5
                    and
                    academic_value < 6
                )


            elif subtopic == 'CGPA_LOW':

                valid_range = (
                    academic_value < 5
                )


            if not valid_range:

                self.add_error(
                    None,
                    'The entered CGPA / SGPA does '
                    'not match the selected achievement.'
                )


            details.update({

                'basis':
                    basis,

                'academic_value':
                    float(
                        academic_value
                    ),
            })


    # =====================================================
    # ATTENDANCE VALIDATION
    # =====================================================

    elif parameter.code == 'ATTENDANCE':

        percentage_text = (
            submitted_details.get(
                'Attendance Percentage',
                ''
            )
        )


        try:

            percentage = Decimal(
                percentage_text
            )

            if (
                percentage < 0
                or
                percentage > 100
            ):

                raise ValueError

        except (
            InvalidOperation,
            ValueError
        ):

            self.add_error(
                None,
                'Enter a valid attendance '
                'percentage between 0 and 100.'
            )

            percentage = Decimal('0')


        valid_range = True


        if subtopic == 'ATT_95':

            valid_range = (
                percentage >= 95
            )


        elif subtopic == 'ATT_90':

            valid_range = (
                percentage >= 90
                and
                percentage < 95
            )


        elif subtopic == 'ATT_85':

            valid_range = (
                percentage >= 85
                and
                percentage < 90
            )


        elif subtopic == 'ATT_80':

            valid_range = (
                percentage >= 80
                and
                percentage < 85
            )


        elif subtopic == 'ATT_LOW':

            valid_range = (
                percentage < 80
            )


        if not valid_range:

            self.add_error(
                None,
                'The attendance percentage does '
                'not match the selected range.'
            )


        details.update({

            'attendance_percentage':
                float(
                    percentage
                ),

            'period':
                submitted_details.get(
                    'Semester / Period',
                    ''
                ),
        })


    # =====================================================
    # ALL OTHER PARAMETERS
    # =====================================================

    else:

        # This makes the score code use
        # the selected highest achievement.
        details[
            'level'
        ] = subtopic


    self.cleaned_progress_details = (
        details
    )

    self.cleaned_progress_subtopic = (
        subtopic
    )


    return cleaned



def save(
    self,
    commit=True
):

    instance = super().save(
        commit=False
    )


    instance.subtopic = getattr(
        self,
        'cleaned_progress_subtopic',
        instance.subtopic
    )


    instance.details = getattr(
        self,
        'cleaned_progress_details',
        {}
    )


    if commit:

        instance.save()


    return instance
    


    