from django.db import models

# Create your models here.
     
class PreCI_Request(models.Model):
    Request_By = models.CharField(max_length=50,verbose_name='Request By')
    HW_Type = models.CharField(max_length=50,verbose_name='HW_Type',choices=(('Macro FDD','Macro FDD'),('Macro TDD','Macro TDD'),('Macro FDD/TDD','Macro FDD/TDD'),('SOC TDD','SOC TDD')),)
    FeatureId = models.CharField(max_length=50,verbose_name='Feature Id')
    Manager = models.CharField(max_length=50,verbose_name='Manager')
    LoadName = models.TextField(max_length=500,verbose_name='Load Name')
    LoadLink = models.TextField(max_length=500,verbose_name='Load Link')
    ReferenceLoad = models.CharField(max_length=500,verbose_name='Reference Load')    
    Note = models.TextField(max_length=500,blank = True, null= True, verbose_name='Note')
    ExpectDate = models.DateField(max_length=50,auto_now=False, auto_now_add=False,verbose_name='Expect Date')
    SubmissionDate = models.DateField(max_length=50,auto_now=False, auto_now_add=False,verbose_name='Submission Date')
    Site = models.CharField(max_length=50,verbose_name='Site',choices=(('beijing','beijing'),('shanghai','shanghai')),)    

    def __unicode__(self):
        return u'%s %s %s' % (self.HW_Type,self.FeatureId, self.ExpectDate)

    class Meta:
        verbose_name = 'PreCI_Request'  
        db_table = 'preci_request' 
