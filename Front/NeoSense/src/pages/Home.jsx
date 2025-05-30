import Header from "../components/Header";
import styles from "../styles/Home.module.css"

const Home = () => {
    return (
    <div className={styles.home_page}>
        <div className={styles.home_img}> 
            <Header />
        </div>
        <div className="main-home">
            <h1 className={styles.main_text}>Type of Sensors</h1>
        </div>
          
    </div>
    
    
        
        
    )
}

export default Home