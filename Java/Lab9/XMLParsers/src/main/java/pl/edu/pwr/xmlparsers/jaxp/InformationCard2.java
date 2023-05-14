package pl.edu.pwr.xmlparsers.jaxp;

public class InformationCard2 {

    private String id;
    private String data;
    private String organizationShortcut;
    private String environmentComponent;
    private String cardType;

    private String typeOfCard;
    private String entryNumber;
    private String thingSign;
    private String applicantData;

    public void setId(String id) {
        this.id = id;
    }

    public void setData(String data) {
        this.data = data;
    }

    public void setOrganizationShortcut(String organizationShortcut) {
        this.organizationShortcut = organizationShortcut;
    }

    public void setEnvironmentComponent(String environmentComponent) {
        this.environmentComponent = environmentComponent;
    }

    public void setCardType(String cardType) {
        this.cardType = cardType;
    }

    public void setTypeOfCard(String typeOfCard) {
        this.typeOfCard = typeOfCard;
    }

    public void setEntryNumber(String entryNumber) {
        this.entryNumber = entryNumber;
    }

    public void setThingSign(String thingSign) {
        this.thingSign = thingSign;
    }

    public void setApplicantData(String applicantData) {
        this.applicantData = applicantData;
    }

    @Override
    public String toString(){
        StringBuilder stringBuilder = new StringBuilder();
        stringBuilder.append("---------------\nId = ");
        stringBuilder.append(id);
        stringBuilder.append("\nData = ");
        stringBuilder.append(data);
        stringBuilder.append("\nSkrót organizacji = ");
        stringBuilder.append(organizationShortcut);
        stringBuilder.append("\nKomponent środowiska = ");
        stringBuilder.append(environmentComponent);
        stringBuilder.append("\nTyp karty = ");
        stringBuilder.append(cardType);
        stringBuilder.append("\nRodzaj karty = ");
        stringBuilder.append(typeOfCard);
        stringBuilder.append("\nNumer wpisu = ");
        stringBuilder.append(entryNumber);
        stringBuilder.append("\nZnak sprawy = ");
        stringBuilder.append(thingSign);
        stringBuilder.append("\nDane wnioskodawcy = ");
        stringBuilder.append(applicantData);
        stringBuilder.append("\n");
        return stringBuilder.toString();
    }
}
