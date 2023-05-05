package pl.edu.pwr.internetprovider.controller;

import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import pl.edu.pwr.internetprovider.model.Installation;
import pl.edu.pwr.internetprovider.service.InstallationServiceImpl;

import java.util.List;


@Tag(name= "Installation controller", description = "Endpoints connected with installations")
@RestController
public class InstallationController {
    private final InstallationServiceImpl installationServiceImpl;

    @Autowired
    public InstallationController(InstallationServiceImpl installationServiceImpl){
        this.installationServiceImpl = installationServiceImpl;
    }

    @ApiResponse(responseCode = "200", description = "Client installations fetched")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Get client installations", description = "Fetching all client installations using client id")
    @GetMapping(value = "/installation/get/{id}")
    public ResponseEntity getInstallationData(@PathVariable("id") String clientIdStr){
        Integer clientId;
        try{
            clientId = Integer.parseInt(clientIdStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid client id");
        }
        List<Installation> installations = installationServiceImpl.getClientInstallations(clientId);
        if(installations == null){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        }
        return ResponseEntity.ok(installations);
    }

    @ApiResponse(responseCode = "200", description = "Installation added")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Add installation", description = "Adding installation to specified client using client id and installation params")
    @PostMapping(value = "/installation/add")
    public ResponseEntity addInstallation(@RequestParam("address") String address,
                                          @RequestParam("routerNumber") String routerNumberStr,
                                          @RequestParam("serviceId") String serviceIdStr,
                                          @RequestParam("clientId") String clientIdStr){

        if(address.length() == 0 || routerNumberStr.length() == 0 || serviceIdStr.length() == 0 ||
                clientIdStr.length() == 0)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        Integer clientId;
        try{
            clientId = Integer.parseInt(clientIdStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid client id");
        }
        Integer serviceId;
        try{
            serviceId = Integer.parseInt(serviceIdStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid service id");
        }
        Integer routerNumber;
        try{
            routerNumber = Integer.parseInt(routerNumberStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid router number");
        }
        List<Installation> installations = installationServiceImpl.addClientInstallations(address,
                routerNumber, serviceId, clientId);
        if(installations == null){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        }
        return ResponseEntity.ok(installations);
    }

    @ApiResponse(responseCode = "200", description = "Installation updated")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Update client installation", description = "Changing client installation using new params")
    @PutMapping(value = "/installation/update")
    public ResponseEntity updateInstallation(@RequestParam("id") String idStr,
                                             @RequestParam("address") String address,
                                             @RequestParam("routerNumber") String routerNumberStr,
                                             @RequestParam("serviceId") String serviceIdStr,
                                             @RequestParam("clientId") String clientIdStr){

        if(idStr .length() == 0 || address.length() == 0 || routerNumberStr.length() == 0 ||
                serviceIdStr.length() == 0 || clientIdStr.length() == 0)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        Integer id;
        try{
            id = Integer.parseInt(idStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid installation id");
        }
        Integer clientId;
        try{
            clientId = Integer.parseInt(clientIdStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid client id");
        }
        Integer serviceId;
        try{
            serviceId = Integer.parseInt(serviceIdStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid service id");
        }
        Integer routerNumber;
        try{
            routerNumber = Integer.parseInt(routerNumberStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid router number");
        }
        Installation installation = installationServiceImpl.updateInstallation(id, address, routerNumber,
                serviceId, clientId);
        if(installation == null){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        }
        return ResponseEntity.ok(installation);
    }

    @ApiResponse(responseCode = "200", description = "Installation deleted")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Delete installation", description = "Delete installation using id")
    @DeleteMapping(value = "/installation/delete")
    public ResponseEntity deleteInstallation(@RequestParam("id") String idStr){
        if(idStr.length() == 0)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid installation id");
        Integer id;
        try{
            id = Integer.parseInt(idStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid installation id");
        }
        List<Installation> installations = installationServiceImpl.deleteInstallation(id);
        if(installations == null){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        }
        return ResponseEntity.ok(installations);
    }
}
