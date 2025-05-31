import React from "react"
import styles from "../styles/Login.module.css"
import Botao from "../components/Botao"
import NeoSense from '../assets/NeoSense.png'


const Login = () => {
    return(
        <div className={styles.login_page}>
            <div className={styles.logo}>
                <img src={NeoSense} alt="Logo Neo Sense" />
            </div>
            <div className={styles.login_part}>
                <div className={styles.login_text}>
                    <h1>Login</h1>
                </div>

               
                <form className={styles.formulario}>
                    <label className={styles.labels}  htmlFor="Email">Email</label>
                    <input
                    placeholder='Username'
                    className={styles.field}
                    />

                    <label className={styles.labels} htmlFor="Senha">Senha</label>
                    <input 
                    placeholder='Password'
                    className={styles.field}
                    />
                

                    <a href="http://" className="forget-password">
                        Esqueceu a senha
                    </a>

                    <Botao text="Entrar"/>
                </form>
                
            </div>
        </div>
    )
}

export default Login
