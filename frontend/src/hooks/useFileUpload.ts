import { useState, useRef } from "react";
import { uploadChatData } from "@/services/api";

export function useFileUpload() {
    const [message, setMessage] = useState("");
    const [model_name, setModel_name] = useState("gpt-4o-mini");
    const [file, setFile] = useState<File | null>(null);
    const [loading, setLoading] = useState(false);
    const [chatMessages, setChatMessages] = useState<{
        sender: "user" | "bot";
        text?: string;
        file?: { name: string; url: string }
    }[]>([]);

    const fileInputRef = useRef<HTMLInputElement | null>(null);

    const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const selectedFile = e.target.files?.[0];

        if (selectedFile?.name.includes(".zip")) {
            setFile(selectedFile);
        } else {
            setFile(null);
            if (fileInputRef.current) fileInputRef.current.value = "";
        }
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!message.trim() && !file) {
            alert("Escribe un mensaje o adjunta un archivo .zip");
            return;
        }
        
        if (!model_name.trim() && !file) {
            alert("Ingrese un modelo de ChatGpt .zip");
            return;
        }

        try {
            setLoading(true);

            // ✅ Agregar el mensaje del usuario con el archivo si existe
            const userMessage = {
                sender: "user",
                text: message || "",
                file: file ? { name: file.name, url: URL.createObjectURL(file) } : undefined
            };

            setChatMessages((prev) => [...prev, userMessage]);

            const result = await uploadChatData(message, model_name,file);

            if (result.success) {
                const botMessage = result.message;
                const downloadUrl = `${process.env.NEXT_PUBLIC_API_URL_DESCA || "http://localhost:8000"}${result.download}`;
                const fileName = result.download?.split("/").pop() || "archivo.zip";
              
                setChatMessages((prev) => [
                  ...prev,
                  {
                    sender: "bot",
                    text: botMessage,
                  },
                  {
                    sender: "bot",
                    file: {
                      name: fileName,
                      url: downloadUrl, // ✅ url completa para descargar
                    },
                  },
                ]);
              
                setMessage("");
                setFile(null);
                if (fileInputRef.current) fileInputRef.current.value = "";
            }else {
                setChatMessages((prev) => [...prev, { sender: "bot", text: result.message }]);
            }
        } catch (error) {
            console.error(error);
            setChatMessages((prev) => [...prev, { sender: "bot", text: "Error en la subida del archivo" }]);
        } finally {
            setLoading(false);
        }
    };


    return { message, setMessage, model_name, setModel_name, file, loading, chatMessages, fileInputRef, handleFileChange, handleSubmit };
}
