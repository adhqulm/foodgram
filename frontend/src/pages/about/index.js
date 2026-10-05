import { Title, Container, Main } from '../../components'
import styles from './styles.module.css'
import MetaTags from 'react-meta-tags'

const About = ({ updateOrders, orders }) => {
  
  return <Main>
    <MetaTags>
      <title>About</title>
      <meta name="description" content="Foodgram - About" />
      <meta property="og:title" content="About" />
    </MetaTags>
    
    <Container>
      <h1 className={styles.title}>Hello!</h1>
      <div className={styles.content}>
        <div>
          <h2 className={styles.subtitle}>What is this site?</h2>
          <div className={styles.text}>
            <p className={styles.textItem}>
              This project was built as part of a learning course, but all of it was created independently.
            </p>
            <p className={styles.textItem}>
              The goal of this site is to let users create and store recipes on an online platform. You can also download a list of the groceries needed to
              cook a dish, browse your friends' recipes and add your favorite recipes to your favorites.
            </p>
            <p className={styles.textItem}>
              You need to sign up to use all of the site's features. Email addresses are not verified, so you can enter any email. 
            </p>
            <p className={styles.textItem}>
              Come in and share your favorite recipes!
            </p>
          </div>
        </div>
        <aside>
          <h2 className={styles.additionalTitle}>
            Links
          </h2>
          <div className={styles.text}>
            <p className={styles.textItem}>
              The project code is here: <a href="#" className={styles.textLink}>Github</a>
            </p>
            <p className={styles.textItem}>
              Project author: <a href="#" className={styles.textLink}>Author Name</a>
            </p>
          </div>
        </aside>
      </div>
      
    </Container>
  </Main>
}

export default About

