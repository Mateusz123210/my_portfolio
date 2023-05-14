package pl.edu.pwr.xmlparsers;


import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Marshaller;
import javafx.fxml.FXML;
import javafx.scene.control.TextArea;
import javafx.scene.control.TextField;
import javafx.scene.layout.AnchorPane;
import javafx.scene.web.WebView;
import javafx.stage.FileChooser;
import javafx.stage.Stage;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.Node;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;
import pl.edu.pwr.xmlparsers.jaxb.BipInformations;
import pl.edu.pwr.xmlparsers.jaxb.InformationCard;
import pl.edu.pwr.xmlparsers.jaxb.Items;
import pl.edu.pwr.xmlparsers.jaxp.InformationCard2;
import pl.edu.pwr.xmlparsers.jaxp.MySAXHandler;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import javax.xml.parsers.*;
import javax.xml.transform.*;
import javax.xml.transform.stream.StreamResult;
import javax.xml.transform.stream.StreamSource;
import java.util.Random;

public class HelloController {

    private BipInformations bipInformations;
    @FXML
    private TextField chooseXMLFileTextField;
    @FXML
    private TextArea outputTextArea;
    @FXML
    private AnchorPane ap;
    @FXML
    private TextField chooseXMLFileTextFieldJAXB;
    @FXML
    private TextArea JAXBOutputTextArea;
    @FXML
    private TextField XMLChosenFile;
    @FXML
    private TextField XSLTChosenFile;
    @FXML
    private WebView webView;

    @FXML
    private void chooseFile1(){chooseFile(chooseXMLFileTextField);
    }

    @FXML
    private void chooseFile2(){chooseFile(chooseXMLFileTextFieldJAXB);
    }

    @FXML
    private void chooseFile3(){chooseFile(XMLChosenFile);
    }

    @FXML
    private void chooseFile4(){chooseFile(XSLTChosenFile);
    }

    @FXML
    private void transformUsingXSLT(){
        if(XMLChosenFile.getText().length() == 0 || XSLTChosenFile.getText().length() == 0) return;
        TransformerFactory factory = TransformerFactory.newInstance();
        Source xslt = new StreamSource(new File(XSLTChosenFile.getText()));
        Transformer transformer = null;
        try {
            transformer = factory.newTransformer(xslt);
            Source text = new StreamSource(new File(XMLChosenFile.getText()));
            StringWriter sw = new StringWriter();

            transformer.transform(text, new StreamResult(sw));
            webView.getEngine().loadContent(sw.toString());
        } catch (TransformerException e) {
            throw new RuntimeException(e);
        }
    }

