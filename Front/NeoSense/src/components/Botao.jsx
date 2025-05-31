import React from "react"
import styles from "../styles/Botao.module.css"

const Botao = (props) => {
    return (
        <div className={styles.botao}>
            <button type="submit">
                <h1>{props.text}</h1>
            </button>
        </div>
    )
}

export default Botao