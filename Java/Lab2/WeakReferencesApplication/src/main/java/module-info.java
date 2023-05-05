module pl.edu.pwr.weakreferencesapplication {
    requires javafx.graphics;
    requires javafx.controls;
    requires javafx.media;
    requires javafx.base;
    requires javafx.fxml;

    requires org.controlsfx.controls;
    requires com.dlsc.formsfx;
    requires org.kordamp.ikonli.javafx;
    requires org.kordamp.bootstrapfx.core;
//    requires com.almasb.fxgl.all;

    opens pl.edu.pwr.weakreferencesapplication to javafx.fxml;
    exports pl.edu.pwr.weakreferencesapplication;
}