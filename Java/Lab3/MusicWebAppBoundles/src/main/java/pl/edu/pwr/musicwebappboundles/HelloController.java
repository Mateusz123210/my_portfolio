package pl.edu.pwr.musicwebappboundles;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.*;
import pl.edu.pwr.api.Api;
import pl.edu.pwr.format.ChoiceFormatter;
import pl.edu.pwr.format.UserPreferences;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.ResourceBundle;

public class HelloController implements Initializable {
    private Api api;
    private String language;
    private String country;
    private Locale locale;
    private ChoiceFormatter choiceFormatter;
    private ResourceBundle rb1, rb2;
    private UserPreferences preferences;
    @FXML
    private ComboBox authorComboBox;
    @FXML
    private Label chooseAuthorLabel;
    @FXML
    private Label recordQuestionLabel;
    @FXML
    private TextField recordAnswer;
    @FXML
    private Button recordSubmitButton;
    @FXML
    private Label recordValidAnswer;
    @FXML
    private Label languageLabel;
    @FXML
    private Slider languageSlider;
    @FXML
    private Label secondQuestionLabel;
    @FXML
    private TextField secondQuestionTextField;
    @FXML
    private Button secondQuestionButton;
    @FXML
    private Label secondQuestionAnswerLabel;

    public HelloController(){
        preferences = new UserPreferences();
        api = new Api();
        choiceFormatter = new ChoiceFormatter();
        language = "en";
        country = "EN";
        getPreferences();
    }

     @FXML
    private void setLanguage(){
        double languageSliderValue = languageSlider.getValue();
        int languageSliderIntValue = (int) (languageSliderValue + 0.5);
        if(languageSliderIntValue == 0){
            preferences.setPreferences("pl,PL");
        }
        else {
            preferences.setPreferences("en,EN");
        }
        getPreferences();
        recordValidAnswer.setText("");
        secondQuestionAnswerLabel.setText("");
        setInitialData();
    }

    @FXML
    private void submitAnswer(){
        if(recordAnswer.getText() != null && recordAnswer.getText().length() > 0){
            Object object = authorComboBox.getValue();
            if(object != null) {
                String validAnswer = api.getNumberOfAuthorRecordings(object.toString());
                if(recordAnswer.getText().equals(validAnswer)){
                    StringBuilder res = new StringBuilder(rb1.getString("validAnswerFirstPart"));
                    if(locale.getCountry().equals("PL")){
                        res.append(choiceFormatter.getRecordingValidFormInPolish(validAnswer, rb1));
                    }else {
                        res.append(choiceFormatter.getRecordingValidForm(validAnswer, rb1));
                    }
                    res.append(".");

                    recordValidAnswer.setText(res.toString());

                }else{
                    StringBuilder res = new StringBuilder(rb1.getString("invalidAnswerFirstPart"));
                    if(locale.getCountry().equals("PL")){
                        res.append(choiceFormatter.getRecordingValidFormInPolish(validAnswer, rb1));
                    }else {
                        res.append(choiceFormatter.getRecordingValidForm(validAnswer, rb1));
                    }
                    res.append(".");
                    recordValidAnswer.setText(res.toString());
                }
            }else{
                recordValidAnswer.setText(rb2.getString("connectionError"));
            }
        }else{
            recordValidAnswer.setText(rb1.getString("noAnswer"));
        }
    }

    @FXML
    private void submitAnswer2(){
        if(secondQuestionTextField.getText() != null && secondQuestionTextField.getText().length() > 0){
            Object object = authorComboBox.getValue();
            if(object != null) {
                String validAnswer = api.getNumberOfEventsArtistTookPartIn(object.toString());
                if(secondQuestionTextField.getText().equals(validAnswer)){
                    StringBuilder res = new StringBuilder(rb1.getString("validAnswer2FirstPart"));
                    if(locale.getCountry().equals("PL")){
                        res.append(choiceFormatter.getEventValidForm(validAnswer, rb1));
                    }else {
                        res.append(choiceFormatter.getEventValidForm(validAnswer, rb1));
                    }
                    res.append(".");

                    secondQuestionAnswerLabel.setText(res.toString());

                }else{
                    StringBuilder res = new StringBuilder(rb1.getString("invalidAnswer2FirstPart"));
                    if(locale.getCountry().equals("PL")){
                        res.append(choiceFormatter.getEventValidForm(validAnswer, rb1));
                    }else {
                        res.append(choiceFormatter.getEventValidForm(validAnswer, rb1));
                    }
                    res.append(".");
                    secondQuestionAnswerLabel.setText(res.toString());
                }
            }else{
                secondQuestionAnswerLabel.setText(rb2.getString("connectionError"));
            }
        }else{
            secondQuestionAnswerLabel.setText(rb1.getString("noAnswer"));
        }
    }

    private void getPreferences(){
        List<String> languageCountry = new ArrayList<>();
        try {
            languageCountry = List.of(preferences.getPreferences("en,EN").split(","));
        }catch(Exception e){e.printStackTrace();}
        if(languageCountry.size() == 2){
            language = languageCountry.get(0);
            country = languageCountry.get(1);
        }
        locale = new Locale(language, country);
        rb1 = ResourceBundle.getBundle("Bundles", locale);
        rb2 = ResourceBundle.getBundle("pl.edu.pwr.bundles.Bundles", locale);
    }

    private void setInitialData(){
        chooseAuthorLabel.setText(rb1.getString("chooseAuthorLabel"));
        recordSubmitButton.setText(rb2.getString("answerButton"));
        recordQuestionLabel.setText(rb1.getString("recordingsQuestionLabel"));
        secondQuestionLabel.setText(rb1.getString("eventsQuestionLabel"));
        secondQuestionButton.setText(rb2.getString("answerButton"));
        languageLabel.setText(rb2.getString("polish") + " / " + rb1.getString("english"));
    }

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        setInitialData();
        if(language.equals("pl")) languageSlider.setValue(0.0);
        else languageSlider.setValue(1.0);
        ObservableList<String> list = FXCollections.observableArrayList(api.getAllPolishAuthors());
        authorComboBox.setItems(list);
    }
}