////查询回复的通用方法
//function responseHandler(res){
//
//    return {
//        rows:res.results,   //每行的数据
//        total:res.count    //总数据量
//    }
//}
//
//function queryParams(params) {   //limit 是pageSize 会根据pagelist中选中的项来变 offset时条目的偏移量
//    return {
//        "limit": params.limit,
//        "page": (params.offset / params.limit) + 1
//    }
//}
//
//
//$('#expertTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'doctorid',
//    title:'医生id',
//    formatter:'nameFormatter',
//    sortable:'true',
//    visible:false
//  },{
//    field:'doctorname',
//    title:'医生姓名',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'doctorsex',
//    title:'医生性别',
//    sortable:'true'
//  },{
//    field:'doctorage',
//    title:'医生年龄',
//    sortable:'true'
//  },{
//    field:'professionalrands',
//    title:'医生职称',
//    sortable:'true'
//  },{
//    field:'doctorworktime',
//    title:'工作时长',
//    sortable:'true'
//  },{
//    field:'doctorsynopsis',
//    title:'医生简介',
//    sortable:'true',
//    visible:false
//  },{
//    field:'researcharea',
//    title:'研究方向',
//    sortable:'true'
//  },{
//    field:'researchfindings',
//    title:'相关研究成果',
//    sortable:'true'
//  },{
//    field:'temp_adminisareaid',
//    title:'行政区划',
//    sortable:'true',
//    visible:false
//  },{
//    field:'temp_doctorexpertiseid',
//    title:'医生专长id',
//    sortable:'true',
//    visible:false
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//  /*method:'get',
//  dataType:'jsonp',
//  responseHandler:function(res){
//    alert(res);
//    return res;
//  }*/
//
////后台用户信息表
//$('#eventsTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'username',
//    title:'用户',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'password',
//    title:'密码',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'所在地',
//    title:'所在地',
//    sortable:'true'
//  //},{
//  //  field:'descrption',
//  //  title:'职位',
//  //  sortable:'true'
//  //},{
//  //  field:'descripti',
//  //  title:'邮箱',
//  //  sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//  });
//
////食物营养表
//$('#FoodNutrient').bootstrapTable({
//      columns:[{
//        field:'state',
//        checkbox:"true"
//      },{
//        field:'foodnutritionid',
//        title:'食物营养成分id',
//        formatter:'nameFormatter',
//        sortable:'true'
//      },{
//        field:'foodenergy',
//        title:'食物能量',
//        sortable:'true'
//      },{
//        field:'foodmoisture',
//        title:'食物水分',
//        sortable:'true'
//      },{
//        field:'proteincontent',
//        title:'蛋白质摄入',
//        sortable:'true'
//      },{
//        field:'fatcontent',
//        title:'脂肪含量',
//        sortable:'true'
//      },{
//        field:'fibercontent',
//        title:'膳食纤维含量',
//        sortable:'true'
//      },{
//        field:'carbohydratecontent',
//        title:'碳水化合物含量',
//        sortable:'true'
//      },{
//        field:'vitaminacontent',
//        title:'维生素A含量',
//        sortable:'true'
//      },{
//        field:'vitaminb1content',
//        title:'维生素B1含量',
//        sortable:'true'
//      },{
//        field:'vitaminb2content',
//        title:'维生素B2含量',
//        sortable:'true'
//      },{
//        field:'vitaminb6content',
//        title:'维生素B6含量',
//        sortable:'true'
//      },{
//        field:'vitaminb12content',
//        title:'维生素B12含量',
//        sortable:'true'
//      },{
//        field:'vitaminccontent',
//        title:'维生素C含量',
//        sortable:'true'
//      },{
//        field:'vitamindcontent',
//        title:'维生素D含量',
//        sortable:'true'
//      },{
//        field:'vitaminecontent',
//        title:'维生素E含量',
//        sortable:'true'
//      },{
//        field:'nicotinicacidcontent',
//        title:"烟酸含量",
//        sortable:'true'
//      },{
//        field:'folatecontent',
//        title:'叶酸含量',
//        sortable:'true'
//      },{
//        field:'sodiumcontent',
//        title:"钠含量",
//        sortable:'true'
//      },{
//        field:'calciumcontent',
//        title:'钙含量',
//        sortable:'true'
//      },{
//        field:'ironcontent',
//        title:'铁含量',
//        sortable:'true'
//      },{
//        field:'potassiumcontent',
//        title:'钾含量',
//        sortable:'true'
//      },{
//        field:'zinccontent',
//        title:'锌含量',
//        sortable:'true'
//      },{
//        field:'mangaesscontent',
//        title:'酶含量',
//        sortable:'true'
//      },{
//        field:'coppercontent',
//        title:'铜含量',
//        sortable:'true'
//      },{
//        field:'chromiumcontent',
//        title:'铬含量',
//        sortable:'true'
//      },{
//        field:'mangaesscontent',
//        title:'锰含量',
//        sortable:'true'
//      },{
//        field:'molybdenumcontent',
//        title:'钼含量',
//        sortable:'true'
//      },{
//        field:'iodinecontent',
//        title:'碘含量',
//        sortable:'true'
//      },{
//        field:'potassiumcontent',
//        title:'磷含量',
//        sortable:'true'
//      },{
//        field:'seleniumcontent',
//        title:'硒含量',
//        sortable:'true'
//      },{
//        field:'fluorinecontent',
//        title:'氟含量',
//        sortable:'true'
//      },{
//        field:'cholesterolcontent',
//        title:'胆固醇含量',
//        sortable:'true'
//      },{
//        field:'saturatedfattyacidcontent',
//        title:'饱和脂肪酸含量',
//        sortable:'true'
//      },{
//        field:'acidregurgitationcontent',
//        title:'泛酸含量',
//        sortable:'true'
//      },{
//        field:'biotincontent',
//        title:'生物酸含量',
//        sortable:'true'
//      },{
//        field:'cholinecontent',
//        title:'胆碱含量',
//        sortable:'true'
//      },{
//        field:'temp_unitattributeid',
//        title:'计量单位id',
//        sortable:'true'
//      }],
//        striped:true,
//        pagination:true,
//        pageList:[10,20,50,100,500],
//        pageSize:10,
//        pageNumber:1,
//        clickToSelect:true,
//        smartDisplay:true,
//        sidePagination:'server',
//        queryParamsType:'limit',
//        responseHandler:responseHandler,
//        queryParams:queryParams
//    }
//);
////营养素平均每天摄入量表
//$('#dietTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'nutrientid',
//    title:'营养素ID',
//    sortable:'true'
//  },{
//    field:'nutrientname',
//    title:'营养素名称',
//    sortable:'true'
//  },{
//    field:'nutrientintakemax',
//    title:'营养素摄入值大值',
//    sortable:'true'
//  },{
//    field:'nutrientintakemin',
//    title:'营养素摄入最小值',
//    sortable:'true'
//  },{
//    field:'maxagefor',
//    title:'适宜人群最大年龄',
//    sortable:'true'
//  },{
//    field:'minagefor',
//    title:'适宜人群最小年龄',
//    sortable:'true'
//  },{
//    field:'nutrientintakeremarks',
//    title:'营养素摄入备注',
//    visible:false
//  },{
//    field:'temp_unitAttributeid',
//    title:'计量单位id',
//    sortable:'true',
//    visible:false
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
////  sidePagination:'server'
//});
//
//
////饮食信息记录表
//$('#eatingRecord').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'eatingrecordid',
//    title:'饮食信息记录ID ',
//    sortable:'true',
//    visible:false
//  },{
//    field:'foodtypename',
//    title:'食物种类名',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'foodname',
//    title:'食物名称',
//    sortable:'true'
//  },{
//    field:'eatingamount',
//    title:'饮食量',
//    sortable:'true'
//  },{
//    field:'unitname',
//    title:'计量单位名',
//    sortable:'true',
//    visible:false
//  },{
//    field:'eatingtime',
//    title:'饮食时间',
//    sortable:'true'
//  },{
//    field:'eatingrecordsuptime',
//    title:'饮食记录上传时间',
//    sortable:'true'
//  },{
//    field:'eatinginforemarks',
//    title:'饮食信息备注',
//    sortable:'true',
//    visible:false
//  },{
//    field:'tempuserid',
//    title:'用户id',
//    sortable:'true'
//  },{
//    field:'temp_eatinganalysisid',
//    title:'temp_饮食状况分析ID',
//    sortable:'true',
//    visible:false
//  },{
//    field:'eatingstateback',
//    title:'饮食后状态反馈',
//    sortable:'true',
//    visible:false
//  },{
//    field:'temp_foodnutritionid',
//    title:'食物营养成分id',
//    sortable:'true',
//    visible:false
//  },{
//    field:'temp_locationinfoid',
//    title:'位置信息id',
//    sortable:'true',
//    visible:false
//  },{
//    field:'temp_intelligentdeviceid',
//    title:'设备id',
//    sortable:'true',
//    visible:false
//  },{
//    field:'intelligentdevicecode',
//    title:'设备代码',
//    sortable:'true',
//    visible:false
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
//
//
//
////营养偏好记录表
//$('#eatingPrefer').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'eatingpreferid',
//    title:'营养偏好ID ',
//    sortable:'true'
//  },{
//    field:'foodtypename',
//    title:'食物种类名',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'foodname',
//    title:'食物名称',
//    sortable:'true'
//  },{
//    field:'preference',
//    title:'偏爱度',
//    sortable:'true'
//  },{
//    field:'averageintake',
//    title:'平均每天摄入量',
//    sortable:'true'
//  },{
//    field:'temp_foodnutritionid',
//    title:'食物营养成分ID',
//    sortable:'true'
//  },{
//    field:'temp-userid',
//    title:'用户ID',
//    sortable:'true'
//  },{
//    field:'eatingoftenstarttime',
//    title:'最频繁发生时间开始',
//    sortable:'true'
//  },{
//    field:'eatingoftenovertime',
//    title:'最频繁发生时间结束',
//    sortable:'true'
//  },{
//    field:'temp_locationinfoid',
//    title:'位置信息ID',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
//
////普通用户表
//$('#healther').bootstrapTable({
//  method:'get',
//  cache:false,
//  striped:true,
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'userid',
//    title:'用户ID',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'username',
//    title:'用户名',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'usersex',
//    title:'用户性别',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'userage',
//    title:'用户年龄',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'userpassword',
//    title:'密码',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'userphonenumber',
//    title:'手机号码',
//    sortable:'true'
//  },{
//    field:'usermail',
//    title:'邮箱',
//    sortable:'true'
//  },{
//    field:'userrank',
//    title:'用户等级',
//    sortable:'true'
//  },{
//    field:'userwroktype',
//    title:'用户工作类型',
//    sortable:'true'
//  },{
//    field:'userbmiindex',
//    title:'用户BMI指数',
//    sortable:'true'
//  },{
//    field:'temp_sleepfeatureid',
//    title:'睡眠特征id',
//    sortable:'true'
//  },{
//    field:'temp_exercisefeatureid',
//    title:'运动特征',
//    sortable:'true'
//  },{
//    field:'temp_eatingfeatureid',
//    title:'饮食特征id',
//    sortable:'true'
//  },{
//    field:'temp_adminisareaid',
//    title:'行政区划',
//    sortable:'true'
//  }],
//  pagination:true,
//  pageList:[10,20,50,100,500],
//  pageSize:10,
//  pageNumber:1,
//  clickToSelect:true,
//  smartDisplay:true,
//  sidePagination:'server',
//  queryParamsType:'limit',
//  responseHandler:responseHandler,
//  queryParams:queryParams
//});
//
////医生专长信息表
//$('#doctorexpetiesTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'doctorexpertiseid',
//    title:'医生专长id',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'doctorexpertisetitle',
//    title:'医生专长主题',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'doctorexpertiseexplain',
//    title:'医生专长简介',
//    sortable:'true'
//  },{
//    field:'temp_doctorexptypeid',
//    title:'医生专长类',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////医生专长代码分类表
//$('#doctorexpTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'doctorexptypeid',
//    title:'医生专长类型id',
//    sortable:'true',
//    formatter:'nameFormatter'
//  },{
//    field:'doctorexptypename',
//    title:'医生专长类型名',
//    sortable:'true'
//  },{
//    field:'doctortypecode',
//    title:'医生专长代码',
//    sortable:'true'
//  },{
//    field:'doctorexptypeexplain',
//    title:'医生专长分类说',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////饮食套餐信息表
//$('#setmealTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'setmealinfoid',
//    title:'套餐信息id',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'foodtypecontent',
//    title:'包含食物种类数',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'setmealname',
//    title:'套餐名',
//    sortable:'true'
//  },{
//    field:'setmealexplain',
//    title:'套餐简介',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////中药信息表
//$('#chinesemedicineTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'chinesemedicineid',
//    title:'药品id',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'medicinename',
//    title:'药名',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'medicinegeneraltype',
//    title:'药品总类别',
//    sortable:'true'
//  },{
//    field:'medicinesubtype',
//    title:'药品子类别',
//    sortable:'true'
//  },{
//    field:'medicineproperty',
//    title:'药性',
//    sortable:'true'
//  },{
//    field:'medicinetaste',
//    title:'药味',
//    sortable:'true'
//  },{
//    field:'indicationsfunction',
//    title:'功能主治',
//    sortable:'true'
//  },{
//    field:'channeltropism',
//    title:'归经',
//    sortable:'true'
//  },{
//    field:'clinicalapplication',
//    title:'临床应用',
//    sortable:'true'
//  },{
//    field:'medicinegenera',
//    title:'科属与药用部分',
//    sortable:'true'
//  },{
//    field:'prescriptionname',
//    title:'处方用名',
//    sortable:'true'
//  },{
//    field:'generaldosage',
//    title:'一般用量',
//    sortable:'true'
//  },{
//    field:'generalusage',
//    title:'一般用法',
//    sortable:'true'
//  },{
//    field:'withmedicine',
//    title:'附药',
//    sortable:'true'
//  },{
//    field:'comment',
//    title:'按语',
//    sortable:'true'
//  },{
//    field:'prescriptionsexample',
//    title:'方济举例',
//    sortable:'true'
//  },{
//    field:'medicineremarks',
//    title:'药品备注',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////智能设备表
//$('#intelligentdeviceTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'intelligentdeviceid',
//    title:'设备id',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'intelligentdevicetype',
//    title:'设备类型',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'intelligentdevicename',
//    title:'设备名称',
//    sortable:'true'
//  },{
//    field:'intelligentdeviceweight',
//    title:'设备重量',
//    sortable:'true'
//  },{
//    field:'intelligentdevicecolor',
//    title:'设备颜色',
//    sortable:'true'
//  },{
//    field:'intelligentdevicefunction',
//    title:'设备主要功能',
//    sortable:'true'
//  },{
//    field:'intelligentdevicecode',
//    title:'设备代码',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////养生知识信息表
//$('#healthknowageTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'healthknowledgeid',
//    title:'养生知识id',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'healthknowledgetitle',
//    title:'养生知识主题',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'healthknowledgecontent',
//    title:'养生知识内容',
//    sortable:'true'
//  },{
//    field:'exersuggtime',
//    title:'发布时间',
//    sortable:'true'
//  },{
//    field:'temp_managerid',
//    title:'管理员id',
//    sortable:'true'
//  },{
//    field:'healthknowledgeremarks',
//    title:'养生知识备注',
//    sortable:'true'
//  },{
//    field:'temp_healthknowltypeid',
//    title:'养生知识类',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////常见疾病信息表
//$('#commondiseaseTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'commondiseaseid',
//    title:'常见疾病id',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'temp_commonditypeid',
//    title:'常见疾病类别id',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'commondiname',
//    title:'常见疾病名称',
//    sortable:'true'
//  },{
//    field:'diseaseexplain',
//    title:'疾病说明',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
//
//
////体质辨识问卷项目表
//$('#identifyissueTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'identifyissueid',
//    title:'体质辨识问题id',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'temp_physiqueinfoid',
//    title:'体质信息id',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'identifyissuecontent',
//    title:'体质辨识问题内容',
//    sortable:'true'
//  },{
//    field:'identifyissueremarks',
//    title:'体质辨识问题备注',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////医院信息表
//$('#hospitalinfoTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'hospitalid',
//    title:'医院id',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'hospitalname',
//    title:'医院名称',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'hospitalexplain',
//    title:'医院简介',
//    sortable:'true'
//  },{
//    field:'temp_locationinfoid',
//    title:'位置信息id',
//    sortable:'true'
//  },{
//    field:'hospitalrank',
//    title:'医院级别',
//    sortable:'true'
//  },{
//    field:'temp_adminisareaid',
//    title:'行政区划id',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////计量单位表
//$('#unitattributeTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'unitattributeid',
//    title:'计量单位id',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'unitattributename',
//    title:'计量单位属性名',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'unitlevel',
//    title:'单位大小级别',
//    sortable:'true'
//  },{
//    field:'unitname',
//    title:'计量单位名',
//    sortable:'true'
//  },{
//    field:'hexadecimal',
//    title:'进制',
//    sortable:'true'
//  },{
//    field:'unitremarks',
//    title:'计量单位备注',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////地理位置信息
//$('#locationinfoTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'locationinfoid',
//    title:'地理位置id',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'locationlongitude',
//    title:'地理位置经度',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'locationlatitude',
//    title:'地理位置纬度',
//    sortable:'true'
//  },{
//    field:'reallocation',
//    title:'具体地理位置',
//    sortable:'true'
//  },{
//    field:'locationremarks',
//    title:'地理位置备注',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////饮食特征信息
//$('#eatingFeature').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'eatingfeatureid',
//    title:'饮食特征id',
//    formatter:'nameFormatter',
//    sortable:true,
//    visible:false
//  },{
//    field:'eatinghabitsdetemine',
//    title:'饮食习惯是否合理',
//    sortable:'true'
//  },{
//    field:'temp_userid',
//    title:'用户id',
//    sortable:'true'
//  },{
//    field:'eatinghabitanalysis',
//    title:'饮食习惯分析结果',
//    sortable:'true'
//  },{
//    field:'averageenergyintake',
//    title:'平均每天能量摄入',
//    sortable:'true'
//  },{
//    field:'averagemoistureintake',
//    title:'平均每天能量摄入'
//  },{
//    field:'averageproteinintake',
//    title:'平均每天蛋白质摄入',
//    sortable:'true'
//  },{
//    field:'averagefatintake',
//    title:'平均每天脂肪摄入',
//    sortable:'true'
//  },{
//    field:'averagefiberintake',
//    title:'平均每天膳食纤维摄入',
//    sortable:'true'
//  },{
//    field:'averagecarbohydrateintake',
//    title:'平均每天碳水化合物摄入',
//    sortable:'true'
//  },{
//    field:'averagevitaminaintake',
//    title:'平均每天维生素A摄入',
//    sortable:'true'
//  },{
//    field:'averagevitaminb1intake',
//    title:'平均每天维生素B1摄入',
//    sortable:'true'
//  },{
//    field:'averagevitaminb2intake',
//    title:'平均每天维生素B2摄入',
//    sortable:'true'
//  },{
//    field:'averagevitaminb6intake',
//    title:'平均每天维生素B6摄入',
//    sortable:'true'
//  },{
//    field:'averagevitaminb12intake',
//    title:'平均每天维生素B12摄入',
//    sortable:'true'
//  },{
//    field:'averagevitamincintake',
//    title:'平均每天维生素C摄入',
//    sortable:'true'
//  },{
//    field:'averagevitamindintake',
//    title:'平均每天维生素D摄入',
//    sortable:'true'
//  },{
//    field:'averagevitamineintake',
//    title:'平均每天维生素E摄入',
//    sortable:'true'
//  },{
//    field:'averagenicotinicacidintake',
//    title:"平均每天烟酸摄入",
//    sortable:'true'
//  },{
//    field:'averagefolateintake',
//    title:'平均每天叶酸摄入',
//    sortable:'true'
//  },{
//    field:'averagesodiumintake',
//    title:"平均每天纳摄入",
//    sortable:'true'
//  },{
//    field:'averagecalciumintake',
//    title:'平均每天钙摄入',
//    sortable:'true'
//  },{
//    field:'averageironintake',
//    title:'平均每天铁摄入',
//    sortable:'true'
//  },{
//    field:'averagepotassiumintake',
//    title:'平均每天钾摄入',
//    sortable:'true'
//  },{
//    field:'averagezincintake',
//    title:'平均每天锌摄入',
//    sortable:'true'
//  },{
//    field:'averagemangaessintake',
//    title:'平均每天酶摄入',
//    sortable:'true'
//  },{
//    field:'averagecopperintake',
//    title:'平均每天铜摄入',
//    sortable:'true'
//  },{
//    field:'averagechromiumintake',
//    title:'平均每天铬摄入',
//    sortable:'true'
//  },{
//    field:'averagemangaessintake',
//    title:'平均每天锰摄入',
//    sortable:'true'
//  },{
//    field:'averagemolybdenumintake',
//    title:'平均每天钴摄入',
//    sortable:'true'
//  },{
//    field:'averageiodineintake',
//    title:'平均每天碘摄入',
//    sortable:'true'
//  },{
//    field:'averagephosphusintake',
//    title:'平均每天磷摄入',
//    sortable:'true'
//  },{
//    field:'averageseleniumintake',
//    title:'平均每天硒摄入',
//    sortable:'true'
//  },{
//    field:'averagefluorineintake',
//    title:'平均每天氟摄入',
//    sortable:'true'
//  },{
//    field:'averagechokesterolintake',
//    title:'平均每天胆固醇摄入',
//    sortable:'true'
//  },{
//    field:'averagesaturatedintake',
//    title:'平均每天饱和脂肪酸摄入',
//    sortable:'true'
//  },{
//    field:'averageacidregurgitationintake',
//    title:'平均每天泛酸摄入',
//    sortable:'true'
//  },{
//    field:'averagebiotinintake',
//    title:'平均每天生物酸摄入',
//    sortable:'true'
//  },{
//    field:'averagecholineintake',
//    title:'平均每天胆碱摄入',
//    sortable:'true'
//  },{
//    field:'temp_unitattributeid',
//    title:'计量单位id',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////体质辨识选项表
//$('#identifychoiceTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//    field:'identifychoiceid',
//    title:'题目选项id',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'identifychoicevalue',
//    title:'题目分数值',
//    sortable:'true',
//    sorter:'starsSorter'
//  },{
//    field:'scriptdescribe',
//    title:'定性描述',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////用药信息表
//$('#medicineuseinfoTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//      field:'medicineuseinfoid',
//      title:'用药信息id',
//      formatter:'nameFormatter',
//      sortable:'true'
//  },{
//    field:'medicineusetype',
//    title:'药品类型',
//    formatter:'nameFormatter',
//    sortable:'true'
//  },{
//    field:'medicineusename',
//    title:'药品名称',
//    sortable:'true'
//  },{
//    field:'medicineusedose',
//    title:'用药剂量',
//    sortable:'true'
//  },{
//    field:'medicineuseremarks',
//    title:'用药备注',
//    sortable:'true'
//  },{
//    field:'prescriptiontag',
//    title:'方剂标识',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////设备参数代码表
//$('#parametercodeTable').bootstrapTable({
//  columns:[{
//    field:'state',
//    checkbox:"true"
//  },{
//      field:'deviceparacodeid',
//      title:'设备参数代码id',
//      formatter:'nameFormatter',
//      sortable:'true'
//  },{
//    field:'parametercode',
//    title:'设备参数代码',
//    sortable:'true'
//  },{
//    field:'parametername',
//    title:'设备参数名称',
//    sortable:'true'
//  },{
//    field:'parametermean',
//    title:'设备参数含义',
//    sortable:'true'
//  }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////设备参数映射表
//$('#parametermappTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'deviceparamappid',
//        title:'设备参数映射id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'temp_intelligentdeviceid',
//        title:'设备id',
//        sortable:'true'
//    },{
//        field:'temp_deviceparacodeid',
//        title:'设备参数代码id',
//        sortable:'true'
//    },{
//        field:'deviceparavalue',//设备参数值
//        title:'设备参数值',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////设备数据采集代码表
//$('#dataacquisitionTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'acquiredataid',
//        title:'采集数据id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'acquiredataname',
//        title:'采集数据名',
//        sortable:'true'
//    },{
//        field:'acquiredataexplain',
//        title:'采集数据说明',
//        sortable:'true'
//    },{
//        field:'temp_acqdatatypeid',
//        title:'数据类型id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////养生知识类别表
//$('#healthknowledgetypeTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'healthknowltypeid',
//        title:'养生知识类别id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'healthknowltypename',
//        title:'养生知识类别名',
//        sortable:'true'
//    },{
//        field:'healthknowltypecode',
//        title:'养生知识类别代码',
//        sortable:'true'
//    },{
//        field:'classifyexplain',
//        title:'分类说明',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////健康建议类别表
//$('#healthsuggtypeTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'healthsuggtypeid',
//        title:'健康建议类别id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'healthsuggtypename',
//        title:'健康建议类别名',
//        sortable:'true'
//    },{
//        field:'healthsuggtypecode',
//        title:'健康建议类别代码',
//        sortable:'true'
//    },{
//        field:'suggclassifyexpla',
//        title:'建议分类说明',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////健康建议表
//$('#healthsuggestionsTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'healthsuggeioniid',
//        title:'健康建议id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'healthsuggtitle',
//        title:'健康建议主题',
//        sortable:'true'
//    },{
//        field:'healthsuggcontent',
//        title:'健康建议内容',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'temp_用户id',
//        sortable:'true'
//    },{
//        field:'temp_healthsuggtypeid',
//        title:'temp_健康建议类别id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////健康指标信息表
//$('#healthindicatorinfoTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'healthindicatorid',
//        title:'健康指标信息id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'healthindicatorname',
//        title:'健康指标名称',
//        sortable:'true'
//    },{
//        field:'healthindicatorvalue',
//        title:'健康指标值',
//        sortable:'true'
//    },{
//        field:'healthindicatorchange',
//        title:'健康指标变化趋势',
//        sortable:'true'
//    },{
//        field:'indicatorchangeexplain',
//        title:'指标变化趋势说明',
//        sortable:'true'
//    },{
//        field:'temp_healthtrendid',
//        title:'temp_健康趋势id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////健康趋势分析记录表
//$('#healthtrendrecordsTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'healthtrendid',
//        title:'健康趋势id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'heaanalysistitle',
//        title:'健康分析主题',
//        sortable:'true'
//    },{
//        field:'healthanalysistime',
//        title:'健康分析时间',
//        sortable:'true'
//    },{
//        field:'healthtrendanalysiresult',
//        title:'健康趋势总分析结果',
//        sortable:'true'
//    },{
//        field:'temp_personalizedhealthid',
//        title:'个性化养生信息id',
//        sortable:'true'
//    },{
//        field:'healthtrendanalysisremarks',
//        title:'健康趋势分析备注',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////健康预警记录表
//$('#healthwarningrecordsTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'healthwarningid',
//        title:'健康预警id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'healthwarningtitle',
//        title:'健康预警主题',
//        sortable:'true'
//    },{
//        field:'healthanwarningcontent',
//        title:'健康预警内容',
//        sortable:'true'
//    },{
//        field:'healthwarningtime',
//        title:'健康预警时间',
//        sortable:'true'
//    },{
//        field:'healthwarningreason',
//        title:'健康预警原因',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'healthwarningremarks',
//        title:'健康预警备注',
//        sortable:'true'
//    },{
//        field:'healthsuggestion',
//        title:'健康建议',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////个性化养生信息表
//$('#personalizedhealthinfoTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'personalizedhealthid',
//        title:'个性化养生信息id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'personalizedhealthtitle',
//        title:'个性化养生主题',
//        sortable:'true'
//    },{
//        field:'personalizedhealthcontent',
//        title:'个性化养生内容',
//        sortable:'true'
//    },{
//        field:'personalizedhealthremarks',
//        title:'个性化养生备注',
//        sortable:'true'
//    },{
//        field:'temp_healthknowltypeid',
//        title:'temp_养生知识类别id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////常见疾病类别表
//$('#commondiseasetypeTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'commonditypeid',
//        title:'常见疾病类别id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'commonditypename',
//        title:'常见疾病类别名',
//        sortable:'true'
//    },{
//        field:'commonditypecode',
//        title:'常见疾病类别代码',
//        sortable:'true'
//    },{
//        field:'diclassifyexplain',
//        title:'常见疾病分类说明',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////体质信息表
//$('#phyciqueinfoTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'physiqueinfoid',
//        title:'体质信息id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'tablescoreheight',
//        title:'量表辨识总分上限',
//        sortable:'true'
//    },{
//        field:'tablescorelow',
//        title:'量表辨识总分下限',
//        sortable:'true'
//    },{
//        field:'switchscoreheight',
//        title:'转换得分上限',
//        sortable:'true'
//    },{
//        field:'switchscorelow',
//        title:'转换得分下限',
//        sortable:'true'
//    },{
//        field:'generacharacter',
//        title:'总体特征',
//        sortable:'true'
//    },{
//        field:'shapefeature',
//        title:'形体特征',
//        sortable:'true'
//    },{
//        field:'commonmanifest',
//        title:'常见表现',
//        sortable:'true'
//    },{
//        field:'mentalcharacter',
//        title:'心理特征',
//        sortable:'true'
//    },{
//        field:'incidencetendency',
//        title:'发病倾向',
//        sortable:'true'
//    },{
//        field:'adaptivecapacity',
//        title:'环境适应能力',
//        sortable:'true'
//    },{
//        field:'physicaltypename',
//        title:'体质类型名',
//        sortable:'true'
//    },{
//        field:'physicaltypecode',
//        title:'体质类型代码',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////体质疾病关系表
//$('#identifydiseaserelTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'identifydirelid',
//        title:'体质疾病关系id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'temp_physiqueinfoid',
//        title:'体质类型id',
//        sortable:'true'
//    },{
//        field:'temp_commondiseaseid',
//        title:'常见疾病id',
//        sortable:'true'
//
//    },{
//        field:'identifydirelexplain',
//        title:'体病关系说明',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////医生专长信息表
//$('#doctorexpertiseinfoTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'doctorexpertiseid',
//        title:'医生专长id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'doctorexpertisetitle',
//        title:'医生专长主题',
//        sortable:'true'
//    },{
//        field:'doctorexpertiseexplain',
//        title:'医生专长简介',
//        sortable:'true'
//    },{
//        field:'temp_doctorexptypeid',
//        title:'医生专长类型id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////医生专长分类代码表
//$('#doctorexpertisetypeTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'doctorexptypeid',
//        title:'医生专长类型id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'doctorexptypename',
//        title:'医生专长类型名',
//        sortable:'true'
//    },{
//        field:'doctorexptypecode',
//        title:'医生专长代码',
//        sortable:'true'
//    },{
//        field:'doctorexptypeexplain',
//        title:'医生专长分类说明',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////医院医生关系表
//$('#hospitaldoctorrelTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'hospitaldocrelid',
//        title:'医院医生关系id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'temp_hospitalid',
//        title:'医院id',
//        sortable:'true'
//    },{
//        field:'temp_doctorid',
//        title:'医生id',
//        sortable:'true'
//    },{
//        field:'temp_hospitalofficeid',
//        title:'医院科室id',
//        sortable:'true'
//    },{
//        field:'workduty',
//        title:'担任职务',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////医院科室信息表
//$('#hospitalofficesinfoTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'hospitalofficeid',
//        title:'医院科室id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'hospitalofficename',
//        title:'医院科室名',
//        sortable:'true'
//    },{
//        field:'hospitalofficeexplain',
//        title:'医院科室简介',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////行政区划代码表
//$('#adminisareaTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'adminisareaid',
//        title:'行政区划id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'adminisareacode',
//        title:'行政区划代码',
//        sortable:'true'
//    },{
//        field:'adminisareaname',
//        title:'行政区划名',
//        sortable:'true'
//    },{
//        field:'adminisarearemarks',
//        title:'行政区划备注',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////手机使用偏好记录表
//$('#phonepreferuserecordsTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'phonepreferuseid',
//        title:'手机使用偏好id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'offenusebeginat',
//        title:'最频繁使用开始时间段',
//        sortable:'true'
//    },{
//        field:'oftenuseovertime',
//        title:'最频繁使用结束时间',
//        sortable:'true'
//    },{
//        field:'temp_locationinfoid',
//        title:'位置信息id',
//        sortable:'true'
//    },{
//        field:'temp-appinfoid',
//        title:'应用信息id',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'calculatetimeup',
//        title:'计算时间上限',
//        sortable:'true'
//    },{
//        field:'calculatetimedown',
//        title:'计算时间下限',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////手机应用信息表
//$('#phoneappinfoTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'phoneappinfoid',
//        title:'应用信息id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'apptype',
//        title:'应用种类',
//        sortable:'true'
//    },{
//        field:'appname',
//        title:'应用名称',
//        sortable:'true'
//    },{
//        field:'apptag',
//        title:'应用标识',
//        sortable:'true'
//    },{
//        field:'appotherinfo',
//        title:'应用其他信息',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////手机监控特征信息表
//$('#phoneinfoTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'phoneinfoid',
//        title:'手机信息id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'phoneuniqunum',
//        title:'手机唯一标识',
//        sortable:'true'
//    },{
//        field:'phonenum',
//        title:'手机号码',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////手机监控记录表
//$('#phonemonitorrecordsTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'phoneappmonitorrecordid',
//        title:'手机应用监控记录id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'temp_appinfoid',
//        title:'应用信息id',
//        sortable:'true'
//    },{
//        field:'appopentime',
//        title:'应用打开时间',
//        sortable:'true'
//    },{
//        field:'appclosetime',
//        title:'应用关闭时间',
//        sortable:'true'
//    },{
//        field:'appusetime',
//        title:'应用使用时长',
//        sortable:'true'
//    },{
//        field:'temp_locationinfoid',
//        title:'位置信息id',
//        sortable:'true'
//    },{
//        field:'temp_phoneinfoid',
//        title:'手机信息id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////饮食状况分析表
//$('#eatinganalysisTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'eatinganalysisid',
//        title:'饮食状况分析id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'energyintake',
//        title:'能量摄入',
//        sortable:'true'
//    },{
//        field:'moistureintake',
//        title:'水分摄入',
//        sortable:'true'
//    },{
//        field:'proteinintake',
//        title:'蛋白质摄入',
//        sortable:'true'
//    },{
//        field:'fatintake',
//        title:'脂肪摄入',
//        sortable:'true'
//    },{
//        field:'fiberintake',
//        title:'膳食纤维摄入',
//        sortable:'true'
//    },{
//        field:'carbohydrateintake',
//        title:'碳水化合物摄入',
//        sortable:'true'
//    },{
//        field:'vitaminaintake',
//        title:'维生素A摄入',
//        sortable:'true'
//    },{
//        field:'vitaminb1intake',
//        title:'维生素B1摄入',
//        sortable:'true'
//    },{
//        field:'vitaminb2intake',
//        title:'维生素B2摄入',
//        sortable:'true'
//    },{
//        field:'vitaminb6intake',
//        title:'维生素B6摄入',
//        sortable:'true'
//    },{
//        field:'vitaminb12intake',
//        title:'维生素B12摄入',
//        sortable:'true'
//    },{
//        field:'vitamincintake',
//        title:'维生素C摄入',
//        sortable:'true'
//    },{
//        field:'vitamindintake',
//        title:'维生素D摄入',
//        sortable:'true'
//    },{
//        field:'vitamineintake',
//        title:'维生素E摄入',
//        sortable:'true'
//    },{
//        field:'nicotinicacidintake',
//        title:"烟酸摄入",
//        sortable:'true'
//    },{
//        field:'folateintake',
//        title:'叶酸摄入',
//        sortable:'true'
//    },{
//        field:'sodiumintake',
//        title:"钠摄入",
//        sortable:'true'
//    },{
//        field:'calciumintake',
//        title:'钙摄入',
//        sortable:'true'
//    },{
//        field:'ironintake',
//        title:'铁摄入',
//        sortable:'true'
//    },{
//        field:'potassiumintake',
//        title:'钾摄入',
//        sortable:'true'
//    },{
//        field:'zincintake',
//        title:'锌摄入',
//        sortable:'true'
//    },{
//        field:'mangaessintake',
//        title:'酶摄入',
//        sortable:'true'
//    },{
//        field:'copperintake',
//        title:'铜摄入',
//        sortable:'true'
//    },{
//        field:'chromiumintake',
//        title:'铬摄入',
//        sortable:'true'
//    },{
//        field:'mangaessintake',
//        title:'锰摄入',
//        sortable:'true'
//    },{
//        field:'molybdenumintake',
//        title:'钼摄入',
//        sortable:'true'
//    },{
//        field:'iodineintake',
//        title:'碘摄入',
//        sortable:'true'
//    },{
//        field:'phosphusintake',
//        title:'磷摄入',
//        sortable:'true'
//    },{
//        field:'seleniumintake',
//        title:'硒摄入',
//        sortable:'true'
//    },{
//        field:'fluorineintake',
//        title:'氟摄入',
//        sortable:'true'
//    },{
//        field:'cholesterolintake',
//        title:'胆固醇摄入',
//        sortable:'true'
//    },{
//        field:'saturatedfattyacidintake',
//        title:'饱和脂肪酸摄入',
//        sortable:'true'
//    },{
//        field:'acidregurgitationintake',
//        title:'泛酸摄入',
//        sortable:'true'
//    },{
//        field:'biotinintake',
//        title:'生物酸摄入',
//        sortable:'true'
//    },{
//        field:'cholineintake',
//        title:'胆碱摄入',
//        sortable:'true'
//    },{
//        field:'temp_eatingrecordid',
//        title:'饮食信息记录id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////用户睡眠特征信息表
//$('#usersleepfeatureTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'sleepfeatureid',
//        title:'睡眠特征id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'airhumidity',
//        title:'空气湿度相对比',
//        sortable:'true'
//    },{
//        field:'ambienttemperature',
//        title:'环境温度',
//        sortable:'true'
//    },{
//        field:'ambientnoise',
//        title:'环境噪声',
//        sortable:'true'
//    },{
//        field:'sleephabits',
//        title:'睡前习惯',
//        sortable:'true'
//    },{
//        field:'goodbedtimehabits',
//        title:'睡前习惯是否健康',
//        sortable:'true'
//    },{
//        field:'siestahabit',
//        title:'是否有午睡习惯',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'averagesleeptime',
//        title:'24小时平均睡眠时长',
//        sortable:'true'
//    },{
//        field:'sleephabitdetemination',
//        title:'睡眠习惯是否合理',
//        sortable:'true'
//    },{
//        field:'sleepindex',
//        title:'睡眠指数',
//        sortable:'true'
//    },{
//        field:'sleephabitanalysis',
//        title:'睡眠习惯分析结果',
//        sortable:'true'
//    },{
//        field:'temp_locationindoid',
//        title:'位置信息id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////睡眠信息记录
//$('#sleepinforecordsTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'sleeprecordid',
//        title:'睡眠信息记录id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'airhumidity',
//        title:'空气湿度相对比',
//        sortable:'true'
//    },{
//        field:'ambienttemperature',
//        title:'环境温度',
//        sortable:'true'
//    },{
//        field:'ambientnoise',
//        title:'环境噪声',
//        sortable:'true'
//    },{
//        field:'sleepbegin',
//        title:'开始睡眠时间',
//        sortable:'true'
//    },{
//        field:'sleepover',
//        title:'结束睡眠时间',
//        sortable:'true'
//    },{
//        field:'deepsleeptime',
//        title:'深睡时长',
//        sortable:'true'
//    },{
//        field:'shallowsleeptime',
//        title:'浅睡时长',
//        sortable:'true'
//    },{
//        field:'sleepremarks',
//        title:'睡眠情况备注',
//        sortable:'true'
//    },{
//        field:'sleeprecordsuptime',
//        title:'睡眠记录上传时间',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'temp_locationindoid',
//        title:'位置信息id',
//        sortable:'true'
//    },{
//        field:'waketimes',
//        title:'醒来次数',
//        sortable:'true'
//    },{
//        field:'temp_intelligentdeviceid',
//        title:'设备id',
//        sortable:'true'
//    },{
//        field:'intelligentdevicecode',
//        title:'设备代码',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////睡眠偏好记录
//$('#sleeppreferrecordsTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'sleeppreferid',
//        title:'睡眠偏好id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'prefersleepbeginat',
//        title:'偏好睡眠开始时间',
//        sortable:'true'
//    },{
//        field:'prefersleepoverat',
//        title:'偏好睡眠结束时间',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'temp_locationinfoid',
//        title:'位置信息id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////用户运动特征信息
//$('#userexercisefeatureTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'exercisefeatureid',
//        title:'运动特征id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'height',
//        title:'身高',
//        sortable:'true'
//    },{
//        field:'weight',
//        title:'体重',
//        sortable:'true'
//    },{
//        field:'steplength',
//        title:'行走步长',
//        sortable:'true'
//    },{
//        field:'runlength',
//        title:'跑步步长',
//        sortable:'true'
//    },{
//        field:'standardweight',
//        title:'标准体重',
//        sortable:'true'
//    },{
//        field:'datauptime',
//        title:'数据上传时间',
//        sortable:'true'
//    },{
//        field:'exercisefeatureremarks',
//        title:'运动特征备注',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'exercisehabitsdetemine',
//        title:'运动习惯是否合理',
//        sortable:'true'
//    },{
//        field:'exercisehabitanalysis',
//        title:'运动习惯分析结果',
//        sortable:'true'
//    },{
//        field:'averageexcitetime',
//        title:'每天平均运动时长',
//        sortable:'true'
//    },{
//        field:'exercisetypeprefer',
//        title:'运动方式偏好',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////运动信息记录
//$('#SportInfoRecordsTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'sportrecordid',
//        title:'运动信息记录id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'walkstepnumber',
//        title:'走路步数',
//        sortable:'true'
//    },{
//        field:'runstepnumber',
//        title:'跑步步数',
//        sortable:'true'
//    },{
//        field:'walkdistance',
//        title:'走路距离',
//        sortable:'true'
//    },{
//        field:'rundistance',
//        title:'跑步距离',
//        sortable:'true'
//    },{
//        field:'calorieconsumption',
//        title:'卡路里消耗量',
//        sortable:'true'
//    },{
//        field:'sportbegintime',
//        title:'记录开始时间',
//        sortable:'true'
//    },{
//        field:'sportovertime',
//        title:'记录结束时间',
//        sortable:'true'
//    },{
//        field:'sportrecorduptime',
//        title:'记录上传时间',
//        sortable:'true'
//    },{
//        field:'sportinforemarks',
//        title:'运动信息备注',
//        sortable:'true'
//    },{
//        field:'sportanalysis',
//        title:'运动情况分析',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'temp_locationinfoid',
//        title:'位置信息id',
//        sortable:'true'
//    },{
//        field:'sport_mode',
//        title:'运动模式',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'设备id',
//        sortable:'true'
//    },{
//        field:'intelligentdevicecode',
//        title:'设备代码',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////运动偏好记录
//$('#exercisepreferrecordsTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'exercisepreferenceid',
//        title:'运动偏好id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'exercisename',
//        title:'运动名称',
//        sortable:'true'
//    },{
//        field:'exercisetype',
//        title:'运动类型',
//        sortable:'true'
//    },{
//        field:'exercisedescribe',
//        title:'运动描述',
//        sortable:'true'
//    },{
//        field:'temp_exerciseid',
//        title:'运动实体id',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'temp_locationinfoid',
//        title:'位置信息id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////运动实体信息
//$('#exerciseinfoTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'exerciseid',
//        title:'运动实体id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'exercisename',
//        title:'运动名称',
//        sortable:'true'
//    },{
//        field:'exercisetypename',
//        title:'运动类型名',
//        sortable:'true'
//    },{
//        field:'energywaste',
//        title:'能量消耗量',
//        sortable:'true'
//    },{
//        field:'exercisetip',
//        title:'运动提醒',
//        sortable:'true'
//    },{
//        field:'exerciseaffect',
//        title:'运动作用介绍',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////中医诊断分类记录
//$('#tcmdiagnosistypeTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'diagnosistypeid',
//        title:'诊断类型id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'diagnosistypename',
//        title:'诊断类型名',
//        sortable:'true'
//    },{
//        field:'diagnosistypecode',
//        title:'诊断类型代码',
//        sortable:'true'
//    },{
//        field:'diagnosistypeexplain',
//        title:'诊断类型说明',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////中医诊疗记录
//$('#ctreatmentrecordsTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'exerciseid',
//        title:'中医诊疗记录id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'integral_spirit',
//        title:'整体_神',
//        sortable:'true'
//    },{
//        field:'integral_look',
//        title:'整体_se',
//        sortable:'true'
//    },{
//        field:'integral_shape',
//        title:'整体_形态',
//        sortable:'true'
//    },{
//        field:'part_head',
//        title:'局部_头颅',
//        sortable:'true'
//    },{
//        field:'part_organs',
//        title:'局部_五官',
//        sortable:'true'
//    },{
//        field:'part_chest',
//        title:'局部_胸腹',
//        sortable:'true'
//    },{
//        field:'part_tonguenature',
//        title:'舌象_舌质',
//        sortable:'true'
//    },{
//        field:'part_fur',
//        title:'舌象_舌苔',
//        sortable:'true'
//    },{
//        field:'pulsecondition',
//        title:'脉象检查',
//        sortable:'true'
//    },{
//        field:'inquiry_fell',
//        title:'问诊_感觉',
//        sortable:'true'
//    },{
//        field:'inquiry_eating',
//        title:'问诊_饮食',
//        sortable:'true'
//    },{
//        field:'inquiry_habit',
//        title:'问诊_习惯',
//        sortable:'true'
//    },{
//        field:'healthcareguid',
//        title:'保健防病指导',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'temp_doctorid',
//        title:'医生id',
//        sortable:'true'
//    },{
//        field:'temp_medicineuseinfoid',
//        title:'用药信息id',
//        sortable:'true'
//    },{
//        field:'examinationtime',
//        title:'诊疗时间',
//        sortable:'true'
//    },{
//        field:'examinationlocation',
//        title:'诊疗地点',
//        sortable:'true'
//    },{
//        field:'examinationresult',
//        title:'诊断结果',
//        sortable:'true'
//    },{
//        field:'examinationremarks',
//        title:'诊疗备注',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
//
////病史记录表
//$('#medicalhistoryrecordsTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'medicalhistoryrecordid',
//        title:'病史记录id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'diseasetype',
//        title:'疾病类型',
//        sortable:'true'
//    },{
//        field:'diseasename',
//        title:'疾病名称',
//        sortable:'true'
//    },{
//        field:'diseaseseverity',
//        title:'疾病严重性',
//        sortable:'true'
//    },{
//        field:'treatmentinfo',
//        title:'治疗相关信息',
//        sortable:'true'
//    },{
//        field:'treatmentdoctor',
//        title:'诊断医生',
//        sortable:'true'
//    },{
//        field:'treatmentunit',
//        title:'诊断单位',
//        sortable:'true'
//    },{
//        field:'treatmentlocation',
//        title:'诊断地点',
//        sortable:'true'
//    },{
//        field:'treatmentresult',
//        title:'诊断结果',
//        sortable:'true'
//    },{
//        field:'recoverydegree',
//        title:'康复程度',
//        sortable:'true'
//    },{
//        field:'treatmenttime',
//        title:'诊疗时间',
//        sortable:'true'
//    },{
//        field:'treatmentremarks',
//        title:'诊疗备注',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'temp_doctorid',
//        title:'医生id',
//        sortable:'true'
//    },{
//        field:'temp_medicineuseinfoid',
//        title:'用药信息id',
//        sortable:'true'
//    },{
//        field:'temp_commondiseaseid',
//        title:'常见疾病id',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////体质辨识结果记录表
//$('#constituteidentifyresultTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'identifyresultid',
//        title:'辨识结果id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户id',
//        sortable:'true'
//    },{
//        field:'temp_physiqueinfoid',
//        title:'体质信息id',
//        sortable:'true'
//    },{
//        field:'constituteidentifytime',
//        title:'体质辨识时间',
//        sortable:'true'
//    },{
//        field:'constituteidentifyremarks',
//        title:'体质辨识备注',
//        sortable:'true'
//    },{
//        field:'constituteidentifyresult',
//        title:'体质辨识结果',
//        sortable:'true'
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
////采集数据分类表
//$('#dataacquiretypeTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'acqdatatypeid',
//        title:'数据类型id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'acqdatatypename',
//        title:'采集数据类型名',
//        sortable:'true'
//    },{
//        field:'acqdatatypeexplain',
//        title:'采集数据类型说明',
//        sortable:'true'
//
//    }],
//    striped:true,
//    pagination:true,
//    pageList:[10,20,50,100,500],
//    pageSize:10,
//    pageNumber:1,
//    clickToSelect:true,
//    smartDisplay:true,
//    sidePagination:'server',
//    queryParamsType:'limit',
//    responseHandler:responseHandler,
//    queryParams:queryParams
//});
//
//
//function l_editable(){
//  $('.item_id').editable({
//    url:'',
//    type:'text',
//    title:'enter username',
//    success:function(response, newValue){
//      userModel.set('name', newValue);
//    }
//  });
//}
//
//
//
//
//
//  /*  ===================================js of nav==========================================================*/
//
//
//

