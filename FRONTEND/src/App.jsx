import React from 'react'
import { BrowserRouter, Routes, Route } from "react-router-dom";
import MainApp from './pages/MainApp'

function App() {
  return (
    <Routes>
      <Route path='/' element={<MainApp/>}/>
    </Routes>
  )
}

export default App