import { configureStore } from "@reduxjs/toolkit";

const persistedState = localStorage.getItem("reduxState")
  ? JSON.parse(localStorage.getItem("reduxState") as string)
  : {};

// export const store = configureStore({

// });
