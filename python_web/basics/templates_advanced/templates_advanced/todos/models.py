from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=30)
    is_done = models.BooleanField(default=False)
    
    
    
    def __str__(self) -> str:
        return f"Todo:{self.text}\tIs_done:{self.is_done}"