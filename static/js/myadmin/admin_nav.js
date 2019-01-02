$(function(){
    var pathname = window.location.pathname;
    console.log(pathname);
    if(pathname.endsWith("myadmin/")) {
        $("#index").addClass("active");
    }
    if(pathname.endsWith("myadmin/video_list/")) {
        $("#video_list").addClass("active");
    }
    if(pathname.indexOf("myadmin/video_edit/") >= 0){
        $("#video_list").addClass("active");
    }
    if(pathname.endsWith("myadmin/video_add/")) {
        $("#video_add").addClass("active");
    }
    if(pathname.endsWith("myadmin/classification_list/")) {
        $("#classification_list").addClass("active");
    }
    if(pathname.indexOf("myadmin/classification_edit/") >= 0){
        $("#classification_list").addClass("active");
    }
    if(pathname.endsWith("myadmin/classification_add/")) {
        $("#classification_add").addClass("active");
    }
    if(pathname.endsWith("myadmin/user_list/")) {
        $("#user_list").addClass("active");
    }
    if(pathname.indexOf("myadmin/user_edit/") >= 0){
        $("#user_list").addClass("active");
    }
    if(pathname.endsWith("myadmin/user_add/")) {
        $("#user_add").addClass("active");
    }
    if(pathname.endsWith("myadmin/comment_list/")) {
        $("#comment_list").addClass("active");
    }
    if(pathname.indexOf("myadmin/setting/") >= 0) {
        $("#setting").addClass("active");
    }
    if(pathname.indexOf("myadmin/subscribe/") >= 0){
        $("#subscribe").addClass("active");
    }
    if(pathname.indexOf("myadmin/feedback_list/") >= 0){
        $("#feedback_list").addClass("active");
    }
});