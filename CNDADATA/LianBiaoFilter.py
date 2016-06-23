# -*- coding: utf-8 -*-
__author__ = 'Mesogene'
from models import *
import rest_framework_filters as filters
from filter import *
class UserhealthknowledgeFilter(filters.FilterSet):
    """
    个人养生知识视图
    """

    username = filters.AllLookupsFilter(name="username", lookup_type='contains')
    healthknowltypename = filters.AllLookupsFilter(name="healthknowltypename", lookup_type='contains')
    healthknowledgetitle = filters.AllLookupsFilter(name="healthknowledgetitle", lookup_type='contains')
    healthknowledgecontent = filters.AllLookupsFilter(name="healthknowledgecontent", lookup_type='contains')
    healthknowledgetime = filters.AllLookupsFilter(name="healthknowledgetime", lookup_type='contains')

    class Meta:
        model = Userhealthknowledge
class Tbhospitalinfocombinefilter(filters.FilterSet):
    """
    医院信息表
    """
    hospitalname = filters.AllLookupsFilter(name="hospitalname", lookup_type='contains')
    hospitalexplain = filters.AllLookupsFilter(name="hospitalexplain", lookup_type='contains')
    hospitalrank = filters.AllLookupsFilter(name="hospitalrank", lookup_type='contains')
    temp_adminisareaid = filters.RelatedFilter(TbAdminisareaFilter, name='temp_adminisareaid')
    class Meta:
        model = TbHospitalinfo

class TbRecommendedconditionsmappcombineFilter(filters.FilterSet):
    """
    健康建议条件限定映射表
    """
    temp_healthsuggestlimitedid = filters.RelatedFilter(TbHealthsuggestlimitedFilter, name='temp_healthsuggestlimitedid')
    recommendmappremarks = filters.AllLookupsFilter(name="recommendmappremarks", lookup_type='contains')
    temp_healthsuggestid = filters.RelatedFilter(TbHealthsuggestionsFilter, name='temp_healthsuggestid')
    class Meta:
        model = TbRecommendedconditionsmapp