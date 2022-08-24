from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
import os
from core.models import *
class SuperUserSerializerMethodField(serializers.SerializerMethodField):

    def get_attribute(self, instance):
        if self.context['request'].user.is_superuser:
            return super(SuperUserSerializerMethodField, self).get_attribute(instance)
        return None
class CustomBaseSerializer(serializers.ModelSerializer):
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name=f'custombase-detail', 
        lookup_field='pk'
    )
    admin_url = SuperUserSerializerMethodField(read_only=True)
    # def get_edit_url(self, obj):
    #     request = self.context.get('request')
    #     if request is None:
    #         return None
    def get_admin_url(self, obj):     
        admin_url_name = "admin:{}_{}_change".format(obj._meta.app_label, obj._meta.model_name)        
        root_admin_url = reverse(admin_url_name, args=(obj.pk,))            
        return os.getenv("SITE_URL")+root_admin_url

class UserPublicSerializer(CustomBaseSerializer):
    username = serializers.CharField(read_only=True)
    pk = serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'admin_url',
        ]
            

class TechnologyTypeSerializer(CustomBaseSerializer):
    class Meta:
        model = TechnologyType
        fields = [
            'pk',
            'name',
        ]
            

class ProjectSerializer(CustomBaseSerializer):
    class Meta:
        model = Project
        fields = [
            'pk',
            'name',
        ]
            

class LanguageSerializer(CustomBaseSerializer):
    class Meta:
        model = Language
        fields = [
            'pk',
            'name',
        ]
            
            
class TechnologySerializer(CustomBaseSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name=f'technology-detail', 
        lookup_field='pk'
    )
    type = TechnologyTypeSerializer(read_only=True, many=True)
    language = LanguageSerializer(read_only=True, many=True)
    projects = serializers.SerializerMethodField()
    
    class Meta:
        model = Technology
        fields = [
            'pk',
            'url',
            'admin_url',
            'name',
            'type',
            'language',
            'image',
            'priority',
            'htmldescription',
            'projects',
        ]

    def get_projects(self, obj):
       products = obj.project_set.all() # will return product query set associate with this category
       response = ProjectSerializer(products, many=True).data
       return response