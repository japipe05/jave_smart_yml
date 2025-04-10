const nextConfig = {
  output: "standalone",
  experimental: {
    disableOptimizedLoading: true, // Mejora compatibilidad con Docker
  },
};

export default nextConfig;
