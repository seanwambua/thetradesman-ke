import React from 'react'
import {Card} from 'react-bootstrap'
import Rating from './Rating'

function Product({product}) {
  return (
    <Card className='my-3 p-3 rounded'>

        <a href={`/product/${product._id}`}>
          <Card.Img src= {product.image}/>
        </a>

        <Card.Body> 

          <Card.Title >
            <strong>{product.name}</strong>
          </Card.Title>

          <Card.Text as="div">
            <div className='my-3'>
              <Rating value={product.rating} text={`${product.numReviews} reviews`} color={'#8885e6'}></Rating>
            </div>
          </Card.Text>

          <Card.Text as="h5">
              Ksh. {product.price * 100.00}
          </Card.Text>

        </Card.Body>
        
    </Card>
  )
}

export default Product