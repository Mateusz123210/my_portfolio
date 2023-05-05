import { combineReducers } from "@reduxjs/toolkit";
import notificationReducer from './slices/notificationSlice'
import basketReducer from './slices/basketSlice'
import userReducer from './slices/userSlice'

export const rootReducer = combineReducers({
    notification: notificationReducer,
    basket: basketReducer,
    user: userReducer
})