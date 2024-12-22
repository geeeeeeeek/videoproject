/**
 *  https://github.com/juliomalegria/django-chunked-upload
 */
$(function () {


var md5 = "",
    lastprogress = 0,
    csrf = $("input[name='csrfmiddlewaretoken']")[0].value,
    form_data = [{"name": "csrfmiddlewaretoken", "value": csrf}];

function calculate_md5(file, chunk_size) {
  var slice = File.prototype.slice || File.prototype.mozSlice || File.prototype.webkitSlice,
      chunks = chunks = Math.ceil(file.size / chunk_size),
      current_chunk = 0,
      spark = new SparkMD5.ArrayBuffer();
  function onload(e) {
    spark.append(e.target.result);  // append chunk
    current_chunk++;
    if (current_chunk < chunks) {
      read_next_chunk();
    } else {
      md5 = spark.end();
    }
  };
  function read_next_chunk() {
    var reader = new FileReader();
    reader.onload = onload;
    var start = current_chunk * chunk_size,
        end = Math.min(start + chunk_size, file.size);
    reader.readAsArrayBuffer(slice.call(file, start, end));
  };
  read_next_chunk();
}

$("#chunked_upload").fileupload({
  url: api_chunked_uplad,
  dataType: "json",
  maxChunkSize: 100000, // Chunks of 100 kB
  formData: form_data,
  add: function(e, data) { // Called before starting upload
    var fileSize = data.originalFiles[0]['size'];
    var type = data.originalFiles[0]['type'];
    console.log('file size --> ' + fileSize);
    console.log('type --> ' + type);

    if(fileSize > 100000000){
        alert('文件太大了，请上传100M以内的文件');
        return;
    }

    if(!type.startsWith("video/")){
        alert('视频格式不正确');
        return;
    }

    // If this is the second file you're uploading we need to remove the
    // old upload_id and just keep the csrftoken (which is always first).
    form_data.splice(1);
    calculate_md5(data.files[0], 100000);  // Again, chunks of 100 kB
    data.submit();

    $('#progress_label').on('click', false);
    $('#progress_layout').show()

  },
  chunkdone: function (e, data) { // Called after uploading each chunk
    if (form_data.length < 2) {
      form_data.push(
        {"name": "upload_id", "value": data.result.upload_id}
      );
    }
    var progress = parseInt(data.loaded / data.total * 100.0, 10);
    console.log(progress);
    if(progress > lastprogress){
        lastprogress = progress
        $('#upload_progress').progress({
            percent: progress
        });
    }
  },
  done: function (e, data) { // Called when the file has completely uploaded
    $.ajax({
      type: "POST",
      url: api_chunked_upload_complete,
      data: {
        csrfmiddlewaretoken: csrf,
        upload_id: data.result.upload_id,
        md5: md5
      },
      dataType: "json",
      success: function(data) {
        console.log(data)
        $('#upload_label').text('上传成功');
        $('#upload_progress').progress({
            percent: 100
        });
        $('#next_layout').show();
        $('#next').click(function(){
            window.location = '/myadmin/video_publish/' + data.video_id
        });
      }
    });
  },
});



})