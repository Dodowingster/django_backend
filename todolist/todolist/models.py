from django.db import models

# Create your models here.
class task(models.Model):
    title=models.CharField(max_length=200)
    description = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
# ______________________________________________________________________________
#                                                                              
#  This Django model definition represents a Task entity with various fields  
#  to store information about the task.                                        
#                                                                              
#  The fields are defined as follows:                                          
#   - title: CharField with a maximum length of 200 characters, storing the    
#            title of the task.                                               
#   - description: TextField allowing for longer text, representing the        
#                  description of the task. It's optional and can be left blank.
#   - status: BooleanField indicating whether the task is completed or not.    
#             It defaults to False, indicating that the task is not completed. 
#   - created_at: DateTimeField automatically recording the date and time when  
#                 the task object is created.                                  
#   - updated_at: DateTimeField automatically updating to the current date and 
#                 time whenever the task object is modified.                   
#                                                                              
#  The __str__ method is defined to return the title of the task when the      
#  object is printed or displayed.                                             
#                                                                              
# ______________________________________________________________________________
