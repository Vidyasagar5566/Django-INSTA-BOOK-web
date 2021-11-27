var names = ["Yaakov","John","Jen","Jason","Paul","Frank","Larry","Paula","Laura","Jim"];

for (var i = 0; i < names.length; i++) {
    a = names[i];
    if (a[0] == "j" || a[0] == "J") {
    	byeSpeaker.speak(a);
    }
    else {
    	helloSpeaker.speak(a);
    }
}
