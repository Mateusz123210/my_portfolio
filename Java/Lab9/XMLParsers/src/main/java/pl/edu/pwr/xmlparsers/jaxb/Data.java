package pl.edu.pwr.xmlparsers.jaxb;

import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlType;

@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {"informationCards"})
public class Data{

    @XmlElement(name = "karty_informacyjne", required = true)
    protected InformationCards informationCards = new InformationCards();

    public InformationCards getInformationCards() {
        return informationCards;
    }

    public void setInformationCards(InformationCards informationCards) {
        this.informationCards = informationCards;
    }
}
