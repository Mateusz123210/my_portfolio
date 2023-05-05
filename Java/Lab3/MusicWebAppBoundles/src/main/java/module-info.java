module pl.edu.pwr.musicwebappboundles {
    requires java.base;
    requires javafx.controls;
    requires javafx.fxml;
//    requires org.controlsfx.controls;
//    requires com.dlsc.formsfx;
//    requires org.kordamp.ikonli.javafx;
//    requires org.kordamp.bootstrapfx.core;
//    requires com.almasb.fxgl.all;
    requires java.xml;
    requires java.prefs;

    opens pl.edu.pwr.musicwebappboundles to javafx.fxml;
    exports pl.edu.pwr.musicwebappboundles;
}