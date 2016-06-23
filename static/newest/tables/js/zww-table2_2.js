/**
 * Created by Mesogene on 2015/5/6.
 */
$(document).ready(function(){
    var data=restful("get",baseAddress+"/tbconstituteidentifyresultcombine/?temp_userid=1","");
    if(data!="fail"){
        var str="";
        var color=["cl1","cl2","cl3","cl5","cl1","cl2","cl3","cl5","cl1"];
        var max;
        var normal;
        var like;
        for(var i=(data.length/9);i>0;i--){
            max="";normal="";like="";
            for(var j=i*9-1;j>=i*9-8;j--){
                if(data[j].constituteldentifyflag=="2"){
                    max=data[j].temp_physiqueinfoid.physicaltypename;
                }
                if(data[j].constituteldentifyflag=="1"){
                    normal+=data[j].temp_physiqueinfoid.physicaltypename+" ";
                }
                if(data[j].constituteldentifyflag=="0"){
                    like+=data[j].temp_physiqueinfoid.physicaltypename+" ";
                }
            }
            if(normal==""&&like!=""){
                like="<br>倾向于:"+like;
            }
            if(normal!=""&&like==""){
                normal="<br>兼有:"+normal;
            }
            if(normal!=""&&like!=""){
                normal="<br>兼有:"+normal;
                like="<br>倾向于:"+like;
            }
            str+="<div style='position: absolute'> " +
            "<span style='margin-left: -210px'>"+data[i*9-1].constituteidentifytime+"</span> </div> " +
            "<div class='p1_box right "+color[i%9]+"'> <div>测试结果为："+max+normal+like+"</div> " +
            "<a class='bot' id='"+(i*9-1)+"'>查看详情<span class='glyphicon glyphicon-chevron-right'></span></a></div>";
        }
        $(".grid_6").append(str);
    }
    var tizhi = ["平和质", "阳虚质", "阴虚质", "痰湿质", "湿热质", "气郁质", "气虚质", "血瘀质", "特禀质"];
    $('.bot').click(function(){
       var id=$(this).attr("id");
        var scores=[];
        var yes=[];
        var yes2=[];
        var likes=[];
        for(var i=parseInt(id)-8;i<=parseInt(id);i++){
            scores.push(data[i].constituteidentifyremarks);
            if(data[i].constituteldentifyflag==0){
                likes.push(i%9);
            }
            if(data[i].constituteldentifyflag==1){
                yes.push(i%9);
                yes2.push(data[i].constituteidentifyremarks);
            }
            if(data[i].constituteldentifyflag==2){
                yes.unshift(i%9);
                yes2.unshift(data[i].constituteidentifyremarks);
            }
        }

       $("#demo01").click();
        /*********************************体质辨识charts*************************************/
        var myChart = echarts.init(window.parent.document.getElementById('main'));
        myChart.setOption({
            title: {
                text: '体质测试'
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                data: ['我的体质得分', '全国平均得分']
            },
            toolbox: {
                show: true,
                feature: {
                    mark: {show: true},
                    dataView: {show: true, readOnly: false},
                    magicType: {show: true, type: ['line', 'bar']},
                    restore: {show: true},
                    saveAsImage: {show: true}
                }
            },
            calculable: true,
            xAxis: [
                {
                    type: 'category',
                    data: tizhi
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    position: 'left',
                    splitNumber: 8,
                    max: 80,
                    min: 0,
                    name: '分数',
                    axisLabel: {
                        formatter: '{value}'
                    }
                },
                {
                    type: 'value',
                    max: 80,
                    min: 0,
                    splitNumber: 8,
                    axisLabel: {
                        formatter: function (value) {
                            // Function formatter
                            if (value == 30) {
                                return '倾向'
                            }
                            else if (value == 40) {
                                return '判定'
                            }
                        }
                    }
                }
            ],
            series: [
                {
                    name: '我的体质得分',
                    type: 'bar',
                    data: scores,
                    itemStyle: {
                        normal: {
                            color: function (params) {
                                if (yes.indexOf(params.dataIndex) >= 0)
                                    return '#ff7f50'
                                else
                                    return '#87cefa'
                            },
                            label: {
                                show: true,
                                position: 'top',
                                formatter: function (params) {
                                    if (yes2.indexOf(params.value) >= 0)
                                        return '我的体质'
                                    else
                                        return ''
                                }
                            }
                        }
                    },

                    markLine: {
                        data: [
                            [{name: '判定', xAxis: -1, yAxis: 40}, {xAxis: 9, yAxis: 40}]
                        ],
                        itemStyle: {
                            normal: {
                                lineStyle: {
                                    color: 'grey'
                                }
                            }
                        }
                    }

                },
                {
                    name: '全国平均得分',
                    type: 'line',
                    data: [35, 36, 42, 41, 36, 39, 41, 39, 26],
                    itemStyle: {
                        normal: {
                            lineStyle: {
                                width: 4,
                                color: '#32cd32'
                            }
                        }
                    },
                    markLine: {
                        data: [
                            [{name: '倾向', xAxis: -1, yAxis: 30}, {xAxis: 9, yAxis: 30}]
                        ],
                        itemStyle: {
                            normal: {
                                lineStyle: {
                                    color: 'grey'
                                },
                                label: {
                                    show: true
                                }
                            }
                        }
                    },
                    yAxisIndex: 1
                }
            ]
        });
        /*********************************体质辨识结果建议************************************/
        var physiqueinfo = restful("get", baseAddress+"/tbphysiqueinfo/", "");
        window.parent.$(window.parent.document).find('#add_middle h3>span,#add_middle p span').html(tizhi[yes[0]]);
        var string = "";
        for (var i = 1; i < yes.length; i++) {
            string += tizhi[yes[i]] + " ";
        }
        if(string!=""){
            string=",兼有"+string;
        }
        $('#add_middle small span').html(string);

        var string2 = "";
        for (var i = 0; i < likes.length; i++) {
                string2 += tizhi[likes[i]] + " ";
        }
        if (string2!="") {
            string2=",倾向于"+string2;
        }
        $('#add_middle small span').append(string2);
        var string3 = "";
        string3 += "<div id='tab1' class='panel tab1'> " +
        "<div class='add_content' style='border:1px solid #CCC;padding:10px;margin-top: 10px'> " +
        "<h2>什么是" + tizhi[yes[0]] + "？</h2> " +
        "<li>" + physiqueinfo[yes[0]].generacharacter +"</li><li>"+ physiqueinfo[yes[0]].shapefeature +"</li><li>"+ physiqueinfo[yes[0]].commonmanifest + "</li><li>"+ physiqueinfo[yes[0]].mentalcharacter + "</li> " +
        "</div> </div>";
        string3 += "<div id='tab2' class='panel tab2'> " +
        "<div class='add_content' style='border:1px solid #CCC;padding:10px;margin-top: 10px'> " +
        "<h2>这些是" + tizhi[yes[0]] + "需要注意的</h2> " +
        "<li>" + physiqueinfo[yes[0]].incidencetendency  + "</li><li>"+ physiqueinfo[yes[0]].foodallowtaboo +"</li>" +
        "</div> </div>";
        string3 += "<div id='tab3' class='panel'> " +
        "<div class='add_content' style='border:1px solid #CCC;padding:10px;margin-top: 10px'> " +
        "<h2>我为什么会有" + tizhi[yes[0]] + "</h2> " +
        "<li>" + physiqueinfo[yes[0]].physicalreason  + "</li> " +
        "</div> </div>";
        string3 += "<div id='tab4' class='panel'> " +
        "<div class='add_content' style='border:1px solid #CCC;padding:10px;margin-top: 10px'> " +
        "<h2>怎么改善" + tizhi[yes[0]] + "</h2> " +
        "<li>" + physiqueinfo[yes[0]].adjustmethod +"</li><li>"+ physiqueinfo[yes[0]].physicaladjustmethod +"</li><li> " +
        "</div> </div>";
        string3 += "<div id='add_header'> " +
        "<h1>你的体质：</h1> " +
        "<ul id='navigation'>" +
        "<li><a id='link-tab1' href='#tab1'>什么是" + tizhi[yes[0]] + "</a></li>" +
        "<li><a id='link-tab2' href='#tab2'>这些是" + tizhi[yes[0]] + "常见疾病</a></li>" +
        "<li><a id='link-tab3' href='#tab3'>我为什么会有" + tizhi[yes[0]] + "</a></li>" +
        "<li><a id='link-tab4' href='#tab4'>怎么改善" + tizhi[yes[0]] + "</a></li>" +
        "</ul> </div>";
        $('#result').html(string3);
        document.getElementById("link-tab1").click();
    });
});
function restful(typeInfo, urlInfo, dataInfo) {
    var result = null;
    $.ajax({
        async: false,
        type: typeInfo,
        //dataType: "json",
        contentType: "application/json",
        data: JSON.stringify(dataInfo),
        url: urlInfo,
        success: function (data) {
            result = data;
        },
        error: function (data) {
            result = "fail";
        }
    });
    return result;
}