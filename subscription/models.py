from django.db import models


class SubscriptionModel(models.Model):

    plan_name = models.CharField(max_length=200, blank=False, null=False)
    plan_amount = models.FloatField()
    plan_description = models.TextField()
    total_queries = models.IntegerField()

    def __str__(self):
        return self.plan_name
