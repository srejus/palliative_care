function hireRequestCareWorker(id){
    fetch('http://127.0.0.1:8000/elders/care-workers/request/'+id);
    alert("Request sent Successfully!");
}

function hireRequestMedicalWorker(id){
    fetch('http://127.0.0.1:8000/elders/medical-workers/request/'+id);
    alert("Request sent Successfully!");
}