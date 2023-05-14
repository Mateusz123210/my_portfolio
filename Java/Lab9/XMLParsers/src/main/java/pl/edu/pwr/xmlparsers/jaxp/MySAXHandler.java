package pl.edu.pwr.xmlparsers.jaxp;

import org.xml.sax.Attributes;
import org.xml.sax.SAXException;
import org.xml.sax.helpers.DefaultHandler;

import java.util.ArrayList;
import java.util.List;

public class MySAXHandler extends DefaultHandler {

    private List<InformationCard2> informationCards = new ArrayList<>();
    private InformationCard2 informationCard = null;
    private boolean bId;
    private boolean bData;
    private boolean bOrganizationShortcut;
    private boolean bEnvironmentComponent;
    private boolean bCardType;
    private boolean bTypeOfCard;
    private boolean bEntryNumber;
    private boolean bThingSign;
    private boolean bApplicantData;

    public List<InformationCard2> getInformationCards() {
        return informationCards;
    }

    @Override
    public void startElement(String uri, String localName, String qName, Attributes attributes)
        throws SAXException {
        if(qName.equalsIgnoreCase("karta_informacyjna")){
            informationCard = new InformationCard2();
        }
        else if(qName.equalsIgnoreCase("id")){
            bId = true;
        }else if(qName.equalsIgnoreCase("data")){
            bData = true;
        }else if(qName.equalsIgnoreCase("skrot_organizacja")){
            bOrganizationShortcut = true;
        }else if(qName.equalsIgnoreCase("komponent_srodowiska")){
            bEnvironmentComponent = true;
        }else if(qName.equalsIgnoreCase("typ_karty")){
            bCardType = true;
        }else if(qName.equalsIgnoreCase("rodzaj_karty")){
            bTypeOfCard = true;
        }else if(qName.equalsIgnoreCase("nr_wpisu")){
            bEntryNumber = true;
        }else if(qName.equalsIgnoreCase("znak_sprawy")){
            bThingSign = true;
        }
        else if(qName.equalsIgnoreCase("dane_wnioskodawcy")){
            bApplicantData = true;
        }
    }

    @Override
    public void endElement(String uri, String localName, String qName) throws SAXException{
        if(qName.equalsIgnoreCase("karta_informacyjna")){
            informationCards.add(informationCard);
        }
    }

    @Override
    public void characters(char[] ch, int start, int length) throws SAXException{
        if(bId){
            informationCard.setId(new String(ch, start, length));
            bId = false;
        }
        else if(bData && informationCard != null){
            informationCard.setData(new String(ch, start, length));
            bData = false;
        }
        else if(bOrganizationShortcut){
            informationCard.setOrganizationShortcut(new String(ch, start, length));
            bOrganizationShortcut = false;
        }
        else if(bEnvironmentComponent){
            informationCard.setEnvironmentComponent(new String(ch, start, length));
            bEnvironmentComponent = false;
        }
        else if(bCardType){
            informationCard.setCardType(new String(ch, start, length));
            bCardType = false;
        }
        else if(bTypeOfCard){
            informationCard.setTypeOfCard(new String(ch, start, length));
            bTypeOfCard = false;
        }
        else if(bEntryNumber){
            informationCard.setEntryNumber(new String(ch, start, length));
            bEntryNumber = false;
        }
        else if(bThingSign){
            informationCard.setThingSign(new String(ch, start, length));
            bThingSign = false;
        }
        else if(bApplicantData){
            informationCard.setApplicantData(new String(ch, start, length));
            bApplicantData = false;
        }
    }
}
