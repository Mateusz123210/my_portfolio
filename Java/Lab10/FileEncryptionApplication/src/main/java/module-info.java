module pl.edu.pwr.fileencryptionapplication {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;
    requires com.almasb.fxgl.all;
    requires FileEncryptionLibrary;

    opens pl.edu.pwr.fileencryptionapplication to javafx.fxml;
    exports pl.edu.pwr.fileencryptionapplication;
}