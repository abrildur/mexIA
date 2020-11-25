function draw(id,color) {
    var canvas = document.getElementById(id);
    if (canvas.getContext) {
      var ctx = canvas.getContext('2d');  
      ctx.lineWidth = 4;
      ctx.strokeStyle = color;    
      ctx.strokeRect(40,40,40,40);
    }
}

var object_colors = [ "bebida",
        "calavera_completa",
        "calavera_de_dulce",
        "cempasuchil",
        "comida",
        "cruz",
        "fruta",
        "pan_de_muerto",
        "papel_picado",
        "retrato" ];
var colorsvalue = [
    "lightgreen",
    "yellow",
    "yellow",
    "orange",
    "blue",
    "gold",
    "magenta",
    "darkcyan",
    "red",
    "cyan"
];
      
var myFile = document.getElementById('fileAjax');  // Our HTML files' ID
var statusP = document.getElementById('status');
var myForm = document.getElementById('formAjax');  // Our HTML form's ID
var imageDiv = document.getElementById('imageDiv');
myForm.onsubmit = function(event) {
    event.preventDefault();

    statusP.innerHTML = 'Uploading...';

    // Get the files from the form input
    var files = myFile.files;

    // Create a FormData object
    var formData = new FormData();

    // Select only the first file from the input array
    var file = files[0]; 

    // Check the file type
    if (!file.type.match('image.*')) {
        statusP.innerHTML = 'The file selected is not an image.';
        return;
    }

    // Add the file to the AJAX request
    formData.append('file', file, file.name);

    // Set up the request
    var xhr = new XMLHttpRequest();

    // Open the connection
    xhr.open('POST', 'http://127.0.0.1:5000/predict_image', true);
    xhr.setRequestHeader("X-My-Custom-Header", "some value");
    // Set up a handler for when the task for the request is complete
    xhr.onload = function () {
      if (xhr.status == 200) {
        statusP.innerHTML = 'Upload copmlete!';
        var obj = JSON.parse(this.responseText);
        var sinduplicados = [...new Set(obj)];
         
        location.reload(); 
      } else {
        statusP.innerHTML = 'Upload error. Try again.';
      }
    };
    // Send the data.
    xhr.send(formData);
}



