/**
 * Created by Mesogene on 2015/4/2.
 */

var table = $('#sample-table-2').bootstrapTable({
    sidePagination: 'server',
    queryParamsType: 'limit',
    responseHandler: function (res) {
        return {
            rows: res.results,
            total: res.count
        }
    },
    queryParams: function queryParams(params) {
        return {
            "page":(params.offset/params.limit)+1,
            "page_size": params.limit
        };
    }
});
$(document).ready(function () {
    /****************************************模态框-查看详情****************************************/
    table.on('click-row.bs.table', function (e, row, $element) {
        var doctorid = row.doctorid;
        var collectiondata = restful("get", baseAddress+"/tbmycollection/?temp_userid=1&collectionclass=1&collectioncode=" + doctorid, "");
        str2 = "";
        str2 += "<button type='button' class='btn btn-default' onclick='collection(" + doctorid + ");'>收藏 </button><button type='button' class='btn btn-default'data-dismiss='modal'>关闭 </button>";
        if (collectiondata != "") {
            str2 = "";
            str2 += "<button type='button' class='btn btn-default' onclick='cancel(" + doctorid + ");'>取消收藏 </button><button type='button' class='btn btn-default'data-dismiss='modal'>关闭 </button>";
        }
        $("#modalfooter").html(str2);
        str = "";
        str += "<ul><li><span>姓名： </span>" + row.doctorname + "</li><li><span>性别： </span>" + row.doctorsex + "</li><li><span>年龄： </span>" + row.doctorage + "</li><li><span>职称： </span>" + row.professionalrands + "</li><li><span>担任职务： </span>" + row.workduty + "</li><li><span>工作年限： </span>" + row.doctorworktime + "</li><li><span>医院： </span>" + row.adminisareaprovince + " " + row.adminisareacity + " " + row.adminisareacounty + " " + row.hospitalname + "</li><li><span>科室： </span>" + row.hospitalofficename + "</li></li><li><span>医生专长： </span>" + row.doctorexptypename + "</li><li><span>研究领域： </span>" + row.researcharea + "</li><li><span>研究成果： </span>" + row.researchfindings + "</li><li><span>医生简介： </span>" + row.doctorsynopsis + "</li></ul>";
        $("#modalbody").html(str);
        $("#doctorinfo-modal").modal('show');
    });
    /****************************************刷新****************************************/
    $("[name='refresh']").click(function () {
        table.bootstrapTable('refresh', {url: baseAddress+'/doctorview/'});
        $("#sheng .my").html("请选择省");
        $("#shi .my").html("请选择市");
        $("#qu .my").html("请选择区(县)");
        $("#yiyuan .my").html("请选择医院");
        txt_sheng = "请选择省";
        txt_shi = "请选择市";
        txt_qu = "请选择区(县)";
        txt_yiyuan = "请选择医院";
    });
});
function detail() {
    return '<a><span class="glyphicon glyphicon-eye-open"></span>&nbsp;&nbsp;查看详情</a>';
}

