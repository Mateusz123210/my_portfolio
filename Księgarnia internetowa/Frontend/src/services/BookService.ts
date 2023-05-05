import axios from "axios"

export interface BookSearchCriteria {
    id?: number, 
    title?:string, 
    genres?: string[], 
    author?: string,
    publisher?: string, 
    releaseDate?: Date, 
    minPrice?: number, 
    maxPrice?: number
}

class BookData{

    private apiUrl1: string = `${process.env.REACT_APP_API_1 as string}/v1`
    private apiUrl2: string = `${process.env.REACT_APP_API_2 as string}`

    getBookData(id: number){

        return axios.get(`${this.apiUrl2}/book/${id}`);
    }

    getBooksByIds(ids: number[]){

        return axios.get(`${this.apiUrl1}/books/by-Ids`, {
            params: {
                bookIds: ids.join(',')
            }
        });
    }

    getFoundBooks(searchCriteria: BookSearchCriteria){

        return axios.get(`${this.apiUrl2}/books/find/`, {
            params: {
              ...searchCriteria, genres: searchCriteria.genres?.join(',')
            },
        });
    }

    getAllAvailableBooks(){

        return axios.get(`${this.apiUrl2}/books/all`);
    }
}
export default new BookData();