"use client";
import Image from "next/image";
import { useFileUpload } from "@/hooks/useFileUpload";
import { FaPaperclip } from "react-icons/fa";
import { IoIosSend } from "react-icons/io";
import { useRef, useEffect, useState } from "react";
import { TypeAnimation } from 'react-type-animation';
import { useRouter } from "next/navigation"

export default function Home() {
  const router = useRouter();
  const [checkingAuth, setCheckingAuth] = useState(true);

  useEffect(() => {
    const token = localStorage.getItem("token")
    if (!token) {
      router.replace("/login")
    } else {
      setCheckingAuth(false);
    }
  }, [router]);

  const logout = () => {
    localStorage.removeItem("token");
    router.push("/login");
  };

  const {
    message,
    setMessage,
    model_name,
    setModel_name,
    chatMessages,
    fileInputRef,
    handleFileChange,
    handleSubmit,

    loading,
  } = useFileUpload();

  const textareaRef = useRef<HTMLTextAreaElement>(null);

  //const [selectedFile, setSelectedFile] = useState<File | null>(null);
  if (checkingAuth) return null;

  return (
    <div
      className="flex min-h-screen items-center justify-center p-6 bg-cover bg-center relative"
      style={{ backgroundImage: "url('/fondo.png')" }}
    >
      <Image
        src="/fondo.png"
        alt="Fondo"
        layout="fill"
        objectFit="cover"
        quality={100}
        className="-z-10 blur-lg"
      />

      <div className="w-full max-w-2xl bg-white/50 backdrop-blur-md border border-gray-300 rounded-lg shadow-xl p-8 flex flex-col items-center relative">
        <button
          onClick={logout}
          className="absolute top-4 right-4 text-sm text-red-600 hover:text-red-800 font-medium transition"
        >
          Cerrar sesión
        </button>

        <div className="flex justify-center items-center w-[100px] h-[100px] bg-white rounded-full shadow-md p-2 mb-4">
          <Image
            src="/Logo-javeriana.png"
            alt="Logo Javeriana"
            width={100}
            height={100}
            className="w-full h-full object-contain"
          />

        </div>

        <h1 className="text-2xl font-bold text-black text-center mb-6">
          ¿Qué Proyecto de Next.js quieres contenerizar?
        </h1>

        <div
          className="w-full flex flex-col bg-white p-4 rounded-md shadow-inner mb-4 transition-all duration-300"
          style={{
            minHeight: "24px",
            maxHeight: "calc(100vh - 300px)",
            overflowY: "auto",
          }}
        >
          {chatMessages.map((msg, index) => {
            const isUser = msg.sender === "user";
            const isError = msg.type === "error";

            return (
              <div
                key={index}
                className={`mb-3 max-w-[80%] md:max-w-md px-4 py-3 rounded-2xl shadow-md text-[15px] leading-relaxed break-words flex flex-col
                ${isUser ? "self-end bg-white text-gray-900 border border-gray-200" :
                    isError ? "self-start bg-red-100 text-red-800 border border-red-300" :
                      "self-start bg-white text-gray-900 border border-gray-200"}`}
                style={{ fontFamily: "Ubuntu, sans-serif", animation: "fadeIn 0.3s ease-in-out" }}
              >
                <div className="text-sm opacity-70 mb-1 flex items-center gap-2">
                  {isError && <>❌ <strong>Error</strong></>}
                  {!isUser && !isError && <>🤖 <strong>IA</strong></>}
                  {isUser && <>👤 <strong>Tú</strong></>}
                </div>

                {msg.text && !isUser ? (
                  <TypeAnimation
                    sequence={[msg.text]}
                    speed={10}
                    cursor={false}
                    style={{ whiteSpace: 'pre-line' }}
                  />
                ) : msg.text ? (
                  <p className="whitespace-pre-line">{msg.text}</p>
                ) : null}

                {msg.file && !isUser ? (
                  <a
                    href={msg.file.url}
                    download={msg.file.name}
                    className="mt-2 underline font-medium text-blue-600 hover:text-blue-800"
                  >
                    <TypeAnimation
                      sequence={[`📎 ${msg.file.name}`]}
                      speed={10}
                      cursor={false}
                      style={{ display: 'inline-block' }}
                    />
                  </a>
                ) : msg.file ? (
                  <a
                    href={msg.file.url}
                    download={msg.file.name}
                    className="mt-2 underline font-medium text-blue-600 hover:text-blue-800"
                  >
                    📎 {msg.file.name}
                  </a>
                ) : null}
              </div>
            );
          })}

          {loading && (
            <div className="mb-2 p-2 rounded-lg max-w-[80%] md:max-w-xs bg-gray-100 text-black self-start mr-auto italic flex items-center space-x-1 animate-pulse">
              <span>Escribiendo</span>
              <span className="animate-bounce">.</span>
              <span className="animate-bounce delay-150">.</span>
              <span className="animate-bounce delay-300">.</span>
            </div>
          )}
        </div>

        <form
          onSubmit={handleSubmit}
          className="w-full bg-white border border-gray-300 rounded-lg shadow-md px-4 py-3 flex flex-col"
        >
          <div className="mb-5">
            <label htmlFor="model" className="block text-sm font-medium text-gray-800 mb-2">
              Selecciona el modelo de ChatGPT
            </label>
            <div className="relative">
              <select
                id="model"
                name="model"
                className="block w-full appearance-none rounded-2xl border border-gray-300 bg-white px-4 py-2 pr-10 text-gray-900 shadow-sm focus:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-500"
                value={model_name}
                onChange={(e) => setModel_name(e.target.value)}
              >
                <option value="gpt-4-turbo">GPT-4 Turbo</option>
                <option value="gpt-4o">gpt-4o</option>
                <option value="gpt-4o-mini">GPT-4 Omni</option>
              </select>
              <div className="pointer-events-none absolute inset-y-0 right-3 flex items-center text-gray-500">
                <svg className="h-4 w-4" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M5.23 7.21a.75.75 0 011.06.02L10 11.584l3.71-4.354a.75.75 0 111.14.976l-4.25 5a.75.75 0 01-1.14 0l-4.25-5a.75.75 0 01.02-1.06z" clipRule="evenodd" />
                </svg>
              </div>
            </div>
          </div>

          <textarea
            ref={textareaRef}
            className="w-full bg-transparent outline-none text-gray-700 placeholder-gray-400 text-lg resize-none overflow-hidden"
            placeholder="Describe tu proyecto y token GITHUB_TOKEN= y VERCEL_TOKEN="
            value={message}
            onChange={(e) => {
              setMessage(e.target.value);
              if (textareaRef.current) {
                textareaRef.current.style.height = "auto";
                const scrollHeight = textareaRef.current.scrollHeight;
                const maxHeight = 4 * 24;
                textareaRef.current.style.height = `${Math.min(scrollHeight, maxHeight)}px`;
              }
            }}
            required
            rows={1}
            style={{ minHeight: "24px", maxHeight: "96px" }}
          />

          {File && (
            <div className="mt-2 p-2 bg-gray-200 text-gray-700 rounded-md flex items-center">
              <span className="text-sm truncate">{File.name}</span>
            </div>
          )}


          <div className="flex justify-between items-center mt-3">
            <label
              htmlFor="file-upload"
              className="text-gray-600 hover:text-black cursor-pointer flex items-center space-x-2"
            >
              <FaPaperclip size={20} />
              <span className="text-sm">Adjuntar ZIP</span>
            </label>
            <input
              id="file-upload"
              type="file"
              accept=".zip"
              onChange={handleFileChange}
              ref={fileInputRef}
              
            />

            <button type="submit" className="text-gray-600 hover:text-black cursor-pointer">
              <IoIosSend size={24} />
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
