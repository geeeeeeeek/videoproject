$(function(){
    var pathname = window.location.pathname;
    console.log(pathname);
    if(pathname.indexOf("myadmin/index/") >= 0 ) {
        $("#index").addClass("active");
    }
    if(pathname.indexOf("myadmin/video_list/") >= 0 ) {
        $("#video_list").addClass("active");
    }
    if(pathname.indexOf("myadmin/video_add/") >= 0 ) {
        $("#video_add").addClass("active");
    }
    if(pathname.indexOf("myadmin/user_list/") >= 0 ) {
        $("#user_list").addClass("active");
    }
    if(pathname.indexOf("myadmin/user_add/") >= 0 ) {
        $("#user_add").addClass("active");
    }
    if(pathname.indexOf("myadmin/comment_list/") >= 0 ) {
        $("#comment_list").addClass("active");
    }
    if(pathname.indexOf("myadmin/setting/") >= 0 ) {
        $("#setting").addClass("active");
    }
});