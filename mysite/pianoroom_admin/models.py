from django.db import models

# Create your models here
# temp databases schema
class Reserve(models.Model):
    def __str__(self):
        return self.reserver_name + ' ' + self.use_text

    # reserver's name .....@shanghaitech.edu.cn
    # we may need to send a mail for verification
    reserver_name = models.CharField(max_length=20)

    # drum or piano or self-bring instruments
    # it should be a multi-checkbox
    use_text = models.CharField(max_length=50)


    # suppose we only accept very-day reservation the time from 9:00-21:00 divided
    # by half-hour | time limit for single person is 3 hours and must be consecutive

    # decode the time into integer 9:00-9:30->0...20:30-21:00->24
    # start time
    start_time = models.IntegerField()
    # end time
    end_time = models.IntegerField()
