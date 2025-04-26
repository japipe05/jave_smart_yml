'use client'

import Image from 'next/image'
import { useState } from 'react'
import Link from 'next/link'

export default function RegisterPage() {
  const [formData, setFormData] = useState({
    email: '',
    celular: '',
    Nombre: '',
    Apellido: '',
    tipo_cedula: 'CC',
    cedula: '',
    password: '',
  })
  {/* comentario
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }
 */}
  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>
  ) => {
    setFormData({ ...formData, [e.target.name]: e.target.value })
  }

  const handleRegister = async () => {
    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL_DESCA}/auth/register`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      })

      const data = await res.json()
      alert(data.message || data.detail || 'Usuario registrado correctamente')
    } catch (error) {
      console.error(error)
      alert('Error al registrarse')
    }
  }

  return (
    <div className="relative flex items-center justify-center min-h-screen overflow-hidden">
      {/* Fondo borroso */}
      <Image
        src="/fondo.png"
        alt="Fondo"
        layout="fill"
        objectFit="cover"
        quality={100}
        className="-z-10 blur-lg"
      />

      {/* Contenedor del formulario */}
      <div className="w-full max-w-2xl bg-white/50 backdrop-blur-md border border-gray-300 rounded-lg shadow-xl p-8 flex flex-col items-center relative">
        <h1 className="text-3xl font-bold text-center mb-6">Registro de Usuario</h1>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 w-full">
          <input
            type="text"
            name="Nombre"
            placeholder="Nombre"
            className="px-4 py-2 rounded bg-white/20 placeholder-black focus:outline-none focus:ring-2 focus:ring-blue-400"
            value={formData.Nombre}
            onChange={handleChange}
          />
          <input
            type="text"
            name="Apellido"
            placeholder="Apellido"
            className="px-4 py-2 rounded bg-white/20 placeholder-black focus:outline-none focus:ring-2 focus:ring-blue-400"
            value={formData.Apellido}
            onChange={handleChange}
          />
          <select
            name="tipo_cedula"
            
            className="px-4 py-2 rounded bg-white/20 text-black focus:outline-none focus:ring-2 focus:ring-blue-400"
            value={formData.tipo_cedula}
            onChange={handleChange}
          >
            <option value="">Selecciona tipo de documento</option>
            <option value="CC">CC - Cédula de Ciudadanía</option>
            <option value="TI">TI - Tarjeta de Identidad</option>
            <option value="CE">CE - Cédula de Extranjería</option>
            <option value="PA">PA - Pasaporte</option>
          </select>

          <input
            type="text"
            name="cedula"
            placeholder="Cédula"
            className="px-4 py-2 rounded bg-white/20 placeholder-black focus:outline-none focus:ring-2 focus:ring-blue-400"
            value={formData.cedula}
            onChange={handleChange}
          />
          <input
            type="text"
            name="celular"
            placeholder="Celular"
            className="px-4 py-2 rounded bg-white/20 placeholder-black focus:outline-none focus:ring-2 focus:ring-blue-400"
            value={formData.celular}
            onChange={handleChange}
          />
          <input
            type="email"
            name="email"
            placeholder="Correo electrónico"
            className="px-4 py-2 rounded bg-white/20 placeholder-black focus:outline-none focus:ring-2 focus:ring-blue-400"
            value={formData.email}
            onChange={handleChange}
          />
          <input
            type="password"
            name="password"
            placeholder="Contraseña"
            className="px-4 py-2 rounded bg-white/20 placeholder-black focus:outline-none focus:ring-2 focus:ring-blue-400 col-span-1 sm:col-span-2"
            value={formData.password}
            onChange={handleChange}
          />
        </div>

        <button
          onClick={handleRegister}
          className="mt-6 w-full py-2 px-2 bg-green-600 hover:bg-green-700 transition rounded font-semibold"
        >
          Registrarse
        </button>

        <p className="mt-6 text-center text-sm text-black/80">
          ¿Ya tienes cuenta?{' '}
          <Link href="/login" className="text-black hover:underline font-medium">
            Inicia sesión aquí
          </Link>
        </p>
      </div>
    </div>
  )
}
