const form = document.querySelector("[data-form]");
const message = document.querySelector("[data-message]");
const downloadLink = document.querySelector("[data-link=download]");
const input = form[0];

form.addEventListener("submit", async (event) => {
   event.preventDefault();

   const formData = new FormData(form);

   if(!downloadLink.classList.contains("hidden")) {
      downloadLink.classList.add("hidden");
   }

   message.textContent = "Buscando informações...";
   input.value = "";

   try {
      // REQUEST
      const response = await fetch("/download", {
         method: "POST",
         body: formData,
      });

      // RESPONSE
      if (response.status !== 200) {
         const data = await response.json();
         message.textContent = data.error;
      } else {
         const blob = await response.blob();
         const url = URL.createObjectURL(blob);

         downloadLink.href = url;
         downloadLink.classList.remove("hidden");
         message.textContent = "Download concluído!"
      }
   } catch (error) {
      message.textContent = "Tivemos um problema, tente novamente!";
   }
});

input.addEventListener("focus", () => {
   if(message.textContent.includes("concluído")) {
      message.textContent = "Salve o seu download!";
   } else if (message.textContent !== "" && !message.textContent.includes("Salve")) {
      message.textContent = "";
   }
});

downloadLink.addEventListener("click", () => {
   downloadLink.classList.add("hidden");
   message.textContent = "";
});