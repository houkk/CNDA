//ajax函数定义
function restful(typeInfo,urlInfo,dataInfo) {
    /**typeInfo:操作类型；
     * urlInfo:地址；
     * dataInfo:json数据；
     * 操作类型：
     * get：获取（dataInfo为空时，查询所有；dataInfo不为空，条件查询）；
     * 查询(数据分页，暂时每页是十条数据，可后台更改)
     * post：上传；
     * put：更新(按照id)；
     * delete：删除数据（id）；
     * */

    var result = null;
    $.ajax({
        async:false,
        type: typeInfo,
        url: urlInfo,
        dataType:"json",
        //contentType:"application/json",
        data:dataInfo,
        success:function(json){
            result=json;
        },
        error:function(){
            result="fail";
        }
    });
    //	.success(function (json) {
    //	//result = json;
    //	result= json;
    //	return result;
    //}).error(function(json){
    //	result = json;
    //	return result;
    //});
    return result;
}

//ajax函数定义——提交数组
function restful1(typeInfo,urlInfo,dataInfo) {
    /**typeInfo:操作类型；
     * urlInfo:地址；
     * dataInfo:json数据；
     * 操作类型：
     * get：获取（dataInfo为空时，查询所有；dataInfo不为空，条件查询）；
     * 查询(数据分页，暂时每页是十条数据，可后台更改)
     * post：上传；
     * put：更新(按照id)；
     * delete：删除数据（id）；
     * */

    var result = null;
    $.ajax({
        async:false,
        type: typeInfo,
        url: urlInfo,
        //dataType:"json",
        contentType:"application/json",
        data:JSON.stringify(dataInfo),
        success:function(json){
            result=json;
        },
        error:function(){
            result="fail";
        }
    });
    //	.success(function (json) {
    //	//result = json;
    //	result= json;
    //	return result;
    //}).error(function(json){
    //	result = json;
    //	return result;
    //});
    return result;
}

/************************点击图片添加到购物车(方法二)************/
function xuanZhong(value,value1){
    var same;
    var flag=0;
        $("#foodList li").each(function(){
            if($(this).find("p").text()==value){
                alert("该食物已存在！");
                flag=1;
            }
        });
        if(flag==0){
            same="<input type='text' style='width:60px;height:25px;'/><span style='margin-top: 0px;width:20px;'>&nbsp克</span><a class='delete1' style='text-decoration: none;cursor: pointer;margin-left: 30px;'>&nbsp;删除" +
            "</a><div style='visibility: hidden;height: 0px;'>"+$("#foodType").find("option:selected").text()+"</div><div style='visibility: hidden;height: 0px;'>"+value1+"</div>";
            var m="<li style=' margin-bottom: 2px;'><p style='width:150px ; margin-top: 0px;float:left;'>"+ value +"</p>"+same+"</li>";
            $("#foodList").append(m);
        }

    //删除购物车食物信息
        $(".delete1").on("click",function(){
            $(this).parent().remove();
        });
}

/**************************我的偏好**********************************/
function showPre(value){
    if(value=="food"){
        $.ajax({
            type:"get",
            dataType:"json",
            url: baseAddress+"/tbeatingpreferrecords/",
            data:{"temp_userid":10},
            success:function(msg){
                //alert(msg);
                for(var i in msg){
                    if(msg[i].currentlypreferflag=="1"){
                    var str="偏好食物种类名称："+msg[i].foodtypename+"<br>偏好食物名称："+msg[i].foodname+"<br>偏爱度："+msg[i].preference+"<br>平均每天摄入量："+msg[i].averageintake+
                        "<br>最频繁开始时间："+msg[i].eatingoftenstarttime+"<br>最频繁结束时间："+msg[i].eatingoftenovertime;
                     }
                }
                //alert(str);
                $("#preTitle").html("饮食偏好");
                $("#preBody").html(str);
            }
        })
    }
    if(value=="sleep"){
        $.ajax({
            type:"get",
            dataType:"json",
            url: baseAddress+"/tbsleeppreferrecords/",
            data:{"temp_userid":10},
            success: function (msg) {
                //alert(msg);
               for(var i in msg){
                   if(msg[i].currentlypreferflag=="1"){
                       var str1="偏好睡眠开始时间："+msg[i].prefersleepbeginat+"<br>偏好睡眠结束时间："+msg[i].prefersleepoverat;
                   }
               }
                //alert(str);
                $("#preTitle").html("睡眠偏好");
                $("#preBody").html(str1);
            }
        })
    }
    if(value=="sport"){
        $.ajax({
            type:"get",
            dataType:"json",
            url: baseAddress+"/tbexercisepreferrecords/",
            data:{"temp_userid":10},
            success: function (msg) {
               for(var i in msg){
                   if(msg[i].currentlypreferflag=="1"){
                       var str2="偏好运动类型名称："+msg[i].exercisetype+"<br>偏好运动名称："+msg[i].exercisename+"<br>运动描述："+msg[i].exercisedescribe;
                   }
               }
                $("#preTitle").html("运动偏好");
                $("#preBody").html(str2);
            }
        })
    }
}

