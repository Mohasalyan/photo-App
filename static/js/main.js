let numofimg=0; 
//upload image by selceting 
const loadFile = (event) => {

    for (let i = numofimg; i < ((event.target.files.length)+numofimg); i++) {
        //creat a container for each image
        let imageCont = document.createElement('div');
        imageCont.className = "imageCont";
        imageCont.id = "imageCont-" + i;
        document.querySelector(".cont").appendChild(imageCont);

        // get images link and creat images
        let image = document.createElement('img');
        image.src = URL.createObjectURL(event.target.files[i-numofimg]);
        image.id = `imageNum-` + i;
        document.querySelector("#imageCont-" + i).appendChild(image);

        //get a natural size for image and creat a span for each image to show the size of image
        image.onload = ()=>{
            getSize(image, i);
        }
    }
    let upload = document.getElementById("upload").classList.add("disableUpload")
    let moreUpload = document.getElementById("moreUpload").classList.remove("disableUpload") 
    numofimg += event.target.files.length;
};

//upload image by drag and drop
const dragging = (e) => {
    e.preventDefault();
  };

const onDrop = (event) => {
    event.preventDefault();
    const { files } = event.dataTransfer;
    for (let i = numofimg; i < (files.length)+numofimg; i++) {
        let imageCont = document.createElement('div');
        imageCont.className = "imageCont";
        imageCont.id = "imageCont-" + i;
        document.querySelector(".cont").appendChild(imageCont);

        // get images link and creat images
        let image = document.createElement('img');
        image.src = URL.createObjectURL(files[i-numofimg]);
        image.id = `imageNum-` + i;
        document.querySelector("#imageCont-" + i).appendChild(image);

        //get a natural size for image and creat a span for each image to show the size of image
        image.onload = function(){
            getSize(image, i);
        }
    }
    let upload = document.getElementById("upload").classList.add("disableUpload")
    let moreUpload = document.getElementById("moreUpload").classList.remove("disableUpload") 
    numofimg+=files.length;
  };



// get image size (width*height) and add span element under the image in the page
function getSize(image, i){
    let imgWidth = image.naturalWidth;
    let imgHight = image.naturalHeight;
    let size = document.createElement('span');
    let txt = document.createTextNode(imgWidth + "x" + imgHight);
    size.id = "sizeOfImgNum-" + i;
    size.appendChild(txt)
    document.querySelector("#imageCont-" + i).appendChild(size);
}


let ResizeHeader = document.querySelector('.ResizeHeader')
ResizeHeader.addEventListener("click", function() {
    let resizeCont= document.querySelector('.resizeCont')
    resizeCont.classList.remove("dsiable")
})

let ResizeCancle = document.querySelector('.ResizeCancle')
ResizeCancle.addEventListener('click', function(){
    let resizeCont= document.querySelector('.resizeCont')
    resizeCont.classList.add("dsiable")
})