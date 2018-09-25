from django.db import models


class Project(models.Model):
    kickstarter_id = models.IntegerField()
    name = models.CharField(max_length=1024)
    category = models.CharField(max_length=1024)
    main_category = models.CharField(max_length=1024)
    currency = models.CharField(max_length=1024)
    deadline = models.CharField(max_length=1024)
    goal = models.FloatField()
    launched = models.CharField(max_length=1024)
    pledged = models.FloatField()
    state = models.CharField(max_length=1024)
    backers = models.CharField(max_length=1024)
    country = models.CharField(max_length=1024)
    usd_pledged = models.FloatField()
    # winery = models.CharField(max_length=1024)

    def __str__(self):
        return '{}'.format(self.name)


