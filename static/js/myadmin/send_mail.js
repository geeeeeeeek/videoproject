
// 写入csrf
$.getScript("/static/js/csrftoken.js");

$('#send-mail').click(function(){

    var video_id = $('.selection.dropdown').dropdown('get value');

    if(video_id == ''){
        alert("不能为空");
        return;
    }
    $('#send-mail-progress').text('正在发送通知...')
    $.ajax({
        url: api_send_mail,
        data: {
            'video_id':video_id,
            'csrf_token': csrftoken
        },
        type: 'POST',
        dataType: 'json',
        success: function (data) {
            console.log(data);
            var code = data.code
            var msg = data.msg
            if(code == 0){
                $('#send-mail-progress').text('发送成功')
            }else{
                $('#send-mail-progress').text(msg)
            }

        },
        error: function(data){
          $('#send-mail-progress').text('发送失败')
        }
    });
});