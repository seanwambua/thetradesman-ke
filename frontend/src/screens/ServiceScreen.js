import React, {useEffect, useState} from 'react'
import {useParams} from 'react-router-dom'
import {Card, Col, ListGroup, Row} from 'react-bootstrap'
import Rating from '../components/Rating'
import axios from "axios";


function ServiceScreen(props) {
    const {id} = useParams()
    const [service, setProduct] = useState([])

    useEffect(() => {

        async function fetchService() {
            const {data} = await axios.get(`/api/services/${id}`)
            setService(data)
        }

        fetchService().then()
    }, []);
    return (
        <div>
            <Row className="mt-4 py-3">
                <Col md={6}>
                    <Card.Img src={product.image} alt={product.title} className="shadow border-0"/>
                </Col>

                <Col md={4}>
                    <Card className="border-0 py-3">
                        <ListGroup variant='flush'>

                            <ListGroup.Item>
                                <h3>{product.title}</h3>
                            </ListGroup.Item>

                            <ListGroup.Item>
                                Description {product.description}
                            </ListGroup.Item>
                        </ListGroup>
                    </Card>

                    <Card className="border-0 py-0">
                        <ListGroup variant='flush'>
                            <ListGroup.Item>
                                <Row>
                                    <Col>
                                        Price:
                                    </Col>
                                    <Col>
                                        <strong>Ksh. {product.price}</strong>
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
                                        {product.stock_count > 0 ? 'In Stock' : 'Out of Stock'}
                                    </Col>

                                </Row>
                            </ListGroup.Item>

                            <ListGroup variant='flush'>
                                <ListGroup.Item>
                                    <Row>
                                        <Col>
                                            Rating:
                                        </Col>
                                        <Col>
                                            <Rating value={product.rating} color='#8885e6'/>
                                        </Col>
                                    </Row>
                                </ListGroup.Item>
                            </ListGroup>
                        </ListGroup>
                    </Card>
                </Col>

                <Col md={2}>
                    <Card className="border-0 py-3">
                        <ListGroup variant='flush'>

                            <ListGroup.Item>
                                <button type="submit" className="btn btn-secondary">Add to Cart</button>
                            </ListGroup.Item>
                        </ListGroup>
                    </Card>
                </Col>
            </Row>
        </div>
    )
}

export default ProductScreen