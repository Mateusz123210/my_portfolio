package pl.edu.pwr.xmlparsers.jaxb;

import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlType;

import java.util.ArrayList;
import java.util.List;

@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {"informationCard"})
public class Items{

    @XmlElement(name = "karta_informacyjna", required = true)
    protected List<InformationCard> informationCard = new ArrayList<>();

    public List<InformationCard> getInformationCard() {
        if(informationCard == null) informationCard = new ArrayList<>();
        return informationCard;
    }

    public void setInformationCard(List<InformationCard> informationCard) {
        this.informationCard = informationCard;
    }
}
