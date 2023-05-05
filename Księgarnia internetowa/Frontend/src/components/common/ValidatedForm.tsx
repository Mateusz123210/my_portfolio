import { Grid, Typography, OutlinedInput, FormControl, FormHelperText, TextField } from "@mui/material";
import { HTMLInputTypeAttribute } from "react";

interface FormElementProps {
    fieldName: string,
    placeholder?: string,
    type?: HTMLInputTypeAttribute,
    error: string,
    value: string,
    onChange: (event: any) => void,
    onErrorChange: (error: string) => void
}

const ValidatedForm = (props: FormElementProps) => {

    const onFieldChange = (event: any) => {
        props.onChange(event.target.value)
        props.onErrorChange('')
    }

    return (
        <Grid item xs={12} container justifyContent="center" alignItems="center">
            <Grid item xs={6}>
                <Typography 
                    textAlign="start" 
                    variant="h6"
                >
                    {props.fieldName}
                </Typography>
            </Grid>
            <Grid item xs={6} container justifyContent="stretch">
                <FormControl fullWidth>
                    <TextField
                        placeholder={props.placeholder}
                        color="secondary"
                        type={props.type}
                        value={props.value}
                        error={props.error !== ''}
                        onChange={(event: any) => onFieldChange(event)} 
                        InputLabelProps={{
                            style: { color: props.error !== '' ? 'red' : '#5CA8EE' },
                        }}
                        sx={{marginTop: 2}}
                    />
                    <FormHelperText error>{props.error + ' '}</FormHelperText>
                </FormControl>
            </Grid>
        </Grid>
    )
}

export default ValidatedForm;