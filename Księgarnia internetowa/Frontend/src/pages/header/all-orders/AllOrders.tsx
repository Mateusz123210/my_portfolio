import {
    Button,
    FormControl,
    FormControlLabel,
    FormHelperText,
    FormLabel,
    Grid,
    OutlinedInput,
    TextField,
    Typography,
  } from "@mui/material";
  import React from "react";
  import useEffect from "react";
  import { useDispatch } from "react-redux";
  import { useNavigate } from "react-router-dom";
import BottomNavigation from "../../../components/common/BottomNavigation";
import DatePickerFormRange from "../../../components/common/DatePickerFormRange";
import FormElement from "../../../components/common/FormElement";
import ValidatedForm from "../../../components/common/ValidatedForm";
import { setNotificationMessage, setNotificationType, setNotificationStatus } from "../../../redux/slices/notificationSlice";
import FormValidator from "../../../services/FormValidator";
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridValueGetterParams } from '@mui/x-data-grid';
import Order from "../../../models/Order";
import OrderService, { OrdersSearchCriteria } from "../../../services/OrderService"
import { Pagination } from "../../../models/Pagination";
import OrderStatusSelect from "../../../components/common/OrderStatusSelect";
import { OrderStatus } from "../../../models/OrderStatus";
import { OrderWithDetails } from "../../../models/OrderWithDetails";
import Page from "../../../models/Page";
import moment from 'moment'
import {PageInfo} from "../../../models/PageInfo";
  
interface FormFields {
  name?: string;
  surname?: string;
  email?: string;
  tel?: string;
  creationDateFrom?: Date;
  creationDateTo?: Date;
  statusId?: number;
  minPrice?: number;
  maxPrice?: number;
}

/*
    id: number,
    creationDate: Date,
    fulfillmentDate?: Date,
    totalPrice: number,
    status: OrderStatus,
    books: OrderBookDetails[],
    receiverData: PersonalData
*/

const columns: GridColDef[] = [
  { 
    field: 'id', 
    headerName: 'Id',
    flex: 1,
    align: 'center',
    headerAlign: 'center',
    renderCell: (params: any) => {
      return (<Typography>
        {params.row.id}
      </Typography>)
    }
  },
  {
    field: 'name',
    headerName: 'Imię',
    flex: 2,
    align: 'center',
    headerAlign: 'center',
    renderCell: (params: any) => {
      return (<Typography>
        {params.row.receiverData.name}
      </Typography>)
    }
  },
  {
    field: 'surname',
    headerName: 'Nazwisko',
    flex: 2,
    align: 'center',
    headerAlign: 'center',
    renderCell: (params: any) => (
      <Typography>
        {params.row.receiverData.surname}
      </Typography>
    )
  },
  {
    field: 'creationDate',
    headerName: 'Data utworzenia',
    flex: 2,
    align: 'center',
    headerAlign: 'center',
    renderCell: (params: any) => (
      <Typography>
        {moment(params.row.creationDate).format("DD.MM.YYYY").toLocaleString()}
      </Typography>
    )
  },
  {
    field: 'num_of_products',
    headerName: 'Liczba produktów',
    flex: 2,
    align: 'center',
    headerAlign: 'center',
    renderCell: (params: any) => (
      <Typography>
        {params.row.books.length}
      </Typography>
    )
  },
  {
    field: 'price',
    headerName: 'Cena',
    type: 'number',
    flex: 2,
    align: 'center',
    headerAlign: 'center',
    renderCell: (params: any) => (
      <Typography>
        {params.row.totalPrice} zł
      </Typography>
    )
  },  
  {
    field: 'status',
    headerName: 'Status',
    type: 'number',
    flex: 2,
    align: 'center',
    headerAlign: 'center',
    renderCell: (params: any) => (
      <Typography>
        {params.row.status.name}
      </Typography>
    )
  },
  {
    field: 'email',
    headerName: 'Email',
    type: 'number',
    flex: 3,
    align: 'center',
    headerAlign: 'center',
    renderCell: (params: any) => (
      <Typography>
        {params.row.receiverData.email}
      </Typography>
    )
  },

];
  //moment(order.creationDate).format("DD.MM.YYYY").toLocaleString()
