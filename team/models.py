from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    logoUri = models.ImageField(null=True, blank=True)
    clubState = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    @property
    def players(self):
        return self.player_set.all()

    @property
    def logoURL(self):
        try:
            url = self.logoUri.url
        except:
            url = ''
        return url


class Player(models.Model):
    firstName = models.CharField(max_length=100, null=True, blank=False)
    lastName = models.CharField(max_length=100, null=True, blank=False)
    imageUri = models.ImageField(null=True, blank=True)
    jerseyNumber = models.IntegerField(default=0, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=False)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        ordering = ['firstName']

    def __str__(self):
        return str(self.firstName) + str(self.lastName)

    # @property
    # def playershistoy(self):
    #     return self.playerhistory_set.all()

    @property
    def imageURL(self):
        try:
            url = self.imageUri.url
        except:
            url = ''
        return url


class PlayerHistory(models.Model):
    player = models.OneToOneField(Player, on_delete=models.CASCADE)
    matches = models.IntegerField(default=0, null=True, blank=True)
    runs = models.IntegerField(default=0, null=True, blank=True)
    highestScore = models.IntegerField(default=0, null=True, blank=True)
    fifties = models.IntegerField(default=0, null=True, blank=True)
    hundreds = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.player.firstName + self.player.lastName


class Matches(models.Model):
    team1 = models.CharField(max_length=10, null=True, blank=True)
    team2 = models.CharField(max_length=10, null=True, blank=True)
    winner = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.team1) + ' X ' + str(self.team2)

    def save(self, *args, **kwargs):
        if str(self.winner) == str(self.team1) or str(self.winner) == str(self.team2):
            super().save(*args, **kwargs)


class PointsTable(models.Model):
    winner = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.winner


@receiver(post_save, sender=Matches)
def matchCompleted(sender, instance, created, **kwargs):
    print(created)
    if created:
        PointsTable.objects.create(winner=instance.winner)
