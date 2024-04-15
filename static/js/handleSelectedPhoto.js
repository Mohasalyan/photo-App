// let filtes = "";
let filtes = document.querySelectorAll('.filters');
let resizeButton = document.querySelector('.ResizeSend');
filtes.forEach((e) => {
    e.addEventListener('click', function () {
        console.log(e.getAttribute('name'))
        console.log(window.isImgSelected)
        if (window.isImgSelected.length > 0) {
            fetch(`${window.location.href}/filter/filter`, {
                method: 'POST',
                body: JSON.stringify({ 'imageList': window.isImgSelected, 'filter': e.getAttribute('name') }),
                "headers": { "Content-Type": "application/json" },
            }).then(function (response) {
                if (response.status == 200) {
                    console.log('s')
                    window.isImgSelected.forEach((imageName) => {
                        document.querySelector(`[name="${imageName}"]`).nextSibling.remove()
                        document.querySelector(`[name="${imageName}"]`).src = ""
                        document.querySelector(`[name="${imageName}"]`).src = `/filter/${imageName}`
                    })
                }
            })
            // document.querySelector('[name="runtime.png"]')
        }
    })
})

resizeButton.addEventListener('click', function () {

    let ResizeImg = document.querySelector('#ResizeImg');
    if (window.isImgSelected.length > 0) {
        fetch(`${window.location.href}/resize/resize`, {
            method: 'POST',
            body: JSON.stringify({ 'image': window.isImgSelected[0], 'sizeIndex':ResizeImg.selectedIndex }),
            "headers": { "Content-Type": "application/json" },
        }).then(function (response) {
            if (response.status == 200) {

                document.querySelector(`[name="${window.isImgSelected[0]}"]`).nextSibling.remove()
                document.querySelector(`[name="${window.isImgSelected[0]}"]`).src = ""
                setTimeout(() => {   document.querySelector(`[name="${window.isImgSelected[0]}"]`).src = `/filter/${window.isImgSelected[0]}` }, 1000);
              
                console.log(12)
            }
        })
    }
    // ResizeImg.options[ResizeImg.selectedIndex].text

});
