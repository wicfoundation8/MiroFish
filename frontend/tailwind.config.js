/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'wic-gold': '#DAA520',
        'wic-cyan': '#00FFFF',
        'wic-dark': '#0d0d0d',
      }
    },
  },
  plugins: [],
}