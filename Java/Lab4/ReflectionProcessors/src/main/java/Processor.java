import javafx.scene.control.Label;

import java.util.Random;

public interface Processor {

	boolean submitTask(String task, StatusListener sl, Label label);

	String getInfo();

	String getResult();

	default void simulateDelationOfWork(StatusListener sl, Label label, int taskId){
		Random random = new Random();
		Integer workTime = random.nextInt(300, 600);
		for(int i = 0; i < 100; i += 10){
			sl.statusChanged(new Status(taskId, i), label);
			try {
				Thread.sleep(workTime);
			} catch (InterruptedException e) {
				throw new RuntimeException(e);
			}
		}
		sl.statusChanged(new Status(taskId, 100), label);
	}

}