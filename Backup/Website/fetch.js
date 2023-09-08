var api = "https://blr1.blynk.cloud/external/api/get?token=3vFr2aWjUDpQ9URBHEK5rK3ObaivKfcT&v0";
var data = 0;
var lastData = 0;

let pranav = false;
let jay = false;

function fetcher()
{
    fetch(api).then((data) => {
        return data.json();
    }).then((value) => {
        document.getElementById("txtapi").innerHTML=value;
        data = String(value);

        if(data !== 0)
    {
        if(data !== lastData)
        {
            switch (data) {
                case 1:
                    pranav = true;
                case 2:
                    jay = true;
                default:
                    lastData = data;
            }
        }
    }
    })
}

