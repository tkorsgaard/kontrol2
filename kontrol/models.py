from django.db import models

class Station(models.Model):
    station_name = models.CharField(max_length=250)

    def __str__(self):
        return "<%s>" % (self.station_name)

class Departure(models.Model):
    departure_station = models.ForeignKey(Station)
    departure_time = models.TimeField()

    def __str__(self):
        return "<Departure from: %s at %s>" % (self.departure_station, self.departure_time)

class Trip(models.Model):
    trip_date = models.DateField()
    departure = models.ForeignKey(Departure)
    tickets_checked = models.BooleanField()
    checked_after = models.ForeignKey(Station, null=True, blank=True)
    bike = models.BooleanField()

    def __str__(self):
        return "<Trip from: %s at %s - %s. Checked: %s>" % (self.departure.departure_station, self.trip_date, self.departure.departure_time, self.tickets_checked)
