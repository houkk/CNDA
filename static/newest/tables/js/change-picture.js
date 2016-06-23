/**
 * Created by Mesogene on 2015/6/14.
 */
$("#mysubmit").click(function(){


    var value=$("#pic-position").val();

    var image=new Image();
    image.src=value;
    console.log(image);
    var path=$(".user_pic").attr("src");
    console.log(path);
    if(value=="未选择任何文件"){
        alert("请选择图片");
    }
    else{
        $.ajax({
            async:false,
            type:"patch",
            //dataType:'json',
            contentType:'application/json',
            url:"http://202.195.210.174:4312/tbuser/36/",
            data:JSON.stringify({'temp_picturelocationid':[{ 'originalpicturepath': path, 'pictureremarks': "head", 'pictureclass':"用户头像"}]}) ,
           /* beforeSend: function (xhr) {
                xhr.setRequestHeader("Authorization","Token "+GetCookie(''));
            },*/
            success: function (msg) {
                alert("保存成功！");
            }
        });
    }
});