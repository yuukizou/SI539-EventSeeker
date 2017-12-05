function checkFormSave() {
  var span = document.getElementsByClassName("close")[0];
  var modal_cr = document.getElementById('myModal');

  document.getElementById('myModal').style.display = "block";

  window.onclick = function(event) {
    if (event.target == modal_cr) {
      modal_cr.style.display = "none";
    };
    span.onclick = function() {
      modal_cr.style.display = "none";
    };
  };

};
function checkFormPub() {
  console.log("Test")
  var eventTitle = document.getElementById("eventTitle");
  var eventLocation = document.getElementById("eventLocation");
  var eventOrganizer = document.getElementById("organizer");
  var date = document.getElementById("date");
  var time = document.getElementById("time");
  var span = document.getElementsByClassName("close")[1];
  var modal_cr = document.getElementById('myModal_publish');

  if(eventTitle.value== "" || eventLocation.value== "" || eventOrganizer.value== "" || date.value== "" || time.value== "") {
    alert("Please finish the form first!")
  }
  else {
    modal_cr.style.display = "block";
  };
  span.onclick = function() {
    console.log("CLose span")
    modal_cr.style.display = "none";
  };
  window.onclick = function(event) {
    if (event.target == modal_cr) {
      modal_cr.style.display = "none";
    };
  };


};

document.getElementById("save_btn").addEventListener("click", checkFormSave);
document.getElementById("publish_btn").addEventListener("click", checkFormPub);
