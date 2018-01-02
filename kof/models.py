from django.db import models


# Create your models here.
class FighterType(models.Model):
    name = models.CharField(max_length=10)  # Defend / Offend / Skill


class Fighter(models.Model):
    name = models.CharField(max_length=50)
    avatar = models.CharField(max_length=255)
    quality = models.PositiveSmallIntegerField()
    type = models.ForeignKey(FighterType)


class SkillType(models.Model):
    type = models.CharField(max_length=50)  # Normal / Special
    level = models.CharField(max_length=20) # Normal / Max / SMax


class Skill(models.Model):
    name = models.CharField(max_length=20)
    type = models.ForeignKey(SkillType)
    explain = models.TextField()
    pros = models.BooleanField()


class Tag(models.Model):
    name = models.CharField(max_length=100)
