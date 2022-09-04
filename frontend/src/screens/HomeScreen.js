import React, {useEffect, useState} from 'react'
import {Col, Row} from 'react-bootstrap'
import Product from '../components/Product'

import axios from 'axios'

function HomeScreen() {
    const [products, setProducts] = useState([])

    useEffect(() => {

        async function fetchProducts() {
            const {data} = await axios.get('/api/products')
            setProducts(data)
        }

        fetchProducts()

    }, [])
    return (
        <div>

            <div className="py-3">
                <h4>Latest Products</h4>
            </div>

            <Row>
                {products.map(product => (
                    <Col key={product.id} sm={12} md={6} lg={4} xl={3}>
                        <Product product={product}/>
                    </Col>
                ))}
            </Row>

        </div>

    )
}

export default HomeScreen