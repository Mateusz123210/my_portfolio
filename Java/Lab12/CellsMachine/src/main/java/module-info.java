module pl.edu.pwr.cellsmachine {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;
    requires com.almasb.fxgl.all;
    requires org.openjdk.nashorn;

    opens pl.edu.pwr.cellsmachine to javafx.fxml;
    exports pl.edu.pwr.cellsmachine;
}