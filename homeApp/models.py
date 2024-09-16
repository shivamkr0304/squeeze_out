from django.db import models
from django.contrib.auth.models import User

# Create your models here.
'''
class Subject_faculty(models.Model):
    sub_id=models.CharField(max_length=5)
    sub_name=models.CharField(max_length=50)
    sem=models.CharField(max_length=5)
    branch=models.CharField(max_length=50)
    facID=models.CharField(max_length=10)
    fac_name=models.CharField(max_length=50)
    fac_dept=models.CharField(max_length=50)


class Student(models.Model):
    roll=models.CharField(max_length=10)
    regd_no=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    sem=models.CharField(max_length=5)
    batch=models.CharField(max_length=10)
    sub_id=models.ForeignKey(Subject_faculty, on_delete=models.CASCADE,blank=True,null=True,related_name="subject_branch")
    facID=models.ForeignKey(Subject_faculty, on_delete=models.CASCADE,blank=True,null=True,related_name="faculty_dept")



class feedback(models.Model):
    roll=models.ForeignKey(Student, on_delete=models.CASCADE,blank=True,null=True)
    sub_id=models.ForeignKey(Subject_faculty, on_delete=models.CASCADE,blank=True,null=True)
    facID=models.ForeignKey(Subject_faculty, on_delete=models.CASCADE,blank=True,null=True)
    feedback=models.CharField(max_length=50)

  '''  

class Student_sub_fac_feedback(models.Model):
    roll_no=models.ForeignKey(User,on_delete=models.CASCADE,default=1)
    roll=models.CharField(max_length=10)
    regd_no=models.CharField(max_length=15)
    name=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    sem=models.CharField(max_length=5)
    batch=models.CharField(max_length=10)

    #sub_id=models.CharField(max_length=5)
    #sub_name=models.CharField(max_length=50)
    sub_name1=models.CharField(max_length=50,null=True,blank=True)
    sub_name2=models.CharField(max_length=50,null=True,blank=True)
    sub_name3=models.CharField(max_length=50,null=True,blank=True)
    sub_name4=models.CharField(max_length=50,null=True,blank=True)
    sub_name5=models.CharField(max_length=50,null=True,blank=True)


    #facID=models.CharField(max_length=10)
    #fac_name=models.CharField(max_length=50)
    #fac_dept=models.CharField(max_length=50)
    fac_name1=models.CharField(max_length=50,null=True,blank=True)
    fac_name2=models.CharField(max_length=50,null=True,blank=True)
    fac_name3=models.CharField(max_length=50,null=True,blank=True)
    fac_name4=models.CharField(max_length=50,null=True,blank=True)
    fac_name5=models.CharField(max_length=50,null=True,blank=True)


    #feedback_fac1=models.CharField(max_length=50,null=True,blank=True)
    #feedback_fac2=models.CharField(max_length=50,null=True,blank=True)
    #feedback_fac3=models.CharField(max_length=50,null=True,blank=True)
    #feedback_fac4=models.CharField(max_length=50,null=True,blank=True)
    #feedback_fac5=models.CharField(max_length=50,null=True,blank=True)

    f_fac1_field1=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field2=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field3=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field4=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field5=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field6=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field7=models.CharField(max_length=50,null=True,blank=True)

    f_fac2_field1=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field2=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field3=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field4=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field5=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field6=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field7=models.CharField(max_length=50,null=True,blank=True)

    f_fac3_field1=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field2=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field3=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field4=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field5=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field6=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field7=models.CharField(max_length=50,null=True,blank=True)
    
    f_fac4_field1=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field2=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field3=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field4=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field5=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field6=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field7=models.CharField(max_length=50,null=True,blank=True)

    f_fac5_field1=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field2=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field3=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field4=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field5=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field6=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field7=models.CharField(max_length=50,null=True,blank=True)


    def __str__(self):
        return self.name
'''   
class feedback_table(models.Model):
    roll=models.CharField(max_length=10)
    f_fac1_field1=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field2=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field3=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field4=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field5=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field6=models.CharField(max_length=50,null=True,blank=True)
    f_fac1_field7=models.CharField(max_length=50,null=True,blank=True)

    f_fac2_field1=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field2=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field3=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field4=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field5=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field6=models.CharField(max_length=50,null=True,blank=True)
    f_fac2_field7=models.CharField(max_length=50,null=True,blank=True)

    f_fac3_field1=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field2=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field3=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field4=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field5=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field6=models.CharField(max_length=50,null=True,blank=True)
    f_fac3_field7=models.CharField(max_length=50,null=True,blank=True)
    
    f_fac4_field1=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field2=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field3=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field4=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field5=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field6=models.CharField(max_length=50,null=True,blank=True)
    f_fac4_field7=models.CharField(max_length=50,null=True,blank=True)

    f_fac5_field1=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field2=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field3=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field4=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field5=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field6=models.CharField(max_length=50,null=True,blank=True)
    f_fac5_field7=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.roll
    
  '''  

#class Whole_details(models.Model):