//中医专家信息表
$('#expertTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'doctorid',
    title:'医生ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'doctorname',
    title:'医生姓名',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'doctorsex',
    title:'医生性别',
    sortable:'true'
  },{
    field:'doctorage',
    title:'医生年龄',
    sortable:'true'
  },{
    field:'professionalrands',
    title:'医生职称',
    sortable:'true'
  },{
    field:'doctorworktime',
    title:'工作时长',
    sortable:'true'
  },{
    field:'doctorsynopsis',
    title:'医生简介',
    sortable:'true',
    visible:false
  },{
    field:'researcharea',
    title:'研究方向',
    sortable:'true'
  },{
    field:'researchfindings',
    title:'相关研究成果',
    sortable:'true'
  },{
    field:'temp_adminisareaid',
    title:'行政区划',
    sortable:'true',
    visible:false
  },{
    field:'temp_doctorexpertiseid',
    title:'医生专长ID',
    sortable:'true',
    visible:false
  },{
    field:'doctorcode',
    title:'医生代码',
    sortable:'true',
    visible:'true'
  },{
     field:'temp_picturelocationid',
     title:'图片位置ID',
     sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
  /*responseHandler:function(res){
    return res.results;
  },
  pagination:true*/
  /*queryParams:function(params){
    alert(params.limit);
    *//*return params.p;*//*
  },*/
  /*queryParamsType:'json'*/
});
  /*method:'get',
  dataType:'jsonp',
  responseHandler:function(res){
    alert(res);
    return res;
  }*/

