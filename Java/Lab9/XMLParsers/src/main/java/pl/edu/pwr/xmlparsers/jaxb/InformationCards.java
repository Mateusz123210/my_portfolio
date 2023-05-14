package pl.edu.pwr.xmlparsers.jaxb;

import jakarta.xml.bind.annotation.XmlAccessType;
import jakarta.xml.bind.annotation.XmlAccessorType;
import jakarta.xml.bind.annotation.XmlElement;
import jakarta.xml.bind.annotation.XmlType;

@XmlAccessorType(XmlAccessType.FIELD)
@XmlType(name = "", propOrder = {"start", "stop", "size", "totalSize", "items"})
public class InformationCards{

    @XmlElement(name = "start", required = true)
    private String start;
    @XmlElement(name = "stop", required = true)
    private String stop;
    @XmlElement(name = "size", required = true)
    private String size;
    @XmlElement(name = "total_size", required = true)
    private String totalSize;
    @XmlElement(name = "items", required = true)
    protected Items items = new Items();

    public String getStart() {
        return start;
    }

    public void setStart(String start) {
        this.start = start;
    }

    public String getStop() {
        return stop;
    }

    public void setStop(String stop) {
        this.stop = stop;
    }

    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }

    public String getTotalSize() {
        return totalSize;
    }

    public void setTotalSize(String totalSize) {
        this.totalSize = totalSize;
    }

    public Items getItems() {
        return items;
    }

    public void setItems(Items items) {
        this.items = items;
    }
}
