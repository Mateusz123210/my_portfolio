package pl.edu.pwr.xmlparsers.jaxb;

import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlType;

@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {"id", "date", "organizationShortcut", "environmentComponent", "cardType",
        "typeOfCard", "entryNumber", "thingSign", "applicantData"})
public class InformationCard{

    @XmlElement(name = "id", required = true)
    private String id;
    @XmlElement(name = "data", required = true)
    private String date;
    @XmlElement(name = "skrot_organizacja", required = true)
    private String organizationShortcut;
    @XmlElement(name = "komponent_srodowiska", required = true)
    private String environmentComponent;
    @XmlElement(name = "typ_karty", required = true)
    private String cardType;
    @XmlElement(name = "rodzaj_karty", required = true)
    private String typeOfCard;
    @XmlElement(name = "nr_wpisu", required = true)
    private String entryNumber;
    @XmlElement(name = "znak_sprawy", required = true)
    private String thingSign;
    @XmlElement(name = "dane_wnioskodawcy", required = true)
    private String applicantData;

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public String getOrganizationShortcut() {
        return organizationShortcut;
    }

    public void setOrganizationShortcut(String organizationShortcut) {
        this.organizationShortcut = organizationShortcut;
    }

    public String getEnvironmentComponent() {
        return environmentComponent;
    }

    public void setEnvironmentComponent(String environmentComponent) {
        this.environmentComponent = environmentComponent;
    }

    public String getCardType() {
        return cardType;
    }

    public void setCardType(String cardType) {
        this.cardType = cardType;
    }

    public String getTypeOfCard() {
        return typeOfCard;
    }

    public void setTypeOfCard(String typeOfCard) {
        this.typeOfCard = typeOfCard;
    }

    public String getEntryNumber() {
        return entryNumber;
    }

    public void setEntryNumber(String entryNumber) {
        this.entryNumber = entryNumber;
    }

    public String getThingSign() {
        return thingSign;
    }

    public void setThingSign(String thingSign) {
        this.thingSign = thingSign;
    }

    public String getApplicantData() {
        return applicantData;
    }

    public void setApplicantData(String applicantData) {
        this.applicantData = applicantData;
    }
}
