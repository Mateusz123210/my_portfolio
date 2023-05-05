import { Box, Button, Checkbox, FormControl, FormControlLabel, FormGroup, FormLabel, Grid, OutlinedInput, Pagination, Paper, Slider, TextField, Typography } from "@mui/material";
import { useState, useEffect } from "react";
import Book from "../../models/Book";
import { book1 } from "../../assets/books";
import BookHeaderView from "./BookHeaderView";
import BookCategory from "../../models/BookCategory";
import FormElement from "../../components/common/FormElement";
import DatePickerForm from "../../components/common/DatePickerForm";
import { privateDecrypt } from "crypto";
import BookService from "../../services/BookService";
import { BookSearchCriteria } from "../../services/BookService";
import React from "react";
import { Pagination as PaginationModel} from "../../models/Pagination";
import { PageInfo } from "../../models/PageInfo";

export const books: Book[] = [
    {
        id: 1,
        title: 'Ostatnie życzenie. Wiedźmin. Tom 1',
        authors: [{author_name: 'Andrzej', author_surname: 'Sapkowski'}],
        book_category: 'Przygodowe',
        publisher: 'SUPERNOWA',
        book_cover: 'okładka miękka',
        language: 'polski',
        avatar: book1,
        description: 'Ostatnie życzenie. Wiedźmin, Tom 1',
        isbn: '978-83-01-00000-1',
        release_number: 1,
        release_date: new Date('2014-10-06'),
        size: '195 x 24 x 125',
        number_of_pages: '332',
        price: 39.92
    }
]

interface BookCategorySelect{
    id: number,
    name: string,
    checked: boolean 
}

interface Form {
    title: string,
    author: string,
    publisher: string,
    releaseDate?: Date,
    priceFrom?: number,
    priceTo?: number,
    bookCategories: BookCategorySelect[]
}

export interface BookHeader {
    id: number,
    title: string,
    price: number,
    avatar?: string
}

