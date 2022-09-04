import React from 'react'
import {Navbar, Nav, Container} from 'react-bootstrap'
import {LinkContainer} from 'react-router-bootstrap'

function Header() {
  return (
    <header>
      
      <Navbar bg="light" variant="light" expand="lg">

        <Container className="container-fluid">

          <LinkContainer to='/'>
            <Navbar.Brand href="#"><h3>Tradesman KE</h3></Navbar.Brand>
          </LinkContainer>

          <Navbar.Toggle aria-controls="navbarScroll" />

          <Navbar.Collapse id="navbarScroll">

            <Nav className="mr-auto">

              <Nav.Link href="About" disabled> Link</Nav.Link>

              <LinkContainer to='/cart' className="justify-content-end">
                <Nav.Link> Cart <i className='fas fa-shopping-cart'></i></Nav.Link>
              </LinkContainer>

              <LinkContainer to='/login'>
                <Nav.Link> Login <i className='fas fa-user'></i></Nav.Link>               
              </LinkContainer>             
              
            </Nav>
            
          </Navbar.Collapse>
          
        </Container>
      </Navbar>
    </header>
  )
}

export default Header