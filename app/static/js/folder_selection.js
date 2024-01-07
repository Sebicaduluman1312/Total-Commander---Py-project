var pathSelector1 = document.querySelector(".first_input")
var currentPath1 = pathSelector1.value

var pathSelector2 = document.querySelector(".second_input")
var currentPath2 = pathSelector2.value



var selectedFolders = document.querySelectorAll(".name");

selectedFolders.forEach(function(selectedFolder) {
    selectedFolder.addEventListener('click', function() {

        if(selectedFolder.parentNode.parentNode.className == 'left-panel-list'){

            currentPath1 += "/" + selectedFolder.innerText
            console.log("primul cadran", currentPath1)

            var leftPath = currentPath1;
            var rightPath = currentPath2;
            const url = `http://localhost:8000/?leftPath=${encodeURIComponent(leftPath)}&rightPath=${encodeURIComponent(rightPath)}`;
            window.location.href = url

            fetch(url, { mode: 'no-cors' })
            .then(() => {
                console.log('Request-ul a fost trimis cu succes.');
            })
            .catch(error => {
                console.error('Eroare în timpul request-ului:', error);
            });

        }
        else{
            
            currentPath2 += "/" + selectedFolder.innerText
            console.log("aldoilea cadran", currentPath2)

            var leftPath = currentPath1;
            var rightPath = currentPath2;
            const url = `http://localhost:8000/?leftPath=${encodeURIComponent(leftPath)}&rightPath=${encodeURIComponent(rightPath)}`;
            window.location.href = url

            fetch(url, { mode: 'no-cors' })
            .then(() => {
                console.log('Request-ul a fost trimis cu succes.');
            })
            .catch(error => {
                console.error('Eroare în timpul request-ului:', error);
            });
        }

    });
});

var backToFolders = document.querySelectorAll(".return")


backToFolders.forEach(function(backToFolder){

    backToFolder.addEventListener("click", function() {

        if (backToFolder.parentNode.className == "left-panel-list"){

            var parentDirPath = currentPath1.substring(0, currentPath1.lastIndexOf('/'))

            var leftPath = parentDirPath
            var rightPath = currentPath2
            const url = `http://localhost:8000/?leftPath=${encodeURIComponent(leftPath)}&rightPath=${encodeURIComponent(rightPath)}`;
            window.location.href = url

            fetch(url, { mode: 'no-cors' })
            .then(() => {
                console.log('Request-ul a fost trimis cu succes.');
            })
            .catch(error => {
                console.error('Eroare în timpul request-ului:', error);
            });


        }
        else{

            var parentDirPath = currentPath2.substring(0, currentPath2.lastIndexOf('/'))

            var leftPath = currentPath1
            var rightPath = parentDirPath
            const url = `http://localhost:8000/?leftPath=${encodeURIComponent(leftPath)}&rightPath=${encodeURIComponent(rightPath)}`;
            window.location.href = url

            fetch(url, { mode: 'no-cors' })
            .then(() => {
                console.log('Request-ul a fost trimis cu succes.');
            })
            .catch(error => {
                console.error('Eroare în timpul request-ului:', error);
            });

        }
    
    })


})

