//import React from "react"
import {Navbar, Nav, Container} from 'react-bootstrap'

import React from 'react'

function Header() {
  return (
    <header>
      
      <Navbar bg="light" variant="light" expand="lg">

        <Container fluid>

          <Navbar.Brand href="#">Tradesman KE</Navbar.Brand>
          <Navbar.Toggle aria-controls="navbarScroll" />

          <Navbar.Collapse id="navbarScroll">
            <Nav className="mr-auto">
              <Nav.Link href="About" disabled> Link</Nav.Link>
              <Nav.Link href="/cart"> Cart <i className='fas fa-shopping-cart'></i></Nav.Link>
              <Nav.Link href="/login"> Login <i className='fas fa-user'></i></Nav.Link>              
            </Nav>
          </Navbar.Collapse>
          
        </Container>
      </Navbar>
    </header>
  )
}

export default Header