//attendence fetcher
function getroll(){
//jay
fetch('https://blr1.blynk.cloud/external/api/get?token=3vFr2aWjUDpQ9URBHEK5rK3ObaivKfcT&v0').then((data)=>
{
   return data.json();
}).then((completedata)=>{
    if(completedata == 2){
        document.getElementById("amark").innerText = "✔"

        var date = new Date();
        var current_time = date.getHours()+":"+date.getMinutes();
        document.getElementById("atime").innerHTML = current_time;
    }
})

//pjk
fetch('https://blr1.blynk.cloud/external/api/get?token=3vFr2aWjUDpQ9URBHEK5rK3ObaivKfcT&v0').then((data)=>
{
   return data.json();
}).then((completedata)=>{
    if(completedata == 1){
        document.getElementById("bmark").innerText = "✔"

        var date = new Date();
        var current_time = date.getHours()+":"+date.getMinutes();
        document.getElementById("btime").innerHTML = current_time
    }
})
}
setInterval(getroll , 1000);

//auth pw gen
function generatePassword() {
    var length = 8,
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789",
        retVal = "";
    for (var i = 0, n = charset.length; i < length; ++i) {
        retVal += charset.charAt(Math.floor(Math.random() * n));
    }
    return retVal;
}
url = ""
//submit
function auth(){
    let input1 = document.getElementById("cam").value
    let input2 = document.getElementById("gsp").value
    let input3 = document.getElementById("key").value


    var boll = false
    var pin1 = -1
    var pin2 = -1

    switch (input3) {
        case"xyx2":
            pin1 = 0;pin2 = 1
            url = input1
            boll = true
    }
    if(boll){
        var randomGen = generatePassword()
            var sendOutput = input1 +"|"+ input2 +"|"+ pin1+"|"+ randomGen
            alert("Your Authentication token : " + randomGen)
            console.log(sendOutput)
            //runPharms = parseURLParams("https://blr1.blynk.cloud/external/api/update?token=3vFr2aWjUDpQ9URBHEK5rK3ObaivKfcT&pin=v"+pin2+"&value="+sendOutput);
            var wndUrl = "https://blr1.blynk.cloud/external/api/update?token=3vFr2aWjUDpQ9URBHEK5rK3ObaivKfcT&pin=v"+pin2+"&value="+sendOutput;
            window.open(wndUrl)
            window.location.replace("cont.html")
    }else{
        alert("Invalid device key.")
        auth()
    }
}
