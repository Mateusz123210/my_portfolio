module com.example.filesmd5snapshotapplication {
    requires FilesMD5SnapshotLibrary;

    requires javafx.controls;
    requires javafx.fxml;

//    requires org.controlsfx.controls;
//    requires com.dlsc.formsfx;
//    requires org.kordamp.ikonli.javafx;
//    requires org.kordamp.bootstrapfx.core;
//    requires com.almasb.fxgl.all;
//
    opens com.example.filesmd5snapshotapplication to javafx.fxml;
    exports com.example.filesmd5snapshotapplication;
}