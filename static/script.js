const form = document.getElementById("download-form");
const messageParagraph = document.getElementById("message");
const downloadDiv = document.getElementById("download-link"); 
const fileLink = document.getElementById("file-link"); // link <a>

form.addEventListener("submit", async (event) => {
   event.preventDefault();
   const formData = new FormData(form);
   messageParagraph.textContent = "Processando...";
   // downloadDiv.classList.add("hidden");

   try {
      const response = await fetch("/download", {
         method: "POST",
         body: formData,
      });

      const data = await response.json();
      console.log(data)
      if (response.ok) {
         messageParagraph.textContent = `${data.message}`;
         fileLink.href = data.download_url; // atualiza o  href com o link recebido do servidor
         fileLink.download = data.filename; // sugere o título original do vídeo presente no YouTube
         downloadDiv.classList.remove("hidden");
      } else {
         messageParagraph.textContent = `${data.error}`;
      }
   } catch (error) {
      messageParagraph.textContent = `Erro ao conectar ao servidor.`;
   }
});