from django.db import models

# Create your models here.
class Antibody(models.Model):
    cat_num = models.CharField(max_length=200, null=True, unique=True)
    name = models.CharField(max_length=200, null=True)
    HOST = (('Rabbit', 'Rabbit'),('Mouse','Mouse'),('Rat','Rat'),('Goat','Goat'),('Horse','Horse'),('Chicken','Chicken'),('Guinea Pig','Guinea Pig'),('Other', 'Other'),)
    host = models.CharField(max_length=200, null=True, choices=HOST)
    production = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True)
    recommended_WB_concentration = models.CharField(max_length=200, null=True, blank=True)
    recommended_IHC_concentration = models.CharField(max_length=200, null=True, blank=True)
    recommended_IHCp_concentration = models.CharField(max_length=200, null=True, blank=True)
    recommended_IF_concentration = models.CharField(max_length=200, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.cat_num

class AntibodyInd(models.Model):
    cat_num = models.ForeignKey(Antibody, null=True, on_delete=models.CASCADE, to_field="cat_num")
    lot_num = models.CharField(max_length=200, null=True)
    location =  models.CharField(max_length=200, null=True)
    ALIQ = (('Yes', 'Yes'),('No','No'))
    aliquoted = models.CharField(max_length=200, null=True, choices=ALIQ)
    date_aliq = models.CharField(max_length=200, null=True, blank=True)
    date_received = models.CharField(max_length=200, null=True, blank=True)
    exp_date = models.CharField(max_length=200, null=True, blank=True)
    amount_remaining = models.IntegerField(null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)


    #add blank=true for ones we want to not be required

class AntibodyArc(models.Model):
    cat_num = models.CharField(max_length=200, null=True, unique=True)
    name = models.CharField(max_length=200, null=True)
    HOST = (('Rabbit', 'Rabbit'),('Mouse','Mouse'),('Rat','Rat'),('Goat','Goat'),('Horse','Horse'),('Chicken','Chicken'),('Guinea Pig','Guinea Pig'),('Other', 'Other'),)
    host = models.CharField(max_length=200, null=True, choices=HOST)
    production = models.CharField(max_length=200, null=True, blank=True)
    company = models.CharField(max_length=200, null=True)
    most_recent_lot_num = models.CharField(max_length=200, null=True)
    recommended_WB_concentration = models.CharField(max_length=200, null=True, blank=True)
    recommended_IHC_concentration = models.CharField(max_length=200, null=True, blank=True)
    recommended_IHCp_concentration = models.CharField(max_length=200, null=True, blank=True)
    recommended_IF_concentration = models.CharField(max_length=200, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    #add blank=true for ones we want to not be required

    def __str__(self):
        return self.cat_num
