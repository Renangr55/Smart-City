import LoginImage from '../assets/LoginImage.jpg'
import '../style/Login.modules.css' 
import { useForm } from "react-hook-form" // Forms do react form
import {z} from 'zod' // zod 
import {zodResolver} from '@hookform/resolvers/zod'




function LoginPage (){
    const loginSchema = z.object({
        username: z.string().min(1,{message: 'Insira seu username'}),
        Password: z.string().min(1,{message: 'Insira sua senha'}),
    })



    const { register, handleSubmit } = useForm()
    const onSubmit = (data) => console.log(data)


    return (
       

    <div id='login-area'>
        <div className='logo'>
            <h1>NeoSense</h1>
        </div>
        <div className='Cadastro'>
            <h1>Login </h1>
            <div className='Form'></div>
        </div>
    </div>

        
        
    )
}

export default LoginPage