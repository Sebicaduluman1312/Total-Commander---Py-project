var pathSelector1 = document.querySelector(".first_input")
var currentPath1 = pathSelector1.value

var pathSelector2 = document.querySelector(".second_input")
var currentPath2 = pathSelector2.value

var createFolder = document.querySelector(".create_folder")
var createFile = document.querySelector(".create_file")
var modalFile = document.querySelector(".modal-file")
var modalFolder = document.querySelector(".modal-folder")



createFolder.addEventListener('click', function(){

    modalFolder.style.display = 'flex'
    modalFolder.style.justifyContent = 'center'
    modalFolder.style.alignItems = 'center'

    var submit = document.querySelector(".submit-name")
    var close = document.querySelector(".close-modal")


    submit.addEventListener('click', function(){
        var nameOfNewFolder = document.getElementById("newFolder")
        var panelFor = document.getElementById("selector-panel")

        var name = nameOfNewFolder.value
        var panel = panelFor.value

        var data_to_send = {
            folder_name : name,
            current_panel : panel
        }

        fetch('/create_folder',{
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify(data_to_send) 
        })
        .then(response => response.json())
        .then(data => {
            console.log('Server response: ', data)
        })
        .catch(error => {
            console.error('Eroare:', error)
        })
    })


    close.addEventListener('click', function(){
        modalFolder.style.display = 'none'
        window.location.reload()

    })


})


createFile.addEventListener('click', function(){

    modalFile.style.display = 'flex'
    modalFile.style.justifyContent = 'center'
    modalFile.style.alignItems = 'center'

    var submit = document.querySelector(".submit-name-file")
    var close = document.querySelector(".close-modal-file")


    submit.addEventListener('click', function(){
        var nameOfNewFile = document.getElementById("newFile")
        var panelFor = document.getElementById("selector-panel-file")

        var name = nameOfNewFile.value
        var panel = panelFor.value

        var data_to_send = {
            file_name : name,
            current_panel : panel
        }

        console.log(data_to_send)

        fetch('/create_file',{
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify(data_to_send) 
        })
        .then(response => response.json())
        .then(data => {
            console.log('Server response: ', data)
        })
        .catch(error => {
            console.error('Eroare:', error)
        })
    })


    close.addEventListener('click', function(){
        modalFile.style.display = 'none'
        window.location.reload()

    })

})