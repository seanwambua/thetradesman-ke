import React from 'react'
import {Card} from 'react-bootstrap'
import Rating from './Rating'
import {Link} from 'react-router-dom'

function Product({product}) {
  return (
    <Link to={`/product/${product._id}`} className="text-decoration-none  text-dark">
      <Card className='shadow my-3 p-0 border-0'>          
          <Card.Img src= {product.image}/>       

          <Card.Body>            
            <Card.Title >
              <h5>{product.name}</h5>
            </Card.Title>

            <Card.Text as="div">
              <div className='my-3'>
                <Rating value={product.rating} text={`${product.numReviews} reviews`} color= {'#8885e6'}></Rating>
              </div>
            </Card.Text>

            <Card.Text as="h5">
                Ksh. {product.price * 100.00}
            </Card.Text>
          </Card.Body>          
      </Card>
    </Link>
  )
}

export default Product