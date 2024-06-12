
// text1 animie
$(document).ready(function () {
    $("#setcontainer").hide()
    $("#main2").hide();
    $("#main3").hide();
    $("#loader").hide();
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeIn",
            delayScale: 1,
        },
        out: {
            effect: "fadeOut",
            delayScale: 1,
        }
    });
    // chat text animie
    $('.text-start').textillate({
        loop: true,
        in: {
            effect: 'flash',
            sequence: true
        },
        out: {
            effect: 'sequence',
            sequence: true
        }
    });
    // wave confi
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 640,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true,
        cover: true,
        color: "red",
    });
    //micbtn event click 
    $("#mic").on("click", function () {
        eel.SS();
        $("#main1").hide();
        $("#main3").hide();
        $("#main2").show();
        eel.voice_command()
    });
    //sendbtn event click 
    $("#send").on("click", function () {
        eel.SS();
        $("#main1").hide();

        $("#main2").show();
        var userInput = $("#text_box").val();
        eel.text_command(userInput);
    });
    $('#text_box').on("keyup", function (event) {
        if (event.key === "Enter") {
            var userInput = $("#text_box").val();
            $("#main1").hide();
            $("#main2").show();
            eel.text_command(userInput)
        }
    })
    function doc_keyup(e) {
        if (e.key === 'j' && (e.metaKey)) {
            eel.SS();
            $("#main1").hide();
            $("#main2").show();
            eel.voice_command();
        }
    }
    document.addEventListener('keyup', doc_keyup, false);
    // to play assisatnt 
    function PlayAssistant(message) {

        if (message != "") {

            $("#vid").hide();
            $("#SiriWave").show();
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#cambtn").show();
            $("#sendbtn").hide();

        }

    } 
    // key up event handler on text box
    $("#text_box").keyup(function () {

        let message = $("#text_box").val();
        ShowHideButton(message)

    });
    // Slide panel functionality
    $('#chat-btn').on('click', function () {
        $('.slide-panel').toggleClass('show');
        $('#main1, #main2, #main3, #bottom_panle1').toggleClass('show-main'); // Toggle class for main content
        // Toggle class for footer
    });
    $('#close-btn').on('click', function () {
        $('.slide-panel').removeClass('show');
        $('#main1, #main2, #main3, #bottom_panle1').toggleClass('show-main'); // Toggle class for main content
    });
    // preloader function
    setTimeout(function () {
        document.querySelector('.preloader').style.display = 'none';  
    }, 10000);
    // Expose the sendertxt function to Python
    eel.expose(sendertxt);
    function sendertxt(message) {
        var text_box = document.getElementById("chat_body");
        if (message.trim() !== "") {
            text_box.innerHTML += `
            <div class="row justify-content-end mb-4">
                <div class="width-size">
                    <div class="sender_msg">${message}</div>
                </div>
            </div>`;
            text_box.scrollTop = text_box.scrollHeight;
        }
    }
    // Expose the recivertxt function to Python
    eel.expose(recivertxt);
    function recivertxt(message) {
        var text_box = document.getElementById("chat_body");
        if (message.trim() !== "") {
            text_box.innerHTML += `
            <div class="row justify-content-start mb-4">
                <div class="width-size">
                    <div class="reciver_msg">${message}</div>
                </div>
            </div>`;
            text_box.scrollTop = text_box.scrollHeight;
        }
    }
    const startButton = document.getElementById('cam');
    const videoElement = document.getElementById('videoElement');
    // Event listener for the button click
    startButton.addEventListener('click', async () => {
        try {
            // Get access to the camera
            const stream = await navigator.mediaDevices.getUserMedia({ video: true });

            // Display the camera stream in the video element
            videoElement.srcObject = stream;
        } catch (err) {
            console.error('Error accessing camera:', err);
        }
    });

});

