import style from "../styles/Header.module.css"
import { FaUser } from 'react-icons/fa';


const Header = () => {
    return (
        <header>
            <div className={style.header_class}>
                <h1 className="logo-text">Neosense</h1>
                
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