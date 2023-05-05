module pl.edu.pwr.discreteconvolutionfunction {
    requires javafx.controls;
    requires javafx.fxml;

//    requires org.controlsfx.controls;
//    requires com.dlsc.formsfx;
//    requires org.kordamp.ikonli.javafx;
//    requires org.kordamp.bootstrapfx.core;
//    requires com.almasb.fxgl.all;

    opens pl.edu.pwr.discreteconvolutionfunction to javafx.fxml;
    exports pl.edu.pwr.discreteconvolutionfunction;
}