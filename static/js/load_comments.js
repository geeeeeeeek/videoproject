
$(function(){
    // 页数
    var page = 0;
    // 每页展示15个
    var page_size = 15;

    // dropload
    $('.comments').dropload({
        scrollArea : window,
        loadDownFn : function(me){
            page++;

            $.ajax({
                type: 'GET',
                url: comments_url,
                data:{
                     video_id: video_id,
                     page: page,
                     page_size: page_size
                },
                dataType: 'json',
                success: function(data){
                    var code = data.code
                    var count = data.comment_count
                    if(code == 0){
                        $('#id_comment_label').text(count + "条评论");
                        $('.comment-list').append(data.html);
                        me.resetload();
                    }else{
                        me.lock();
                        me.noData();
                        me.resetload();
                    }
                },
                error: function(xhr, type){
                    me.resetload();
                }
            });
        }
    });
});