import React from 'react'
import {Card} from 'react-bootstrap'
import Rating from './Rating'
import {Link} from 'react-router-dom'

function Product({product}) {
    return (
        <Link to={`/product/${product.id}`} className="text-decoration-none  text-dark">
            <Card className='shadow my-3 p-0 border-0 rounded-0'>
                <Card.Img className='rounded-0 border-0' src={product.image}/>

                <Card.Body>
                    <Card.Title>
                        <h5>{product.title}</h5>
                    </Card.Title>

                    <Card.Text as="div">
                        <div className='mt-4 h6'>
                            <Rating value={product.rating} text={`${product.review_count} reviews`} color={'#8885e6'}/>
                        </div>
                    </Card.Text>

                    <Card.Text as="h6">
                        Ksh. {product.price}
                    </Card.Text>
                </Card.Body>
            </Card>
        </Link>
    )
}

export default Product