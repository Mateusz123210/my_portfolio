import { LocalizationProvider } from '@mui/x-date-pickers';
import { Grid, TextField, Typography } from "@mui/material";
import React from "react";
import { AdapterMoment } from '@mui/x-date-pickers/AdapterMoment';
import { DatePicker } from '@mui/x-date-pickers/DatePicker';
import FormElement from "./FormElement";

export interface DatePickerRangeFormProps {
    fieldName: string,
    valueFrom?: Date,
    valueTo?: Date,
    minDate?: Date,
    maxDate?: Date,
    error?: boolean,
    onChangeFrom: (newDate: Date | null) => void
    onChangeTo: (newDate: Date | null) => void
}

const DatePickerFormRange = (props: DatePickerRangeFormProps) => {
    
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
            <Grid item xs={6} container justifyContent="space-between">
                <LocalizationProvider dateAdapter={AdapterMoment}>
                    <Grid item xs={5.5}>
                        <DatePicker
                            label="Od"
                            value={props.valueFrom === undefined ? null : props.valueFrom}
                            minDate={props.minDate}
                            maxDate={props.maxDate}
                            onChange={(newValue: Date | null) => props.onChangeFrom(newValue)}
                            renderInput={(params: any) => (
                                <TextField 
                                    {...params}
                                    error={props.error == true}
                                    color="secondary"
                                />
                            )}
                        />
                    </Grid>
                    <Grid item xs={5.5}>
                        <DatePicker
                            label="Do"
                            value={props.valueTo === undefined ? null : props.valueTo}
                            minDate={props.minDate}
                            maxDate={props.maxDate}
                            onChange={(newValue: Date | null) => props.onChangeTo(newValue)}
                            renderInput={(params: any) => (
                                <TextField 
                                    {...params}
                                    error={props.error == true}
                                    color="secondary"
                                />
                            )}
                        />
                    </Grid>
                </LocalizationProvider>
            </Grid>
        </Grid>
    );
}

export default DatePickerFormRange;