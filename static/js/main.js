let numofimg=0; 
let imgSrcArr=[];
let imageSelectIcons;
let isImgSelected = [];
let ImagesUploadedToBackend =[] 
let imageFormData = new FormData()
window.isImgSelected = isImgSelected // globale variable for another files 

//upload image by selceting 
const loadFile = (event) => {
    for (let i = numofimg; i < ((event.target.files.length)+numofimg); i++) {
        //creat a container for each image
        let imageCont = document.createElement('div');
        imageCont.className = "imageCont";
        imageCont.id = "imageCont-" + i;
        document.querySelector(".cont").appendChild(imageCont);
        addSelectImg(i);

        // get images link and creat images
        let image = document.createElement('img');
        image.src = URL.createObjectURL(event.target.files[i-numofimg]);
        image.setAttribute('name',event.target.files[i-numofimg].name) // insert attribute name to refer to the name file of image
        imgSrcArr.push(image.src);
        image.id = `imageNum-` + i;
        image.className = "myImg"
        document.querySelector("#imageCont-" + i).appendChild(image);
        /*
        collect the image uploaded to send to back-end
        */
        imageFormData.append('files', event.target.files[i - numofimg]) 
        imageFormData.append('name', event.target.files[i - numofimg].name)         
        //get a natural size for image and creat a span for each image to show the size of image
        image.onload = ()=>{
            getSize(image, i);
        }
    }
    fetch(`${ window.location.href}/ImageUploaded`, { 
        method: 'POST', 
        body: imageFormData, 
    }).then(function (response) { 
        // console.log(response) 
        imageFormData =new FormData(); 
    }) 
    let upload = document.getElementById("upload").classList.add("disableUpload")
    let moreUpload = document.getElementById("moreUpload").classList.remove("disableUpload") 
    numofimg += event.target.files.length;
    imageSelectIcons = document.querySelectorAll(".selectIcon");
    imageSelectIcons.forEach(getImgSelected);
    imagePopUp(imgSrcArr)

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

        addSelectImg(i);

        // get images link and creat images
        let image = document.createElement('img');
        image.src = URL.createObjectURL(files[i-numofimg]);
        imgSrcArr.push(image.src);
        image.id = `imageNum-` + i;
        image.className = "myImg"
        image.setAttribute('name',event.target.files[i-numofimg].name) // insert attribute name to refer to the name file of image
        document.querySelector("#imageCont-" + i).appendChild(image);

        imageFormData.append('files', files[i - numofimg]) 
        imageFormData.append('name', files[i - numofimg].name)       
        //get a natural size for image and creat a span for each image to show the size of image
        image.onload = function(){
            getSize(image, i);
        }

    }
    fetch(`${ window.location.href}/ImageUploaded`, { 
        method: 'POST', 
        body: imageFormData, 
    }).then(function (response) { 
        // console.log(response) 
        imageFormData =new FormData(); 
    }) 
    let upload = document.getElementById("upload").classList.add("disableUpload")
    let moreUpload = document.getElementById("moreUpload").classList.remove("disableUpload") 
    numofimg+=files.length;
    imageSelectIcons = document.querySelectorAll(".selectIcon");
    imageSelectIcons.forEach(getImgSelected);
    let allImg = document.querySelectorAll(".myImg")
    allImg.forEach(imagePopUp);
  };



// get image size (width*height) and add span element under the image in the page
function getSize(image, i){
    let imgWidth = image.naturalWidth;
    let imgHight = image.naturalHeight;
    let size = document.createElement('span');
    let txt = document.createTextNode(imgWidth + "x" + imgHight + " px");
    size.id = "sizeOfImgNum-" + i;
    size.appendChild(txt)
    document.querySelector("#imageCont-" + i).appendChild(size);
}


function addSelectImg(i){
    let selectIcon = document.createElement('span');
    selectIcon.classList.add("selectIcon")
    selectIcon.id = "selectIcon" + i;
    document.querySelector("#imageCont-" + i).appendChild(selectIcon);  
}


function getImgSelected(item){
    item.addEventListener('click', function(){
        if(!(item.classList.contains("bgFill"))){
            item.classList.add("bgFill")
            // console.log(document.getElementById("imageNum-" + item.id.slice(10, item.id.length)))
            isImgSelected.push(document.getElementById("imageNum-" + item.id.slice(10, item.id.length)).name)//change to name
            // console.log(isImgSelected)
            window.isImgSelected = isImgSelected
        }
        else{
            item.classList.remove("bgFill")
            isImgSelected = isImgSelected.filter(e => e!== (document.getElementById("imageNum-" + item.id.slice(10, item.id.length)).name))
            // console.log(isImgSelected)
            window.isImgSelected = isImgSelected
        }
    })
}