function restful(typeInfo, urlInfo, dataInfo) {
    var result = null;
    $.ajax({
        async: false,
        type: typeInfo,
        dataType: "json",
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
/**********************************************选择地区****************************************************************/
var txt_sheng = "请选择省";
var txt_shi = "请选择市";
var txt_qu = "请选择区(县)";
var txt_yiyuan = "请选择医院";
function select_sheng() {
    var data = restful("get", baseAddress+"/tbadminisarea/?adminisareacode=0000", "");
    //省的下拉框
    var str = "";
    for (var i in data) {
        str += " <li><a>" + data[i].adminisareaprovince + "</a></li>";
    }
    $('#sheng ul').html(str);
    $('#sheng a').click(function () {
        $("#shi .my").html("请选择市");
        $("#qu .my").html("请选择区(县)");
        $("#yiyuan .my").html("请选择医院");
        txt_sheng = $(this).text();
        $("#sheng .my").html(txt_sheng);
        search_area(txt_sheng, " ", " ", " ");
    });
}
function select_shi() {
    var data = restful("get", baseAddress+"/tbadminisarea/?adminisareaprovince=" + txt_sheng + "&adminisareacode__endswith=00", "");
    //市的下拉框
    var str = "";
    for (var i in data) {
        str += " <li><a>" + data[i].adminisareacity + "</a></li>";
    }
    $('#shi ul').html(str);
    $('#shi a').click(function () {
        $("#qu .my").html("请选择区(县)");
        $("#yiyuan .my").html("请选择医院");
        txt_shi = $(this).text();
        $("#shi .my").html(txt_shi);
        search_area(txt_sheng, txt_shi, " ", " ");
    });
}
function select_qu() {
    var data = restful("get", baseAddress+"/tbadminisarea/?adminisareaprovince=" + txt_sheng + "&adminisareacity=" + txt_shi, "")
    //区的下拉框
    var str = "";
    for (var i in data) {
        str += " <li><a>" + data[i].adminisareacounty + "</a></li>";
    }
    $('#qu ul').html(str);
    $('#qu a').click(function () {
        $("#yiyuan .my").html("请选择医院");
        txt_qu = $(this).text();
        $("#qu .my").html(txt_qu);
        search_area(txt_sheng, txt_shi, txt_qu, " ");
    });
}
function select_yiyuan() {
    var data = restful("get", baseAddress+"/tbhospitalinfocombine/?temp_adminisareaid__adminisareaprovince=" + txt_sheng + "&temp_adminisareaid__adminisareacity=" + txt_shi + "&temp_adminisareaid__adminisareacounty=" + txt_qu, "");

    //医院的下拉框
    var str = "";
    for (var i in data) {
        str += " <li><a>" + data[i].hospitalname + "</a></li>";
    }
    $('#yiyuan ul').html(str);
    $('#yiyuan a').click(function () {
        txt_yiyuan = $(this).text();
        $("#yiyuan .my").html(txt_yiyuan);
        search_area(txt_sheng, txt_shi, txt_qu, txt_yiyuan);

    });
}
/************************************************根据区域表格刷新*******************************************************/
function search_area(val_sheng, val_shi, val_qu, val_yiyuan) {
    if ((val_shi == " ") && (val_qu == " ") && (val_yiyuan = " ")) {
        $('#sample-table-2').bootstrapTable('refresh', {url: baseAddress+'/doctorview/?id=&adminisareaprovince=' + val_sheng});
    }
    else if ((val_shi != " ") && (val_qu == " ") && (val_yiyuan = " ")) {
        $('#sample-table-2').bootstrapTable('refresh', {url: baseAddress+'/doctorview/?id=&adminisareaprovince=' + val_sheng + '&adminisareacity=' + val_shi});
    }
    else if ((val_shi != " ") && (val_qu != " ") && (val_yiyuan = " ")) {
        $('#sample-table-2').bootstrapTable('refresh', {url:baseAddress+ '/doctorview/?id=&adminisareaprovince=' + val_sheng + '&adminisareacity=' + val_shi + '&adminisareacounty=' + val_qu});
    }
    else {
        $('#sample-table-2').bootstrapTable('refresh', {url:baseAddress+ '/doctorview/?id=&adminisareaprovince=' + val_sheng + '&adminisareacity=' + val_shi + '&adminisareacounty=' + val_qu + '&hospitalname' + val_yiyuan});
    }
}
/***************************************************收藏button功能****************************************************/
function collection(doctorid) {
    var data = restful("post", baseAddress+"/tbmycollection/", {
        'collectionclass': '1',
        'collectioncode': doctorid,
        'temp_userid': 1
    });
    if (data != "") {
        str2 = "";
        str2 += "<button type='button' class='btn btn-default' onclick='cancel(" + doctorid + ");'>取消收藏 </button><button type='button' class='btn btn-default'data-dismiss='modal'>关闭 </button>";
        $("#modalfooter").html(str2);
    }
}
/***************************************************取消收藏button****************************************************/
function cancel(doctorid) {
    var data = restful("get", baseAddress+"/tbmycollection/?temp_userid=1&collectionclass=1&collectioncode=" + doctorid, "");
    var deletedata = restful("delete", baseAddress+"/tbmycollection/" + data[0].mycollectionid + "/", "");
    if (data != "") {
        str2 = "";
        str2 += "<button type='button' class='btn btn-default' onclick='collection(" + doctorid + ");'>收藏 </button><button type='button' class='btn btn-default'data-dismiss='modal'>关闭 </button>";
        $("#modalfooter").html(str2);
    }
}

