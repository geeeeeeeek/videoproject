

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
    })
});
