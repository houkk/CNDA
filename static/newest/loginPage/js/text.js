$(function () {
    //点击登录进行判断
    $("#submit").click(function () {
        var user=$("#username").val();
       // alert(user);
        var pass=$("#password").val();
        $.ajax({
            async:false,
            type:"get",
            dataType:"json",
            url:baseAddress+"/validate/",
            data:{"username":user},
            success:function(msg){
               // alert(msg);
                if(msg.result==0){
                    alert("该用户名不存在！");
                    $('#username').focus();
                    $('#password').val("");
                }
                else if(msg.result==1){
                    $.ajax({
                        async:false,
                        type:"post",
                        dataType:"json",
                        url:baseAddress+"/auth/login",
                        data:{"username": user,"password":pass},
                        success: function (msg) {
                          //  alert("success"+msg.auth_token);
                            var authtoken=msg.auth_token;
                            SetCookie(authtoken);
                           // alert("success");
                            location.href=document.referrer;

                        },
                        error: function () {
                            alert("密码错误！");
                            $("#password").val("").focus();
                        }
                    });
                }
            }
        })
    });

    $("body").keydown(function() {
        if (event.keyCode == "13") {       //keyCode=13是回车键
            $('#submit').click();
        }
    });

    document.onkeydown = function(event) {
        e = event ? event : (window.event ? window.event : null);
        if (e.keyCode == 13) {
            $('#submit2').click();
        }
    };

    //点击注册
    $("#submit2").click(function () {
        var user2=$("#username2").val();
        // alert(user);
        var pass2=$("#password2").val();
        var pass3=$("#password3").val();
        var email=$("#email").val();
        if(pass2==pass3){
            $.ajax({
                async:false,
                type:"post",
                dataType:"json",
                url:baseAddress+"/auth/register",
                data:{'username': user2, 'password': pass2, 'email': email},
                success:function(msg){
                    SetCookie(msg.auth_token);
                    alert("success");
                    history.go(-1);
                }
            })
        }
        else{
            alert("两次输入密码不相同");
            $("#password2").val("").focus();
            $("#password3").val("");
        }

    });

});