//管理员表
$('#eventsTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'managerid',
    title:'管理员ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'managername',
    title:'管理员名',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'managerpassword',
    title:'管理员密码',
    sortable:'true'
  },{
    field:'managerunit',
    title:'管理员单位',
    sortable:'true'
  },{
    field:'descrption',
    title:'职位',
    sortable:'true'
  //},{
  //  field:'descripti',
  //  title:'邮箱',
  //  sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
  });

//食物营养含量信息表
$('#FoodNutrientTable').bootstrapTable({
      columns:[{
        field:'state',
        checkbox:"true"
      },{
        field:'foodnutritionid',
        title:'食物营养成分ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
      },{
        field:'foodenergy',
        title:'食物能量',
        sortable:'true'
      },{
        field:'energyunit',
        title:'能量单位',
        sortable:'true',
        visible:false
      },{
        field:'foodmoisture',
        title:'食物水分',
        sortable:'true'
       },{
        field:'moistureunit',
        title:'水分单位',
        sortable:'true',
        visible:false
      },{
        field:'proteincontent',
        title:'蛋白质含量',
        sortable:'true'
      },{
        field:'proteinunit',
        title:'蛋白质单位',
        sortable:'true',
        visible:false
      },{
        field:'fatcontent',
        title:'脂肪含量',
        sortable:'true'
      },{
        field:'fatunit',
        title:'脂肪单位',
        sortable:'true',
        visible:false
      },{
        field:'fibercontent',
        title:'膳食纤维含量',
        sortable:'true'
      },{
        field:'fiberunit',
        title:'膳食纤维单位',
        sortable:'true',
        visible:false
      },{
        field:'carbohydratecontent',
        title:'碳水化合物含量',
        sortable:'true'
      },{
        field:'carbohydrateunit',
        title:'碳水化合物单位',
        sortable:'true',
        visible:false
      },{
        field:'vitaminacontent',
        title:'维生素A含量',
        sortable:'true'
      },{
        field:'vitaminaunit',
        title:'维生素A单位',
        sortable:'true',
        visible:false
      },{
        field:'vitaminb1content',
        title:'维生素B1含量',
        sortable:'true'
      },{
        field:'vitaminb1unit',
        title:'维生素B1单位',
        sortable:'true',
        visible:false
      },{
        field:'vitaminb2content',
        title:'维生素B2含量',
        sortable:'true'
      },{
        field:'vitaminb2unit',
        title:'维生素B2单位',
        sortable:'true',
        visible:false
      },{
        field:'vitaminb6content',
        title:'维生素B6含量',
        sortable:'true'
          },{
        field:'vitaminb6unit',
        title:'维生素B6单位',
        sortable:'true',
        visible:false
      },{
        field:'vitaminb12content',
        title:'维生素B12含量',
        sortable:'true'
          },{
        field:'vitaminb12unit',
        title:'维生素B12单位',
        sortable:'true',
        visible:false
      },{
        field:'vitaminccontent',
        title:'维生素C含量',
        sortable:'true'
          },{
        field:'vitamincunit',
        title:'维生素C单位',
        sortable:'true',
        visible:false
      },{
        field:'vitamindcontent',
        title:'维生素D含量',
        sortable:'true'
          },{
        field:'vitamindunit',
        title:'维生素D单位',
        sortable:'true',
        visible:false
      },{
        field:'vitaminecontent',
        title:'维生素E含量',
        sortable:'true'
      },{
        field:'vitamineunit',
        title:'维生素E单位',
        sortable:'true',
        visible:false
      },{
        field:'nicotinicacidcontent',
        title:"烟酸含量",
        sortable:'true'
           },{
        field:'nicotinicacidunit',
        title:"烟酸单位",
        sortable:'true',
        visible:false
      },{
        field:'folatecontent',
        title:'叶酸含量',
        sortable:'true'
      },{
        field:'folateunit',
        title:'叶酸单位',
        sortable:'true',
        visible:false
      },{
        field:'sodiumcontent',
        title:"纳含量",
        sortable:'true'
      },{
        field:'sodiumunit',
        title:"纳单位",
        sortable:'true',
        visible:false
      },{
        field:'calciumcontent',
        title:'钙含量',
        sortable:'true'
      },{
        field:'calciumunit',
        title:'钙单位',
        sortable:'true',
        visible:false
      },{
        field:'ironcontent',
        title:'铁含量',
        sortable:'true'
      },{
        field:'ironunit',
        title:'铁单位',
        sortable:'true',
        visible:false
      },{
        field:'potassiumcontent',
        title:'钾含量',
        sortable:'true'
      },{
        field:'potassiumunit',
        title:'钾单位',
        sortable:'true',
        visible:false
      },{
        field:'zinccontent',
        title:'锌含量',
        sortable:'true'
      },{
        field:'zincunit',
        title:'锌单位',
        sortable:'true',
        visible:false
      },{
        field:'mangaesscontent',
        title:'镁含量',
        sortable:'true'
      },{
        field:'mangaessunit',
        title:'镁单位',
        sortable:'true',
        visible:false
      },{
        field:'coppercontent',
        title:'铜含量',
        sortable:'true'
      },{
        field:'copperunit',
        title:'铜单位',
        sortable:'true',
        visible:false
      },{
        field:'chromiumcontent',
        title:'铬含量',
        sortable:'true'
      },{
        field:'chromiumunit',
        title:'铬单位',
        sortable:'true',
        visible:false
      },{
        field:'mangaesscontent',
        title:'锰含量',
        sortable:'true'
      },{
        field:'mangaessunit',
        title:'锰单位',
        sortable:'true',
        visible:false
      },{
        field:'molybdenumcontent',
        title:'钼含量',
        sortable:'true'
      },{
        field:'molybdenumunit',
        title:'钼单位',
        sortable:'true',
        visible:false
      },{
        field:'iodinecontent',
        title:'碘含量',
        sortable:'true'
      },{
        field:'iodineunit',
        title:'碘单位',
        sortable:'true',
        visible:false
      },{
        field:'phosphuscontent',
        title:'磷含量',
        sortable:'true'
      },{
        field:'phosphusunit',
        title:'磷单位',
        sortable:'true',
        visible:false
      },{
        field:'seleniumcontent',
        title:'硒含量',
        sortable:'true'
      },{
        field:'seleniumunit',
        title:'硒单位',
        sortable:'true',
        visible:false
      },{
        field:'fluorinecontent',
        title:'氟含量',
        sortable:'true'
      },{
        field:'fluorineunit',
        title:'氟单位',
        sortable:'true',
        visible:false
      },{
        field:'cholesterolcontent',
        title:'胆固醇含量',
        sortable:'true'
      },{
        field:'cholesterolunit',
        title:'胆固醇单位',
        sortable:'true',
        visible:false
      },{
        field:'saturatedfattyacidcontent',
        title:'饱和脂肪酸含量',
        sortable:'true'
      },{
        field:'saturatedfattyacidunit',
        title:'饱和脂肪酸单位',
        sortable:'true',
        visible:false
      },{
        field:'acidregurgitationcontent',
        title:'泛酸含量',
        sortable:'true'
      },{
        field:'acidregurgitationunit',
        title:'泛酸单位',
        sortable:'true',
        visible:false
      },{
        field:'biotincontent',
        title:'生物酸含量',
        sortable:'true'
      },{
        field:'biotinunit',
        title:'生物酸单位',
        sortable:'true',
        visible:false
      },{
        field:'cholinecontent',
        title:'胆碱含量',
        sortable:'true'
      },{
        field:'cholineunit',
        title:'胆碱单位',
        sortable:'true',
        visible:false
      }],
        striped:true,
        pagination:true,
        pageList:[10,20,50,100,500],
        pageSize:10,
        pageNumber:1,
        clickToSelect:true,
        smartDisplay:true
    }
);
//营养素平均每天摄入量表
$('#commonnutrientintakeTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'nutrientid',
    title:'营养素ID',
    sortable:'true',
    visible:false
  },{
    field:'nutrientname',
    title:'营养素名称',
    sortable:'true'
  },{
    field:'nutrientintakemax',
    title:'营养素摄入值大值',
    sortable:'true'
  },{
    field:'nutrientintakemin',
    title:'营养素摄入最小值',
    sortable:'true'
  },{
    field:'maxagefor',
    title:'适宜人群最大年龄',
    sortable:'true'
  },{
    field:'minagefor',
    title:'适宜人群最小年龄',
    sortable:'true'
  },{
    field:'nutrientintakeremarks',
    title:'营养素摄入备注',
    sortable:'true',
    visible:false
  },{
    field:'temp_unitattributeid',
    title:'计量单位ID',
    sortable:'true',
    visible:false
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
//  sidePagination:'server'
});

