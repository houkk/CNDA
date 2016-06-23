/**
 * Created by Mesogene on 2015/6/11.
 */
var judge1,judge2,judge3=0;
$("#cd-password").blur(function(){
    judge1 = 0;
    $(this).next().css('display', "none");
    $(this).removeClass("error");
    var oldpassword = $("#cd-password").val().trim();
    if (oldpassword=="") {
        $('#cd-password').next().html("不能为空");
        $('#cd-password').next().css('display', "");
        $("#cd-password").addClass("error");
        judge1 = 1;
    }
});
$("#new-password").blur(function(){
    judge2 = 0;
    $(this).next().css('display', "none");
    $(this).removeClass("error");
    var newpassword = $("#new-password").val().trim();
    if (newpassword=="") {
        $('#new-password').next().html("不能为空");
        $('#new-password').next().css('display', "");
        $("#new-password").addClass("error");
        judge2 = 1;
    }
});
$("#new-password2").blur(function(){
    judge3 = 0;
    $(this).next().css('display', "none");
    $(this).removeClass("error");
    var newpassword = $("#new-password").val().trim();
    var newpassword2 = $("#new-password2").val().trim();
    if (newpassword2=="") {
        $('#new-password2').next().html("不能为空");
        $('#new-password2').next().css('display', "");
        $("#new-password2").addClass("error");
        judge3 = 1;
    }
    if(newpassword!=newpassword2){
        $('#new-password2').next().html("两次密码不一致");
        $('#new-password2').next().css('display', "");
        $("#new-password2").addClass("error");
        judge3 = 1;
    }
});

$("#mysubmit").click(function () {
    var oldpassword = $("#cd-password").val();
    var newpassword = $("#new-password").val();
    var newpassword2 = $("#new-password2").val();
    if(judge1==0&&judge2==0&&judge3==0){
        $.ajax({
            url:baseAddress+'/changepassword/',
            type:'post',
            dataType:'json',
            data:{'new_password': newpassword, 'current_password': oldpassword},
            beforeSend:function(xhr) {
                xhr.setRequestHeader("Authorization", 'Token '+GetCookie());

            },
            error:function(msg){
                if(msg.status==401){
                    alert("未登录");
                }
                else if(msg.status==400){
                    alert("原密码输入错误");
                }
                else{
                    alert("保存成功");
                    DeleteCookie();
                    window.location.href="../loginPage/index.html";
                }
            }
        });
    }


});