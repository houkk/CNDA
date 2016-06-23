/**
 * Created by Mesogene on 2015/5/25.
 */
/*
$(document).ready(function(){

});*/
var str="<div class='in_navigation isDown'> " +
    "<div> " +
    "<div class='link-holder' > " +
    "<ul> " +
    "<div class='in_img'><img id='perPic' src='../images/3.jpg' style='width: 70px;height: 70px;overflow: hidden'></div>" +
    "<div><p style='text-decoration: underline' id='perName'>用户名</p></div>" +
    "<li><a href='userprofile.html' class='scroll-link'><span class='glyphicon glyphicon-cog'></span>&nbsp;&nbsp;个人设置</a></li>" +
    "<li><a href='../index2_2.html' class='scroll-link'><span class='glyphicon glyphicon-heart'></span>&nbsp;&nbsp;我的收藏</a></li>" +
    "<li><a href='../index2.html' class='scroll-link'><span class='glyphicon glyphicon-user'></span>&nbsp;&nbsp;我的体质</a></li>" +
    "<li><a href='#' class='scroll-link' data-toggle='modal' data-target='#myModalMessage' id='MessageReminder'><span class='glyphicon glyphicon-envelope'></span>&nbsp;&nbsp;消息中心</a></li> " +
    "<li><a href='../index2_6.html' class='scroll-link'><span class='glyphicon glyphicon-exclamation-sign'></span>&nbsp;&nbsp;预警消息</a> </li>" +
    "<li><a href='#' class='scroll-link'><span class='glyphicon glyphicon-off'></span>&nbsp;&nbsp;锁屏</a></li>" +
    "<li><a id='logout2' class='scroll-link'><span class='glyphicon glyphicon-log-out'></span>&nbsp;&nbsp;注销</a> </li> " +
    "</ul>" +
    "</div> " +
    "</div> " +
    "</div>";
$("body").prepend(str);