//饮食信息记录表
$('#eatingRecord').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'eatingrecordid',
    title:'饮食信息记录ID ',
    sortable:'true',
    visible:false
  },{
    field:'foodtypename',
    title:'食物种类名',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'foodname',
    title:'食物名称',
    sortable:'true'
  },{
    field:'eatingamount',
    title:'饮食量',
    sortable:'true'
  },{
    field:'unitname',
    title:'计量单位名',
    sortable:'true'
  },{
    field:'eatingtime',
    title:'饮食时间',
    sortable:'true'
  },{
    field:'eatingrecordsuptime',
    title:'饮食记录上传时间',
    sortable:'true'
  },{
    field:'eatinginforemarks',
    title:'饮食信息备注',
    sortable:'true'
  },{
    field:'temp_userid',
    title:'temp_用户ID',
    sortable:'true'
  },{
    field:'eatingstateback',
    title:'饮食后状态反馈',
    sortable:'true'
  },{
    field:'temp_foodnutritionid',
    title:'食物营养成分ID',
    sortable:'true'
  },{
    field:'temp_locationinfoid',
    title:'位置信息ID',
    sortable:'true'
  },{
    field:'temp_intelligentdeviceid',
    title:'设备ID',
    sortable:'true'
  },{
    field:'intelligentdevicecode',
    title:'设备代码',
    sortable:'true'
   },{
    field:'eatingupflag',
    title:'一次上传标识',
    sortable:'true'
  },{
    field:'setmealcode',
    title:'套餐代码值',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
  //sidePagination:'server',
  //queryParamsType:'limit',
  //responseHandler:responseHandler,
  //queryParams:queryParams

});


