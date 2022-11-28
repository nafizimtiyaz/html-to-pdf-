from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class new(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.URLField(blank=True,null=True)
    name=models.TextField(max_length=100, blank=True)
    email=models.EmailField(max_length=150, blank=True)
    number=models.CharField(max_length=20, blank=True)
    description=models.TextField(max_length=1000, blank=True)
    s_school = models.TextField(max_length=200, blank=True)
    s_s_p_year = models.CharField(max_length=200, blank=True)
    h_school = models.TextField(max_length=200, blank=True)
    h_s_p_year = models.CharField(max_length=200, blank=True)
    hons_school = models.TextField(max_length=200, blank=True)
    hons_p_year = models.CharField(max_length=200, blank=True)
    work_ex_c_name_one = models.TextField(max_length=150, blank=True)
    work_desig_one = models.TextField(max_length=200, blank=True)
    work_year_one = models.CharField(max_length=200, blank=True)
    work_ex_c_name_two = models.TextField(max_length=150, blank=True)
    work_desig_two = models.TextField(max_length=200, blank=True)
    work_year_two = models.CharField(max_length=200, blank=True)
    work_ex_c_name_three = models.TextField(max_length=150, blank=True)

    work_year_three = models.CharField(max_length=200, blank=True)
    soft_skill = models.TextField(max_length=800, blank=True)
