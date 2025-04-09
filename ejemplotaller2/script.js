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
        alert("Por favor, ingresa una URL.");
    }
}

// Función para descargar el QR como imagen
function descargarQR() {
    let qrCanvas = document.querySelector("#qr-result canvas");
    let qrImg = qrCanvas.toDataURL("image/png");

    let link = document.createElement("a");
    link.href = qrImg;
    link.download = "QR_info.png";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}
