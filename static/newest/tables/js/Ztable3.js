/**
 * Created by Mesogene on 2015/4/13.
 */
$(document).ready(function () {
    init();
    //全屏模态框
    $('[data-type="modal-trigger"]').on('click', function(){
        var actionBtn = $(this), scaleValue = retrieveScale($('.cd-modal-bg'));
        actionBtn.addClass('to-circle');
        $('.cd-modal-bg').addClass('is-visible').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function(){
            animateLayer($('.cd-modal-bg'), scaleValue, true);
        });
        if($('.no-csstransitions').length > 0 ) animateLayer($('.cd-modal-bg'), scaleValue, true);
        var i=$(".glyphicon-tags").next().attr('name');
        $(".cd-section h1").html(data[i].healthknowledgetitle);
        $(".cd-section h1").next().html(data[i].exersuggtime);
        $(".cd-section .flag3").append("&nbsp;&nbsp;&nbsp;"+data[i].healthknowledgeremarks);
        $(".cd-section .flag3").next().html(data[i].healthknowledgecontent);
    });
    $('.cd-modal-close').on('click', function(){
        closeModal();
    });
});
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
/*************************************************中医知识初始化*******************************************************/
var data;
function init() {
    data = restful("get", baseAddress+"/personaltuijian/?filtercontent=", "");
    var sort = restful("get", baseAddress+"/tbhealthknowledgetype/", "");

    for (var i in data) {
        var test;
        if (data[i].healthknowledgecontent.length >= 100) {
            test = data[i].healthknowledgecontent.substring(0, 100);
        }
        else {
            test = data[i].healthknowledgecontent;
        }
        var str = "<div style='width: 610px;'> " +
            "<p> <h3><a>" + data[i].healthknowledgetitle + "</a></h3></p> " +
            "<p class='flag'>" + data[i].exersuggtime + "</p> " +
            "<div><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + test + "…<a data-type='modal-trigger'>[更多..]</a></p></div> " +
            "<div class='flag2'><span class='glyphicon glyphicon-tags'></span>&nbsp;&nbsp;" + data[i].healthknowledgeremarks + " <a id='" + data[i].healthknowledgeid + "' name='" + i + "' onclick='collection(" + data[i].healthknowledgeid + ")' ><span class='glyphicon glyphicon-star-empty span'></span></a><a><span  class='glyphicon glyphicon-share span'></span></a></div> " +
            "</div> <hr>";
        var collectiondata = restful("get", baseAddress+"/tbmycollection/?collectionclass=2&temp_userid=1&collectioncode=" + data[i].healthknowledgeid, "");
        if (collectiondata != "") {
            var str = "<div style='width: 610px;'> " +
                "<p> <h3><a>" + data[i].healthknowledgetitle + "</a></h3></p> " +
                "<p class='flag'>" + data[i].exersuggtime + "</p> " +
                "<div><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + test + "…<a data-type='modal-trigger'>[更多..]</a></p></div> " +
                "<div class='flag2'><span class='glyphicon glyphicon-tags'></span>&nbsp;&nbsp;" + data[i].healthknowledgeremarks + " <a id='" + data[i].healthknowledgeid + "' name='" + i + "' onclick='cancel(" + data[i].healthknowledgeid + ")'><span class='glyphicon glyphicon-star span'></span></a><a><span  class='glyphicon glyphicon-share span'></span></a></div> " +
                "</div> <hr>";
        }
        $(".news").append(str);
    }
    for (var i in sort) {
        var str = "<li><a  onclick='sortflag(" + sort[i].healthknowltypeid + ");'>" + sort[i].healthknowltypename + "</a></li> ";
        $("#fenlei").append(str);
    }

}
function sortflag(id) {
    var count = 0;
    $(".news").html("");
    for (var i in data) {
        if (id == data[i].temp_healthknowltypeid) {
            count = 1;
            var test;
            if (data[i].healthknowledgecontent.length >= 100) {
                test = data[i].healthknowledgecontent.substring(0, 100);
            }
            else {
                test = data[i].healthknowledgecontent;
            }
            var str = "<div style='width: 610px;'> " +
                "<p> <h3><a>" + data[i].healthknowledgetitle + "</a></h3></p> " +
                "<p class='flag'>" + data[i].exersuggtime + "</p> " +
                "<div><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + test + "…<a data-type='modal-trigger'>[更多..]</a></p></div> " +
                "<div class='flag2'><span class='glyphicon glyphicon-tags'></span>&nbsp;&nbsp;" + data[i].healthknowledgeremarks + " <a id='" + data[i].healthknowledgeid + "' name='" + i + "' onclick='collection(" + data[i].healthknowledgeid + ")'><span class='glyphicon glyphicon-star-empty span'></span></a><a><span  class='glyphicon glyphicon-share span'></span></a></div> " +
                "</div> <hr>";
            var collectiondata = restful("get", baseAddress+"/tbmycollection/?collectionclass=2&temp_userid=1&collectioncode=" + data[i].healthknowledgeid, "");
            if (collectiondata != "") {
                var str = "<div style='width: 610px;'> " +
                    "<p> <h3><a>" + data[i].healthknowledgetitle + "</a></h3></p> " +
                    "<p class='flag'>" + data[i].exersuggtime + "</p> " +
                    "<div><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + test + "…<a data-type='modal-trigger'>[更多..]</a></p></div> " +
                    "<div class='flag2'><span class='glyphicon glyphicon-tags'></span>&nbsp;&nbsp;" + data[i].healthknowledgeremarks + " <a id='" + data[i].healthknowledgeid + "' name='" + i + "' onclick='cancel(" + data[i].healthknowledgeid + ")'><span class='glyphicon glyphicon-star span'></span></a><a><span  class='glyphicon glyphicon-share span'></span></a></div> " +
                    "</div> <hr>";
            }
            $(".news").append(str);
        }
    }
    if (count == 0) {
        var str = "<div style='width: 610px;'> " +
            "<div><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;没有相关信息...</p></div> ";
        $(".news").append(str);
    }
}
/*************************************************导航栏点击事件*******************************************************/
$(".nav a").click(function () {
    $(".nav li").each(function () {
        $(this).removeClass("active");
    });
    $(this).parent().addClass("active");
});
/******************************************************搜索事件********************************************************/
function EnterPress(e) {
    if (e.keyCode == 13) {
        $(".news").html("");
        var search = $(".form-control").val();
        var data = restful("get", baseAddress+"/personaltuijian/?filtercontent=" + search, "");
        for (var i in data) {
            var test;
            if (data[i].healthknowledgecontent.length >= 100) {
                test = data[i].healthknowledgecontent.substring(0, 100);
            }
            else {
                test = data[i].healthknowledgecontent;
            }
            var str = "<div style='width: 610px;'> " +
                "<p> <h3><a>" + data[i].healthknowledgetitle + "</a></h3></p> " +
                "<p class='flag'>" + data[i].exersuggtime + "</p> " +
                "<div><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + test + "…<a data-type='modal-trigger'>[更多..]</a></p></div> " +
                "<div class='flag2'><span class='glyphicon glyphicon-tags'></span>&nbsp;&nbsp;" + data[i].healthknowledgeremarks + " <a id='" + data[i].healthknowledgeid + "' name='" + i + "' onclick='collection(" + data[i].healthknowledgeid + ")' ><span class='glyphicon glyphicon-star-empty span'></span></a><a><span  class='glyphicon glyphicon-share span'></span></a></div> " +
                "</div> <hr>";
            var collectiondata = restful("get", baseAddress+"/tbmycollection/?collectionclass=2&temp_userid=1&collectioncode=" + data[i].healthknowledgeid, "");
            if (collectiondata != "") {
                var str = "<div style='width: 610px;'> " +
                    "<p> <h3><a>" + data[i].healthknowledgetitle + "</a></h3></p> " +
                    "<p class='flag'>" + data[i].exersuggtime + "</p> " +
                    "<div><p>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + test + "…<a data-type='modal-trigger'>[更多..]</a></p></div> " +
                    "<div class='flag2'><span class='glyphicon glyphicon-tags'></span>&nbsp;&nbsp;" + data[i].healthknowledgeremarks + " <a id='" + data[i].healthknowledgeid + "' name='" + i + "' onclick='cancel(" + data[i].healthknowledgeid + ")'><span class='glyphicon glyphicon-star span'></span></a><a><span  class='glyphicon glyphicon-share span'></span></a></div> " +
                    "</div> <hr>";
            }
            $(".news").append(str);
        }
    }
}
/******************************************************收藏button*******************************************************/
function collection(konwledgeid) {
    var data = restful("post", baseAddress+"/tbmycollection/", {
        'collectionclass': '2',
        'collectioncode': konwledgeid,
        'temp_userid': 1
    });
    if (data != "") {
        $("#" + konwledgeid).find("span").removeClass("glyphicon-star-empty").addClass("glyphicon-star");
        var change = $("#" + konwledgeid).parent().html().replace(/collection/, "cancel");
        $("#" + konwledgeid).parent().html(change);
        alert("收藏成功");
    }
}
/***************************************************取消收藏button****************************************************/
function cancel(konwledgeid) {
    var data = restful("get", baseAddress+"/tbmycollection/?collectionclass=2&temp_userid=1&collectioncode=" + konwledgeid, "");
    var deletedata = restful("delete", baseAddress+"/tbmycollection/" + data[0].mycollectionid + "/", "");
    if (data != "") {
        $("#" + konwledgeid).find("span").removeClass("glyphicon-star").addClass("glyphicon-star-empty");
        var change = $("#" + konwledgeid).parent().html().replace(/cancel/, "collection");
        $("#" + konwledgeid).parent().html(change);
        alert("取消收藏成功");
    }
}
