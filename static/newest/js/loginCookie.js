$(function(){
    $.ajax({
        async:false,
        type:"get",
        contentType:'application/json',
        url:baseAddress+"/me/",
        beforeSend: function (xhr) {
            //alert(GetCookie());
            xhr.setRequestHeader("Authorization","Token "+GetCookie());
        },
        success: function (msg) {
            //alert(msg);
            var user=msg[0].username;
            var userPicture=msg[0].temp_picturelocationid;
            $("#login").html(user);
            $("#login").attr("href","#");
            $("#perName").html(user);
            //alert(userPicture);
            if(userPicture!=null){
                $("#perPic").attr("src",userPicture);
            }
        }
    });

    //注销用户
    $("#logout").click(function () {
        DeleteCookie();
        window.location.href='loginPage/index.html';
    });

    $("#logout2").click(function () {
        DeleteCookie();
        window.location.href='../loginPage/index.html';
    })
});