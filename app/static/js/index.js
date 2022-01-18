$(function () {
    $(".btn-delete").click(function(){
        var id = $(this).attr('data-id');
        if(confirm("Are your sure?")) {
            $.ajaxSetup({
                headers: {
                    'X-CSRF-TOKEN': $('meta[name="csrf-token"]').attr('content')
                }
            });

            $.ajax({url: url,
                method: 'post',
                data: {id:id},
                success: function(result){
                   console.log(result);
                   if(result.success) {
                        alert(result.message);
                       location.reload()
                   } else {
                       alert(result.message);
                   }
                }});
        }
    });

    $(".btn-edit").click(function(){
        var id = $(this).attr('data-id');
        location.href = urledit + `?id=${id}`;
    });

    $("#selectItem").change(function(){
        location.href = '/main' + `?id=${value}`;
    });



});
