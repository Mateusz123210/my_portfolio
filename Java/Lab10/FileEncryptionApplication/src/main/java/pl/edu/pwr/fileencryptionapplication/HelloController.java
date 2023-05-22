package pl.edu.pwr.fileencryptionapplication;

import javafx.fxml.FXML;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import pl.edu.pwr.Encryption;

import java.io.File;

public class HelloController{

    @FXML
    private AnchorPane ap;
    @FXML
    private TextField inputFileTextField;
    @FXML
    private TextField outputFileTextField;
    @FXML
    private TextField publicKeyTextField, privateKeyTextField;
    @FXML
    private TextField decryptionTextField;
    @FXML
    private Label messageLabel;
    private Encryption encryption;

    public HelloController(){
        encryption = new Encryption();
    }

    @FXML
    private void chooseInputFile(){
        chooseFile(inputFileTextField, false);
    }

    @FXML
    private void chooseOutputFile(){
        chooseFile(outputFileTextField, true);
    }

    @FXML
    private void choosePrivateKeyFile(){
        chooseFile(privateKeyTextField, false);
    }

    @FXML
    private void choosePublicKeyFile(){
        chooseFile(publicKeyTextField, false);
    }

    @FXML
    private void chooseDecryptionOutputFile(){
        chooseFile(decryptionTextField, true);
    }

    @FXML
    private void encrypt(){
        String input = inputFileTextField.getText();
        String output = outputFileTextField.getText();
        String privateKey = privateKeyTextField.getText();
        if(input.length() == 0 || output.length() == 0 || privateKey.length() == 0){
            messageLabel.setText("Choose input file, output file and private key!");
            return;
        }
        messageLabel.setText(encryption.encrypt(input, output, privateKey));
    }

    @FXML
    private void decrypt(){
        String input = outputFileTextField.getText();
        String output = decryptionTextField.getText();
        String publicKey = publicKeyTextField.getText();
        if(input.length() == 0 || output.length() == 0 || publicKey.length() == 0){
            messageLabel.setText("Choose input file, output file and public key!");
            return;
        }
        messageLabel.setText(encryption.decrypt(input, output, publicKey));
    }

    private void chooseFile(TextField textField, boolean save){
        messageLabel.setText("");
        Stage stage = (Stage) ap.getScene().getWindow();
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Choose file");
        fileChooser.setInitialDirectory(new File(System.getProperty("user.dir")));
        File file = null;
        if(save) file = fileChooser.showSaveDialog(stage);
        else file = fileChooser.showOpenDialog(stage);
        if(file != null){
            textField.setText(String.valueOf(file));
        }else textField.setText("");
    }
}