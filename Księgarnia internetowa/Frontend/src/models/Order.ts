import Book from "./Book";
import { OrderStatus } from "./OrderStatus";

export default interface Order{
    id: number,
    orderStatusEntity: OrderStatus,
    books: Book[],
    totalPrice: number,
    creationDate: Date,
    fullfillmentDate?: Date
}