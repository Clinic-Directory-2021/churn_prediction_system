var user_id;
function get_edit_data(first_name, last_name, email, selected_id, ){

$('#first_name_edit').val(first_name)
$('#last_name_edit').val(last_name)
$('#email_edit').val(email)

}
function get_status(status,user_id){
    $('#status_edit').val(status)
    $('#selected_id').val(user_id)
}