/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/**/*.html',
      './node_modules/flowbite/**/*.js'
  ],
  theme: {
    colors: {
      'red': '#dc2626',
    },

    extend: {},
  },
  plugins: [
      require('flowbite/plugin'),
      preflight: false
  ],
}
