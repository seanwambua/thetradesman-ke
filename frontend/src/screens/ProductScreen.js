import React from 'react'
import {Link, useParams} from 'react-router-dom'
import {Row, Col, Image, ListGroup, Card} from 'react-bootstrap'
import Rating from '../components/Rating'
import products from '../products'

function ProductScreen() {
  const {id} = useParams()
  const product = products.find((p)=>p._id ===id)
  return (
    <div>
      <Link to='/'className="btn btn-light my-3 border-0"> Go back</Link>
     
      <Row>
        <Col md={6}>
          <Image src={product.image} alt={product.name} fluid />
        </Col>

        <Col md={3}>
          <ListGroup variant='flush'>
          <ListGroup.Item>
              <h3>{product.name}</h3>
            </ListGroup.Item>

            <ListGroup.Item>
              <Rating value={product.rating} color='#8885e6' text={`${product.numReviews} reviews`}/>
            </ListGroup.Item>

            <ListGroup.Item>
              Price: Ksh. {product.price*100}
            </ListGroup.Item>

            <ListGroup.Item>
              Description {product.description}
            </ListGroup.Item>
          </ListGroup>
        </Col>

        <Col md={3}>
          <Card className="shadow border-0 py-3">
          <ListGroup variant='flush'>
            <ListGroup.Item>
              <Row>
                <Col>
                  Price: 
                </Col>
                <Col>
                  <strong>Ksh. {product.price * 100}</strong>
                </Col>
              </Row>              
            </ListGroup.Item>
          </ListGroup>

          <ListGroup variant='flush'>
            <ListGroup.Item>
              <Row>
                <Col>
                  Status:
                </Col>
                <Col>
                  {product.countInStock>0 ? 'In Stock' : 'Out of Stock'}
                </Col>
              </Row>              
            </ListGroup.Item>
          </ListGroup>
          </Card>
        </Col>
        
      </Row>
    </div>
  )
}

export default ProductScreen