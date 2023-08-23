# from django.db import models
#
#
# class Hospital(models.Model):
#     name = models.CharField(max_length=255)
#     photo = models.ImageField(upload_to='home/')
#     location = models.CharField(max_length=255)
#     map = models.URLField()
#     bio = models.TextField()
#     phone = models.CharField(max_length=255)
#     phone2 = models.CharField(max_length=255)
#     email = models.EmailField()
#
#
# class New(models.Model):
#     photo = models.ImageField(upload_to="new/")
#     video = models.FileField()
#     short = models.CharField(max_length=2555)
#     created_at = models.DateTimeField(auto_now_add=True)
#
#
# class Direction(models.Model):
#     name = models.CharField(max_length=255)
#     short = models.CharField(max_length=255)
#
#
# class Doctor(models.Model):
#     name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     experience = models.CharField(max_length=255)
#     bio = models.TextField()
#     direction = models.ForeignKey(Direction, on_delete=models.PROTECT)
#     total_time = models.PositiveIntegerField(help_text="Doctor's total available time in minutes")
#
#
# class Customer(models.Model):
#     patient_name = models.CharField(max_length=255)
#     patient_last_name = models.CharField(max_length=255)
#     ill_name = models.CharField(max_length=255)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     appointment_date = models.DateField()
#     appointment_time = models.TimeField()
#
#     def __str__(self):
#         return f"{self.patient_name} - {self.patient_last_name} - {self.appointment_date} - {self.appointment_time}"
#
#
# class DoctorAboutOpinion(models.Model):
#     patient_name = models.CharField(max_length=255)
#     patient_last_name = models.CharField(max_length=255)
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     stars = models.IntegerField(choices=(
#         (1, "Juda Yomon"),
#         (2, "Yomon"),
#         (3, "O`rta"),
#         (4, "Yaxshi"),
#         (5, "A`lo"),
#     ))
#     opinion = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.doctor.name} - {self.stars} stars"
#
#
# class HospitalAboutOpinion(models.Model):
#     name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     star = models.IntegerField(choices=(
#         (1, "Juda Yomon"),
#         (2, "Yomon"),
#         (3, "O`rta"),
#         (4, "Yaxshi"),
#         (5, "A`lo"),
#     ))
#     opinion = models.TextField(blank=True, null=True)
#
#
# class Info(models.Model):
#     photo = models.ImageField(upload_to="info/")
#     name = models.CharField(max_length=255)
#     motto = models.CharField(max_length=255)
#     telegram = models.URLField()
#     instagram = models.URLField()
#     youtube = models.URLField()
#     facebook = models.URLField()
#     email = models.EmailField()
#     phone = models.CharField(max_length=255)
#     map = models.URLField()
#     location = models.CharField(max_length=255)
#
#
# class Advice(models.Model):
#     photo = models.ImageField(upload_to='advice/')
#     name = models.CharField(max_length=255)
#     text = models.TextField()
#     is_popular = models.BooleanField(default=True)
#
#
# class HealthyFood(models.Model):
#     photo = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     bio = models.CharField(max_length=255)
#
#
# class Exercises(models.Model):
#     photo = models.ImageField(upload_to="Exercises")
#     name = models.CharField(max_length=255)
#     video = models.URLField()
#
#
# class Donation(models.Model):
#     donor_name = models.CharField(max_length=100)
#     amount = models.DecimalField(max_digits=10, decimal_places=2)
#     donation_date = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.donor_name} - {self.amount}"
#
#
# class ResultDonation(models.Model):
#     photo = models.ImageField()
#     video = models.FileField()
#     short = models.CharField(max_length=255)
#
#
# class Donor(models.Model):
#     name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     phone_number = models.CharField(max_length=15)
#     blood_group = models.CharField(max_length=5)
#     donation_type = models.CharField(max_length=255)
#     hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)



# diyorbek
