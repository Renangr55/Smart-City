import React from "react"
import styles from "../styles/Login.module.css"
import Botao from "../components/Botao"

const Login = () => {
    return(
        <div className={styles.login_page}>
            <div className={styles.NeoSense}>
                <h1>NeoSense</h1>
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
                </form>

                <a href="http://" className="forget-password">
                    Esqueceu a senha
                </a>

                <Botao />
                
            </div>
        </div>
    )
}

export default Login
