module pl.edu.pwr.reflection {
    requires javafx.controls;
    requires javafx.fxml;

//    requires org.controlsfx.controls;
//    requires com.dlsc.formsfx;
//    requires org.kordamp.ikonli.javafx;
//    requires org.kordamp.bootstrapfx.core;
//    requires com.almasb.fxgl.all;


    exports pl.edu.pwr.reflection.window;
    opens pl.edu.pwr.reflection.window to javafx.fxml;
}