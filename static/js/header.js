

$(function(){

    // 头像dropdown
    $('#v-header-avatar').dropdown();

    $('#v-search').bind('keypress',function(event){
        var word = $('#v-search').val()
        if(event.keyCode == "13" && word.length > 0)
        {
            window.location = search_url + '?q='+word;
        }
    });

    $('#search').click(function(){
        var word = $('#v-search').val()
        if(word.length > 0){
            window.location = search_url + '?q='+word;
        }
    });

    var explorerName = getExploreName();
    if(explorerName.startsWith("Safari")||explorerName.startsWith("IE")){
        alert("请使用Chrome浏览器访问该网站");
    }

    function getExploreName(){
      var userAgent = navigator.userAgent;
      if(userAgent.indexOf("Opera") > -1 || userAgent.indexOf("OPR") > -1){
        return 'Opera';
      }else if(userAgent.indexOf("compatible") > -1 && userAgent.indexOf("MSIE") > -1){
        return 'IE';
      }else if(userAgent.indexOf("Edge") > -1){
        return 'Edge';
      }else if(userAgent.indexOf("Firefox") > -1){
        return 'Firefox';
      }else if(userAgent.indexOf("Safari") > -1 && userAgent.indexOf("Chrome") == -1){
        return 'Safari';
      }else if(userAgent.indexOf("Chrome") > -1 && userAgent.indexOf("Safari") > -1){
        return 'Chrome';
      }else if(!!window.ActiveXObject || "ActiveXObject" in window){
        return 'IE>=11';
      }else{
        return 'Unkonwn';
      }
    }

});