//中医诊断分类记录
$('#tcmdiagnosistypeTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'diagnosistypeid',
        title:'诊断类型ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'diagnosistypename',
        title:'诊断类型名',
        sortable:'true'
    },{
        field:'diagnosistypecode',
        title:'诊断类型代码',
        sortable:'true'
    },{
        field:'diagnosistypeexplain',
        title:'诊断分类说明',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//中医诊疗记录表
$('#ctreatmentrecordsTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'tcmexaminationid',
        title:'中医诊疗记录ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'integral_spirit',
        title:'整体_神',
        sortable:'true'
    },{
        field:'integral_look',
        title:'整体_色',
        sortable:'true'
    },{
        field:'integral_shape',
        title:'整体_形态',
        sortable:'true'
    },{
        field:'part_head',
        title:'局部_头颅',
        sortable:'true'
    },{
        field:'part_organs',
        title:'局部_五官',
        sortable:'true'
    },{
        field:'part_chest',
        title:'局部_胸腹',
        sortable:'true'
    },{
        field:'part_tonguenature',
        title:'舌象_舌质',
        sortable:'true'
    },{
        field:'part_fur',
        title:'舌象_舌苔',
        sortable:'true'
    },{
        field:'pulsecondition',
        title:'脉象检查',
        sortable:'true'
    },{
        field:'inquiry_fell',
        title:'问诊_感觉',
        sortable:'true'
    },{
        field:'inquiry_eating',
        title:'问诊_饮食',
        sortable:'true'
    },{
        field:'inquiry_habit',
        title:'问诊_习惯',
        sortable:'true'
    },{
        field:'healthcareguid',
        title:'保健防病指导',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'temp_doctorid',
        title:'医生ID',
        sortable:'true'
    },{
        field:'temp_medicineuseinfoid',
        title:'用药信息ID',
        sortable:'true'
    },{
        field:'examinationtime',
        title:'诊疗时间',
        sortable:'true'
    },{
        field:'examinationlocation',
        title:'诊疗地点',
        sortable:'true'
    },{
        field:'examinationresult',
        title:'诊断结果',
        sortable:'true'
    },{
        field:'examinationremarks',
        title:'诊疗备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//饮食偏好记录表
$('#eatingPrefer').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'eatingpreferid',
    title:'饮食偏好ID ',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'foodtypename',
    title:'食物种类名',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'foodname',
    title:'食物名称',
    sortable:'true'
  },{
    field:'preference',
    title:'偏爱度',
    sortable:'true'
  },{
    field:'averageintake',
    title:'平均每天摄入量',
    sortable:'true'
  },{
    field:'temp_foodnutritionid',
    title:'食物营养成分ID',
    sortable:'true'
  },{
    field:'temp_userid',
    title:'用户ID',
    sortable:'true'
  },{
    field:'eatingoftenstarttime',
    title:'最频繁发生时间开始',
    sortable:'true'
  },{
    field:'eatingoftenovertime',
    title:'最频繁发生时间结束',
    sortable:'true'
  },{
    field:'temp_locationinfoid',
    title:'位置信息ID',
    sortable:'true'
  },{
    field:'additemtime',
    title:'增加时间',
    sortable:'true'
  },{
    field:'currentlypreferflag',
    title:'当前偏好标识',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
  //sidePagination:'server',
  //queryParamsType:'limit',
  //responseHandler:responseHandler,
  //queryParams:queryParams
});

//普通用户表
$('#healther').bootstrapTable({
  method:'get',
  cache:false,
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'userid',
    title:'用户ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'username',
    title:'用户名',
    formatter:'nameFormatter',
    sortable:'true'
  },{
    field:'usersex',
    title:'用户性别',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'userage',
    title:'用户年龄',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'userpassword',
    title:'密码',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'userphonenumber',
    title:'手机号码',
    sortable:'true'
  },{
    field:'usermail',
    title:'邮箱',
    sortable:'true'
  },{
    field:'userrank',
    title:'用户等级',
    sortable:'true'
  },{
    field:'userwroktype',
    title:'用户工作类型',
    sortable:'true'
  },{
    field:'userbmiindex',
    title:'用户BMI指数',
    sortable:'true'
  },{
      field:'temp_sleepfeatureid',
      title:'睡眠特征ID',
      sortable:'true',
      visible:false
  },{
      field:'temp_exercisefeatureid',
      title:'运动特征ID',
      sortable:'true',
      visible:false
  },{
      field:'temp_eatingfeatureid',
      title:'饮食特征ID',
      sortable:'true',
      visible:false
  },{
      field:'temp_adminisareaid',
      title:'行政区划ID',
      sortable:'true',
      visible:false
  },{
      field:'temp_picturelocationid',
      title:'图片位置ID',
      sortable:'true',
      visible:false
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
  //sidePagination:'server',
  //responseHandler:responseHandler,
  //queryParams:queryParams

});

