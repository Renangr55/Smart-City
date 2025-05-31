import style from "../styles/Header.module.css"
import { FaUser } from 'react-icons/fa';
import NeoSense from '../assets/NeoSense.png'


const Header = (props) => {
    return (
        <header>
            <div className={style.header_class}>
                <img src={NeoSense} alt="Logo NeoSense" className={style.logo} />
                
                <ul className="header-links">
                    <li><a href="#">{props.first}</a></li>
                    <li><a href="#">{props.second}</a></li>
                    <li><a href="#">{props.thirst}</a></li>
                </ul>

                <div className="icon-signup">
                  <FaUser />
                </div>
            </div>
        </header>


    )
}

export default Header