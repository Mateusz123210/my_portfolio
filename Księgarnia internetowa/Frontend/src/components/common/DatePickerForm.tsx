import { LocalizationProvider } from '@mui/x-date-pickers';
import { Grid, TextField, Typography } from "@mui/material";
import React from "react";
import { AdapterMoment } from '@mui/x-date-pickers/AdapterMoment';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import FormElement from "./FormElement";

export interface DatePickerFormProps {
    fieldName: string,
    placeholder?: string,
    value?: Date,
    minDate?: Date,
    maxDate?: Date,
    error?: boolean,
    onChange: (newDate: Date | null) => void
}

const DatePickerForm = (props: DatePickerFormProps) => {
    
    return (
        <Grid item xs={12} container alignItems="center">
            <Grid item xs={6}>
                <Typography 
                    textAlign="start" 
                    variant="h6"
                >
                    {props.fieldName}
                </Typography>
            </Grid>
            <Grid item xs={6}>
                <LocalizationProvider dateAdapter={AdapterMoment}>
                    <DatePicker
                        label={props.placeholder}
                        value={props.value === undefined ? null : props.value}
                        minDate={props.minDate}
                        maxDate={props.maxDate}
                        onChange={(newValue: Date | null) => props.onChange(newValue)}
                        renderInput={(params: any) => (
                            <TextField 
                                {...params}
                                error={props.error == true}
                                color="secondary"
                            />
                        )}
                    />
                </LocalizationProvider>
            </Grid>
        </Grid>
    );
}

export default DatePickerForm;