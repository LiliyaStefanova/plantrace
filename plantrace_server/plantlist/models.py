from django.db import models

class PlantGroup(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)
    type=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)

class Plant(models.Model):
    common_name=models.CharField(max_length=100)
    botanical_name=models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    is_toxic=models.BooleanField(default=False)
    # annual or perennial
    longevity=models.CharField(max_length=30)
    # foliage, flowering, cacti, trailing, tree, fruit bearing and so on
    type=models.CharField(max_length=50)
    # seed, bulb, sapling
    source=models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now_add=True)
    plant_group=models.ForeignKey(PlantGroup, on_delete=models.CASCADE, related_name='plants')


class MajorLifeEvent(models.Model):
    type=models.CharField(max_length=50)
    details=models.CharField(max_length=100)
    time_stamp=models.DateTimeField(auto_now_add=True)
    plant=models.ForeignKey(Plant,on_delete=models.CASCADE, related_name='life_events')
