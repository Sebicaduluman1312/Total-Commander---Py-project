var pathSelector1 = document.querySelector(".first_input")
var currentPath1 = pathSelector1.value

var pathSelector2 = document.querySelector(".second_input")
var currentPath2 = pathSelector2.value

var modalEdit = document.querySelector(".modal-edit")
var editBtn = document.querySelector(".edit_file")


editBtn.addEventListener('click', function(){

    let checkedBoxes = left_panel_selected_items.length + right_panel_selected_items.length
    if (checkedBoxes < 1  || checkedBoxes > 1)
        alert("You need to select only one element for edit operation!!!")
    else{

        modalEdit.style.display = 'flex'
        modalEdit.style.justifyContent = 'center'
        modalEdit.style.alignItems = 'center'

    
        var text_area = document.querySelector(".content_f")
        //FETCH!
        let data_to_go

        if(left_panel_selected_items.length == 1)
        {
            var path_to_go = currentPath1 + '/' + left_panel_selected_items[0]
            data_to_go = {path : path_to_go}
        
        }
        else if (right_panel_selected_items.length == 1)
        {
            var path_to_go = currentPath2 + '/' + right_panel_selected_items[0]
            data_to_go = {path : path_to_go}
        }  
        
        fetch('/get_content',{
            method: 'POST',
            headers: {
                'Content-Type' : 'application/json'
            },
            body: JSON.stringify(data_to_go) 
        })
        .then(response => response.json())
        .then(data => {
            console.log('Server response: ', data)
            text_area.value = data.content
        })
        .catch(error => {
            console.error('Eroare:', error)
        })
        
        var text_to_write = ""
        text_area.addEventListener("input", function(){
            text_to_write = this.value
        })

        var savBut = document.querySelector(".submit-edit")
        savBut.addEventListener('click', function(){
            console.log(text_to_write)
            var data_to_go2 = {content_to : text_to_write, path : path_to_go}
            fetch('/edit_file',{
                method: 'POST',
                headers: {
                    'Content-Type' : 'application/json'
                },
                body: JSON.stringify(data_to_go2) 
            })
            .then(response => response.json())
            .then(data => {
                console.log('Server response: ', data)
                text_area.value = data.content
            })
            .catch(error => {
                console.error('Eroare:', error)
            })            
        })
            
        
        var close_btn = document.querySelector(".close-modal-edit")
        close_btn.addEventListener('click', function(){
            modalEdit.style.display = 'none'
            window.location.reload()
        }) 
    }
 })

 


