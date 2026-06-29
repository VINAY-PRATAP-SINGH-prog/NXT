console.log("Script Loaded");


 async function loadEvents(){
    
        const response = await
fetch("http://127.0.0.1:5000/events");
        const data = await response.json();
        
        console.log(data);         
}
async function loadThreats() {
    const response = await
    fetch("http://127.0.0.1:5000/events");
    
    const data = await response.json();
    document.getElementById("threat-count").innerText = data.length;

    const alerts = data.filter(t=>t.severity == "HIGH" || t.severity === "CRITICAL").length;

    document.getElementById("alert-count").innerText = alerts;

    document.getElementById("file-count").innerText = "ACTIVE";

    const threatList = document.getElementById("threat-list");

    threatList.innerHTML = "";

    data.forEach(threat => {
        threatList.innerHTML += `
        <div class="threat">
            <p><strong>[${threat.severity}]</strong>${threat.type}</p>
            <p>Time: ${threat.time}</p>
            <p>Path: ${threat.path}</p>

        </div>`;
        
    });
}

loadThreats();
setInterval(loadThreats, 1000);
    
 

