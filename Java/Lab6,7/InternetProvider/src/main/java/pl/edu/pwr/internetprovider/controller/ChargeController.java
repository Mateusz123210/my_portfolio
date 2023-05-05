package pl.edu.pwr.internetprovider.controller;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;
import pl.edu.pwr.internetprovider.model.Charge;
import pl.edu.pwr.internetprovider.service.ChargeServiceImpl;

import java.util.List;


@Tag(name= "Charge controller", description = "Endpoints connected with charges")
@RestController
public class ChargeController {
    private final ChargeServiceImpl chargeServiceImpl;

    @Autowired
    public ChargeController(ChargeServiceImpl chargeServiceImpl) {
        this.chargeServiceImpl = chargeServiceImpl;
    }

    @ApiResponse(responseCode = "200", description = "Installation charges fetched")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Get installation charges", description = "Fetching data of all charges of installation using id")
    @GetMapping(value = "/charge/get/{installation-id}")
    public ResponseEntity getInstallationCharges(@PathVariable("installation-id") String installationIdStr){
        Integer installationId;
        try{
            installationId = Integer.parseInt(installationIdStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid installation id");
        }
        List<Charge> charges = chargeServiceImpl.getInstallationCharges(installationId);
        if(charges == null)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        return ResponseEntity.ok(charges);
    }
}
