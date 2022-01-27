ID;
current_id;
function delete_customer_get(ID,current_id){
    this.ID = ID
    this.current_id = current_id
}

function delete_customer(){
    window.location.href = "../delete_customer/?ID=" + this.ID + "&current_id=" + this.current_id 
}