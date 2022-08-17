import React from "react"
import { Container } from 'react-bootstrap';
//import {BrowserRouter} from 'react-router-dom'
import './App.css';
import Header from './components/Header'
import Footer from './components/Footer'
import HomeScreen from './screens/HomeScreen'


function App() {
  return (
    <div className="App">
      <Header />
      <main className='py-3'>
        <Container>
          <HomeScreen />
        </Container>        
      </main>
      <Footer />
    </div>
  );
}

export default App;
