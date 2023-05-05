import { AppBar, Button, createTheme, ThemeProvider } from "@mui/material";
import React from "react";
import { Route, BrowserRouter, Routes, Outlet } from "react-router-dom";
import Header from "./components/layout/header/Header";
import Content from "./components/layout/content/Content";
import Shop from "./pages/shop/Shop";
import Login from "./pages/header/Login";
import Register from "./pages/header/Register";
import Notification from "./components/common/Notification";
import NotFound from "./pages/errors/NotFound";
import './index.css';
import BookDetails from "./pages/book-details/BookDetails";
import Basket from "./pages/basket/Basket";
import MyOrders from "./pages/header/my-orders/MyOrders";
import OrderView from "./pages/placeOrder/OrderView";
import SearchOrders from "./pages/header/all-orders/AllOrders";
import OrderData from "./pages/header/all-orders/OrderData";
import moment from 'moment'
import 'moment/locale/pl'
import { plPL as plPLLocale } from '@mui/material/locale';
import { plPL as plPLGrid} from '@mui/x-data-grid';
import { plPL as plPLDatePickers } from '@mui/x-date-pickers';
import ProtectedRoute from "./components/common/ProtectedRoute";

moment.locale("pl")

const theme = createTheme(
  {
    typography: {
      fontFamily: "Source Sans Pro, sans-serif",
      fontSize: 13,
      fontWeightLight: 300,
      fontWeightRegular: 400,
      fontWeightMedium: 500,
      button: {
        textTransform: "none",
      },
    },
    palette: {
      primary: {
        main: "#ca2f2f",
        contrastText: "#000",
      },
      secondary: {
        main: "#D9D9D9",
        contrastText: "#000",
      },
      info: {
        main: "#008080",
        contrastText: "#fff",
      },
      background: {
        paper: '#E8EEF6'
      }
    },
  },
  plPLLocale,
  plPLGrid,
  plPLDatePickers
);

function App() {
  return (
    <React.StrictMode>
      <BrowserRouter>
        <ThemeProvider theme={theme}>
          <Header />
          <Content>
            <Routes>
              <Route path="/" element={<Shop />} />
              <Route path="/login" element={<Login />} />
              <Route path="/register" element={<Register />} />
              <Route path="/book-details/:bookId" element={<BookDetails />} />
              <Route path="/basket" element={
                <ProtectedRoute isNotLogged={true} isClient={true} isEmployee={false}>
                  <Basket/>
                </ProtectedRoute>
              } />
              <Route path="/order" element={
                <ProtectedRoute isNotLogged={false} isClient={true} isEmployee={false}>
                  <OrderView />
                </ProtectedRoute>
              } />
              <Route path="/my-orders" element={
                <ProtectedRoute isNotLogged={false} isClient={true} isEmployee={false}>
                  <MyOrders />
                </ProtectedRoute>
              } />
              <Route path="/all-orders" element={
                <ProtectedRoute isNotLogged={false} isClient={false} isEmployee={true}>
                  <SearchOrders />
                </ProtectedRoute>
              } />
              <Route path="/order/:orderId" element={
                <ProtectedRoute isNotLogged={false} isClient={false} isEmployee={true}>
                  <OrderData />
                </ProtectedRoute>
              } />
              <Route path="*" element={<NotFound /> } />
            </Routes>
          </Content>
        </ThemeProvider>
      </BrowserRouter>
      <Notification />
    </React.StrictMode>
  );
}

export default App;
