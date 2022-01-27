var visual_id;
function delete_batch_get(visual_id){
    this.visual_id = visual_id
}
function delete_batch(){
    window.location.href = "../delete_batch/?visual_id=" + this.visual_id
}