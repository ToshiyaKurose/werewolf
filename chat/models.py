from django.db import models

class Log(models.Model):
    team = [
        (0,"進行中"),
        (1,"村人"),
        (2,"人狼"),
        (3,"妖孤"),
        (4,"恋人"),
        (5,"全滅"),
        (6,"廃村"),
    ]
    end_time = models.DateTimeField(null=True)
    name = models.CharField()
    winner = models.IntegerField(choices=team)
    gm = models.BooleanField()
    wish = models.BooleanField()
    death_note = models.BooleanField()
    pattern = models.CharField()
    log = models.JSONField(null=True)

class PersonalLog(models.Model):
    role_list = [
        (0,"未決定"),
        (1,"村人"),
        (2,"人狼"),
        (3,"占い師"),
        (4,"預言者"),
        (5,"霊能者"),
        (6,"狩人"),
        (7,"共有者"),
        (8,"猫又"),
        (9,"狂人"),
        (10,"狂信者"),
        (11,"聴覚狂人"),
        (12,"妖狐"),
        (13,"背徳者"),
    ]
    person = models.IntegerField()
    village = models.ForeignKey(
        Log,
        on_delete=models.CASCADE,
    )
    name = models.CharField()
    profile = models.CharField(blank=True)
    icon = models.IntegerField()
    role = models.IntegerField(choices=role_list)
    is_love = models.BooleanField(default=False)
    wish = models.IntegerField(choices=role_list)
    is_suddendeath = models.BooleanField(default=False)
    ip = models.GenericIPAddressField()

class CurrentVillage(models.Model):
    person = models.IntegerField()
    village = models.ForeignKey(
        Log,
        on_delete=models.CASCADE,
    )
    is_player = models.BooleanField()