//医生专长信息表
$('#doctorexpetiesTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'doctorexpertiseid',
    title:'医生专长ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'doctorexpertisetitle',
    title:'医生专长主题',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'doctorexpertiseexplain',
    title:'医生专长简介',
    sortable:'true'
  },{
    field:'temp_doctorexptypeid',
    title:'医生专长类型ID',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//医生专长代码分类表
$('#doctorexpTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'doctorexptypeid',
    title:'医生专长类型ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'doctorexptypename',
    title:'医生专长类型名',
    sortable:'true'
  },{
    field:'doctortypecode',
    title:'医生专长代码',
    sortable:'true'
  },{
    field:'doctorexptypeexplain',
    title:'医生专长分类说明',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//饮食套餐信息表
$('#setmealTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'setmealinfoid',
    title:'套餐信息ID',
    sortable:'true',
    visible:false
  },{
    field:'foodtypecontent',
    title:'包含食物种类数',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'setmealname',
    title:'套餐名',
    sortable:'true'
  },{
    field:'setmealexplain',
    title:'套餐简介',
    sortable:'true'
  },{
    field:'setmealremarks',
    title:'套餐备注',
    sortable:'true'
  },{
    field:'setmealcode',
    title:'套餐代码值',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//中药信息表
$('#chinesemedicineTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'chinesemedicineid',
    title:'药品ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'medicinename',
    title:'药名',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'medicinegeneraltype',
    title:'药品总类别',
    sortable:'true'
  },{
    field:'medicinesubtype',
    title:'药品子类别',
    sortable:'true'
  },{
    field:'medicinetoxicity',
    title:'毒性',
    sortable:'true'
  },{
    field:'medicineproperty',
    title:'药性',
    sortable:'true'
  },{
    field:'medicinetaste',
    title:'药味',
    sortable:'true'
  },{
    field:'indicationsfunction',
    title:'功能主治',
    sortable:'true'
  },{
    field:'channeltropism',
    title:'归经',
    sortable:'true'
  },{
    field:'clinicalapplication',
    title:'临床应用',
    sortable:'true'
  },{
    field:'medicinegenera',
    title:'科属与药用部分',
    sortable:'true'
  },{
    field:'prescriptionname',
    title:'处方用名',
    sortable:'true'
  },{
    field:'generaldosage',
    title:'一般用量',
    sortable:'true'
  },{
    field:'generalusage',
    title:'一般用法',
    sortable:'true'
  },{
    field:'withmedicine',
    title:'附药',
    sortable:'true'
  },{
    field:'comment',
    title:'按语',
    sortable:'true'
  },{
    field:'prescriptionsexample',
    title:'方剂举例',
    sortable:'true'
  },{
    field:'medicineremarks',
    title:'药品备注',
    sortable:'true'
  },{
    field:'medicinecode',
    title:'中药代码',
    sortable:'true'
  },{
      field:'temp_picturelocationid',
      title:'图片位置ID',
      sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//智能设备表
$('#intelligentdeviceTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'intelligentdeviceid',
    title:'设备ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'intelligentdevicetype',
    title:'设备类型',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'intelligentdevicename',
    title:'设备名称',
    sortable:'true'
  },{
    field:'intelligentdeviceweight',
    title:'设备重量',
    sortable:'true'
  },{
    field:'intelligentdevicecolor',
    title:'设备颜色',
    sortable:'true'
  },{
    field:'intelligentdevicefunction',
    title:'设备主要功能',
    sortable:'true'
  },{
    field:'intelligentdevicecode',
    title:'设备代码',
    sortable:'true'
  },{
      field:'temp_picturelocationid',
      title:'图片位置ID',
      sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//养生知识信息表
$('#healthknowageTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'healthknowledgeid',
    title:'养生知识ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'healthknowledgetitle',
    title:'养生知识主题',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'healthknowledgecontent',
    title:'养生知识内容',
    sortable:'true'
  },{
    field:'exersuggtime',
    title:'发布时间',
    sortable:'true'
  },{
    field:'temp_managerid',
    title:'管理员ID',
    sortable:'true'
  },{
    field:'healthknowledgeremarks',
    title:'养生知识备注',
    sortable:'true'
  },{
    field:'temp_healthknowltypeid',
    title:'养生知识类别ID',
    sortable:'true'
  },{
    field:'healthknowledgecode',
    title:'养生知识代码',
    sortable:'true'
  },{
    field:'healthknowledgeflag',
    title:'养生知识标识',
    sortable:'true'
  },{
      field:'temp_picturelocationid',
      title:'图片位置ID',
      sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//常见疾病信息表
$('#commondiseaseTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'commondiseaseid',
    title:'常见疾病ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'temp_commonditypeid',
    title:'常见疾病类别ID',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'commondiname',
    title:'常见疾病名称',
    sortable:'true'
  },{
    field:'diseaseexplain',
    title:'疾病说明',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//体质辨识问卷项目表
$('#identifyissueTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'identifyissueid',
    title:'体质辨识问题ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'temp_physiqueinfoid',
    title:'体质类型ID',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'identifyissuecontent',
    title:'体质辨识问题内容',
    sortable:'true'
  },{
    field:'identifyissueremarks',
    title:'体质辨识问题备注',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//医院信息表
$('#hospitalinfoTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'hospitalid',
    title:'医院ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'hospitalname',
    title:'医院名称',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'hospitalexplain',
    title:'医院简介',
    sortable:'true'
  },{
    field:'temp_locationinfoid',
    title:'位置信息ID',
    sortable:'true'
  },{
    field:'hospitalrank',
    title:'医院级别',
    sortable:'true'
  },{
    field:'temp_adminisareaid',
    title:'行政区划ID',
    sortable:'true'
  },{
      field:'temp_picturelocationid',
      title:'图片位置ID',
      sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//计量单位表
$('#unitattributeTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'unitattributeid',
    title:'计量单位ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'unitattributename',
    title:'计量单位属性名',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'unitlevel',
    title:'单位大小级别',
    sortable:'true'
  },{
    field:'unitname',
    title:'计量单位名',
    sortable:'true'
  },{
    field:'hexadecimal',
    title:'进制',
    sortable:'true'
  },{
    field:'unitremarks',
    title:'计量单位备注',
    sortable:'true'
  },{
    field:'unitattributecode',
    title:'计量单位代码值',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//地理位置信息
$('#locationinfoTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'locationinfoid',
    title:'地理位置ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'locationlongitude',
    title:'地理位置经度',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'locationlatitude',
    title:'地理位置纬度',
    sortable:'true'
  },{
    field:'reallocation',
    title:'具体地理位置',
    sortable:'true'
  },{
    field:'locationremarks',
    title:'地理位置备注',
    sortable:'true'
  },{
    field:'locationprovince',
    title:'所在省',
    sortable:'true'
  },{
    field:'locationcity',
    title:'所在市',
    sortable:'true'
  },{
    field:'locationclassify',
    title:'所在区',
    sortable:'true'
  },{
    field:'locationcounty',
    title:'所在县',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//饮食特征信息
$('#eatingFeature').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'eatingfeatureid',
    title:'饮食特征ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'eatinghabitsdetermine',
    title:'饮食习惯是否合理',
    sortable:'true'
  },{
    field:'temp_userid',
    title:'用户ID',
    sortable:'true',
    visible:false
  },{
    field:'eatinghabitanalysis',
    title:'饮食习惯分析结果',
    sortable:'true'
  },{
    field:'averageenergyintake',
    title:'平均每天能量摄入',
    sortable:'true'
  },{
    field:'moistureintakeunit',
    title:'能量摄入单位'
  },{
    field:'averageproteinintake',
    title:'平均每天蛋白质摄入',
    sortable:'true'
  },{
    field:'proteinintakeunit',
    title:'蛋白质摄入单位',
    sortable:'true'
  },{
    field:'averagefatintake',
    title:'平均每天脂肪摄入',
    sortable:'true'
  },{
    field:'fatintakeunit',
    title:'脂肪摄入单位',
    sortable:'true'
  },{
    field:'averagefiberintake',
    title:'平均每天膳食纤维摄入',
    sortable:'true'
  },{
    field:'fiberintakeunit',
    title:'膳食纤维摄入单位',
    sortable:'true'
  },{
    field:'averagecarbohydrateintake',
    title:'平均每天碳水化合物摄入',
    sortable:'true'
  },{
    field:'carbohydrateintakeunit',
    title:'碳水化合物摄入单位',
    sortable:'true'
  },{
    field:'averagevitaminaintake',
    title:'平均每天维生素A摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitaminaintakeunit',
    title:'维生素A摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagevitaminb1intake',
    title:'平均每天维生素B1摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb1intakeunit',
    title:'维生素B1摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagevitaminb2intake',
    title:'平均每天维生素B2摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb2intakeunit',
    title:'维生素B2摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagevitaminb6intake',
    title:'平均每天维生素B6摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb6intakeunit',
    title:'维生素B6摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagevitaminb12intake',
    title:'平均每天维生素B12摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb12intakeunit',
    title:'维生素B12摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagevitamincintake',
    title:'平均每天维生素C摄入',
    sortable:'true'
  },{
    field:'vitamincintakeunit',
    title:'维生素C摄入单位',
    sortable:'true'
  },{
    field:'averagevitamindintake',
    title:'平均每天维生素D摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitamindintakeunit',
    title:'维生素D摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagevitamineintake',
    title:'平均每天维生素E摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitamineintakeunit',
    title:'维生素E摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagenicotinicacidintake',
    title:"平均每天烟酸摄入",
    sortable:'true',
    visible:false
  },{
    field:'nicotinicacidintakeunit',
    title:"烟酸摄入单位",
    sortable:'true',
    visible:false
  },{
    field:'averagefolateintake',
    title:'平均每天叶酸摄入',
    sortable:'true',
    visible:false
  },{
    field:'folateintakeunit',
    title:'叶酸摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagesodiumintake',
    title:"平均每天纳摄入",
    sortable:'true',
    visible:false
  },{
    field:'sodiumintakeunit',
    title:"纳摄入单位",
    sortable:'true',
    visible:false
  },{
    field:'averagecalciumintake',
    title:'平均每天钙摄入',
    sortable:'true',
    visible:false
  },{
    field:'calciumintakeunit',
    title:'钙摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averageironintake',
    title:'平均每天铁摄入',
    sortable:'true',
    visible:false
    },{
    field:'ironintakeunit',
    title:'铁摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagepotassiumintake',
    title:'平均每天钾摄入',
    sortable:'true',
    visible:false
  },{
    field:'potassiumintakeunit',
    title:'钾摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagezincintake',
    title:'平均每天锌摄入',
    sortable:'true',
    visible:false
  },{
    field:'zincintakeunit',
    title:'锌摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagemangaessintake',
    title:'平均每天镁摄入',
    sortable:'true',
    visible:false
  },{
    field:'mangaessintakeunit',
    title:'镁摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagecopperintake',
    title:'平均每天铜摄入',
    sortable:'true',
    visible:false
  },{
    field:'copperintakeunit',
    title:'铜摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagechromiumintake',
    title:'平均每天铬摄入',
    sortable:'true',
    visible:false
  },{
    field:'chromiumintakeunit',
    title:'铬摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagemangaessintake',
    title:'平均每天锰摄入',
    sortable:'true',
    visible:false
  },{
    field:'mangaessintakeunit',
    title:'锰摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagemolybdenumintake',
    title:'平均每天钴摄入',
    sortable:'true',
    visible:false
  },{
    field:'molybdenumintakeunit',
    title:'钴摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averageiodineintake',
    title:'平均每天碘摄入',
    sortable:'true',
    visible:false
  },{
    field:'iodineintakeunit',
    title:'碘摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagephosphusintake',
    title:'平均每天磷摄入',
    sortable:'true',
    visible:false
  },{
    field:'phosphusintakeunit',
    title:'磷摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averageseleniumintake',
    title:'平均每天硒摄入',
    sortable:'true',
    visible:false
  },{
    field:'seleniumintakeunit',
    title:'硒摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagefluorineintake',
    title:'平均每天氟摄入',
    sortable:'true',
    visible:false
  },{
    field:'fluorineintakeunit',
    title:'氟摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagechokesterolintake',
    title:'平均每天胆固醇摄入',
    sortable:'true',
    visible:false
  },{
    field:'chokesterolintakeunit',
    title:'胆固醇摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagesaturatedintake',
    title:'平均每天饱和脂肪酸摄入',
    sortable:'true'
  },{
    field:'saturatedintakeunit',
    title:'饱和脂肪酸摄入单位',
    sortable:'true'
  },{
    field:'acidregurgitationintake',
    title:'平均每天泛酸摄入',
    sortable:'true',
    visible:false
  },{
    field:'acidregurgitationintakeunit',
    title:'泛酸摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagebiotinintake',
    title:'平均每天生物酸摄入',
    sortable:'true',
    visible:false
  },{
    field:'biotinintakeunit',
    title:'生物酸摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'averagecholineintake',
    title:'平均每天胆碱摄入',
    sortable:'true',
    visible:false
  },{
    field:'cholineintakeunit',
    title:'胆碱摄入单位',
    sortable:'true',
    visible:false
  },{
    field:'temp_amountstdid',
    title:'平均量计算标准id',
    sortable:'true',
    visible:false
  },{
    field:'latelymaintentime',
    title:'最近维护时间',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
  //sidePagination:'server',
  //queryParamsType:'limit',
  //responseHandler:responseHandler,
  //queryParams:queryParams
});

//体质辨识选项表
$('#identifychoiceTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'identifychoiceid',
    title:'题目选项ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'identifychoicevalue',
    title:'题目分数值',
    sortable:'true',
    sorter:'starsSorter'
  },{
    field:'scriptdescribe',
    title:'定性描述',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//用药信息表
$('#medicineuseinfoTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
      field:'medicineuseinfoid',
      title:'用药信息ID',
      formatter:'nameFormatter',
      sortable:'true',
      visible:false
  },{
    field:'medicineusetype',
    title:'药品类型',
    formatter:'nameFormatter',
    sortable:'true'
  },{
    field:'medicineusename',
    title:'药品名称',
    sortable:'true'
  },{
    field:'medicineusedose',
    title:'用药剂量',
    sortable:'true'
  },{
    field:'medicineuseremarks',
    title:'用药备注',
    sortable:'true'
  },{
    field:'temp_tcmexaminationid',
    title:'中医诊疗记录ID',
    sortable:'true'
  },{
    field:'temp_unitattributeid',
    title:'计量单位ID',
    sortable:'true'
  },{
    field:'prescriptiontag',
    title:'方剂标识',
    sortable:'true'
   },{
    field:'temp_chinesemedicineid',
    title:'药品ID',
    sortable:'true'
  },{
    field:'temp_medicineprescriptionid',
    title:'中药方剂ID',
    sortable:'true'
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
});

//设备参数代码表
$('#parametercodeTable').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
      field:'deviceparacodeid',
      title:'设备参数代码ID',
      formatter:'nameFormatter',
      sortable:'true',
      visible:false
  },{
    field:'parametercode',
    title:'设备参数代码',
    sortable:'true'
  },{
    field:'parametername',
    title:'设备参数名称',
    sortable:'true'
  },{
    field:'parametermean',
    title:'设备参数含义',
    sortable:'true'
  }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//设备参数映射表
$('#parametermappTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'deviceparamappid',
        title:'设备参数映射ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_intelligentdeviceid',
        title:'设备ID',
        sortable:'true'
    },{
        field:'temp_deviceparacodeid',
        title:'设备参数代码ID',
        sortable:'true'
    },{
        field:'deviceparavalue',
        title:'设备参数值',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//设备数据采集代码表
$('#dataacquisitionTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'acquiredataid',
        title:'采集数据ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'acquiredataname',
        title:'采集数据名',
        sortable:'true'
    },{
        field:'acquiredataexplain',
        title:'采集数据说明',
        sortable:'true'
    },{
        field:'temp_acqdatatypeid',
        title:'数据类型ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//养生知识类别表
$('#healthknowledgetypeTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'healthknowltypeid',
        title:'养生知识类别ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'healthknowltypename',
        title:'养生知识类别名',
        sortable:'true'
    },{
        field:'healthknowltypecode',
        title:'养生知识类别代码',
        sortable:'true'
    },{
        field:'healthkonwltypeexp',
        title:'养生知识分类说明',
        sortable:'true'
    },{
        field:'healthkonwltyperemarks',
        title:'养生知识分类备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//健康建议类别表
$('#healthsuggtypeTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'healthsuggtypeid',
        title:'健康建议类别ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'healthsuggtypename',
        title:'健康建议类别名',
        sortable:'true'
    },{
        field:'healthsuggtypecode',
        title:'健康建议类别代码',
        sortable:'true'
    },{
        field:'suggclassifyexpla',
        title:'建议分类说明',
        sortable:'true'
    },{
        field:'healthsuggtyperemarks',
        title:'健康建议分类备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//健康建议表
$('#healthsuggestionsTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'healthsuggestid',
        title:'健康建议ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'healthsuggesttitle',
        title:'健康建议主题',
        sortable:'true'
    },{
        field:'healthsuggestcontent',
        title:'健康建议内容',
        sortable:'true'
    },{
        field:'healthsuggestremarks',
        title:'健康建议备注',
        sortable:'true'
    },{
        field:'temp_healthsuggtypeid',
        title:'健康建议类别ID',
        sortable:'true'
    },{
        field:'healthsuggestflag',
        title:'健康建议标识',
        sortable:'true'
    },{
        field:'healthsuggestcode',
        title:'健康建议代码',
        sortable:'true'
    },{
        field:'temp_picturelocationid',
        title:'图片位置ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//健康指标信息表
$('#healthindicatorinfoTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'healthindicatorid',
        title:'健康指标信息id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'healthindicatorname',
        title:'健康指标名称',
        sortable:'true'
    },{
        field:'healthindicatorvalue',
        title:'健康指标值',
        sortable:'true'
    },{
        field:'healthindicatorchange',
        title:'健康指标变化趋势',
        sortable:'true'
    },{
        field:'indicatorchangeexplain',
        title:'指标变化趋势说明',
        sortable:'true'
    },{
        field:'temp_healthtrendid',
        title:'健康趋势ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//健康趋势分析记录表
$('#healthtrendrecordsTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'healthtrendid',
        title:'健康趋势ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'heaanalysistitle',
        title:'健康分析主题',
        sortable:'true'
    },{
        field:'healthanalysistime',
        title:'健康分析时间',
        sortable:'true'
    },{
        field:'healthtrendanalysiresult',
        title:'健康趋势总分析结果',
        sortable:'true'
    },{
        field:'healthknowledgeid',
        title:'养生知识ID',
        sortable:'true'
    },{
        field:'healthtrendanalysisremarks',
        title:'健康趋势分析备注',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//用户预警映射表
$('#userhealthwarningmappTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'userhealthwarningid',
        title:'用户预警ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'healthwarningcontent',
        title:'健康预警内容',
        sortable:'true',
        visible:false
    },{
        field:'healthwarningtime',
        title:'健康预警时间',
        sortable:'true'
    },{
        field:'healthwarningreason',
        title:'健康预警原因',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'healthwarningremarks',
        title:'健康预警备注',
        sortable:'true'
    },{
        field:'temp_healthwarningmessid',
        title:'健康预警信息ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

////个性化养生信息表
//$('#personalizedhealthinfoTable').bootstrapTable({
//    columns:[{
//        field:'state',
//        checkbox:"true"
//    },{
//        field:'personalizedhealthid',
//        title:'个性化养生信息id',
//        formatter:'nameFormatter',
//        sortable:'true'
//    },{
//        field:'temp_userid',
//        title:'用户ID',
//        sortable:'true'
//    },{
//        field:'personalizedhealthtitle',
//        title:'个性化养生主题',
//        sortable:'true'
//    },{
//        field:'personalizedhealthcontent',
//        title:'个性化养生内容',
//        sortable:'true'
//    },{
//        field:'personalizedhealthremarks',
//        title:'个性化养生备注',
//        sortable:'true'
//    },{
//        field:'temp_healthknowltypeid',
//        title:'养生知识类别ID',
//        sortable:'true'
//     },{
//        field:'personalizedhealthflag',
//        title:'养生信息标识',
//        sortable:'true'
//    }]
//});

//用户养生知识映射表
$('#userknowledgemappTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'userknowledgemappid',
        title:'用户养生知识映射ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'healthknowledgecontent',
        title:'养生知识内容',
        sortable:'true'
    },{
        field:'temp_healthknowledgeid',
        title:'养生知识id',
        sortable:'true'
    },{
        field:'healthknowledgereason',
        title:'养生知识生成原因',
        sortable:'true'
     },{
        field:'healthknowledgetime',
        title:'养生知识生成时间',
        sortable:'true'
    },{
        field:'healthknowledgeremarks',
        title:'养生知识生成备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//常见疾病类别表
$('#commondiseasetypeTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'commonditypeid',
        title:'常见疾病类别ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'commonditypename',
        title:'常见疾病类别名',
        sortable:'true'
    },{
        field:'commonditypecode',
        title:'常见疾病类别代码',
        sortable:'true'
    },{
        field:'diclassifyexplain',
        title:'常见疾病分类说明',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//体质信息表
$('#phyciqueinfoTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'physiqueinfoid',
        title:'体质信息ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'tablescoreheight',
        title:'量表辨识总分上限',
        sortable:'true'
    },{
        field:'tablescorelow',
        title:'量表辨识总分下限',
        sortable:'true'
    },{
        field:'switchscoreheight',
        title:'转换得分上限',
        sortable:'true'
    },{
        field:'switchscorelow',
        title:'转换得分下限',
        sortable:'true'
    },{
        field:'generacharacter',
        title:'总体特征',
        sortable:'true'
    },{
        field:'shapefeature',
        title:'形体特征',
        sortable:'true'
    },{
        field:'commonmanifest',
        title:'常见表现',
        sortable:'true'
    },{
        field:'mentalcharacter',
        title:'心理特征',
        sortable:'true'
    },{
        field:'incidencetendency',
        title:'发病倾向',
        sortable:'true'
    },{
        field:'adaptivecapacity',
        title:'环境适应能力',
        sortable:'true'
          },{
        field:'physicaltypename',
        title:'体质类型名',
        sortable:'true'
    },{
        field:'physicaltypecode',
        title:'体质类型代码',
        sortable:'true'
    },{
        field:'temp_picturelocationid',
        title:'图片位置ID',
        sortable:'true'
    },{
        field:'adjustmethod',
        title:'调节方法',
        sortable:'true'
    },{
        field:'mutiplepeople',
        title:'多发人群',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//体质疾病关系表
$('#identifydiseaserelTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'identifydirelid',
        title:'体质疾病关系ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_physiqueinfoid',
        title:'体质类型ID',
        sortable:'true'
    },{
        field:'temp_commondiseaseid',
        title:'常见疾病ID',
        sortable:'true'
    },{
        field:'identifydirelexplain',
        title:'关系说明',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//医生专长信息表
$('#doctorexpertiseinfoTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'doctorexpertiseid',
        title:'医生专长ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'doctorexpertisetitle',
        title:'医生专长主题',
        sortable:'true'
    },{
        field:'doctorexpertiseexplain',
        title:'医生专长简介',
        sortable:'true'
    },{
        field:'temp_doctorexptypeid',
        title:'医生专长类型ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//医生专长分类代码表
$('#doctorexpertisetypeTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'doctorexptypeid',
        title:'医生专长类型ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'doctorexptypename',
        title:'医生专长类型名',
        sortable:'true'
    },{
        field:'doctorexptypecode',
        title:'医生专长代码',
        sortable:'true'
    },{
        field:'doctorexptypeexplain',
        title:'医生专长分类说明',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//医院医生关系表
$('#hospitaldoctorrelTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'hospitaldocrelid',
        title:'医院医生关系ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_hospitalid',
        title:'医院ID',
        sortable:'true'
    },{
        field:'temp_doctorid',
        title:'医生ID',
        sortable:'true'
    },{
        field:'temp_hospitalofficeid',
        title:'医院科室ID',
        sortable:'true'
    },{
        field:'workduty',
        title:'担任职务',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//医院科室信息表
$('#hospitalofficesinfoTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'hospitalofficeid',
        title:'医院科室ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'hospitalofficename',
        title:'医院科室名',
        sortable:'true'
    },{
        field:'hospitalofficeexplain',
        title:'医院科室简介',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
});

//行政区划代码表
$('#adminisareaTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'adminisareaid',
        title:'行政区划ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'adminisareacode',
        title:'行政区划代码',
        sortable:'true'
    },{
        field:'adminisareaprovince',
        title:'行政区划省',
        sortable:'true'
    },{
        field:'adminisareacity',
        title:'行政区划市',
        sortable:'true'
    },{
        field:'adminisareacounty',
        title:'行政区划区/县',
        sortable:'true'
    },{
        field:'adminisarearemarks',
        title:'行政区划备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true

});

//饮食状况分析表
$('#EatingAnalysis').bootstrapTable({
  columns:[{
    field:'state',
    checkbox:"true"
  },{
    field:'eatinganalysisid',
    title:'饮食状况分析ID',
    formatter:'nameFormatter',
    sortable:'true',
    visible:false
  },{
    field:'energyintake',
    title:'能量摄入',
    sortable:'true'
  },{
    field:'moistureunit',
    title:'能量单位'
  },{
    field:'proteinintake',
    title:'蛋白质摄入',
    sortable:'true'
  },{
    field:'proteinunit',
    title:'蛋白质单位',
    sortable:'true'
  },{
    field:'fatintake',
    title:'脂肪摄入',
    sortable:'true'
  },{
    field:'fatunit',
    title:'脂肪单位',
    sortable:'true'
  },{
    field:'fiberintake',
    title:'膳食纤维摄入',
    sortable:'true'
  },{
    field:'fiberunit',
    title:'膳食纤维单位',
    sortable:'true'
  },{
    field:'carbohydrateintake',
    title:'碳水化合物摄入',
    sortable:'true'
  },{
    field:'carbohydrateunit',
    title:'碳水化合物单位',
    sortable:'true'
  },{
    field:'vitaminaintake',
    title:'维生素A摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitaminaunit',
    title:'维生素A单位',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb1intake',
    title:'维生素B1摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb1unit',
    title:'维生素B1单位',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb2intake',
    title:'维生素B2摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb2unit',
    title:'维生素B2单位',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb6intake',
    title:'维生素B6摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb6unit',
    title:'维生素B6单位',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb12intake',
    title:'维生素B12摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitaminb12unit',
    title:'维生素B12单位',
    sortable:'true',
    visible:false
  },{
    field:'vitamincintake',
    title:'维生素C摄入',
    sortable:'true'
  },{
    field:'vitamincunit',
    title:'维生素C单位',
    sortable:'true'
  },{
    field:'vitamindintake',
    title:'维生素D摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitamindunit',
    title:'维生素D单位',
    sortable:'true',
    visible:false
  },{
    field:'vitamineintake',
    title:'维生素E摄入',
    sortable:'true',
    visible:false
  },{
    field:'vitamineunit',
    title:'维生素E单位',
    sortable:'true',
    visible:false
  },{
    field:'nicotinicacidintake',
    title:"烟酸摄入",
    sortable:'true',
    visible:false
  },{
    field:'nicotinicacidunit',
    title:"烟酸单位",
    sortable:'true',
    visible:false
  },{
    field:'folateintake',
    title:'叶酸摄入',
    sortable:'true',
    visible:false
  },{
    field:'folateunit',
    title:'叶酸单位',
    sortable:'true',
    visible:false
  },{
    field:'sodiumintake',
    title:"纳摄入",
    sortable:'true',
    visible:false
   },{
    field:'sodiumunit',
    title:"纳单位",
    sortable:'true',
    visible:false
  },{
    field:'calciumintake',
    title:'钙摄入',
    sortable:'true',
    visible:false
  },{
    field:'calciumunit',
    title:'钙单位',
    sortable:'true',
    visible:false
  },{
    field:'ironintake',
    title:'铁摄入',
    sortable:'true',
    visible:false
  },{
    field:'ironunit',
    title:'铁单位',
    sortable:'true',
    visible:false
  },{
    field:'potassiumintake',
    title:'钾摄入',
    sortable:'true',
    visible:false
  },{
    field:'potassiumunit',
    title:'钾单位',
    sortable:'true',
    visible:false
  },{
    field:'zincintake',
    title:'锌摄入',
    sortable:'true',
    visible:false
  },{
    field:'zincunit',
    title:'锌单位',
    sortable:'true',
    visible:false
  },{
    field:'mangaessintake',
    title:'镁摄入',
    sortable:'true',
    visible:false
  },{
    field:'mangaessunit',
    title:'镁单位',
    sortable:'true',
    visible:false
  },{
    field:'copperintake',
    title:'铜摄入',
    sortable:'true',
    visible:false
  },{
    field:'copperunit',
    title:'铜单位',
    sortable:'true',
    visible:false
  },{
    field:'chromiumintake',
    title:'铬摄入',
    sortable:'true',
    visible:false
  },{
    field:'chromiumunit',
    title:'铬单位',
    sortable:'true',
    visible:false
  },{
    field:'mangaessintake',
    title:'锰摄入',
    sortable:'true',
    visible:false
  },{
    field:'mangaessunit',
    title:'锰单位',
    sortable:'true',
    visible:false
  },{
    field:'molybdenumintake',
    title:'钴摄入',
    sortable:'true',
    visible:false
  },{
    field:'molybdenumunit',
    title:'钴单位',
    sortable:'true',
    visible:false
  },{
    field:'iodineintake',
    title:'碘摄入',
    sortable:'true',
    visible:false
  },{
    field:'iodineunit',
    title:'碘单位',
    sortable:'true',
    visible:false
  },{
    field:'phosphusintake',
    title:'磷摄入',
    sortable:'true',
    visible:false
  },{
    field:'phosphusunit',
    title:'磷单位',
    sortable:'true',
    visible:false
  },{
    field:'seleniumintake',
    title:'硒摄入',
    sortable:'true',
    visible:false
  },{
    field:'seleniumunit',
    title:'硒单位',
    sortable:'true',
    visible:false
  },{
    field:'fluorineintake',
    title:'氟摄入',
    sortable:'true',
    visible:false
  },{
    field:'fluorineunit',
    title:'氟单位',
    sortable:'true',
    visible:false
  },{
    field:'chokesterolintake',
    title:'胆固醇摄入',
    sortable:'true',
    visible:false
  },{
    field:'chokesterolunit',
    title:'胆固醇单位',
    sortable:'true',
    visible:false
  },{
    field:'saturatedintake',
    title:'饱和脂肪酸摄入',
    sortable:'true',
    visible:false
  },{
    field:'saturatedunit',
    title:'饱和脂肪酸单位',
    sortable:'true',
    visible:false
  },{
    field:'acidregurgitationintake',
    title:'泛酸摄入',
    sortable:'true',
    visible:false
  },{
    field:'acidregurgitationunit',
    title:'泛酸单位',
    sortable:'true',
    visible:false
  },{
    field:'biotinintake',
    title:'生物酸摄入',
    sortable:'true',
    visible:false
  },{
    field:'biotinunit',
    title:'生物酸单位',
    sortable:'true',
    visible:false
  },{
    field:'cholineintake',
    title:'胆碱摄入',
    sortable:'true',
    visible:false
  },{
    field:'cholineunit',
    title:'胆碱单位',
    sortable:'true',
    visible:false
  },{
    field:'temp_eatingrecordid',
    title:'饮食信息记录ID',
    sortable:'true',
    visible:false
  }],
  striped:true,
  pagination:true,
  pageList:[10,20,50,100,500],
  pageSize:10,
  pageNumber:1,
  clickToSelect:true,
  smartDisplay:true
  //sidePagination:'server',
  //queryParamsType:'limit',
  //responseHandler:function(res) {
  //  /*var rest = $.parseJSON(res.results);*/
  //  /*alert(res.results[1].username);*/
  //  return {
  //    rows:res.results,
  //    total:res.count
  //  }
  //},
  //queryParams:function queryParams(params){   //limit 是pageSize 会根据pagelist中选中的项来变 offset时条目的偏移量
  //  return {"limit":params.limit,
  //          "page":(params.offset/params.limit)+1
  //  };
  //}
});

//睡眠信息记录表
$('#sleepinforecordsTable').bootstrapTable({
   columns:[{
        field:'state',
        checkbox:"true"
   },{
      field:'sleeprecordid',
      title:'睡眠信息记录ID',
      formatter:'nameFormatter',
      sortable:'true',
      visible:false
   },{
       field:'airhumidity',
       title:'空气湿度相对比',
       sortable:'true'
   },{
       field:'ambienttemperature',
       title:'环境温度',
       sortable:'true'
   },{
       field:'ambientnoise',
       title:'环境噪声',
       sortable:'true'
   },{
       field:'sleepbegin',
       title:'开始睡眠时间',
       sortable:'true'
   },{
       field:'sleepover',
       title:'结束睡眠时间',
       sortable:'true'
   },{
       field:'deepsleeptime',
       title:'深睡时间',
       sortable:'true'
   },{
       field:'shallowsleeptime',
       title:'浅睡时间',
       sortable:'true'
   },{
       field:'sleepremarks',
       title:'睡眠情况备注',
       sortable:'true'
   },{
       field:'sleeprecorduptime',
       title:'睡眠记录上传时间',
       sortable:'true'
   },{
       field:'temp_userid',
       title:'用户ID',
       sortable:'true'
   },{
       field:'temp_locationinfoid',
       title:'位置信息ID',
       sortable:'true'
   },{
       field:'waketimes',
       title:'醒来次数',
       sortable:'true'
   },{
       field:'temp_intelligentdeviceid',
       title:'设备ID',
       sortable:'true'
   },{
       field:'intelligentdevicecode',
       title:'设备代码',
       sortable:'true'
   },{
       field:'sleepuploadflag',
       title:'一次上传标识',
       sortable:'true'
   },{
       field:'awaketime',
       title:'醒来时间',
       sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//用户睡眠特征信息表
$('#usersleepfeatureTable').bootstrapTable({
   columns:[{
        field:'state',
        checkbox:"true"
    },{
       field:'sleepfeatureid',
       title:'睡眠特征ID',
       formatter:'nameFormatter',
       sortable:'true',
       visible:false
    },{
        field:'airhumidity',
        title:'空气湿度相对比',
        sortable:'true'
    },{
        field:'ambienttemperature',
        title:'环境温度',
        sortable:'true'
    },{
        field:'ambientnoise',
        title:'环境噪声',
        sortable:'true'
    },{
        field:'bedtimehabits',
        title:'睡前习惯',
        sortable:'true'
    },{
        field:'goodbedtimehabits',
        title:'睡前习惯是否健康',
        sortable:'true'
    },{
        field:'siestahabit',
        title:'是否有午睡习惯',
        sortable:'true'
    },{
        field:'averagesleeptime',
        title:'24小时平均睡眠时长',
        sortable:'true'
    },{
        field:'sleephabitdetermination',
        title:'睡眠习惯是否合理',
        sortable:'true'
    },{
        field:'sleepreindex',
        title:'睡眠指数',
        sortable:'true'
    },{
        field:'sleephabitanalysis',
        title:'睡眠习惯分析结果',
        sortable:'true'
    },{
        field:'temp_locationinfoid',
        title:'位置信息ID',
        sortable:'true'
    },{
        field:'latelymaintentime',
        title:'最近维护时间',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//睡眠偏好记录表
$('#sleeppreferRecords').bootstrapTable({
  columns:[{
        field:'state',
        checkbox:"true"
    },{
      field:'sleeppreferid',
      title:'睡眠偏好ID',
      formatter:'nameFormatter',
      sortable:'true',
      visible:false
    },{
      field:'prefersleepbeginat',
      title:'偏好睡眠开始时间',
      sortable:'true'
    },{
        field:'prefersleepoverat',
        title:'偏好睡眠结束时间',
        sortable:'true'
    },{
        field:'temp_locationinfoid',
        title:'位置信息ID',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'sleepfeatureaddtime',
        title:'增加时间',
        sortable:'true'
    },{
        field:'currentlypreferflag',
        title:'当前偏好标识',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//运动信息记录表
$('#sportinfoRecords').bootstrapTable({
  columns:[{
        field:'state',
        checkbox:"true"
    },{
      field:'sportrecordid',
      title:'运动信息记录ID',
      formatter:'nameFormatter',
      sortableL:true,
      visible:false
    },{
        field:'walkstepnumber',
        title:'走路步数',
        sortable:'true'
    },{
        field:'runstepnumber',
        title:'跑步步数',
        sortable:'true'
      },{
        field:'walkdistance',
        title:'走路距离',
        sortable:'true'
    },{
        field:'rundistance',
        title:'跑步距离',
        sortable:'true'
    },{
        field:'calorieconsumption',
        title:'卡路里消耗量',
        sortable:'true'
    },{
        field:'sportbegintime',
        title:'记录开始时间',
        sortable:'true'
    },{
        field:'sportovertime',
        title:'记录结束时间',
        sortable:'true'
    },{
        field:'sportrecorduptime',
        title:'记录上传时间',
        sortable:'true'
    },{
        field:'sportinforemarks',
        title:'运动信息备注',
        sortable:'true'
    },{
        field:'sportanalysis',
        title:'运动情况分析',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'temp_locationinfoid',
        title:'位置信息ID',
        sortable:'true'
    },{
        field:'sport_mode',
        title:'运动模式',
        sortable:'true'
    },{
        field:'temp_intelligentdeviceid',
        title:'设备ID',
        sortable:'true'
    },{
        field:'intelligentdevicecode',
        title:'设备代码',
        sortable:'true'
    },{
        field:'uploadflag',
        title:'一次上传标识',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//运动偏好记录表
$('#exercisepreferrecords').bootstrapTable({
  columns:[{
        field:'state',
        checkbox:"true"
    },{
      field:'exercisepreferenceid',
      title:'运动偏好ID',
      formatter:'nameFormatter',
      sortable:'true',
      visible:false
    },{
        field:'exercisetype',
        title:'运动类型',
        sortable:'true'
    },{
        field:'exercisename',
        title:'运动名称',
        sortable:'true'
    },{
        field:'exercisedescribe',
        title:'运动描述',
        sortable:'true'
    },{
        field:'temp_exerciseid',
        title:'运动实体ID',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'temp_locationinfoid',
        title:'位置信息ID',
        sortable:'true'
    },{
        field:'additemtime',
        title:'增加时间',
        sortable:'true'
    },{
        field:'currentlypreferflag',
        title:'当前偏好标识',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//运动实体信息表
$('#exerciseinfoTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'exerciseid',
        title:'运动实体ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'exercisename',
        title:'运动名称',
        sortable:'true'
    },{
        field:'exercisetypename',
        title:'运动类型名',
        sortable:'true'
    },{
        field:'energywaste',
        title:'能量消耗量',
        sortable:'true'
    },{
        field:'exercisetip',
        title:'运动提醒',
        sortable:'true'
    },{
        field:'exerciseaffect',
        title:'运动作用介绍',
        sortable:'true'
    },{
        field:'temp_picturelocationid',
        title:'图片位置ID',
        sortable:'true'
    },{
        field:'temp_exercisetypeid',
        title:'运动类型ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});


//西医诊疗记录表
$('#wTreatmentRecordid').bootstrapTable({
  columns:[{
        field:'state',
        checkbox:"true"
    },{
      field:'wtreatmentrecordid',
      title:'西医诊疗记录ID',
      formatter:'nameFormatter',
      sortable:'true',
      visible:false
    },{
        field:'temp_westmedicineexamid',
        title:'西医检查项目ID',
        sortable:'true'
    },{
        field:'westexamresultval',
        title:'检查结果值',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//西医体检项目表
$('#wesmedicineexamitem').bootstrapTable({
  columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'westmedicineexamid',
        title:'西医检查项目ID',
        formatter:'nameFormatter',
        visible:false
    },{
        field:'westmedicineitemname',
        title:'西医检查项目名称',
        sortable:'true'
    },{
        field:'wesmedicineitemexpl',
        title:'西医检查项目简介',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});


//病史记录表
$('#medicineHistoryRecords').bootstrapTable({
  columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'medicalhistoryrecordid',
        title:'病史记录ID',
        formatter:'nameFormatter',
        visible:false
    },{
        field:'diseasetype',
        title:'疾病类型',
        sortable:'true'
    },{
        field:'diseasename',
        title:'疾病名称',
        sortable:'true'
    },{
        field:'diseaseseverity',
        title:'疾病严重性',
        sortable:'true'
    },{
        field:'treatmentinfo',
        title:'治疗相关信息',
        sortable:'true'
    },{
        field:'treatmentdoctor',
        title:'诊断医生',
        sortable:'true'
    },{
        field:'treatmentunit',
        title:'诊断单位',
        sortable:'true'
    },{
        field:'treatmentlocation',
        title:'诊断地点',
        sortable:'true'
    },{
        field:'treatmentresult',
        title:'诊断结果',
        sortable:'true'
    },{
        field:'recoverydegree',
        title:'康复程度',
        sortable:'true'
    },{
        field:'treatmenttime',
        title:'诊疗时间',
        sortable:'true'
    },{
        field:'treatmentremarks',
        title:'诊断备注',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true',
        visible:false
     },{
        field:'temp_doctorid',
        title:'医生ID',
        sortable:'true',
        visible:false
    },{
        field:'temp_medicineuseinfoid',
        title:'用药信息ID',
        sortable:'true',
        visible:false
    },{
        field:'temp_commondiseaseid',
        title:'常见疾病ID',
        sortable:'true',
        visible:false
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//体质辨识结果记录表
$('#identifyResult').bootstrapTable({
  columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'identifyresultid',
        title:'体质辨识结果ID',
        formatter:'nameFormatter',
        visible:false
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'

    },{
        field:'temp_physiqueinfoid',
        title:'体质信息ID',
        sortable:'true'
    },{
        field:'constituteidentifytime',
        title:'体质辨识时间',
        sortable:'true'
    },{
        field:'constituteidentifyremarks',
        title:'体质辨识备注',
        sortable:'true'
    },{
        field:'constituteidentifyresult',
        title:'体质辨识结果',
        sortable:'true'
    },{
        field:'constituteidentifyflag',
        title:'一次辨识标识',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//采集数据分类表
$('#dataacquiretypeTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'acqdatatypeid',
        title:'数据类型ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'acqdatatypename',
        title:'采集数据类型名',
        sortable:'true'
    },{
        field:'acqdatatypeexplain',
        title:'采集数据类型说明',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});


//手机使用偏好记录表
$('#phonepreferuserecordsTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'phonepreferuseid',
        title:'手机使用偏好ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'offenusebeginat',
        title:'最频繁使用开始时间段',
        sortable:'true'
    },{
        field:'oftenuseovertime',
        title:'最频繁使用结束时间',
        sortable:'true'
    },{
        field:'temp_locationinfoid',
        title:'位置信息ID',
        sortable:'true'
    },{
        field:'temp-appinfoid',
        title:'应用信息ID',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'temp_amountstdid',
        title:'平均量计算标准ID',
        sortable:'true'
    },{
        field:'additemtime',
        title:'增加时间',
        sortable:'true'
    },{
        field:'currentlypreferflag',
        title:'平均量计算标准ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//手机应用信息表
$('#phoneappinfoTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'phoneappinfoid',
        title:'应用信息ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'apptype',
        title:'应用种类',
        sortable:'true'
    },{
        field:'appname',
        title:'应用名称',
        sortable:'true'
    },{
        field:'apptag',
        title:'应用标识',
        sortable:'true'
    },{
        field:'appotherinfo',
        title:'应用其他信息',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//手机监控特征信息表
$('#phoneinfoTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'phoneinfoid',
        title:'手机信息ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'phoneuniqunum',
        title:'手机唯一标识',
        sortable:'true'
    },{
        field:'phonenum',
        title:'手机号码',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//手机监控记录表
$('#phonemonitorrecordsTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'phoneappmonitorrecordid',
        title:'手机应用监控记录ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_appinfoid',
        title:'应用信息ID',
        sortable:'true'
    },{
        field:'appopentime',
        title:'应用打开时间',
        sortable:'true'
    },{
        field:'appclosetime',
        title:'应用关闭时间',
        sortable:'true'
    },{
        field:'appusetime',
        title:'应用使用时长',
        sortable:'true'
    },{
        field:'temp_locationinfoid',
        title:'位置信息ID',
        sortable:'true'
    },{
        field:'temp_phoneinfoid',
        title:'手机信息id',
        sortable:'true'
    },{
        field:'recordproducttime',
        title:'记录生成时间',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//用户运动特征信息表
$('#userexercisefeature').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'exercisefeatureid',
        title:'运动特征ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'height',
        title:'身高',
        sortable:'true'
    },{
        field:'weight',
        title:'体重',
        sortable:'true'
    },{
        field:'steplength',
        title:'行走步长',
        sortable:'true'
    },{
        field:'runlength',
        title:'跑步步长',
        sortable:'true'
    },{
        field:'standardweight',
        title:'标准体重',
        sortable:'true'
    },{
        field:'datauptime',
        title:'数据上传时间',
        sortable:'true'
    },{
        field:'exercisefeatureremarks',
        title:'运动特征备注',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'exercisehabitsdetemine',
        title:'运动习惯是否合理',
        sortable:'true'
    },{
        field:'exercisehabitanalysis',
        title:'运动习惯分析结果',
        sortable:'true'
    },{
        field:'averageexcitetime',
        title:'每天平均运动时长',
        sortable:'true'
    },{
        field:'exercisetypeprefer',
        title:'运动方式偏好',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//点击量统计表
$('#statisticofclickTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'statisticclickid',
        title:'点击量统计id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'clickclass',
        title:'点击类别',
        sortable:'true'
    },{
        field:'clickitem',
        title:'点击项目',
        sortable:'true'
    },{
        field:'praiseyn',
        title:'是否点赞',
        sortable:'true'
    },{
        field:'statisticclickremarks',
        title:'统计量备注',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'ipaddress',
        title:'IP地址',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//用户答题记录表
$('#useranswerrecordsTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'issuescoremappid',
        title:'题目分数映射ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_identifyissueid',
        title:'体质辨识问题ID',
        sortable:'true'
    },{
        field:'temp_identifyscoreid',
        title:'题目选项ID',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'getscore',
        title:'题目得分',
        sortable:'true'
    },{
        field:'answerflag',
        title:'一次答题标识',
        sortable:'true'
    },{
        field:'answertime',
        title:'答题时间',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//用户评论统计表
$('#userreviewstatTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'userreviewstatid',
        title:'用户评论id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'userreviewstatclass',
        title:'用户评论类型id',
        sortable:'true'
    },{
        field:'userreviewstatitem',
        title:'用户评论项目',
        sortable:'true'
    },{
        field:'userreviewstatcontent',
        title:'用户评论内容',
        sortable:'true'
    },{
        field:'userreviewstatremarks',
        title:'用户评论备注',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'

    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//平均量计算标准表
$('#averageamountstdtable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'amountstdid',
        title:'平均量计算标准id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'amountnumofdays',
        title:'计算天数',
        sortable:'true'
    },{
        field:'averageamountremarks',
        title:'平均计算备注',
        sortable:'true'
    },{
        field:'amountbegintime',
        title:'开始计算时间',
        sortable:'true'
    },{
        field:'amountstoptime',
        title:'计算截止时间',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//图片列表
$('#picturelist').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'picturelocationid',
        title:'图片位置ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'originalpicturepath',
        title:'原图路径',
        sortable:'true'
    },{
        field:'smallpicturepath',
        title:'缩略图',
        sortable:'true'
    },{
        field:'pictureclass',
        title:'图片类型',
        sortable:'true'
    },{
        field:'picturename',
        title:'图片名',
        sortable:'true'
    },{
        field:'picturetitle',
        title:'图片主题',
        sortable:'true'
    },{
        field:'pictureusecode',
        title:'图片使用代码值',
        sortable:'true'
    },{
        field:'pictureremarks',
        title:'图片备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});


//我的收藏
$('#mycollection').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'mycollectionid',
        title:'我的收藏id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'collectionclass',
        title:'收藏类别',
        sortable:'true'
    },{
        field:'collectioncode',
        title:'收藏代码值',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'

    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//诊断对象表
$('#tcmdiagnosisobj').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'diagnosisobjid',
        title:'诊断对象id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'diagnosisobjname',
        title:'诊断对象名',
        sortable:'true'
    },{
        field:'diagnosisobjexplain',
        title:'诊断对象说明',
        sortable:'true'
    },{
        field:'temp_diagnosistypeid',
        title:'诊断类型id',
        sortable:'true'

    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//诊断动态记录表
$('#diagnosistrendrecords').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'diatrendid',
        title:'诊断动态记录id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'temp_diagnosisobjid',
        title:'诊断对象id',
        sortable:'true'
    },{
        field:'temp_doctorid',
        title:'医生id',
        sortable:'true'
    },{
        field:'diatrendres',
        title:'诊断结果',
        sortable:'true'
    },{
        field:'diatrendresexplain',
        title:'诊断结果说明',
        sortable:'true'
    },{
        field:'diatrendtime',
        title:'诊断时间',
        sortable:'true'
    },{
        field:'diatrendplacce',
        title:'诊断地点',
        sortable:'true'
    },{
        field:'temp_locationinfoid',
        title:'位置信息ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//常见食物类别表
$('#commonfoodtypeTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'commonfoodtypeid',
        title:'常见食物分类id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'commonfoodtypename',
        title:'常见食物分类名',
        sortable:'true'
    },{
        field:'commonfoodtypecode',
        title:'常见食物分类代码',
        sortable:'true'
    },{
        field:'foodtypeexplain',
        title:'食物分类说明',
        sortable:'true'

    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//套餐食物映射表
$('#setmealfoodmappTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'temp_commonfoodid',
        title:'常见食物id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_setmealinfoid',
        title:'套餐信息id',
        sortable:'true'
    },{
        field:'mealfoodmapremarks',
        title:'套餐食物映射备注',
        sortable:'true'

    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//常见食物信息表
$('#commonfoodinfoTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'commonfoodid',
        title:'常见食物id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'commonfoodname',
        title:'常见食物名称',
        sortable:'true'
    },{
        field:'temp_commonfoodtypeid',
        title:'常见食物分类id',
        sortable:'true'
    },{
        field:'commonfoodexplain',
        title:'常见食物简介',
        sortable:'true'
     },{
        field:'temp_foodnutritionid',
        title:'食物营养成分id',
        sortable:'true'
    },{
        field:'temp_picturelocationid',
        title:'图片位置ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//智能设备采集数据记录表
$('#deviceacquiredatarecordsTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'deviceacquirerecordsid',
        title:'数据采集记录id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_intelligentdeviceid',
        title:'设备id',
        sortable:'true'
    },{
        field:'temp_acquiredataid',
        title:'采集数据id',
        sortable:'true'
    },{
        field:'deviceacquiredatavalue',
        title:'采集数据值',
        sortable:'true'
     },{
        field:'temp_unitattributeid',
        title:'计量单位ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//各类指标标准表
$('#variousindicatorstandardTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'indicatorstandardid',
        title:'指标标准id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'indicatorname',
        title:'指标名称',
        sortable:'true'
    },{
        field:'indicatorcode',
        title:'指标代码',
        sortable:'true'
    },{
        field:'indicatorstatus',
        title:'指标状态',
        sortable:'true'
     },{
        field:'indicatorvalue',
        title:'指标值',
        sortable:'true'
    },{
        field:'indicatorremarks',
        title:'指标备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//各类指标限定表
$('#variousindicatorlimitedTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'indicatorlimitedid',
        title:'指标限定id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_indicatorstandardid',
        title:'指标标准id',
        sortable:'true'
    },{
        field:'indicatorstandardname',
        title:'指标限定属性名',
        sortable:'true'
    },{
        field:'indicatorstandardstatus',
        title:'指标限定状态',
        sortable:'true'
     },{
        field:'indicatorstandardcode',
        title:'指标限定代码',
        sortable:'true'
    },{
        field:'indicatorstandardvalue',
        title:'指标限定值',
        sortable:'true'
        },{
        field:'indicatorstandardstatusleval',
        title:'指标限定状态级别',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});


//指标用户映射表
$('#indicatorusermappTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'indicatorusermappid',
        title:'指标用户映射id',
        formatter:'nameFormatter',
        visible:false
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
     },{
        field:'temp_indicatorstandardid',
        title:'指标标准id',
        sortable:'true'
    },{
        field:'userindicatorvalue',
        title:'用户指标值',
        sortable:'true'
     },{
        field:'userindicatorexp',
        title:'用户指标说明',
        sortable:'true'
    },{
        field:'userindicatorramarks',
        title:'用户指标备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//健康建议限定条件表
$('#healthsuggestlimitedTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'healthsuggestlimitedid',
        title:'健康建议限制条件id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'suggestlimitedattrname',
        title:'建议限制属性名',
        sortable:'true'
     },{
        field:'suggestlimitedstatus',
        title:'建议限制状态',
        sortable:'true'
    },{
        field:'suggestlimitedstatuslevel',
        title:'建议限制状态级别',
        sortable:'true'
     },{
        field:'temp_healthsuggestid',
        title:'健康建议id',
        sortable:'true'
     },{
        field:'suggestlimitedexplain',
        title:'建议限制说明',
        sortable:'true'
    },{
        field:'suggestlimitedramarks',
        title:'建议限制备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//养生知识限定条件表
$('#healthknowledgelimitedTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'healthknowlimitedid',
        title:'养生知识限定id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'healthknowlimitedattrname',
        title:'养生知识限定属性名',
        sortable:'true'
     },{
        field:'healthknowlimitedstatus',
        title:'养生知识限定状态',
        sortable:'true'
    },{
        field:'healthknowlimitedstatuslevel',
        title:'养生知识限定状态级别',
        sortable:'true'
     },{
        field:'temp_healthknowledgeid',
        title:'养生知识id',
        sortable:'true'
     },{
        field:'healthknowlimitedexp',
        title:'养生知识限定说明',
        sortable:'true'
    },{
        field:'healthknowlimitedramarks',
        title:'养生知识限定备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//中药方剂表
$('#medicineprescriptionTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'medicineprescriptionid',
        title:'中药方剂ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'medicineprescriptionname',
        title:'中药方剂名',
        sortable:'true'
    },{
        field:'prescriptionindications',
        title:'功能主治',
        sortable:'true'
    },{
        field:'prescriptionusage',
        title:'用法用量',
        sortable:'true'
    },{
        field:'prescriptionmethod',
        title:'制法',
        sortable:'true'
    },{
        field:'prescriptioncharacters',
        title:'性状',
        sortable:'true'
    },{
        field:'prescriptionspecification',
        title:'规格',
        sortable:'true'
    },{
        field:'prescriptionstore',
        title:'储藏',
        sortable:'true'
    },{
        field:'prescriptioncontraindicat',
        title:'注意',
        sortable:'true'
    },{
        field:'prescriptiontheories',
        title:'各家论述',
        sortable:'true'
    },{
        field:'prescriptionextract',
        title:'摘录',
        sortable:'true'
    },{
        field:'prescriptionremarks',
        title:'方剂备注',
        sortable:'true'
    },{
        field:'prescriptiontag',
        title:'方剂标识',
        sortable:'true'
    },{
        field:'temp_picturelocationid',
        title:'图片位置ID',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//药品方剂映射表
$('#medicineprescriptionmappTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'medprescriptmappid',
        title:'中药方剂映射id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_chinesemedicineid',
        title:'药品id',
        sortable:'true'
    },{
        field:'temp_medicineprescriptionid',
        title:'中药方剂id',
        sortable:'true'
    },{
        field:'medicineamount',
        title:'中药用量',
        sortable:'true'
    },{
        field:'medprescriptmappremarks',
        title:'映射备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//健康预警类别表
$('#healthwarningtypeTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'healthwarningtypeid',
        title:'健康预警类别id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'healthwarningname',
        title:'健康预警类别名',
        sortable:'true'
    },{
        field:'healthwarningtypecode',
        title:'健康预警类别代码',
        sortable:'true'
    },{
        field:'healthwarningtypeexp',
        title:'健康预警分类说明',
        sortable:'true'
    },{
        field:'healthwarningtyepremarks',
        title:'健康预警分类备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//健康预警信息表
$('#healthwarningmessTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'healthwarningmessid',
        title:'健康预警信息id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'healthwarningtitle',
        title:'健康预警主题',
        sortable:'true'
    },{
        field:'healthwarningcontent',
        title:'健康预警内容',
        sortable:'true'
    },{
        field:'healthwarningremarks',
        title:'健康预警备注',
        sortable:'true'
    },{
        field:'temp_healthsuggestid',
        title:'健康建议id',
        sortable:'true'
    },{
        field:'temp_healthwarningtypeid',
        title:'健康预警类别id',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//用户健康建议映射表
$('#healthsuggestionsmappTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'healthsuggestmappid',
        title:'健康建议映射id',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'healthsuggestcontent',
        title:'健康建议内容',
        sortable:'true'
    },{
        field:'temp_userid',
        title:'用户ID',
        sortable:'true'
    },{
        field:'temp_healthsuggestid',
        title:'健康建议id',
        sortable:'true'
    },{
        field:'healthsuggestreason',
        title:'健康建议原因',
        sortable:'true'
    },{
        field:'healthsuggesttime',
        title:'建议生成时间',
        sortable:'true'
    },{
        field:'healthsuggestremarks',
        title:'建议生成备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//管理员权限表
$('#supervisorylevel').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'superlevelid',
        title:'管理级别ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'temp_managerid',
        title:'管理员ID',
        sortable:'true'
    },{
        field:'temp_adminisaresid',
        title:'行政区划ID',
        sortable:'true'
    },{
        field:'managerrank',
        title:'管理权限',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});

//运动类型表
$('#exercisetypeTable').bootstrapTable({
    columns:[{
        field:'state',
        checkbox:"true"
    },{
        field:'exercisetypeid',
        title:'运动类型ID',
        formatter:'nameFormatter',
        sortable:'true',
        visible:false
    },{
        field:'exercisetypename',
        title:'运动类型名',
        sortable:'true'
    },{
        field:'exercisetypeexplain',
        title:'运动类型说明',
        sortable:'true'
    },{
        field:'exercisetypecode',
        title:'运动类型代码',
        sortable:'true'
    },{
        field:'exercisetyperemarks',
        title:'运动类型备注',
        sortable:'true'
    }],
    striped:true,
    pagination:true,
    pageList:[10,20,50,100,500],
    pageSize:10,
    pageNumber:1,
    clickToSelect:true,
    smartDisplay:true
    //sidePagination:'server',
    //queryParamsType:'limit',
    //responseHandler:responseHandler,
    //queryParams:queryParams
});



function responseHandler(res){

  return {
      rows:res.results,
      total:res.count
    }

}

function queryParams(params){
  return {//:this.options.pageSize,
          //limit:params.limit,
          //page:(params.offset/params.limit)+1
          //page:this.options.pageNumber,
          //searchText:this.searchText
          page:params.pageNumber,
          limit:params.pageSize,
          searchText:params.searchText

  }
}


  /*  ===================================js of nav==========================================================*/



