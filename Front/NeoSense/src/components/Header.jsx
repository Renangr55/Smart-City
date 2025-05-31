import style from "../styles/Header.module.css"
import { FaUser } from 'react-icons/fa';
import NeoSense from '../assets/NeoSense.png'


const Header = () => {
    return (
        <header>
            <div className={style.header_class}>
                <img src={NeoSense} alt="Logo NeoSense" className={style.logo} />
                
                <ul className="header-links">
                    <li><a href="#">About</a></li>
                    <li><a href="#">Sensors</a></li>
                    <li><a href="#">Export</a></li>
                </ul>

                <div className="icon-signup">
                  <FaUser />
                </div>
            </div>
        </header>


    )
}

export default Header