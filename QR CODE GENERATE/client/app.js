// JAVA SCRIPT
function onClickedCreateQRC() {
  console.log("Generate QR button clicked");
  var qrd = document.getElementById("qrd");
  alert("The data for Qr is: \n"+qrd.value)

  var url = "http://127.0.0.1:5000/gen_qr_code"; 

  $.post(url, {
      qrdata: qrd.value
  });
}

function loadQRC(){
  var image= document.getElementById("pic");
  image.src=`../server/QRTest.png#${new Date().getTime()}`;
}

function onPageLoad() {
  console.log( "document loaded" );
  var url = "http://127.0.0.1:5000/";
  $.get(url)
}

window.onload = onPageLoad;