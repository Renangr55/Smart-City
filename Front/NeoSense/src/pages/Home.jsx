import Header from "../components/Header";
import styles from "../styles/Home.module.css"
import Card from "../components/Card";
import { BsThermometer } from 'react-icons/bs';
import { FaLightbulb } from 'react-icons/fa';
import { FaTint } from 'react-icons/fa';
import { FiActivity } from 'react-icons/fi';






const Home = () => {
    return (

    

    <div className={styles.home_page}>
        <div className={styles.home_img}> 
            <Header first="About" second="Sensors" thirst="Export"/>
        </div>
 
        <div className="main-home">
            <h1 className={styles.main_text}>Type of Sensors</h1>

            <div className="main-parts-of-sensor">
                <Card 
                    width_icon={50}
                    icon_sensor={BsThermometer}
                    title="temporality" 
                    color_icon="#E49047" 
                    title_color="#E49047" 
                    description="A temperature sensor measures the heat or cold of an environment." 
                />
                
                <Card 
                    width_icon={50}
                    icon_sensor={FaLightbulb}
                    title="Luminosity"
                    color_icon="#FFE386" 
                    title_color = "#FFE386"
                    description="A temperature sensor measures the heat or cold of an environment." /> 

                <Card 
                    width_icon={50}
                    icon_sensor={FaTint}
                    title="Humidity" 
                    color_icon="#1EDCF1" 
                    title_color="#1EDCF1"  
                    description="A temperature sensor measures the heat or cold of an environment."
                />

                <Card 
                    width_icon={50}
                    icon_sensor={FiActivity}
                    title="Count"  
                    description="A temperature sensor measures the heat or cold of an environment."/>
            </div>
        </div>

        <div className={styles.main_second_part}>
            <div className="text-crud">
                <h1>Operações</h1>
            </div>

            <div className="main_crud">
                <div className="Sensors">
                    <h1>teste</h1>
                </div>

                <div className="Ambiente">
                    <h1>teste</h1>
                </div>

                <div className="Historic">
                    <h1>teste</h1>
                </div>
            </div>
        </div>

        
          
    </div>
    
    
        
        
    )
}

export default Home