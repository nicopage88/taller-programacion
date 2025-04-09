// Función para generar QR
function generarQR() {
    let texto = document.getElementById("qr-text").value;
    let qrContainer = document.getElementById("qr-result");
    let downloadBtn = document.getElementById("download-btn");

    if (texto.trim() !== "") {
        qrContainer.innerHTML = "";
        let qrCode = new QRCode(qrContainer, {
            text: texto,
            width: 200,
            height: 200
        });

        // Mostrar el botón de descarga
        setTimeout(() => {
            downloadBtn.style.display = "block";
        }, 500);
    } else {
        alert("Por favor, ingresa un mensaje.");
    }
}

// Función para descargar el QR como imagen
function descargarQR() {
    let qrCanvas = document.querySelector("#qr-result canvas");
    let qrImg = qrCanvas.toDataURL("image/png");

    let link = document.createElement("a");
    link.href = qrImg;
    link.download = "QR_code.png";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Función para escanear QR con la cámara
function iniciarEscaneo() {
    let video = document.getElementById("video");
    let canvas = document.getElementById("canvas");
    let context = canvas.getContext("2d");
    let qrOutput = document.getElementById("qr-output");

    navigator.mediaDevices.getUserMedia({ video: { facingMode: "environment" } })
        .then(stream => {
            video.srcObject = stream;
            setInterval(() => {
                context.drawImage(video, 0, 0, canvas.width, canvas.height);
                let imageData = context.getImageData(0, 0, canvas.width, canvas.height);
                let qrCode = jsQR(imageData.data, canvas.width, canvas.height);

                if (qrCode) {
                    qrOutput.innerText = "QR Detectado: " + qrCode.data;

                    // Mensaje especial si se detecta un código QR especial
                    if (qrCode.data === "feriaQR2025") {
                        alert("🎉 ¡Felicidades! Has encontrado el QR secreto 🎉");
                    }
                }
            }, 500);
        })
        .catch(err => console.error("Error al acceder a la cámara:", err));
}
