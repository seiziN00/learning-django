from django.db import models





class Salary(models.Model):
  amount = models.IntegerField(blank=False, null=False)
  extra_dec = models.BooleanField(default=False)
  extra_jun = models.BooleanField(default=False)

  def __str__(self):
    return self.amount


class Job(models.Model):
  title = models.CharField(max_length=100, blank=False, null=False)
  description = models.TextField(null=True)
  salary_id = models.ForeignKey(Salary, on_delete=models.CASCADE)

  def __str__(self):
    return self.title


class Country(models.Model):
  name = models.CharField(max_length=50, blank=False, null=False)
  country_code = models.CharField(max_length=10, blank=False, null=False)

  def __str__(self):
    return self.name


class City(models.Model):
  name = models.CharField(max_length=50, blank=False, null=False)
  country_id = models.ForeignKey(Country, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class Factory(models.Model):
  name = models.CharField(max_length=50, blank=False, null=False)
  address = models.CharField(max_length=100, blank=False, null=False)
  zip_code = models.CharField(max_length=10, blank=False, null=False)
  city = models.ForeignKey(City, on_delete=models.CASCADE)

  def __str__(self):
    return self.name


class Employee(models.Model):
  national_id = models.CharField(max_length=10, blank=False, null=False)
  name = models.CharField(max_length=50, blank=False, null=False)
  last_name = models.CharField(max_length=50, blank=False, null=False)
  email = models.EmailField(max_length=30, blank=False, null=False)
  address = models.CharField(max_length=100, blank=False, null=False)
  job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
  location_id = models.ForeignKey(Factory, on_delete=models.CASCADE)

  def __str__(self):
    return self.name