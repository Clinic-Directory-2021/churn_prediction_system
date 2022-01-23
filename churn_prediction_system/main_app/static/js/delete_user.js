var uid;
var user_id;
function delete_user(){
    window.location.href = "../delete_user/?uid=" + this.uid + "&user_id=" + this.user_id
}

function delete_user_data(uid, user_id){
    this.uid = uid
    this.user_id = user_id
}