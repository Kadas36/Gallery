var modal = document.getElementById("imageModal");
var i;
for (i = 0; i < 20; i++) {
    var x = document.getElementsByClassName("myImg")[i].id;
    var img = document.getElementById(x);
    var modalImg = document.getElementById("img01");
    var captionText = document.getElementById("caption");
    var imageUrl = document.getElementById('url')
    console.log(imageUrl)
    img.onclick = function(){
        modal.style.display = "block";
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
        imageUrl.innerHTML = this.src;
    

    
    var span = document.getElementsByClassName("close")[0];
    span.onclick = function() { 
        modal.style.display = "none";
    }    
}
    
}




