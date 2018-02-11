var messageForm = document.getElementById("messageForm");
messageForm.addEventListener("submit", function(event) {
    event.preventDefault();
    if (this.message.value) {
        var message = {
            "code": "msg",
            "text": this.message.value
        }
        socketSend(message);
    }
    this.message.value = "";
    this.message.focus();
});


var vueChat = new Vue({
    el: "#vueChat",
    data: {
        messages: [],
        styleObject: {
            height: (window.innerHeight-100) + "px"
        }
    },
    methods: {
        updateHeight: function(value) {
            this.styleObject.height = (value-100) + "px"
        }
    }
});


window.addEventListener("resize", function() {
    vueChat.updateHeight(window.innerHeight);
});


var socket = new WebSocket("ws://127.0.0.1:8004/websocket");


socket.onopen = function() {
    socket.send(JSON.stringify({'code': 'msgs'}));
};


socket.onmessage = function(message) {
    var message = JSON.parse(message.data);
    if (message['code'] === "msg") {
        vueChat.messages.push(message);
    }
    else if (message['code'] === "msgs") {
        vueChat.messages.push.apply(vueChat.messages, message['messages']);
    }
    setTimeout(() => {
        scrollBottom(chatWindow);
    }, 10);
};


socket.onclose = function() {
    socket.send("disconnect");
};


function socketSend(message) {
    socket.send(JSON.stringify(message));
}


function scrollBottom(element) {
    element.scrollTop = element.scrollHeight;
}