import { useEffect, useState } from 'react'
import './App.css'

function App() {
  const [todo, setTodo] = useState([])
  let value = ""

  return (
    <>
      <div className='w-full p-[5%] inline-flex justify-center gap-[2%]'>
        <input id="add" className='border rounded-[1vw] text-[150%] p-[1%]' type="text" placeholder="Enter the Data: " onChange={(e)=>{
          value = e.target.value
          
        }}/>
        <button className='border p-[1%] rounded-[1vw] text-[150%] font-bold' onClick={()=>{
          setTodo(value)          
        }}>Add (+)</button>
      </div>
      {useEffect(()=>{
        <div>
          
        </div>
      }, todo)}
    </>
  )
}

export default App
