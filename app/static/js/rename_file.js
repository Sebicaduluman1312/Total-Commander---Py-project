var rnmBtn = document.getElementById("rename-btn")
var rnmModal = document.querySelector(".modal-rename")

rnmBtn.addEventListener('click', function(){
    let checkedBoxes = left_panel_selected_items.length + right_panel_selected_items.length
    if (checkedBoxes < 1  || checkedBoxes > 1)
        alert("You need to select only one element for rename operation!!!")
    else
    {
        rnmModal.style.display = 'flex'
        rnmModal.style.justifyContent = 'center'
        rnmModal.style.alignItems = 'center'

        var submit = document.querySelector(".submit-name-rename-file")
        var close = document.querySelector(".close-modal-rename")

        submit.addEventListener('click', function(){
            var old_name
            if (left_panel_selected_items.length == 1)
                old_name = left_panel_selected_items[0]
            else if (righ_panel_selected_items.length == 1)
                old_name = right_panel_selected_items[0] 

            let newName = document.getElementById("newRenameFile")
            let data_to_send = {
                old_value: old_name, 
                rename_value : newName.value 
            }
                        

            console.log(data_to_send)

            fetch('/rename',{
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
            rnmModal.style.display = 'none'
            window.location.reload()
    
        })
    }

})