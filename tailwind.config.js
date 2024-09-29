/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',            // ระบุไฟล์ HTML ในโฟลเดอร์ templates ระดับโปรเจกต์หลัก (ถ้ามี)
    './store/templates/**/*.html',      // ระบุไฟล์ HTML ในโฟลเดอร์ templates ของแอป store
    './store/static/**/*.js',           // ระบุไฟล์ JavaScript ในโฟลเดอร์ static ของแอป store
    './store/static/**/*.css',          // ระบุไฟล์ CSS ในโฟลเดอร์ static ของแอป store
    './store/**/*.py',                  // ระบุไฟล์ Python ของแอป store
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