//  select custm size of image problem
let ResizeImgSelect = document.getElementById("ResizeImg")
let inputInResizeInput = document.querySelectorAll(".resizeInput input")
if(!(ResizeImgSelect.value === "custom")){
    inputInResizeInput.forEach((e)=>{
        e.value = null
        e.setAttribute("readonly", "readonly")
    })
}
else{
    inputInResizeInput.forEach((e)=>{
        e.removeAttribute("readonly", "readonly")
    })
}

ResizeImgSelect.addEventListener("change", ()=>{
    if(!(ResizeImgSelect.value === "custom")){
        inputInResizeInput.forEach((e)=>{
            e.value = null
            e.setAttribute("readonly", "readonly")
        })
    }
    else{
        inputInResizeInput.forEach((e)=>{
            e.removeAttribute("readonly", "readonly")
        })
    }
})











let ulOfCol2 = document.querySelectorAll(".sidebar .row .col2 ul")
ulOfCol2.forEach((e, i) =>{
    if(!(ulOfCol2[0] ===e)){
        e.classList.add("noneDisplay")
    }
})


let colOneSidebarList = document.querySelectorAll("#colOneSidebarList li")
colOneSidebarList.forEach((el, i)=>{
    el.addEventListener("click", ()=>{
        colOneSidebarList.forEach((el1, i2)=>{
            if(!(el == el1)){
                el1.classList.remove("liActive")
                el1.firstElementChild.firstElementChild.src = el1.firstElementChild.firstElementChild.src.slice(0, el1.firstElementChild.firstElementChild.src.indexOf("com")+3) + ".svg"

                document.querySelector(".ulNum-" + i2).classList.add("noneDisplay")
            }
            else{

                    el.classList.add("liActive")
                    el.firstElementChild.firstElementChild.src = el.firstElementChild.firstElementChild.src.slice(0, el.firstElementChild.firstElementChild.src.indexOf("com")+3) + "-fill.svg"

                document.querySelector(".ulNum-" + i2).classList.remove("noneDisplay")
            }
        })
    })

})


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


let popUpWindow = document.querySelector(".popUp")
function imagePopUp(arr){
    let mainImg = document.querySelector(".popUp .mainImg .img")
    let elseImg = document.querySelector(".popUp  .elseImg")
    let allImg = document.querySelectorAll("#moreUpload .imageCont img")
    let closePopUp = document.querySelector(".closePopUp")
    let imggg = document.createElement("img")
    let pre = document.querySelector(".pre")
    let next = document.querySelector(".nex")

    for(let i = 1; i<=arr.length; i++){
        let image = document.createElement('img');
        image.src = arr[i-1]
        image.className = "imgPopUp-" + i
        elseImg.appendChild(image)
    }
    
    allImg.forEach((item,i)=>{
        item.addEventListener('click', function(){

            imggg.src = item.src
            mainImg.appendChild(imggg)
            document.getElementById("moreUpload").style.opacity = 0.5;
            document.querySelector(".cont").classList.add("hidden")
            popUpWindow.classList.remove("disable")
            console.log()
            for(let i = 1; i<=arr.length; i++){
                if(imggg.src == arr[i-1]){
                    document.querySelector(".imgPopUp-" + i).style.opacity = 1
                }
                else{
                    document.querySelector(".imgPopUp-" + i).style.opacity = 0.5
                }
            }


        })
        closePopUp.addEventListener('click', ()=>{
            imggg.innerHTML = ''
            popUpWindow.classList.add("disable")
            document.querySelector(".cont").classList.remove("hidden")
            document.getElementById("moreUpload").style.opacity = 1;
        })


    })

    pre.addEventListener('click', ()=>{
        if(arr.indexOf(imggg.src)>0){
            imggg.src = arr[arr.indexOf(imggg.src)-1]
        }
        else{
            imggg.src = arr[arr.length-1]
        }
        for(let i = 1; i<=arr.length; i++){
            if(imggg.src == arr[i-1]){
                document.querySelector(".imgPopUp-" + i).style.opacity = 1
            }
            else{
                document.querySelector(".imgPopUp-" + i).style.opacity = 0.5
            }
        }

    })
    next.addEventListener('click', ()=>{
        if(arr.indexOf(imggg.src)< arr.length-1){
            imggg.src = arr[arr.indexOf(imggg.src)+1]
        }
        else{
            imggg.src = arr[0]

        }
        for(let i = 1; i<=arr.length; i++){
            if(imggg.src == arr[i-1]){
                document.querySelector(".imgPopUp-" + i).style.opacity = 1
            }
            else{
                document.querySelector(".imgPopUp-" + i).style.opacity = 0.5
            }
        }
    })


}