/**************************生活习惯**********************************/
function teZheng(value){
    $.ajax({
        type:"get",
        dataType:"json",
        url: baseAddress+"/tbuser/",
        success:function(msg){
            var id;
            for(var i in msg){
                if(msg[i].userid==1){
                    if(value=="饮食"){
                        id=msg[i].temp_eatingfeatureid;   //饮食特征记录表
                        $.ajax({
                            type:"get",
                            dataType:"json",
                            url: baseAddress+"/tbfoodfeature/",
                            success:function(msg){
                                var str1;
                                for(var i in msg){
                                    if(id==msg[i].eatingfeatureid){
                                        str1="饮食习惯是否合理："+ msg[i].eatinghabitsdetermine +"<br>饮食习惯分析结果："+ msg[i].eatinghabitanalysis +"<br>平均每天能量摄入："+ msg[i].averageenergyintake + msg[i].energyintakeunit+ "<br>平均每天水分摄入:" +msg[i].averagemoistureintake+msg[i].moistureintakeunit+"<br>平均每天蛋白质摄入:"+msg[i].averageproteinintake+msg[i].proteinintakeunit +
                                        "<br>平均每天脂肪摄入："+msg[i].averagefatintake+msg[i].fatintakeunit+"<br>平均每天膳食纤维摄入："+msg[i].averagefiberintake+msg[i].fiberintakeunit+"<br>平均每天碳水化合物摄入："+msg[i].averagecarbohydrateintake+msg[i].carbohydrateintakeunit+"<br>平均每天维生素A摄入："+msg[i].averagevitaminaintake+msg[i].vitaminaintakeunit+"<br>平均每天维生素B1摄入："+
                                        msg[i].averagevitaminb1intake+msg[i].vitaminb1intakeunit+"<br>平均每天维生素B2摄入："+msg[i].averagevitaminb2intake+msg[i].vitaminb2intakeunit+"<br>平均每天维生素B6摄入："+msg[i].averagevitaminb6intake+msg[i].vitaminb6intakeunit+"<br>平均每天维生素B12摄入："+msg[i].averagevitaminb12intake+msg[i].vitaminb12intakeunit+"<br>平均每天维生素C摄入："+msg[i].averagevitamincintake+
                                        msg[i].vitamincintakeunit+"<br>平均每天维生素D摄入："+msg[i].averagevitamindintake+msg[i].vitamindintakeunit+"<br>平均每天维生素E摄入："+msg[i].averagevitamineintake+msg[i].vitamineintakeunit+"<br>平均每天维生素K摄入："+msg[i].averagevitaminkintake+msg[i].vitaminkintakeunit;
                                    }
                                }
                                $("#teZhengTitle").html("饮食特征");
                                $("#character").html(str1);
                            }
                        })

                    }
                    if(value=="睡眠"){
                        id=msg[i].temp_sleepfeatureid;  //睡眠特征记录表
                        $.ajax({
                            type:"get",
                            dataType:"json",
                            url: baseAddress+"/tbusersleepfeature/",
                            success:function(msg){
                                var str;
                                for(i in msg){
                                    if(id==msg[i].sleepfeatureid){
                                        str="空气湿度相对比："+ msg[i].airhumidity +"<br>环境温度："+ msg[i].ambienttemperature +"摄氏度<br>环境噪声："+ msg[i].ambientnoise + "分贝<br>睡前习惯：" +msg[i].bedtimehabits+"<br>睡前习惯是否健康："+msg[i].goodbedtimehabits+
                                        "<br>是否有午睡习惯："+msg[i].siestahabit+"<br>24小时平均睡眠："+msg[i].averagesleeptime+"小时<br>睡眠习惯是否合理："+msg[i].sleephabitdetermination+"<br>睡眠指数："+msg[i].sleepindex+"<br>睡眠习惯分析结果："+ msg[i].sleephabitanalysis;
                                    }
                                }
                                $("#teZhengTitle").html("睡眠特征");
                                $("#character").html(str);
                            }
                        })
                    }
                    if(value=="运动"){
                        id=msg[i].temp_exercisefeatureid;
                        $.ajax({
                            type:"get",
                            dataType:"json",
                            url: baseAddress+"/tbuserexercisefeature/",
                            success:function(msg){
                                var str2;
                                for(i in msg){
                                    if(id=msg[i].ExerciseFeatureID){
                                        str2="身高："+msg[i].Height+"<br>体重："+msg[i].Weight+"<br>行走步长"+msg[i].StepLength+"<br>跑步步长："+msg[i].RunStepLength+"<br>标准体重："+msg[i].StandardWeight+"<br>数据上传时间："+
                                            msg[i].DataUpTime+"<br>运动特征备注："+msg[i].ExerciseFeatureRemarks+"<br>运动指数："+msg[i].MotilityIndex+"<br>运动习惯是否合理："+msg[i].ExerciseHabitsDetermine+"<br>运动习惯分析结果："+
                                            msg[i].ExerciseHabitAnalysis+"<br>每天平均运动时间："+msg[i].AverageExciteTime+"<br>运动方式偏好："+msg[i].ExerciseTypePrefer;
                                    }
                                }
                                $("#teZhengTitle").html("运动特征");
                                $("#character").html(str2);
                            }
                        })
                    }
                }
            }
        }
    })
}

