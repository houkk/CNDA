/**
 * Created by Mesogene on 2015/5/12.
 */
/*********************************************用户信息*****************************************************************/
$(document).ready(function () {
    userInfo();
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
            result = " ";
        }
    });
    return result;
}
function restful_admin(typeInfo, urlInfo, dataInfo){
    var result = null;
    $.ajax({
        async:false,
        type:typeInfo,
        contentType:'application/json',
        url:urlInfo,//baseAddress+"/me/"
        data:dataInfo,
        beforeSend: function (xhr) {
            xhr.setRequestHeader("Authorization","Token "+GetCookie());
        },
        success: function (data) {
            result=data;
        }
    });
    return result;
}

function userInfo() {
    var msg = restful_admin("get", baseAddress+"/me/", "");
    var name = msg[0].username;
    var sex = msg[0].usersex;
    var age = msg[0].userage;
    var worktype = msg[0].userwroktype;
    var phone = msg[0].userphonenumber;
    var email = msg[0].email;
    var arr = {"1": ["name", "age", "worktype", "phone", "email"], "2": [name, age, worktype, phone, email]};

    for (var i in arr[1]) {
        $("#cd-" + arr[1][i]).attr("value", arr[2][i]);
    }
    if (msg.usersex == "男") {
        $("#sex_m").attr("checked", true);
    }
    else if (msg.usersex == "女") {
        $("#sex_w").attr("checked", true);
    }


    $("#mysubmit").click(function () {
        name = $("#cd-name").val().trim();
        sex = $('input:radio[name="radio-button"]:checked').val();
        age = $("#cd-age").val().trim();
        worktype = $("#cd-worktype").val().trim();
        phone = $("#cd-phone").val().trim();
        email = $("#cd-email").val().trim();
        arr = {"1": ["name", "age", "worktype", "phone", "email"], "2": [name, age, worktype, phone, email]};
        var judge = 0;
        for (var i in arr[2]) {
            $("#cd-" + arr[1][i]).next().css('display', "none");
            $("#cd-" + arr[1][i]).removeClass("error");
        }
        for (var i in arr[2]) {
            if (arr[2][i].length == 0) {
                if (i == 2) {
                    continue;
                }
                $("#cd-" + arr[1][i]).next().html("不能为空");
                $("#cd-" + arr[1][i]).next().css('display', "");
                $("#cd" + arr[1][i]).addClass("error");
                judge = 1;
            }
        }
        if (age >= 150 || age <= 0) {
            $('#cd-age').next().html("数值范围不在1~150之间");
            $('#cd-age').next().css('display', "");
            $("#cd-age").addClass("error");
            judge = 1;
        }
        var re = /^1\d{10}$/;
        if (!re.test(phone)) {
            $('#cd-phone').next().html("手机号码格式不正确");
            $('#cd-phone').next().css('display', "");
            $("#cd-phone").addClass("error");
            judge = 1;
        }
        var mail = /^\w+([-.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$/;
        if (!mail.test(email)) {
            $('#cd-email').next().html("邮箱地址格式不正确");
            $('#cd-email').next().css('display', "");
            $("#cd-email").addClass("error");
            judge = 1;
        }

        if (judge == 0) {
            var data = restful("patch", baseAddress+"/tbuser/" + userid + "/", {
                'username': name,
                'usersex': sex,
                'userage': age,
                'userwroktype': worktype,
                'userphonenumber': phone,
                'usermail': email
            });
            if (data != " ") {
                alert("修改成功！");
            }
        }
    });
}
