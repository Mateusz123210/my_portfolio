package pl.edu.pwr.internetprovider.controller;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import pl.edu.pwr.internetprovider.model.Payment;
import pl.edu.pwr.internetprovider.service.PaymentServiceImpl;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;
import java.util.List;


@Tag(name= "Payment controller", description = "Endpoints connected with payments")
@RestController
public class PaymentController {

    private final PaymentServiceImpl paymentServiceImpl;

    @Autowired
    public PaymentController(PaymentServiceImpl paymentServiceImpl) {
        this.paymentServiceImpl = paymentServiceImpl;
    }

    @ApiResponse(responseCode = "200", description = "Installation payments fetched")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Get installation payments", description = "Fetching all installation payments using installation id")
    @GetMapping(value = "/payment/get/{installation-id}")
    public ResponseEntity getInstallationPayments(@PathVariable("installation-id") String installationIdStr){
        Integer installation;
        try{
            installation = Integer.parseInt(installationIdStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid installation id");
        }
        List<Payment> payments = paymentServiceImpl.getInstallationPayments(installation);
        if(payments == null)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        return ResponseEntity.ok(payments);
    }

    @ApiResponse(responseCode = "200", description = "Payment added")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Add payment", description = "Adding payment to specified installation using installation id and payment params")
    @PostMapping(value = "/payment/add")
    public ResponseEntity addInstallationPayment(@RequestParam String date, @RequestParam String price,
                                                 @RequestParam String installationId){
        if(date.length() == 0 || price.length() == 0 || installationId.length() == 0)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        LocalDate localDate;
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("d/MM/yyyy");
        try{
            localDate = LocalDate.parse(date, formatter);
        }catch(DateTimeParseException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid date");
        }
        Float priceFloat;
        try{
            priceFloat = Float.parseFloat(price);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid price");
        }
        Integer installationInt;
        try{
            installationInt = Integer.parseInt(installationId);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid installation id");
        }
        if(priceFloat < 0.0f)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Price cannot be less than 0");
        List<Payment> payments = paymentServiceImpl.addInstallationPayment(localDate, priceFloat,
                installationInt);
        if(payments == null)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        return ResponseEntity.ok(payments);
    }

    @ApiResponse(responseCode = "200", description = "Payment updated")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Update payment", description = "Changing installation payment using installation id, payment id and new params")
    @PutMapping(value = "/payment/update")
    public ResponseEntity updateInstallationPayment(@RequestParam String paymentId, @RequestParam String date,
                                                    @RequestParam String price,
                                                    @RequestParam String installationId){

        if(paymentId.length() == 0 || date.length() == 0 || price.length() == 0 ||
                installationId.length() == 0)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        Integer paymentInt;
        try{
            paymentInt = Integer.parseInt(paymentId);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid installation id");
        }
        LocalDate localDate;
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("d/MM/yyyy");
        try{
            localDate = LocalDate.parse(date, formatter);
        }catch(DateTimeParseException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid date");
        }
        Float priceFloat;
        try{
            priceFloat = Float.parseFloat(price);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid price");
        }
        if(priceFloat < 0.0f)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Price cannot be less than 0");
        Integer installationInt;
        try{
            installationInt = Integer.parseInt(installationId);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid installation id");
        }
        List<Payment> payments = paymentServiceImpl.updatePayment(paymentInt, localDate, priceFloat,
                installationInt);
        if(payments == null)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        return ResponseEntity.ok(payments);
    }

    @ApiResponse(responseCode = "200", description = "Payment deleted")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Delete payment", description = "Deleting payment using id")
    @DeleteMapping(value = "/payment/delete")
    public ResponseEntity deleteInstallationPayment(@RequestParam String paymentId){
        Integer paymentInt;
        try{
            paymentInt = Integer.parseInt(paymentId);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid installation id");
        }
        List<Payment> payments = paymentServiceImpl.deletePayment(paymentInt);
        if(payments == null)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        return ResponseEntity.ok(payments);
    }
}
