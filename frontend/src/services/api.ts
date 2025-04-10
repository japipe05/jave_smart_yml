import axios from "axios";

const api = axios.create({
  baseURL: process.env.NEXT_PUBLIC_API_URL_SUBIR || "http://localhost:8000/files",
  headers: {
    "Content-Type": "multipart/form-data",
  },
});

export const uploadChatData = async (message: string, model_name: string, file: File | null) => {
  const formData = new FormData();
  formData.append("message", message);
  formData.append("model_name", model_name);

  console.log("Enviando mensaje:", message);
  console.log("Enviando model_name:", model_name);


  if (file) formData.append("file", file);

  try {
    const response = await api.post("/upload", formData);

    // ✅ Verifica si la subida fue exitosa según la respuesta del servidor
    if (response.status === 200 || response.status === 201) {
      console.log("✅ Archivo subido correctamente:", response.data);
      //return { success: true, message: "Archivo subido con éxito"+ response.data , data: response.data };
      // Como response.data ya es un objeto, simplemente accede a sus propiedades
      const botMessage = response.data.message || ""; // Extrae "bbb"
      const zipUrl = response.data.generated_files?.zip_url || "";
      const fileName = zipUrl.split("/").pop() || "";
      return { success: true, 
        message: `${botMessage}`,
        data: response.data ,
        download: `/files/download/${fileName}` 
      };

    } else {
      console.log("⚠️ Error en la subida:", response.data);
      return { success: false, message: "Error al subir el archivo" };
    }
  } catch (error) {
    console.error("❌ Error enviando datos:", error);
    return { success: false, message: "Error en la subida del archivo" };
  }
};
