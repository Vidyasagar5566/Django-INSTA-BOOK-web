var names = new Array();
names[0] = "Ramana";
names[1] = "vidya";
names[2] = "joe";
names[3] = "sagar";
names[4] = "Jhon";
names[5] = "jogesh";
names[6] = "srinivas Chandu";
names[7] = "Jagadesh";
names[8] = "chinni";
names[9] = "jeon";
names[10] = "chinni"
for (var i = 0; i < names.length; i++) {
    a = names[i];
    if (a[0] == "j" || a[0] == "J") {
    	console.log("Goodbye " + names[i]);
    }
    else {
    	console.log("Hello " + names[i]);
    }
}
