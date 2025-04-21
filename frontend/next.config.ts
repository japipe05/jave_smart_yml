const nextConfig = {
  output: "standalone",
  experimental: {
    disableOptimizedLoading: true, // Mejora compatibilidad con Docker
  },
  images: {
    domains: ["sibcolombia.net"],
  }
  
};

export default nextConfig;
