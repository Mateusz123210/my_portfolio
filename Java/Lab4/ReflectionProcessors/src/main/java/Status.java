public class Status {

	private final int taskId;

	private final int progress;

	public int getProgress() {
		return progress;
	}

	public int getTaskId() {
		return taskId;
	}

	public Status(int taskId, int progress) {
		this.taskId = taskId;
		this.progress = progress;
	}
}

