import axios from "axios"

class OrderStatusService {

    private apiUrl: string = `${process.env.REACT_APP_API_1 as string}/v1/order-statuses`

    getAll = () => {
        return axios.get(this.apiUrl)
    }
}

export default new OrderStatusService()