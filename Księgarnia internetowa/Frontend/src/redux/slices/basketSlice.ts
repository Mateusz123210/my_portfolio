import { createSlice, PayloadAction } from "@reduxjs/toolkit";
import Book from "../../models/Book";

export interface BasketProduct {
    id: number,
    price: number,
    quantity: number
}

export interface CreateBasketProduct {
    id: number,
    price: number,
}

export interface UpdateBasketProduct {
    id: number,
    quantity: number
}

export interface BasketState {
    products: BasketProduct[],
    totalPrice: number
}

const initialState: BasketState = {
    products: [],
    totalPrice: 0
}

export const basketSlice = createSlice({
    name: 'basket',
    initialState,
    reducers: {
        addProduct(state, action: PayloadAction<CreateBasketProduct>){
            const id = action.payload.id
            const price = +action.payload.price

            if(!state.products.map((p: BasketProduct) => p.id).includes(id)){
                state.products = [...state.products, {id: id, price: price, quantity: 1}]
                state.totalPrice += price
            }
            else{

                let newProducts = [...state.products]
                const index = state.products.map(p => p.id).indexOf(id)

                let existingProduct = state.products[index]

                existingProduct.quantity++
                newProducts[index] = existingProduct

                state.products = newProducts
                state.totalPrice += +price
            }
        },
        updateProductQuantity(state, action: PayloadAction<UpdateBasketProduct>){
            const data = action.payload
            if(data.quantity <= 0){
                return
            }
            let newProducts = [...state.products]

            const index = state.products.map(p => p.id).indexOf(data.id)

            let existingProduct = state.products[index]

            const priceDiff = (data.quantity - existingProduct.quantity) * existingProduct.price
            existingProduct.quantity = data.quantity
            newProducts[index] = existingProduct

            state.products = newProducts
            state.totalPrice += +priceDiff
        },
        removeProduct(state, action: PayloadAction<number>){
            const id = action.payload

            const index = state.products.map(p => p.id).indexOf(id)
            
            const reducedPrice = state.products[index].price * state.products[index].quantity

            const newProducts = [...state.products]
            newProducts.splice(index, 1)

            state.products = newProducts
            state.totalPrice -= +reducedPrice
        },
        clear(state){
            state.products = []
            state.totalPrice = 0
        }
    }
})

export const { addProduct, removeProduct, updateProductQuantity, clear } = basketSlice.actions
export default basketSlice.reducer