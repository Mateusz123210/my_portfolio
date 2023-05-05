import axios from 'axios'

class ClientService {

    private apiUrl1: string = `${process.env.REACT_APP_API_1 as string}/v1/client`

    getClientPersonalData = (clientId: number) => {
        return axios.get(`${this.apiUrl1}/${clientId}/personal-data`)
    }
}

export default new ClientService()