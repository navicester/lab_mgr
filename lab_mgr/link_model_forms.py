
from django import forms
from lab_mgr import models
from django.forms.models import ModelForm

class Rail_PackageForm(ModelForm):
    class Meta:
        model = models.Rail_Package
        verbose_name = 'Rail Package'
        
    id = forms.CharField(max_length=11, widget = forms.TextInput(attrs={'readonly':'readonly','disable':True}), label = 'id') 
    Name = forms.CharField(max_length=11, required=False, label = 'Name', widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Description = forms.CharField(max_length=50, label = 'Description', required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    
    Total_Price_exclude_VAT = forms.CharField(max_length=11, label = 'Total_Price_exclude_VAT', required=False, widget = 
                             forms.TextInput(attrs={'readonly':'readonly','disable':True}))    

    def __unicode__(self):
        return u'%s %s' % (self.id, self.Name)  

    ''' # why here it doesn't work ?
    def __init__(self, *args, **kwargs):
        super(Rail_PackageForm, self).__init__(*args, **kwargs)
        self.fields['id'].label = "id"
        self.fields['Name'].label = "Name"
        self.fields['Description'].label = "Description"
        self.fields['Total_Price_exclude_VAT'].label = "Total_Price_exclude_VAT"        
    '''
