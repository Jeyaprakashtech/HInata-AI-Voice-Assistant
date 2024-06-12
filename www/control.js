$(document).ready(function () {
    //diplay msg
    eel.expose(displaymsg);
    function displaymsg(msg) {
        // Set the maximum length of the message
        var maxLength = 45;
        
        // Truncate the message if it exceeds the maximum length
        var truncatedMsg = msg.length > maxLength ? msg.substring(0, maxLength) + '...' : msg;
    
        $(".aimsg").text(truncatedMsg);
        $(".aimsg li:first").textillate('start');
    }
    eel.expose(showhood)
    function showhood() {
        $("#main1").show();
        $("#main2").hide();
        $("#main3").hide();
        displaymsg("")
    }
    eel.expose(showbox)
    function showbox(){
        $("#main3").show();
        $("#main2").hide();
        $("#main1").hide();
        
    }
    eel.expose(showloader)
    function showloader(){
        $("#listen").hide();
        $("#loader").show();
        
        
    }
    eel.expose(selectFileAutomatically)
    function selectFileAutomatically() {
        // Create a file input element
        var input = document.createElement('input');
        input.type = 'file';
        input.style.display = 'none';

        // Attach event listener to handle file selection
        input.addEventListener('change', function(event) {
            var file = event.target.files[0];
            console.log("Selected file:", file);
            // Send the selected file path to Python using Eel
            eel.process_file_path(file.path)();
        });

        // Add the file input element to the document
        document.body.appendChild(input);

        // Trigger file selection dialog
        input.click();

        // Remove the file input element from the document after the dialog is closed
        input.remove();
    }
    // Automatically trigger file selection dialog when the page loads
    window.onload = function() {
        selectFileAutomatically();
    };
})