/***************************点击套餐获取相应图片*****************************/
function picAcquire(value){
    var tempSeriesPicture=restful("get",baseAddress+"/tbsetmealfoodmappcombine/",{"temp_setmealinfoid":value});
    var picStr="";
    for(var i in tempSeriesPicture){
        picStr+="<img src='http://10.120.59.9:81/"+tempSeriesPicture[i].temp_commonfoodid.temp_picturelocationid+"'style='width:80px;height:70px;margin-right:5px'>";
    }
    $("#"+value+" div").html("<div style='float:left'>"+picStr+"</div>");
}

/***************************点击checkbox获取相应套餐信息*****************************/
function radioChange(value){
    $(this).iCheck('check');
    radioId = value;    //设置checkbox全局变量获取value值
}

//加载页面时执行
$(function() {

    //currentTime记录电脑当前时间
    var myDate=new Date();
    var myTime1=myDate.getFullYear();
    var myTime2=myDate.getMonth()+1;
    var myTime3=myDate.getDate();
    var myTime4=myDate.getHours();
    var myTime5=myDate.getMinutes();
    var myTime6=myDate.getSeconds();
    currentTime="";
    currentTime =myTime1+"-"+(myTime2<10?"0"+myTime2:myTime2)+"-"+(myTime3<10?"0"+myTime3:myTime3)+" "+(myTime4<10?"0"+myTime4:myTime4)+":"+
    (myTime5<10?"0"+myTime5:myTime5)+":"+(myTime6<10?"0"+myTime6:myTime6);


    //点击确定选中套餐
    $("#pacDetermine").click(function () {
        var flag=0;
        var taocanList=$("#accordion input");
        for(var i=0;i<taocanList.length;i++){
            if(taocanList[i].checked){
                var tempSeries=restful("get",baseAddress+"/tbsetmealfoodmappcombine/",{"temp_setmealinfoid":radioId});
                var picStr1="";
                for(var j in tempSeries){
                    var same="<input type='text' style='width:60px;height:25px;'/><span style='margin-top: 0px;width:20px;'>&nbsp克</span><a class='delete' style='text-decoration: none;" +
                        "cursor: pointer;margin-left: 30px;'>" + "&nbsp;删除" + "</a><div style='visibility: hidden;height: 0px;'>"+tempSeries[j].temp_commonfoodid.temp_commonfoodtypeid+"</div>"+
                        "<div style='visibility: hidden;height: 0px;'>"+tempSeries[j].temp_commonfoodid.temp_foodnutritionid+"</div>";
                    picStr1+="<li style=' margin-bottom: 2px;'><p style='width:150px ; margin-top: 0px;float:left;'>"+ tempSeries[j].temp_commonfoodid.commonfoodname +"</p>"+same+"</li>";
                }
                $("#foodList").html(picStr1);
                $("#myModalTaoCan").modal('hide');
                flag=1;
            }
        }
        if(flag==0){
            alert("未选中任何套餐");
        }
        //删除购物车食物信息
        $(".delete").on("click",function(){
            $(this).parent().remove();
        });
    });


    /*************食物类型下拉框**********************/
    var dataFoodWide=restful("get",baseAddress+"/tbfoodwidecategories/",null);
    var strFoodWide="";
    $.each(dataFoodWide, function (i) {
        strFoodWide+="<option value=" + dataFoodWide[i].foodwidecategoryid +">" + dataFoodWide[i].foodwidecatename + "</option>";
    });
    $("#foodTypeOne").append(strFoodWide);

    /*********************提交食物信息****************************/
    $("#foodSubmit").click(function(){
        var foodArray=[];
        var flag=0;
        if($("#foodList li").length<=0){
            alert("食物列表为空！");
        }
        else{
            if($.trim($("#eatStartTime").val()).length<=0||$.trim($("#eatEndTime").val()).length<=0){
                alert("饮食时间为空！");
            }
            else{
                $("#foodList li").each(function(){
                    if($(this).find("input").val()==""){
                        flag=1;
                    }
                });
                if(flag==1){
                    alert("请输入食用数量！");
                }
                else{
                    $("#foodList li").each(function () {
                        var timS=$("#eatStartTime").val();
                        var timE=$("#eatEndTime").val();
                        var beiz=$("#beiZhu").val();
                        var shiw=$(this).find("p").text();
                        var shul=$(this).find("input").val();
                        var typ=$(this).find("div").first().text();
                        var foodNutri=$(this).find("div").last().text();
                        alert(typ);
                        alert(foodNutri);
                        foodArray.push({'foodtypename':typ,'foodname':shiw,'eatingamount':shul,'unitname': '克','eatingtime': timS,"eatingovertime":timE,'eatingrecordsuptime':currentTime,'eatinginforemarks':beiz,'temp_userid':11,"temp_foodnutritionid":foodNutri});
                    });
                    restful1("post",baseAddress+"/tbdietaryrecords/",foodArray);
                    alert("提交成功！");
                    $("#foodList").empty();
                }
            }
        }
    });

    /*************运动类型下拉框**********************/
    var dataSportType=restful("get",baseAddress+"/tbexercisetype/",null);
    var strSportType="";
    for(var i in dataSportType){
        strSportType +=  "<option value=" + dataSportType[i].exercisetypeid +">" + dataSportType[i].exercisetypename + "</option>";
    }
    $("#sportType").html( "<option>请选择运动类型</option>"+strSportType);

    /*********************提交运动信息****************************/
    $("#sportSubmit").click(function(){
        if($.trim($("#sportInfo").val()).length<=0) {
            alert("运动实体为空！");
        }
        else{
            if($.trim($("#end").val()).length<=0||$.trim($("#begin").val()).length<=0) {
                alert("运动时间为空！");
            }
            else{
                var sb=$("#begin").val();
                var se=$("#end").val();
                var bz=$("#sportBeiZhu").val();
                var lb=$("#sportInfo").find("option:selected").val();
                $.ajax({
                    type: "post",
                    dataType: "json",
                    url: baseAddress+"/tbsportinforecords/",
                    data:{"sportbegintime":sb,"sportovertime":se,"sportrecorduptime":currentTime,"sportinforemarks":bz,"temp_userid":"张传清","temp_exerciseid":lb},
                    success:function( ){
                        alert("运动信息录入成功！");
                    }
                });
            }
        }
    });

    /*********************提交睡眠信息****************************/
    $("#sleepSubmit").click(function () {
        if($.trim($("#sleepBegin").val()).length<=0) {
            alert("睡眠开始时间为空！");
        }
        else{
            if($.trim($("#sleepOver").val()).length<=0) {
                alert("睡眠结束时间为空！");
            }
            else{
                var sBegin=$("#sleepBegin").val();
                var sOver=$("#sleepOver").val();
                var sBeiZhu=$("#sleepBeiZhu").val();
                alert(currentTime);
                restful("post",baseAddress+"/tbsleepinforecords/",{"sleepbegin":sBegin,"sleepover":sOver,"sleepremarks":sBeiZhu,"sleeprecorduptime":currentTime,"temp_userid":"张传清"});
                alert("睡眠信息录入成功！");
            }
        }
    });

    /************************获取选择套餐数据***************************/
    $("#pacChoice").click(function(){
        var pacList=restful("get",baseAddress+"/tbeatingsetmealinfo/",null);
        var pacStr="";
        for(var i in pacList){
            pacStr +="<div class='panel panel-default'><div class='panel-heading' style='height:30px;padding-bottom:5px;padding-top: 5px;'><input onclick='radioChange("+pacList[i].setmealinfoid+")' type='radio' name='iCheck' style='width:30px;height:15px;float: left;'><h5 class='panel-title'>" +
            "<a onclick='picAcquire("+pacList[i].setmealinfoid+")' data-toggle='collapse'" + "data-parent='#accordion' href='#"+ pacList[i].setmealinfoid+"'><font size='2.5'>"+pacList[i].setmealname+":" + pacList[i].setmealexplain+"</font></a></h5></div><div id='"+
            pacList[i].setmealinfoid+ "' class='panel-collapse collapse'>"+" <div class='panel-body'></div></div></div>";
        }
        $("#accordion").html(pacStr);
    });

});











