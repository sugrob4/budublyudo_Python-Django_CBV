$(document).ready(function(){
	$('input[placeholder], textarea[placeholder]').focus(function(){
       $(this).data('placeholder',$(this).attr('placeholder'));
       $(this).attr('placeholder','');
    }).blur(function(){
       $(this).attr('placeholder',$(this).data('placeholder'));
    });

    $("#formID").validationEngine();

    $('#auth').submit(function(e){
        e.preventDefault();
        var data = $(this).serialize();
        $.ajax({
            type: "POST",
            url: "/login/",
            data: data,
            cache: false,
            success: function(data){
                if (data == 'ok'){
                  location.reload();
                }
                else{
                  $('#h2_auth').hide();
                  $('.login_error').remove();
                  $('.autorization').prepend('<h2 class="login_error"></h2>');
                  $('.login_error').hide().fadeIn(500).html(data);
                }
            }
       });
    });

    new WOW().init();
});
