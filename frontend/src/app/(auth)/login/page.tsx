'use client'

import Image from 'next/image'
import { useState } from 'react'
import { useRouter } from 'next/navigation'
import Link from 'next/link'

export default function LoginPage() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)
  const router = useRouter()

  const handleLogin = async () => {
    setLoading(true)
    try {
      const res = await fetch('http://127.0.0.1:8000/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      })

      const data = await res.json()

      if (res.ok) {
        // Si el login fue exitoso, redirige
        // Podrías guardar el token en localStorage o cookie si lo necesitas luego
        localStorage.setItem('token', data.access_token) // ejemplo si devuelve un token
        router.push('/chatweb')
      } else {
        alert(data.message || data.detail || 'Credenciales inválidas')
      }
    } catch (error) {
      console.error(error)
      alert('Error al iniciar sesión')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="relative flex items-center justify-center min-h-screen overflow-hidden">
      <Image
        src="/fondo.png"
        alt="Fondo"
        layout="fill"
        objectFit="cover"
        quality={100}
        className="-z-10"
      />

      <div className="w-full max-w-2xl bg-white/50 backdrop-blur-md border border-gray-300 rounded-lg shadow-xl p-8 flex flex-col items-center relative">
        <h1 className="text-3xl font-bold mb-6 text-center">Iniciar Sesión</h1>

        <div className="space-y-4">
          <input
            type="email"
            placeholder="Correo electrónico o telefono"
            className="w-full px-4 py-2 rounded bg-white/20 focus:outline-none focus:ring-2 focus:ring-blue-400 placeholder-black"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />

          <input
            type="password"
            placeholder="Contraseña"
            className="w-full px-4 py-2 rounded bg-white/20 focus:outline-none focus:ring-2 focus:ring-blue-400 placeholder-black"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />

          <button
            onClick={handleLogin}
            disabled={loading}
            className="text-white w-full py-2 px-4 bg-blue-600 hover:bg-blue-700 transition rounded font-semibold disabled:opacity-60"
          >
            {loading ? 'Iniciando...' : 'Iniciar Sesión'}
          </button>

          <p className="mt-6 text-center text-sm text-black/80">
            ¿No tienes cuenta?{' '}
            <Link href="/register" className="text-black hover:underline font-medium">
              Regístrate aquí
            </Link>
          </p>
        </div>
      </div>
    </div>
  )
}