const SearchOrders = () => {
  
  const [orders, setOrders] = React.useState<OrderWithDetails[]>([])

  const [form, setForm] = React.useState<FormFields>({});

  const [errors, setErrors] = React.useState<{email: string}>({
    email: ""
  });

  const [pagination, setPagination] = React.useState<Pagination>({
    page: 0,
    size: 5,
  })

  const [pageInfo, setPageInfo] = React.useState<PageInfo>({
    numberOfElements: 0,
    totalPages: 0,
    totalElements: 0,
  })

  const navigate = useNavigate();

  const dispatch = useDispatch();

  const validateForm = () => {
    let success = true;

    let newErrorsState = { ...errors };
    if (form.email && FormValidator.checkIfIsRequired(form.email)) {
      if (!FormValidator.checkEmail(form.email as string)) {
          newErrorsState.email = FormValidator.emailMessage;
          success = false;
      }
    } 

    setErrors(newErrorsState);

    return success;
  };

  const handleSubmit = (actualPage: number) => {
    if (!validateForm()) return;

    let creationDateFrom = null
    let creationDateTo = null

    if(form.creationDateFrom){
      creationDateFrom = new Date(form.creationDateFrom as Date).setUTCHours(0)
      creationDateFrom = new Date(creationDateFrom)
      creationDateFrom = creationDateFrom.setUTCDate(creationDateFrom.getDate() + 1)
      creationDateFrom = new Date(creationDateFrom)
    }

    if(form.creationDateTo){
      creationDateTo = new Date(form.creationDateTo as Date).setUTCHours(23, 59, 59, 999)
      creationDateTo = new Date(creationDateTo)
      creationDateTo = creationDateTo.setUTCDate(creationDateTo.getDate())
      creationDateTo = new Date(creationDateTo)
    }

    const searchCriteria: OrdersSearchCriteria = {
      ...form,
      creationDateFrom: creationDateFrom?.toISOString().replace('Z',''),
      creationDateTo:  creationDateTo?.toISOString().replace('Z','')
    }

    console.log(searchCriteria)

    OrderService.searchOrders(searchCriteria, {...pagination, page: actualPage})
    .then((response) => {
        const page: Page = response.data
        setOrders(page.content)
        setPageInfo({
          numberOfElements: page.numberOfElements,
          totalPages: page.totalPages,
          totalElements: page.totalElements
        })
    })
    .catch((error) => {
        dispatch(setNotificationMessage(error.message.data));
        dispatch(setNotificationType("error"));
        dispatch(setNotificationStatus(true));
    })
}

  return (
    <Grid item container justifyContent="center" alignSelf="start" marginTop={6} marginBottom={6}>
      <Grid item xs={12}>
        <Typography variant="h4" textAlign="center">
          Wyszukiwanie zamówień
        </Typography>
      </Grid>
      <Grid item xs={9} container marginTop={10} justifyContent="space-between">
        <Grid item xs={5} container rowSpacing={2}>
          <Grid item xs={12} marginBottom={2}>
            <FormElement
              fieldName="Imię"
              placeholder="Wpisz imię..."
              value={form.name ? form.name : ""}
              onChange={(event) => setForm({ ...form, name: event.target.value })}
            />
          </Grid>
          <FormElement
            fieldName="Nazwisko"
            placeholder="Wpisz nazwisko..."
            value={form.surname ? form.surname : ""}
            onChange={(event) => setForm({ ...form, surname: event.target.value })}
          />
          <ValidatedForm
            fieldName="E-mail"
            placeholder="Wpisz e-mail..."
            value={form.email ? form.email : ""}
            error={errors.email}
            onChange={(value) => setForm({ ...form, email: value })}
            onErrorChange={(error) => setErrors({ ...errors, email: error })}
          />
          <FormElement
            fieldName="Numer telefonu"
            placeholder="Wpisz numer telefonu..."
            value={form.tel ? form.tel : ""}
            onChange={(event) => setForm({ ...form, tel: event.target.value })}
          />
        </Grid>
        <Grid item xs={5} container>
          <DatePickerFormRange
            fieldName="Data utworzenia"
            maxDate={new Date()}
            valueFrom={form.creationDateFrom}
            valueTo={form.creationDateTo}
            onChangeFrom={(newValue) => setForm({...form, creationDateFrom: newValue != null ? newValue : undefined})}
            onChangeTo={(newValue) => setForm({...form, creationDateTo: newValue != null ? newValue : undefined})}
          />
          <OrderStatusSelect setStatus={(status: OrderStatus) => setForm({...form, statusId: status.id})} canBeEmpty={true}/>
          <Grid item xs={12} container alignItems="center">
            <Grid item xs={6}>
                <Typography
                    textAlign="start" 
                    variant="h6"
                >
                    Łączna kwota
                </Typography>
            </Grid>
            <Grid item xs={6} container justifyContent="space-between">
              <Grid item xs={5.5}>
                  <TextField
                      fullWidth
                      color="secondary"
                      placeholder="Od"
                      value={form.minPrice}
                      InputProps={{ inputProps: { min: 0, max: form.maxPrice } }}
                      onChange={(event: any) => setForm({...form, minPrice: event.target.value})}
                  />
              </Grid>
              <Grid item xs={5.5}>
                <TextField
                    fullWidth
                    color="secondary"
                    placeholder="Do"
                    value={form.maxPrice}
                    InputProps={{ inputProps: { min: form.minPrice, max: 1000 } }}
                    onChange={(event: any) => setForm({...form, maxPrice: event.target.value})}
                />
              </Grid>
            </Grid>
          </Grid>
        </Grid>
      </Grid>
      <Grid
        item
        xs={12}
        container
        marginTop={6}
        justifyContent="center"
      >
        <Grid item xs={1.5}>
          <Button
            fullWidth
            variant="contained"
            color="secondary"
            onClick={() => handleSubmit(pagination.page)}
          >
            Szukaj
          </Button>
        </Grid>
      </Grid>
      <Grid item xs={10} marginTop={4} marginBottom={8}>
        <Box sx={{ height: 400, width: '100%' }} justifyContent="center">
          <DataGrid
            rows={orders}
            rowCount={pageInfo.totalElements}
            pagination
            columns={columns}
            page={pagination.page}
            paginationMode="server"
            pageSize={pagination.size}
            rowsPerPageOptions={[5]}
            onSelectionModelChange={(id) => navigate(`../order/${id}`)}
            onPageChange={(page: number) => {
              handleSubmit(page)
              setPagination({...pagination, page: page})
            }}
          />
        </Box>
      </Grid>
      <BottomNavigation text={"Wróć do strony głównej"} path="../" />
    </Grid>
  );
};

export default SearchOrders;