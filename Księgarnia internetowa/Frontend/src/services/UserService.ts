import axios from "axios"
import { PersonalData } from "../models/PersonalData"

export interface Credentials {
    username: string,
    password: string
}

class UserService {

    private apiUrl1: string = `${process.env.REACT_APP_API_1 as string}/v1/user`

    register(credentials: Credentials, personalData: PersonalData){
        return axios.post(`${this.apiUrl1}/register`, {...credentials, ...personalData})
    }

    login(credentials: Credentials){
        return axios.post(`${this.apiUrl1}/token`, {}, {
            auth: {
                username: credentials.username,
                password: credentials.password
            }
        })
    }
}

export default new UserService()