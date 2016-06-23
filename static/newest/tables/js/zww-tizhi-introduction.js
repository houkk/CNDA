/**
 * Created by Mesogene on 2015/5/15.
 */
$(document).ready(function(){
    var data=restful("get",baseAddress+"/tbphysiqueinfo/","")
    var arr={"平和质":[1,"精力<br>充沛","面色<br>红润","睡眠<br>良好","食欲<br>良好","随和<br>开朗","二便<br>正常"],
              "阳虚质":[2,"手脚<br>发凉","平时<br>怕冷","睡眠<br>偏多","容易<br>腹泻","容易<br>脱发","大便<br>稀溏"],
              "阴虚质":[3,"手脚<br>发热","两颧<br>潮红","总想<br>喝水","大便<br>干燥","眼睛<br>干涩","容易<br>失眠"],
              "痰湿质":[4,"腹部<br>松软","体型<br>肥胖","痰多","脸上<br>出油多","容易<br>困倦","感到<br>身体沉"],
              "湿热质":[5,"面部<br>油腻","口苦<br>口臭","易长<br>痤疮","大便<br>黏滞","皮肤<br>瘙痒","脾气<br>急躁"],
              "气郁质":[6,"闷闷<br>不乐","精神<br>紧张","容易<br>受惊吓","睡眠<br>较差","经常<br>叹气","体型<br>偏瘦"],
              "气虚质":[7,"容易<br>疲乏","肌肉<br>松软","声音<br>低弱","容易<br>出汗","喜欢<br>安静","容易<br>感冒"],
              "血瘀质":[8,"口唇<br>偏暗","皮肤<br>易淤青","容易<br>忘事","牙龈<br>易出血","皮肤<br>粗糙","眼里<br>血丝多"],
              "特禀质":[9,"容易<br>过敏","易得<br>荨麻疹","皮肤易<br>有抓痕","经常<br>打喷嚏","经常<br>流鼻涕","经常<br>鼻塞"]};
    var img="yinxu.jpg";
    $(".button--itzel").click(function(){
        var k=$(this).find("span").text();
        var str="<h4>-----------------------------------------------"+k+"----------------------------------------------</h4>" +
            "<div class='base_style color_blue'>"+arr[k][1]+"</div>" +
            "<div class='base_style color_purple'>"+arr[k][2]+"</div> " +
            "<div class='base_style color_green'>"+arr[k][3]+"</div>" +
            "<div class='base_style color_red'>"+arr[k][4]+"</div> " +
            "<div class='base_style color_yellow'>"+arr[k][5]+"</div> " +
            "<div class='base_style color_pink'>"+arr[k][6]+"</div>" +
          /*  "<img src="+data[arr[k][0]-1].temp_picturelocationid+" class='image_style'/>" +*/
            "<li style='margin-top: 15%'><div><strong>体质描述：</strong></div><div class='where'>"+data[arr[k][0]-1].physicalinterpretation+"</div></li>" +
            "<li><div><strong>总体特征：</strong></div><div class='where'>"+data[arr[k][0]-1].generacharacter+"</div></li>" +
            "<li><div><strong>形体特征：</strong></div><div class='where'>"+data[arr[k][0]-1].shapefeature+"</div></li>" +
            "<li><div><strong>常见表现：</strong></div><div class='where'>"+data[arr[k][0]-1].commonmanifest+"</div> </li> " +
            "<li><div><strong>心理特征：</strong></div><div class='where'>"+data[arr[k][0]-1].mentalcharacter+"</div></li>" +
            "<li><div><strong>发病倾向：</strong></div><div class='where'>"+data[arr[k][0]-1].incidencetendency+"</div></li>" +
            "<li><div><strong>适应能力：</strong></div><div class='where'>"+data[arr[k][0]-1].adaptivecapacity+"</div></li>" +
            "<li><div><strong>形成原因：</strong></div><div class='where'>"+data[arr[k][0]-1].physicalreason+"</div></li>" +
            "<li><div><strong>注意事项：</strong></div><div class='where'>"+data[arr[k][0]-1].foodallowtaboo+"</div></li>";
        $("#introduction").html(str);
    });
    $("#first").click();
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