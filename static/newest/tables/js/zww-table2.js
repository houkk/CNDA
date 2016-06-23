/**
 * Created by Mesogene on 2015/4/4.
 */
$(document).ready(function () {
});
function restful(typeInfo, urlInfo, dataInfo) {
    var result = null;
    $.ajax({
        async: false,
        type: typeInfo,
        dataType: "json",
        contentType: "application/json",
        data: dataInfo,
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
function restful2(typeInfo, urlInfo, dataInfo) {
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
var data;
/************************************************开始测试，显示题目****************************************************/
$("#total").click(function () {
    $("#tizhi").attr("style", "display:none");
    $("#progress-bar").attr("style", "display:block");
    $("#detail").attr("style", "display:block");
    $("#id_form").attr("style", "display:block");
    data = restful("get", baseAddress+"/tbidentificationissuess/", "");
    var msg = restful("get", baseAddress+"/tbidentifychoices/", "");
    var str = "";
    var count = 1;
    var count2 = 1;
    var arr = new Array();
    var tootip = {
        0: ["似乎从来没发生过"],
        1: ["好像有，不过很久没法发生过了。或者好像是很偶然的事情，觉得没必要放在心上"],
        2: ["间或一段时间出现，好像没什么规律，有一点担心"],
        3: ["有这个问题，好像已经摸到一些规律了"],
        4: ["是一直以来困扰我的问题"]
    };
    for (var j in msg) {
        arr.push(msg[j].identifychoicevalue);
    }
    for (var i in data) {
        var str2 = "";
        for (var j in msg) {
            var k = parseInt(j) + 1;
            if (data[i].identifyissuecontent.indexOf('*') != -1) {
                str2 += "<div title='" + tootip[j] + "'><input type='radio' name='question" + count2 + "' value='" + arr[arr.length - j - 1] + "' class='" + k + "'>" + msg[j].scriptdescribe + "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</div>";
            }
            else {
                str2 += "<div title='" + tootip[j] + "'><input type='radio' name='question" + count2 + "' value='" + arr[j] + "' class='" + k + "'>" + msg[j].scriptdescribe + "&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp</div>";
            }
        }
        var t = parseInt(i) + 1;
        if (data[i].temp_physiqueinfoid == 1) {
            str += "<li name='" + data[i].temp_physiqueinfoid + "' style='display:block'><div class='ques'>" + t + "、" + data[i].identifyissuecontent + "</div><div>" + str2 + "</div></li>"
        }
        else {
            str += "<li name='" + data[i].temp_physiqueinfoid + "' style='display:none'><div class='ques'>" + t + "、" + data[i].identifyissuecontent + "</div><div>" + str2 + "</div></li>"
        }
        count++;
        count2++;

    }
    $("#id_form").html("");
    $("#id_form").append("<ul>" + str + "<li class='ques'><a onclick='before_next(1)'><<&nbsp;上一组测试</a><button id='next' class='btn btn-default' onclick='before_next(2);'>下一组测试&nbsp;>></button></li></ul>");
    var btn = "<button id='submit' class='btn btn-success' onclick='submit();' style='display: none'>辛苦了！完成测试！&nbsp;</button>";
    $("#next").parent().append(btn);    //radio样式
    $('input').iCheck({
        radioClass: 'iradio_flat-orange'
    });

});
/************************************************提交体质测试表单******************************************************/
function submit() {
    var tizhi = ["平和质", "阳虚质", "阴虚质", "痰湿质", "湿热质", "气郁质", "气虚质", "血瘀质", "特禀质"];
    var str = new Array();
    var radio = [];
    var scores = new Array();
    var counts = new Array();
    var len = 0;
    var score;
    var count;
    var date = new Date().format("yyyy-MM-dd hh:mm:ss");
    for (var i = 1; i <= 9; i++) {
        score = 0;
        count = 0;
        $("li[name=" + i + "]").each(function () {
            len++;
            count++;
            var value = $(this).find("input:radio:checked").val();
            var num = parseInt($("input:radio[name='question" + i + "']:checked").attr("class"));
            if (value == null) {
                str.push(len);
            }
            else {
                score += parseInt(value);
                radio[len - 1] = {
                    'temp_identifyissueid': data[len - 1].identifyissueid,
                    'temp_identifychoiceid': parseInt(num),
                    'temp_userid': "舒文",
                    'getscore': parseInt(value),
                    'answerflag': 11,
                    'answertime': date
                };
            }
        });
        scores.push(score);
        counts.push(count);
    }
    if (str.length) {
        alert("第" + str + "题未回答，请补充完整。");
    }
    else {
        var result = new Array();
        var yes = new Array();//记录是此种体质的数组下标
        var yes2 = new Array();//记录是此种体质的分数
        for (var i = 1; i <= 8; i++) {
            scores[i] = (scores[i] * 1.0 / counts[i] - 1) * 25;
            if (scores[i] >= 40) {
                result[i] = 1;//是某种体质
                yes.push(i);
                yes2.push(scores[i]);
            }
            else if (scores[i] >= 30 && scores[i] < 40) {
                result[i] = 0;//倾向于某种体质
            }
            else {
                result[i] = -1;
            }
        }
        for (var j = 0; j < yes2.length - 1; j++) {
            var max = yes2[j];
            for (var i = 0; i < yes2.length - 1; i++) {
                if (yes2[j] < yes2[i + 1]) {
                    var k = yes2[j];
                    yes2[j] = yes2[i + 1];
                    yes2[i + 1] = k;
                    var p = yes[j];
                    yes[j] = yes[i + 1];
                    yes[i + 1] = p;
                }
            }
        }

        if (scores[0] >= 60 && scores[1] < 30 && scores[2] < 30 && scores[3] < 30 && scores[4] < 30 && scores[5] < 30 && scores[6] < 30 && scores[7] < 30 && scores[8] < 30) {
            result[0] = 1;//是平和质
        }
        else if (scores[0] >= 60 && (scores[1] < 40 && scores[1] >= 30) && (scores[2] < 40 && scores[2] >= 30) && (scores[3] < 40 && scores[3] >= 30) && (scores[4] < 40 && scores[4] >= 30) && (scores[5] < 40 && scores[5] >= 30) && (scores[6] < 40 && scores[6] >= 30) && (scores[7] < 40 && scores[7] >= 30) && (scores[8] < 40 && scores[8] >= 30)) {
            result[0] = 0;//基本是平和质
        }
        else {
            result[0] = -1;
        }
        result[yes[0]] = 2;
        var upload = new Array();
        for (var i = 0; i <= 8; i++) {
            if (result[i] == -1) {
                upload.push({
                    'temp_userid': "舒文",
                    'temp_physiqueinfoid': parseInt(i + 1),
                    'constituteidentifytime': date,
                    'constituteidentifyremarks': scores[i].toString(),
                    'constituteidentifyresult': '不是' + tizhi[i],
                    "constituteldentifyflag": result[i]
                });
            }
            else if (result[i] == 0) {
                upload.push({
                    'temp_userid': "舒文",
                    'temp_physiqueinfoid': parseInt(i + 1),
                    'constituteidentifytime': date,
                    'constituteidentifyremarks': scores[i].toString(),
                    'constituteidentifyresult': '倾向' + tizhi[i],
                    "constituteldentifyflag": result[i]
                });
            }
            else {
                upload.push({
                    'temp_userid': "舒文",
                    'temp_physiqueinfoid': parseInt(i + 1),
                    'constituteidentifytime': date,
                    'constituteidentifyremarks': scores[i].toString(),
                    'constituteidentifyresult': '是' + tizhi[i],
                    "constituteldentifyflag": result[i]
                });
            }

        }
        var per_ques = restful2("post", baseAddress+"/tbuseranswerrecords/", radio);
        var msg = restful2("post", baseAddress+"/tbconstituteidentifyresult/", upload);
        if (per_ques != "fail" && msg != "fail") {
            alert("hsah");
            window.parent.$(window.parent.document).find("#demo01").click();
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
            window.parent.$(window.parent.document).find('#add_middle h3>span,#add_middle p span').append(tizhi[yes[0]]);
            var string = "，兼有";
            for (var i = 1; i < yes.length; i++) {
                string += tizhi[yes[i]] + " ";
            }
            if (string.indexOf("质") > 0) {
                window.parent.$(window.parent.document).find('#add_middle small span').append(string);
            }
            var string2 = "，倾向于";
            for (var i = 0; i < 9; i++) {
                if (result[i] == 0) {
                    string2 += tizhi[i] + " ";
                }
            }
            if (string2.indexOf("质") > 0) {
                window.parent.$(window.parent.document).find('#add_middle small span').append(string2);
            }
            var string3 = "";
            string3 += "<div id='tab_tizhi0' class='panel'> " +
            "<div class='add_content' style='border:1px solid #CCC;padding:10px;margin-top: 10px'> " +
            "<h2>什么是" + tizhi[yes[0]] + "？</h2> " +
            "<li>" + physiqueinfo[yes[0]].generacharacter +"</li><li>"+ physiqueinfo[yes[0]].shapefeature +"</li><li>"+ physiqueinfo[yes[0]].commonmanifest + "</li><li>"+ physiqueinfo[yes[0]].mentalcharacter + "</li> " +
            "</div> </div>";
            string3 += "<div id='tab_tizhi1' class='panel'> " +
            "<div class='add_content' style='border:1px solid #CCC;padding:10px;margin-top: 10px'> " +
            "<h2>这些是" + tizhi[yes[0]] + "需要注意的</h2> " +
            "<li>" + physiqueinfo[yes[0]].incidencetendency  + "</li> " +
            "</div> </div>";
            string3 += "<div id='tab_tizhi2' class='panel'> " +
            "<div class='add_content' style='border:1px solid #CCC;padding:10px;margin-top: 10px'> " +
            "<h2>怎么改善" + tizhi[yes[0]] + "</h2> " +
            "<li>" + physiqueinfo[yes[0]].adjustmethod +"</li> " +
            "</div> </div>";
            string3 += "<div class='add_header'> " +
            "<h1>你的体质：</h1> " +
            "<ul id='navigation'>" +
            "<li><a id='link-0' href='#tab_tizhi0'>什么是" + tizhi[yes[0]] + "</a></li>" +
            "<li><a id='link-1' href='#tab_tizhi1'>这些是" + tizhi[yes[0]] + "常见疾病</a></li>" +
            "<li><a id='link-2' href='#tab_tizhi2'>怎么改善" + tizhi[yes[0]] + "</a></li>" +
            "</ul> </div>";
            window.parent.$(window.parent.document).find('#result').append(string3);
            window.parent.document.getElementById("link-0").click();
        }

    }
}
/****************************************************上一组/下一组测试*************************************************/
var type = {
    1: ["平和质", "【平和质】为正常体质"],
    2: ["阳虚质", "【阳虚质】的人平时比较怕冷，手脚常冰冷，口唇的颜色也较白，不爱说话，而且睡眠也偏多。"],
    3: ["阴虚质", "【阴虚质】的人常有热象表现，经常口渴，喉咙干、容易失眠、头昏眼花、容易心烦气躁、脾气差，皮肤枯燥无光泽、形体消瘦、盗汗、手足易冒汗发热、小便黄、粪便硬、常便秘等"],
    4: ["痰湿质", "【痰湿质】是目前比较常见的一种体质类型，多见于肥胖人，或以前偏瘦后来发胖的人。常表现有体形肥胖，腹部肥满松软，面部皮肤油脂较多，多汗且粘，胸闷，痰多，面色淡黄而暗，容易困倦。"],
    5: ["湿热质", "【湿热质】是指湿热内蕴，以面垢油光、口苦苔黄腻等湿热表现为主要特征的体质状态。"],
    6: ["气郁质", "【气郁质】是指气机郁滞，以神情抑郁、忧虑脆弱等气郁表现为主要特征的体质状态。"],
    7: ["气虚质", "【气虚质】的人常形体消瘦或偏胖，身体容易疲倦乏力，面色也比较苍白，说话声音低怯，常自汗出，且动则尤甚，心跳较快，食量偏少，舌头颜色淡、舌苔白，脉虚弱。"],
    8: ["血瘀质", "【血瘀质】是指血行不畅，肤色晦暗、舌质紫暗等血瘀表现为主要特征的体质状态。"],
    9: ["特禀质", "【特禀质】是指先天失常，以生理缺陷、过敏反应等为主要特征的体质状态。"]
}

function before_next(val) {
    var be = $("li[style='display:block']").attr('name');
    var af;
    if (val == 1) {
        af = parseInt(be) - 1;
    }
    else if (val == 2) {
        af = parseInt(be) + 1;
    }
    if (af == 10) {
        $("#next").attr("style", "display:none");
        $("#submit").attr("style", "display:block");
    }
    else if (af == 0) {
        alert("这是第一组");
    }
    else {
        if (val == 1) {
            $("#next").attr("style", "display:block");
            $("#submit").attr("style", "display:none");
            var p = parseInt(af * 11.2);
            var str = "<h4>【" + type[af][0] + "】测试</h4> " +
                "<div class='progress'> " +
                "<div class='progress-bar progress-bar-warning' role='progressbar' aria-valuenow='60' aria-valuemin='0' aria-valuemax='100' style='width: " + p + "%'>" + af + "/9组 " +
                "</div>" +
                "</div>";
            var str2 = "<div>" + type[af][1] + "</div>";

            $("#progress-bar").html(str);
            $("#detail").html(str2);
            $("li[name='" + be + "']").attr("style", "display:none");
            $("li[name='" + af + "']").attr("style", "display:block");
        }
        else {
            var judge = 0;
            $("li[name=" + be + "]").each(function () {
                var value = $(this).find("input:radio:checked").val();
                if (value == null) {
                    $(this).find(".ques").attr("class", "ques alert alert-danger");
                    judge = 1;
                }
                else {
                    $(this).find(".ques").attr("class", "ques");
                }
            });
            if (judge == 1) {
                alert("请完成该页的选项！");
            }
            else {
                $("#next").attr("style", "display:block");
                $("#submit").attr("style", "display:none");
                var p = parseInt(af * 11.2);
                var str = "<h4>【" + type[af][0] + "】测试</h4> " +
                    "<div class='progress'> " +
                    "<div class='progress-bar progress-bar-warning' role='progressbar' aria-valuenow='60' aria-valuemin='0' aria-valuemax='100' style='width: " + p + "%'>" + af + "/9组 " +
                    "</div>" +
                    "</div>";
                var str2 = "<div>" + type[af][1] + "</div>";

                $("#progress-bar").html(str);
                $("#detail").html(str2);
                $("li[name='" + be + "']").attr("style", "display:none");
                $("li[name='" + af + "']").attr("style", "display:block");
            }
        }

    }
}
/****************************************************时间对象的格式化;*************************************************/
Date.prototype.format = function (format) {
    /*
     * eg:format="YYYY-MM-dd hh:mm:ss";
     */
    var o = {
        "M+": this.getMonth() + 1, // month
        "d+": this.getDate(), // day
        "h+": this.getHours(), // hour
        "m+": this.getMinutes(), // minute
        "s+": this.getSeconds(), // second
        "q+": Math.floor((this.getMonth() + 3) / 3), // quarter
        "S": this.getMilliseconds()
        // millisecond
    }

    if (/(y+)/.test(format)) {
        format = format.replace(RegExp.$1, (this.getFullYear() + "")
            .substr(4 - RegExp.$1.length));
    }

    for (var k in o) {
        if (new RegExp("(" + k + ")").test(format)) {
            format = format.replace(RegExp.$1, RegExp.$1.length == 1 ? o[k]
                : ("00" + o[k]).substr(("" + o[k]).length));
        }
    }
    return format;
}