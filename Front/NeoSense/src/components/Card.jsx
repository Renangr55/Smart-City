import styles from "../styles/Card.module.css"
import {Link} from 'react-router-dom'

const Card = (props) => {
    return (
        <div className={styles.card_area}>
            <div className="icon">
                {props.icon_sensor && <props.icon_sensor size={props.width_icon} style={{color: props.color_icon}} />}
            </div>

            <h1 className={styles.title_card} style={{ color: props.title_color }}>
                {props.title}
            </h1>
            
            <p className={styles.description}>{props.description}</p>

            <div className="btn_card"> 
                <button>
                    ver informações 
                </button>
            </div>  
                


        </div>
    )
}

export default Card