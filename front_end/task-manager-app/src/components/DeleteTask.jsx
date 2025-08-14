import useTaskStore from "../store/TaskStore";

const DeleteTask = ({ taskId }) => {
  const deleteTask = useTaskStore((state) => state.deleteTask);
  const handleClick = () => {
    deleteTask(taskId);
  };

  return (
    <div>
      <button onClick={handleClick}>Delete</button>
    </div>
  );
};

export default DeleteTask;
