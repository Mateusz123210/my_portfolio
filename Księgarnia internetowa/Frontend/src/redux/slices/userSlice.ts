import { createSlice, PayloadAction } from "@reduxjs/toolkit";

export interface UserState {
    userId?: number,
    clientId?: number,
    isLogged: boolean
}

const initialState: UserState = {
    isLogged: false
}

export interface LoginData {
    userId?: number,
    clientId?: number,
}

export const userSlice = createSlice({
    name: 'user',
    initialState,
    reducers: {
        login(state, action: PayloadAction<LoginData>){
            const data = action.payload
            state.userId = data.userId
            state.clientId = data.clientId
            state.isLogged = true
        },
        logout(state){
            state.userId = undefined
            state.clientId = undefined
            state.isLogged = false
        }
    }
})

export const { login, logout } = userSlice.actions
export default userSlice.reducer