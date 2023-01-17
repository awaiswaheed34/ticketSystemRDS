from django.db import models

# Create your models here.
class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    
    class Meta:
        db_table = 'user'


class Bus(models.Model):
    name= models.CharField(max_length=20)
    number = models.CharField(max_length=9)
    bus_id = models.AutoField(primary_key=True)
    time = models.TimeField()
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)


#bus has 40 seats and each seat has a seat_id and a seat_number and a seat_status (booked or not) create a table for seats
class Seat(models.Model):
    seat_id = models.AutoField(primary_key=True)
    seat_number = models.IntegerField()
    seat_status = models.BooleanField()
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)

class Ticket(models.Model):
    ticket_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    bus_id = models.ForeignKey(Bus, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seat, on_delete=models.CASCADE)
    ticket_status = models.BooleanField()
    ticket_price = models.IntegerField()
    ticket_date = models.DateField()
    ticket_time = models.TimeField()

user = User()
