from django.db import models
from multiselectfield import MultiSelectField  

PURPOSE_CHOICES = [
    ('Coding', 'Coding'),
    ('Research', 'Research'),
    ('Design', 'Design'),
    ('Career Prep', 'Career Prep'),
    ('Entertainment', 'Entertainment'),
    ('Other', 'Other')
]

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)

    YEAR_CHOICES = [
        ('1', '1st Year'),
        ('2', '2nd Year'),
        ('3', '3rd Year'),
        ('4', '4th Year'),
    ]
    year = models.CharField(max_length=2, choices=YEAR_CHOICES)

    DEPARTMENT_CHOICES = [
        ('IOD', 'MIT Institute of Design (IOD)'),
        ('ISBJ', 'International School of Broadcasting & Journalism (ISBJ)'),
        ('MANET', 'Maharashtra Academy of Naval Engineering and Training'),
        ('MITCOM', 'MIT College of Management'),
        ('SBSR', 'MIT School of Bioengineering Science & Research'),
        ('SFTh', 'MIT School of Film and Theatre'),
        ('SICS', 'MIT School of Indian Civil Services'),
        ('SOA', 'MIT School of Architecture'),
        ('SOC', 'MIT School of Computing'),
        ('SOER', 'MIT School of Education & Research'),
        ('SOES', 'MIT School of Engineering and Sciences'),
        ('SOFA', 'MIT School of Fine Art & Applied Art'),
        ('SoFT', 'MIT School of Food Technology'),
        ('SOH', 'MIT School of Humanities'),
        ('SOL', 'MIT School of Law'),
        ('SVS', 'School of Vedic Sciences'),
        ('VSKA', 'MIT Vishwashanti Sangeet Kala Academy'),
    ]
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, default='IOD')

    TOOLS_CHOICES = [
        ('ChatGPT', 'ChatGPT'),
        ('Bard', 'Google Bard'),
        ('Bing', 'Microsoft Bing Chat'),
        ('Copilot', 'GitHub Copilot'),
        ('Claude', 'Claude'),
        ('Midjourney', 'Midjourney'),
        ('DALL-E', 'DALL·E'),
        ('Gemini', 'Gemini'),
        ('DeepSeek', 'DeepSeek'),
        ('Other', 'Other'),
    ]
    tools = models.CharField(max_length=20, choices=TOOLS_CHOICES, default='Other')


    purposes = MultiSelectField(choices=PURPOSE_CHOICES, max_length=200)

    accuracy = models.IntegerField(default=0)

    def __str__(self):
        return self.name
