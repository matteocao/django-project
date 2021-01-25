from django.db import models

class Data(models.Model):
    dataset_url = models.URLField(max_length=200, default='')
    dataset_name = models.CharField(max_length=200)
    def __str__(self):
        return self.dataset_name


class Parameter(models.Model):
    data = models.ForeignKey(Data, on_delete=models.CASCADE)
    max_edge_length = models.FloatField()
    homology = models.CharField(max_length=200)
    def __str__(self):
        return self.homology + " " + str(self.max_edge_length)

    
class Result(models.Model):
    parameter = models.ForeignKey(Parameter, on_delete=models.CASCADE)
    result = models.TextField()#text for the CSV file
    diagram = models.JSONField()
    def __str__(self):
        return "Persistent diagram"
