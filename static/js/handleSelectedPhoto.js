// let filtes = "";
let filtes = document.querySelectorAll('.filters');
filtes.forEach((e) => {
    e.addEventListener('click', function () {
        console.log(e.getAttribute('name'))
        console.log(window.isImgSelected)
        if (window.isImgSelected.length > 0) {
            fetch(`${window.location.href}/filter/filter`, {
                method: 'POST',
                body: JSON.stringify({ 'imageList': window.isImgSelected, 'filter': e.getAttribute('name') }),
                "headers": {"Content-Type": "application/json"},
            }).then(function(response){ 
                if(response.status == 200) { 
                    console.log('s')
                    window.isImgSelected.forEach((imageName)=>{ 
                        document.querySelector(`[name="${imageName}"]`).nextSibling.remove()
                        document.querySelector(`[name="${imageName}"]`).src =""
                        document.querySelector(`[name="${imageName}"]`).src = `/filter/${imageName}`
                    })
                }
            })
            // document.querySelector('[name="runtime.png"]')
        }
    })
})

console.log()