    @FXML
    private void serializeToXML(){
        boolean wasNull = false;
        if(bipInformations == null){
            wasNull = true;
            bipInformations = new BipInformations();
            bipInformations.getData().getInformationCards().setSize(generateRandomString());
            bipInformations.getData().getInformationCards().setStart(generateRandomString());
            bipInformations.getData().getInformationCards().setStop(generateRandomString());
            bipInformations.getData().getInformationCards().setTotalSize(generateRandomString());
            int randomCardsNumber = new Random().nextInt(3, 7);
            for(int i = 0; i < randomCardsNumber; i++){
                bipInformations.getData().getInformationCards().getItems().getInformationCard()
                    .add(new InformationCard());
                bipInformations.getData().getInformationCards().getItems().getInformationCard().get(i)
                    .setId(generateRandomString());
                bipInformations.getData().getInformationCards().getItems().getInformationCard().get(i)
                    .setDate(generateRandomString());
                bipInformations.getData().getInformationCards().getItems().getInformationCard().get(i)
                    .setApplicantData(generateRandomString());
                bipInformations.getData().getInformationCards().getItems().getInformationCard().get(i)
                    .setCardType(generateRandomString());
                bipInformations.getData().getInformationCards().getItems().getInformationCard().get(i)
                    .setEntryNumber(generateRandomString());
                bipInformations.getData().getInformationCards().getItems().getInformationCard().get(i)
                    .setEnvironmentComponent(generateRandomString());
                bipInformations.getData().getInformationCards().getItems().getInformationCard().get(i)
                    .setOrganizationShortcut(generateRandomString());
                bipInformations.getData().getInformationCards().getItems().getInformationCard().get(i)
                    .setThingSign(generateRandomString());
                bipInformations.getData().getInformationCards().getItems().getInformationCard().get(i)
                    .setTypeOfCard(generateRandomString());
            }
        }
        try {
            JAXBContext context = JAXBContext.newInstance(BipInformations.class);
            Marshaller marshaller = context.createMarshaller();
            marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, Boolean.TRUE);
            StringWriter stringWriter = new StringWriter();
            marshaller.marshal(bipInformations, stringWriter);
            if(wasNull)
                JAXBOutputTextArea.setText("Random java class was created and serialized to XML\n------------------\n" +
                    stringWriter.toString());
            else{
                JAXBOutputTextArea.setText("Java class was serialized to XML\n------------------\n" +
                        stringWriter.toString());
            }
        } catch (JAXBException e) {
            e.printStackTrace();
        }
    }

    @FXML
    private void deserializeFromXML(){
        if(chooseXMLFileTextFieldJAXB.getText().length() == 0) {
            JAXBOutputTextArea.setText("Choose file first!");
            return;
        }
        try {
            JAXBContext context = JAXBContext.newInstance(BipInformations.class);
            bipInformations = (BipInformations) context.createUnmarshaller().unmarshal(
                    new FileReader(chooseXMLFileTextFieldJAXB.getText()));
        } catch (JAXBException | FileNotFoundException e) {
            bipInformations = null;
            JAXBOutputTextArea.setText("Deserialization failed");
        }
        if(bipInformations != null){
            Items item  = bipInformations.getData().getInformationCards().getItems();
            int length = item.getInformationCard().size();
            StringBuilder stringBuilder = new StringBuilder();
            for(int i = 0; i < length; i++){
                stringBuilder.append("---------------\nId = ");
                stringBuilder.append(item.getInformationCard().get(i).getId());
                stringBuilder.append("\nData = ");
                stringBuilder.append(item.getInformationCard().get(i).getDate());
                stringBuilder.append("\nSkrót organizacji = ");
                stringBuilder.append(item.getInformationCard().get(i).getOrganizationShortcut());
                stringBuilder.append("\nKomponent środowiska = ");
                stringBuilder.append(item.getInformationCard().get(i).getEnvironmentComponent());
                stringBuilder.append("\nTyp karty = ");
                stringBuilder.append(item.getInformationCard().get(i).getCardType());
                stringBuilder.append("\nRodzaj karty = ");
                stringBuilder.append(item.getInformationCard().get(i).getTypeOfCard());
                stringBuilder.append("\nNumer wpisu = ");
                stringBuilder.append(item.getInformationCard().get(i).getEntryNumber());
                stringBuilder.append("\nZnak sprawy = ");
                stringBuilder.append(item.getInformationCard().get(i).getThingSign());
                stringBuilder.append("\nDane wnioskodawcy = ");
                stringBuilder.append(item.getInformationCard().get(i).getApplicantData());
                stringBuilder.append("\n");
            }
            JAXBOutputTextArea.setText("XML file was deserialized\n" + stringBuilder.toString());
        }
    }

    @FXML
    private void parseUsingSAX(){
        if(chooseXMLFileTextField.getText().length() == 0) return;
        SAXParserFactory saxParserFactory = SAXParserFactory.newInstance();
        try{
            SAXParser parser = saxParserFactory.newSAXParser();
            MySAXHandler myHandler = new MySAXHandler();
            parser.parse(new File(chooseXMLFileTextField.getText()), myHandler);
            List<InformationCard2> informationCards = myHandler.getInformationCards();
            StringBuilder stringBuilder = new StringBuilder();
            informationCards.forEach(c -> {
                stringBuilder.append(c.toString());
            });
            outputTextArea.setText("SAX results\n" + stringBuilder.toString());
        }catch (ParserConfigurationException | SAXException | IOException e) {
            e.printStackTrace();
        }
    }

    @FXML
    private void parseUsingDOM(){
        if(chooseXMLFileTextField.getText().length() == 0) return;
        try {
            DocumentBuilderFactory documentBuilderFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder documentBuilder = documentBuilderFactory.newDocumentBuilder();
            Document doc = documentBuilder.parse(new File(chooseXMLFileTextField.getText()));
            doc.getDocumentElement().normalize();
            NodeList nodes = doc.getElementsByTagName("karta_informacyjna");
            Node innerNode;
            Element element;
            List<InformationCard2> informationCards = new ArrayList<>();
            InformationCard2 informationCard;
            for(int i = 0; i < nodes.getLength(); i++){
                innerNode = nodes.item(i);
                if(innerNode.getNodeType() == Node.ELEMENT_NODE){
                    informationCard = new InformationCard2();
                    element = (Element) innerNode;
                    informationCard.setId(element.getElementsByTagName("id")
                            .item(0).getTextContent());
                    informationCard.setData(element.getElementsByTagName("data")
                            .item(0).getTextContent());
                    informationCard.setOrganizationShortcut(element.getElementsByTagName("skrot_organizacja")
                            .item(0).getTextContent());
                    informationCard.setEnvironmentComponent(element.getElementsByTagName("komponent_srodowiska")
                            .item(0).getTextContent());
                    informationCard.setCardType(element.getElementsByTagName("typ_karty")
                            .item(0).getTextContent());
                    informationCard.setTypeOfCard(element.getElementsByTagName("rodzaj_karty")
                            .item(0).getTextContent());
                    informationCard.setEntryNumber(element.getElementsByTagName("nr_wpisu")
                            .item(0).getTextContent());
                    informationCard.setThingSign(element.getElementsByTagName("znak_sprawy")
                            .item(0).getTextContent());
                    informationCard.setApplicantData(element.getElementsByTagName("dane_wnioskodawcy")
                            .item(0).getTextContent());
                    informationCards.add(informationCard);
                }
            }
            StringBuilder stringBuilder = new StringBuilder();
            informationCards.forEach(c -> {
                stringBuilder.append(c.toString());
            });
            outputTextArea.setText("DOM results\n" + stringBuilder.toString());
        } catch (ParserConfigurationException | IOException | SAXException e) {
            throw new RuntimeException(e);
        }
    }

    private void chooseFile(TextField textField){
        Stage stage = (Stage) ap.getScene().getWindow();
        FileChooser fileChooser = new FileChooser();
        fileChooser.setTitle("Choose xml file");
        fileChooser.setInitialDirectory(new File(System.getProperty("user.dir")));
        File file = fileChooser.showOpenDialog(stage);
        if(file != null){
            textField.setText(String.valueOf(file));
        }
    }

    private String generateRandomString(){
        int leftLimit = 97;
        int rightLimit = 122;
        Random random = new Random();
        int length = random.nextInt(3, 10);
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < length; i++){
            int randomLimitedInt = leftLimit + (int)
                    (random.nextFloat() * (rightLimit - leftLimit + 1));
            sb.append((char) randomLimitedInt);
        }
        return sb.toString();
    }
}