const Shop = () => {

    const [form, setForm] = useState<Form>({
        title: '',
        author: '',
        publisher: '',
        bookCategories: []
    })

    const [books, setBooks] = useState<BookHeader[]>([])

    const [pagination, setPagination] = React.useState<PaginationModel>({
        page: 0,
        size: 8,
    })
    
    const [pageInfo, setPageInfo] = React.useState<PageInfo>({
        numberOfElements: 0,
        totalPages: 0,
        totalElements: 0,
    })

    useEffect(() => {
        BookService.getAllAvailableBooks()
        .then((response) => {
            const newBooks = response.data[0].books.slice(pagination.page * pagination.size, (pagination.page+1) * pagination.size)
            setBooks(newBooks)
            setPageInfo({
                ...pageInfo,
                totalPages: Math.ceil(response.data[0].books.length / pagination.size)
            })

            const foundCategories = response.data[1].categories.map((category: BookCategory, index: number) => ({
                id: index,
                name: category.name,
                checked: false
            }))

            setForm({...form, bookCategories: foundCategories})
        })
        .catch((error) => {
            console.log(error)
        })
    }, [])

    const handleChangeBookCategory = (event: React.ChangeEvent<HTMLInputElement>, checked: boolean) => {

        const bookCategoryId: number = +event.target.id

        let newBookCategories: BookCategorySelect[] = form.bookCategories ? form.bookCategories : []

        const changedBookCategoryIndex = newBookCategories.map((category: BookCategorySelect) => category.id)
        .indexOf(bookCategoryId)

        newBookCategories[changedBookCategoryIndex].checked = checked

        setForm({...form, bookCategories: newBookCategories})
    }

    const getBooksByCriterias = (actualPage: number) => {

        const selectedBookCategories: string[] = form.bookCategories ? form.bookCategories
            .filter((category: BookCategorySelect) => category.checked)
            .map((category: BookCategorySelect) => category.name)
        : []

        let criteria: any = {}

        if(form.title !== ''){
            criteria['title'] = form.title
        }

        if(selectedBookCategories.length < form.bookCategories.length && selectedBookCategories.length !== 0) {

            criteria['genres'] = [...selectedBookCategories]
            
        }

        if(form.author !== ''){
            criteria['author'] = form.author 
        }

        if(form.publisher !== ''){
            criteria['publisher'] = form.publisher 
        }

        if(form.releaseDate){
            criteria['releaseDate'] = form.releaseDate 
        }

        if(form.priceFrom){
            criteria['minPrice'] = form.priceFrom 
        }

        if(form.priceTo){
            criteria['maxPrice'] = form.priceTo 
        }

        BookService.getFoundBooks(criteria)
        .then((response) => {
            const newBooks = response.data.slice(actualPage * pagination.size, (actualPage+1) * pagination.size)
            setBooks(newBooks)
            setPageInfo({
                ...pageInfo,
                totalPages: Math.ceil(response.data.length / pagination.size)
            })
        })
        .catch((error) => {
            console.log(error)
        })
    }

    const setPriceRange = (event: Event, newValue: number | number[]) => {
        const priceRange: number[] = newValue as number[]
        setForm({...form, priceFrom: priceRange[0], priceTo: priceRange[1]})
    };

    return (
        <Grid container justifyContent="center" marginTop={8}>
            <Grid item xs={11} container justifyContent="end">
                <Grid item xs={9} container spacing={3} alignItems="center">
                    <Grid item xs={10}>
                        <TextField
                            fullWidth   
                            placeholder="Podaj tytuł książki..."
                            value={form.title ? form.title : ''}
                            onChange={(event) => setForm({...form, title: event.target.value})}
                        />
                    </Grid>
                    <Grid item xs={2}>
                        <Button
                            fullWidth
                            variant="contained"
                            color="secondary"
                            sx={{padding: '14px 0px'}}
                            onClick={() => getBooksByCriterias(pagination.page)}
                        >
                            Szukaj
                        </Button>
                    </Grid>
                </Grid>
            </Grid>
            <Grid item xs={11} container justifyContent="space-between" marginTop={8} columnSpacing={8}>
                <Grid item xs={3} container justifyContent="center" alignSelf="start">
                    <Paper sx={{padding: '10px 20px', minWidth: 140, minHeight: 233}}>
                        <Typography component="h5" textAlign="left">
                            Gatunek
                        </Typography>
                        <FormControl component="fieldset" variant="standard">
                            <FormGroup>
                                {(form.bookCategories ? form.bookCategories : []).map((category: BookCategorySelect, index: number) => (
                                    <FormControlLabel
                                        key={category.id}
                                        label={category.name}
                                        control={
                                            <Checkbox
                                                id={category.id.toString()}
                                                checked={category.checked}
                                                onChange={handleChangeBookCategory}
                                            />
                                        }
                                    />
                                ))}
                            </FormGroup>
                        </FormControl>
                    </Paper>
                    <Grid item container rowSpacing={2} marginTop={4}>
                        <FormElement
                            fieldName="Autor:"
                            placeholder="Wpisz autora..."
                            value={form.author ? form.author : ''}
                            onChange={(event) => setForm({...form, author: event.target.value})}
                        />
                        <FormElement
                            fieldName="Wydawca:"
                            placeholder="Wpisz wydawcę..."
                            value={form.publisher ? form.publisher : ''}
                            onChange={(event) => setForm({...form, publisher: event.target.value})}
                        />
                        <DatePickerForm
                            fieldName="Data wydania"
                            placeholder="Wpisz datę..."
                            maxDate={new Date()}
                            value={form.releaseDate}
                            onChange={(newValue) => setForm({...form, releaseDate: newValue != null ? newValue : undefined})}
                        />
                        <Grid item container alignItems="center">
                            <Grid item xs={6}>
                                <Typography 
                                    textAlign="start" 
                                    variant="h6"
                                >
                                    Cena
                                </Typography>
                            </Grid>
                            <Grid item xs={6} container justifyContent="center" alignItems="center" marginTop={3}>
                                <Slider
                                    getAriaLabel={() => 'Temperature range'}
                                    value={[form.priceFrom, form.priceTo] as number[]}
                                    onChange={setPriceRange}
                                    max={1000}
                                    valueLabelDisplay="auto"
                                    getAriaValueText={(value: number) => `${value}zł`}
                                />
                                <Typography 
                                    textAlign="center" 
                                    variant="h6"
                                >
                                    {`${form.priceFrom !== undefined ? form.priceFrom : 0} zł - `}
                                    {`${form.priceTo !== undefined ? form.priceTo : 1000} zł`}
                                </Typography>
                            </Grid>
                        </Grid> 
                    </Grid>
                </Grid>
                <Grid item xs={9} container justifyContent="start" alignItems="center" rowSpacing={6}>
                    {!books ? null : books.map((b: BookHeader) => (
                        <BookHeaderView key={b.id} book={b}/>
                    ))}
                </Grid>
                <Grid item xs={12} container justifyContent="end" alignItems="center" marginBottom={8} marginTop={-3}>
                    <Grid item xs={9} container justifyContent="center">
                        <Pagination 
                            variant="outlined"
                            color="secondary"
                            sx={{backgroundColor: 'white'}}
                            shape="rounded"
                            count={pageInfo.totalPages}
                            onChange={(event: any, page: number) => {
                                getBooksByCriterias(page-1)
                                setPagination({...pagination, page: page-1})
                            }}
                        />
                    </Grid>
                </Grid>
            </Grid>
        </Grid>
    )
}

export default Shop;