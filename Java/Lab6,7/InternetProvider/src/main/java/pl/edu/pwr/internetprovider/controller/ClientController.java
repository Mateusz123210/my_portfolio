package pl.edu.pwr.internetprovider.controller;


import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.tags.Tag;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import pl.edu.pwr.internetprovider.model.Client;
import pl.edu.pwr.internetprovider.service.ClientServiceImpl;

import java.util.List;


@Tag(name= "Client controller", description = "Endpoints connected with clients")
@RestController
public class ClientController {

    private final ClientServiceImpl clientServiceImpl;

    @Autowired
    public ClientController(ClientServiceImpl clientServiceImpl) {
        this.clientServiceImpl = clientServiceImpl;
    }

    @ApiResponse(responseCode = "200", description = "Clients fetched")
    @Operation(summary = "Get all clients", description = "Fetching data of all clients")
    @GetMapping(value = "/client/all")
    public ResponseEntity<List<Client>> getAllClientsData(){

        List<Client> allClientsData = clientServiceImpl.getAll();
        return ResponseEntity.ok(allClientsData);
    }

    @ApiResponse(responseCode = "200", description = "Client fetched")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Get client using id", description = "Fetching data of specified client using id")
    @GetMapping(value = "/client/get/{id}")
    public ResponseEntity getClientData(@PathVariable("id") String clientIdStr){
        Integer clientId;
        try{
            clientId = Integer.parseInt(clientIdStr);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid client id");
        }
        Client client = clientServiceImpl.getById(clientId);
        if(client == null){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Client with this id does not exist");
        }
        return ResponseEntity.ok(client);
    }

    @ApiResponse(responseCode = "200", description = "Client added")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Add client", description = "Adding client with specified name and surname")
    @PostMapping(value = "/client/add")
    public ResponseEntity addClient(@RequestParam String name, @RequestParam String surname){
        if(name.length() == 0 || surname.length() == 0)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        return ResponseEntity.ok(clientServiceImpl.addClient(name, surname));
    }

    @ApiResponse(responseCode = "200", description = "Client updated")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Update client", description = "Changing name and surname of client using id")
    @PutMapping(value = "/client/update")
    public ResponseEntity updateClient(@RequestParam String number, @RequestParam String name,
                                       @RequestParam String surname){
        if(number.length() == 0 || name.length() == 0 || surname.length() == 0)
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid data");
        Integer clientId;
        try{
            clientId = Integer.parseInt(number);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid client id");
        }
        Client client = clientServiceImpl.updateClient(clientId, name, surname);
        if(client == null){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Client with this id does not exist");
        }
        return ResponseEntity.ok(client);
    }

    @ApiResponse(responseCode = "200", description = "Client deleted")
    @ApiResponse(responseCode = "400", description = "Invalid params given")
    @Operation(summary = "Delete client", description = "Deleting client using id")
    @DeleteMapping(value = "/client/delete")
    public ResponseEntity deleteClient(@RequestParam String clientId){
        if(clientId.length() == 0) return ResponseEntity.status(HttpStatus.BAD_REQUEST).
                body("Invalid client id");
        Integer clientIdInt;
        try{
            clientIdInt = Integer.parseInt(clientId);
        }
        catch(NumberFormatException e){
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body("Invalid client id");
        }
        return ResponseEntity.ok(clientServiceImpl.deleteClient(clientIdInt));
    }
}
