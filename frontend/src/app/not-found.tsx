'use client'

import Image from 'next/image'
import { usePathname } from 'next/navigation'

export default function NotFound() {
  const pathname = usePathname()
  const productId = pathname.split('/')[2]
  const reviewId = pathname.split('/')[4]

  return (
    <div className="relative flex items-center justify-center min-h-screen text-white overflow-hidden">
      {/* Fondo borroso */}
      <Image
        src="/fondo.png"
        alt="Fondo"
        layout="fill"
        objectFit="cover"
        quality={100}
        className="-z-10"
      />

      {/* Contenido centrado */}
      <div className="w-full max-w-md bg-white/30 backdrop-blur-md p-8 rounded-2xl border border-white/40 shadow-2xl text-white">
        <h1 className="text-4xl font-bold">Página no encontrada</h1>
        <p className="text-lg">
          La reseña con ID <span className="font-semibold text-red-400">{reviewId}</span> no fue encontrada
          para el producto <span className="font-semibold text-blue-400">{productId}</span>.
        </p>
        <p>Por favor, verifica la URL o regresa al inicio.</p>
      </div>
    </div>
  )
}
