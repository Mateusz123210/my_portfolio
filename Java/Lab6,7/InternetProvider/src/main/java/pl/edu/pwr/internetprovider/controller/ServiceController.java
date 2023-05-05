package pl.edu.pwr.internetprovider.controller;


import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import pl.edu.pwr.internetprovider.model.Service;
import pl.edu.pwr.internetprovider.service.ServiceServiceImpl;

import java.util.List;


@Tag(name= "Service controller", description = "Endpoints connected with services")
@RestController
public class ServiceController {

    @Autowired
    private final ServiceServiceImpl serviceServiceImpl;

    public ServiceController(ServiceServiceImpl serviceServiceImpl) {
        this.serviceServiceImpl = serviceServiceImpl;
    }

    @ApiResponse(responseCode = "200", description = "All services fetched")
    @Operation(summary = "Get all services", description = "Get data about all available services")
    @GetMapping(value = "/service/all")
    public ResponseEntity<List<Service>> getAllServices(){
        return ResponseEntity.ok(serviceServiceImpl.getAllServices());
    }

    @ApiResponse(responseCode = "200", description = "Service fetched")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Get service by id", description = "Get service using id")
    @GetMapping(value = "/service/get/{id}")
    public ResponseEntity getClientData(@PathVariable("id") String serviceIdStr){
        Integer serviceId;
        try{
            serviceId = Integer.parseInt(serviceIdStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid service id");
        }
        Service service = serviceServiceImpl.getById(serviceId);
        if(service == null){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Service with this id does not exist");
        }
        return ResponseEntity.ok(service);
    }

    @ApiResponse(responseCode = "200", description = "Service added")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Add service", description = "Adding service using type and price")
    @PostMapping(value = "/service/add")
    public ResponseEntity addService(@RequestParam String type, @RequestParam String price){
        if(type.length() == 0 || price.length() == 0){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid service data");
        }
        Float priceFloat;
        try{
            priceFloat = Float.parseFloat(price);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid price");
        }
        List<Service> allServices = serviceServiceImpl.addService(type, priceFloat);
        return ResponseEntity.ok(allServices);
    }

    @ApiResponse(responseCode = "200", description = "Service updated")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Update service", description = "Changing data of service using service id and new params")
    @PutMapping(value = "/service/update")
    public ResponseEntity updateService(@RequestParam String id, @RequestParam String type,
                                        @RequestParam String price){
        if(id.length() == 0 || type.length() == 0 || price.length() == 0)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        Integer serviceId;
        try{
            serviceId = Integer.parseInt(id);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid service id");
        }
        Float priceFloat;
        try{
            priceFloat = Float.parseFloat(price);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid price");
        }
        Service service = serviceServiceImpl.updateService(serviceId, type, priceFloat);
        if(service == null){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Service with this id does not exist");
        }
        return ResponseEntity.ok(service);
    }

    @ApiResponse(responseCode = "200", description = "Service deleted")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Delete service", description = "Deleting service using id")
    @DeleteMapping(value = "/service/delete")
    public ResponseEntity deleteService(@RequestParam String id){
        if(id.length() == 0)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        Integer serviceId;
        try{
            serviceId = Integer.parseInt(id);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid service id");
        }
        return ResponseEntity.ok(serviceServiceImpl.deleteService(serviceId));
    }
}
