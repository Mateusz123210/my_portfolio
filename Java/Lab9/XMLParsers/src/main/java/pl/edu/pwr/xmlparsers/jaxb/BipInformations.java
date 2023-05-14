package pl.edu.pwr.xmlparsers.jaxb;


import jakarta.xml.bind.annotation.*;

@XmlRootElement(name = "bip.poznan.pl")
@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {"data"})
public class BipInformations {

    @XmlElement(name = "data", required = true)
    protected Data data = new Data();

    public Data getData() {
        return data;
    }

    public void setData(Data data) {
        this.data = data;
    }
}
