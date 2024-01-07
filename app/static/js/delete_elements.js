var delBtn = document.getElementById("delete-btn")

delBtn.addEventListener('click', function(){

    let content_to_send = {
        left_panel : left_panel_selected_items,
        right_panel : right_panel_selected_items
    }
    console.log(JSON.stringify(content_to_send))

    fetch('/delete_elements',{
        method: 'POST',
        headers: {
            'Content-Type' : 'application/json'
        },
        body: JSON.stringify(content_to_send) 
    })
    .then(response => response.json())
    .then(data => {
        console.log('Server response: ', data)
    })
    .catch(error => {
        console.error('Eroare:', error)
    })

    window.location.reload


})