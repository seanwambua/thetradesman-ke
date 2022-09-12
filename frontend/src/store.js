//import {applyMiddleware, combineReducers, createStore} from "@reduxjs/toolkit";
import { createStore, combineReducers, applyMiddleware } from 'redux'
import thunk from "redux-thunk";
//import {composeWithDevTools} from "@reduxjs/toolkit/dist/devtoolsExtension";
import { composeWithDevTools } from 'redux-devtools-extension'
import {productListReducers} from "./reducers/productReducers";

const reducer = combineReducers({
    productList: productListReducer,
})
const initialState = {}
const middleware = [thunk]
const store = createStore(reducer, initialState,
    composeWithDevTools(applyMiddleware(...middleware)))

export default store
