import { defineConfig } from 'vite';
import solidPlugin from 'vite-plugin-solid';
import path from "path";

console.log(path.resolve(__dirname, "./src/*"))

export default defineConfig({
  resolve: {
    alias: {
      "@assets": path.resolve(__dirname, "./src/assets/"),
      "@pages": path.resolve(__dirname, "./src/pages/"),
      "@widgets": path.resolve(__dirname, "./src/widgets/"),
      "@features": path.resolve(__dirname, "./src/features/"),
      "@entities": path.resolve(__dirname, "./src/entities/"),
      "@shared": path.resolve(__dirname, "./src/shared/"),
    },
  },
  plugins: [solidPlugin()],
  server: {
    port: 3000,
    hmr: true
  },
  build: {
    target: 'esnext',
  },
});
