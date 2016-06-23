/**
 * Created by Mesogene on 2015/5/8.
 */
$(document).ready(function() {
    var data = restful("get", baseAddress+"/tbconstituteidentifyresultcombine/?temp_userid=1", "");
    var tizhi = ["平和质", "阳虚质", "阴虚质", "痰湿质", "湿热质", "气郁质", "气虚质", "血瘀质", "特禀质"];
    var scores=[];
    var yes=[];
    var yes2=[];
    var like=[];
    for(var i=data.length-9;i<data.length;i++){
        scores.push(data[i].constituteidentifyremarks);
        if(data[i].constituteldentifyflag==0){
            like.push(i%9);
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
    var myChart = echarts.init(document.getElementById('main'));
    myChart.setOption({
        title: {
            text: '体质测试'
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['我的体质得分'],
            backgroundColor: '#eee'
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
                name:['我的体质得分'],
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
                                    return '我的体质：'+parseInt(params.value);
                                else
                                    return parseInt(params.value);
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
        ]
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