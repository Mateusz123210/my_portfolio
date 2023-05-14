module pl.edu.pwr.xmlparsers {
    requires javafx.controls;
    requires javafx.fxml;
    requires javafx.web;
    requires  jakarta.xml.bind;
    requires com.sun.xml.bind;
    opens pl.edu.pwr.xmlparsers to javafx.fxml, jakarta.xml.bind;
    opens pl.edu.pwr.xmlparsers.jaxb to jakarta.xml.bind;
    exports pl.edu.pwr.xmlparsers;
    exports pl.edu.pwr.xmlparsers.jaxp;
    opens pl.edu.pwr.xmlparsers.jaxp to javafx.fxml;
    exports pl.edu.pwr.xmlparsers.jaxb;
}