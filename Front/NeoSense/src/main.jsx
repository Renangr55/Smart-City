import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import App from './App.jsx'
import './styles/Global.css'
import Login from './pages/Login.jsx'
import Home from './pages/Home.jsx'


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Login />
  
  </StrictMode>,
)
