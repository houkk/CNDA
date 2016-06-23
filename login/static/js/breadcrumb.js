/**
 * Created by Mesogene on 2015/4/10.
 */
 $(function ($) {
     $('#back_user').click(function () {
//{#        var backuser = '/login/tableview/';#}
//{#        var area = 'back/dashboard/main/test.html';#}
         $('#bread').empty();
         $('#bread').append('<li><a"><div>用户管理</div></a></li> <li><a>后台用户管理</a></li>');
     });
     $('#supervisorylevel').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户管理</div></a></li> <li><a >权限管理</a></li>');
     });
     $('#health_user').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户管理</div></a></li> <li><a>健康用户管理</a></li>');
     });

     $('#dietlist1').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>饮食数据管理</a></li> <li><a>饮食信息记录</a></li>');
     });
     $('#dietlist2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>饮食数据管理</a></li> <li><a>饮食偏好记录</a></li>');
     });
     $('#dietlist3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>饮食数据管理</a></li> <li><a>饮食特征信息</a></li>');
     });
     $('#dietlist4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>饮食数据管理</a></li> <li><a>饮食状况分析</a></li>');
     });

     $('#sleepinfo2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>作息数据管理</a></li> <li><a>睡眠信息记录</a></li>');
     });
     $('#sleepinfo3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>作息数据管理</a></li> <li><a>睡眠偏好记录</a></li>');
     });
     $('#sleepinfo4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>作息数据管理</a></li> <li><a>用户睡眠特征信息</a></li>');
     });
     $('#sleepinfo5').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>作息数据管理</a></li> <li><a>睡眠详细过程记录</a></li>');
     });
     $('#sleepinfo6').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>作息数据管理</a></li> <li><a>睡眠状态类别</a></li>');
     });

     $('#sportinfo2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>运动数据管理</a></li> <li><a>运动信息记录</a></li>');
     });
     $('#sportinfo3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>运动数据管理</a></li> <li><a>运动偏好记录</a></li>');
     });
     $('#sportinfo4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>运动数据管理</a></li> <li><a>运动实体记录</a></li>');
     });
     $('#sportinfo5').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>运动数据管理</a></li> <li><a>运动特征信息</a></li>');
     });
     $('#sportinfo6').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>运动数据管理</a></li> <li><a>运动类型</a></li>');
     });
     $('#sportinfo7').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>运动数据管理</a></li> <li><a>运动详细过程记录</a></li>');
     });

     $('#treatinfo1').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>诊疗数据管理</a></li> <li><a>中医诊断分类</a></li>');
     });
     $('#treatinfo2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>诊疗数据管理</a></li> <li><a>中医诊疗记录</a></li>');
     });
     $('#treatinfo3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>诊疗数据管理</a></li> <li><a>西医体检项目</a></li>');
     });
     $('#treatinfo4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>诊疗数据管理</a></li> <li><a>西医诊疗记录</a></li>');
     });

     $('#medicinehistory').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>病史数据管理</a></li>');
     });

     $('#identify2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>体质辨识/养生数据管理</a></li> <li><a>体质辨识结果记录</a></li>');
     });
     $('#identify3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>体质辨识/养生数据管理</a></li> <li><a>用户答题记录</a></li>');
     });
     $('#identify4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>体质辨识/养生数据管理</a></li> <li><a>用户养生知识映射</a></li>');
     });
     $('#identify5').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>体质辨识/养生数据管理</a></li> <li><a>用户健康建议映射</a></li>');
     });
     $('#identify6').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>体质辨识/养生数据管理</a></li> <li><a>用户健康预警映射</a></li>');
     });
     $('#identify7').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>体质辨识/养生数据管理</a></li> <li><a>健康趋势分析记录</a></li>');
     });
     $('#identify8').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>体质辨识/养生数据管理</a></li> <li><a>扩展健康属性</a></li>');
     });
     $('#identify9').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>体质辨识/养生数据管理</a></li> <li><a>用户健康属性映射</a></li>');
     });

     $('#collection1').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>收藏管理</a></li> <li><a>我的收藏</a></li>');
     });
     $('#collection2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>收藏管理</a></li> <li><a>专家收藏</a></li>');
     });
     $('#collection3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>收藏管理</a></li> <li><a>养生建议收藏</a></li>');
     });
     $('#collection4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>收藏管理</a></li> <li><a>养生知识收藏</a></li>');
     });

     $('#others2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>其他数据管理</a></li> <li><a>用户评论统计</a></li>');
     });
     $('#others3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>其他数据管理</a></li> <li><a>点击量统计</a></li>');
     });
     $('#others4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>其他数据管理</a></li> <li><a>诊断对象</a></li>');
     });
     $('#others5').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>其他数据管理</a></li> <li><a>诊断动态记录</a></li>');
     });
     $('#others6').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>用户健康数据管理</div></a></li> <li><a>其他数据管理</a></li> <li><a>指标用户映射</a></li>');
     });

     $('#dietdatachart').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>区域管理</div></a></li> <li><a>饮食数据图</a></li> ');
     });
     $('#sleepdatachart').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>区域管理</div></a></li> <li><a>作息数据图</a></li> ');
     });
     $('#sportdatachart').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>区域管理</div></a></li> <li><a>运动数据图</a></li> ');
     });


     $('#setmealinfo2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>食物/套餐信息</a></li> <li><a>饮食套餐信息</a></li>');
     });
     $('#setmealinfo3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>食物/套餐信息</a></li> <li><a>食物营养成分</a></li>');
     });
     $('#setmealinfo4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>食物/套餐信息</a></li> <li><a>套餐食物映射</a></li>');
     });
     $('#setmealinfo5').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>食物/套餐信息</a></li> <li><a>常见食物信息</a></li>');
     });
     $('#setmealinfo6').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>食物/套餐信息</a></li> <li><a>常见食物类别</a></li>');
     });
     $('#setmealinfo7').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>食物/套餐信息</a></li> <li><a>食物药用功效类别</a></li>');
     });
     $('#setmealinfo8').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>食物/套餐信息</a></li> <li><a>食物药用属性映射</a></li>');
     });
     $('#setmealinfo9').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>食物/套餐信息</a></li> <li><a>食物药用属性</a></li>');
     });

     $('#medicine1').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>中药/用药信息</a></li> <li><a>中药信息</a></li>');
     });
     $('#medicine2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>中药/用药信息</a></li> <li><a>用药信息</a></li>');
     });
     $('#medicine3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>中药/用药信息</a></li> <li><a>中药方剂</a></li>');
     });
     $('#medicine4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>中药/用药信息</a></li> <li><a>药品方剂映射</a></li>');
     });

     $('#equipabment0').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>智能设备</a></li> <li><a>智能设备基本信息</a></li>');
     });
     $('#equipabment1').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>智能设备</a></li> <li><a>设备参数代码</a></li>');
     });
     $('#equipabment2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>智能设备</a></li> <li><a>设备参数映射</a></li>');
     });
     $('#equipabment3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>智能设备</a></li> <li><a>设备数据采集代码</a></li>');
     });
     $('#equipabment4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>智能设备</a></li> <li><a>采集数据分类</a></li>');
     });

     $('#healthknowage2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>养生/健康知识信息</a></li> <li><a>养生知识信息</a></li>');
     });
     $('#healthknowage3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>养生/健康知识信息</a></li> <li><a>养生知识类别</a></li>');
     });
     $('#healthknowage4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>养生/健康知识信息</a></li> <li><a>健康建议类别</a></li>');
     });
     $('#healthknowage5').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>养生/健康知识信息</a></li> <li><a>健康建议</a></li>');
     });
     $('#healthknowage6').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>养生/健康知识信息</a></li> <li><a>健康指标信息</a></li>');
     });
     $('#healthknowage7').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>养生/健康知识信息</a></li> <li><a>健康预警类别</a></li>');
     });
     $('#healthknowage8').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>养生/健康知识信息</a></li> <li><a>健康建议限定条件</a></li>');
     });
     $('#healthknowage9').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>养生/健康知识信息</a></li> <li><a>养生知识限定条件</a></li>');
     });
     $('#healthknowage10').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>养生/健康知识信息</a></li> <li><a>健康预警信息</a></li>');
     });

     $('#commondisease2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>常见疾病</a></li> <li><a>常见疾病信息</a></li>');
     });
     $('#commondisease3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>常见疾病</a></li> <li><a>常见疾病类别</a></li>');
     });
     $('#identifyissue1').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>体质辨识库</a></li> <li><a>体质辨识问卷项目</a></li>');
     });
     $('#identifyissue2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>体质辨识库</a></li> <li><a>体质辨识选项</a></li>');
     });
     $('#identifyissue3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>体质辨识库</a></li> <li><a>体质信息</a></li>');
     });
     $('#identifyissue4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>体质辨识库</a></li> <li><a>体质疾病类别</a></li>');
     });

     $('#hospitalinfo2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>医院信息</a></li> <li><a>中医专家信息</a></li>');
     });
     $('#hospitalinfo3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>医院信息</a></li> <li><a>医院信息</a></li>');
     });
     $('#hospitalinfo4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>医院信息</a></li> <li><a>医生专长信息</a></li>');
     });
     $('#hospitalinfo5').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>医院信息</a></li> <li><a>医生专长分类代码</a></li>');
     });
     $('#hospitalinfo6').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>医院信息</a></li> <li><a>医院医生关系</a></li>');
     });
     $('#hospitalinfo7').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>医院信息</a></li> <li><a>医院科室信息</a></li>');
     });

     $('#unitattribute3').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>计量单位/标准</a></li> <li><a>计量单位</a></li>');
     });
     $('#unitattribute4').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>计量单位/标准</a></li> <li><a>平均量计算标准</a></li>');
     });
     $('#unitattribute5').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>计量单位/标准</a></li> <li><a>营养素每日平均摄入量</a></li>');
     });
     $('#unitattribute6').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>计量单位/标准</a></li> <li><a>各类指标标准</a></li>');
     });
     $('#unitattribute7').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>计量单位/标准</a></li> <li><a>各类指标限定</a></li>');
     });
     $('#unitattribute8').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>计量单位/标准</a></li> <li><a>图片列表</a></li>');
     });

     $('#area1').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>地理/行政区划信息</a></li> <li><a>行政区划代码</a></li>');
     });
     $('#area2').click(function () {
         $('#bread').empty();
         $('#bread').append('<li><a ><div>客观信息</div></a></li> <li><a>地理/行政区划信息</a></li> <li><a>地理位置信息</a></li>');
     });

 })(jQuery);