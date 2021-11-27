var helloSpeaker = new Object();
helloSpeaker.speakWord = "Hello";
helloSpeaker.speak = function (name) {
    console.log(helloSpeaker.speakWord + " " + name);
};