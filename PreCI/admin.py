from django.contrib.admin.options import *
from django.contrib import admin

from PreCI.models import *
from PreCI import models


class PreCI_RequestAdmin(admin.ModelAdmin):
    list_display = ('Request_By','HW_Type','FeatureId','Manager','LoadName','ExpectDate','SubmissionDate','Site',)
    search_fields = ('Request_By','HW_Type','FeatureId','Manager','LoadName','ExpectDate','SubmissionDate','LoadLink','Note',)
    list_filter = ('Request_By','HW_Type','FeatureId','Manager','LoadName','ExpectDate','SubmissionDate',)
    ordering = ('Request_By','HW_Type','FeatureId','Manager','LoadName','ExpectDate','SubmissionDate',)

    save_as = True
    
