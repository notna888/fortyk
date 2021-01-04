from django.db import models

AVAILABILITY_TYPES = (
    ('P', 'Plentiful'),
    ('C', 'Common'),
    ('A', 'Average'),
    ('S', 'Scarce'),
    ('R', 'Rare'),
    ('V', 'Very Rare'),
    ('E', 'Extremely Rare'),
    ('N', 'Near Unique'),
    ('U', 'Unique'),
)

class Weapon(models.Model):
    WEAPONTYPES = (
        ('B', 'Basic'),
        ('P', 'Pistol'),
        ('H', 'Heavy'),
        ('M', 'Melee'),
    )

    DAMAGETYPES = (
        ('E', 'Energy'),
        ('I', 'Impact'),
        ('R', 'Rending'),
        ('X', 'Explosive'),
        ('', 'Other'),
    )

    name = models.CharField(max_length=30)
    weapon_class = models.CharField(max_length=1, choices=WEAPONTYPES)
    range = models.IntegerField()

    rate_of_fire_single = models.BooleanField()
    rate_of_fire_semi_auto = models.IntegerField()
    rate_of_fire_full_auto = models.IntegerField()

    damage = models.CharField(max_length=30)
    damage_type = models.CharField(max_length=1, choices=DAMAGETYPES)

    pen = models.IntegerField()
    clip = models.IntegerField(null=True)
    rld = models.CharField(max_length=10)

    weight = models.IntegerField()

    description = models.TextField()

    las = models.BooleanField()
    force = models.BooleanField()

    ref = models.CharField(max_length=30)


class SpecialWeaponFeature(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    ref = models.CharField(max_length=30)


class WeaponSpecial(models.Model):
    weapon = models.ForeignKey(
        Weapon,
        on_delete=models.CASCADE
    )
    special = models.ForeignKey(
        SpecialWeaponFeature,
        on_delete=models.CASCADE
    )
    number_modifier = models.IntegerField(null=True)
