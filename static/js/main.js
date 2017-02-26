/**
 * Created by Tal Taub on 23/02/2017.
 */


$(document).ready(function () {
    validate_inputs("#email", "#val_email","#email_wrap");
    validate_inputs("#password", "#val_password","#pass_wrap");
});


function validate_inputs(input1, input2, wraper) {
    $(input2).keyup(function () {
        if ($(input1).val().toLowerCase() == $(input2).val().toLowerCase()) {
            $(wraper).removeClass("has-warning");
            $(wraper).addClass("has-success");
        }
        else {
            $(wraper).removeClass("has-success");
            $(wraper).addClass("has-warning");
        }
    });
}