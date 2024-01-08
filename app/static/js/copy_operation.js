var pathSelector1 = document.querySelector(".first_input")
var currentPath1 = pathSelector1.value

var pathSelector2 = document.querySelector(".second_input")
var currentPath2 = pathSelector2.value

var copyBtn = document.getElementById("copy-btn")

copyBtn.addEventListener('click', function(){

    if (left_panel_selected_items.length > 0 && right_panel_selected_items.length > 0)
        alert("You need to have selected items just from one panel !!!")
    else if(left_panel_selected_items.length == 0 && right_panel_selected_items.length == 0)
        alert("You need to select something")
    else{

        let data_to_send
        if (left_panel_selected_items.length > 0)
        {
            var left_vector = []
            for (let i=0; i<left_panel_selected_items.length; i++)
            {
                all_paths = currentPath1 + '/' + left_panel_selected_items[i]
                left_vector.push(all_paths)
            }
            data_to_send = { start_path : left_vector, end_path : currentPath2}
        }
        else
        {
            var right_vector = []
            for (let i=0; i<right_panel_selected_items.length; i++)
            {
                all_paths = currentPath2 + '/' + right_panel_selected_items[i]
                right_vector.push(all_paths)
            }
            data_to_send = {start_path : right_vector, end_path : currentPath1}

        }
        fetch('/copy',{
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

        // setTimeout(() => window.location.reload(), 1000);


    }



})