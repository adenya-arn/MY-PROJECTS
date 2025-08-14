import useTaskStore from "../store/TaskStore";
import { useState } from "react";

const UpdateTask = ({ task }) => {
  const [editTitle, setEditTitle] = useState(task.Title);
  const [editDescription, setEditDescription] = useState(task.Description);

  const updateTask = useTaskStore((state) => state.updateTask);

  const handleSubmit = (event) => {
    event.preventDefault();
    updateTask(task.id, { Title: editTitle, Description: editDescription });
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={editTitle}
        placeholder="Edit task"
        type="text"
        onChange={(e) => setEditTitle(e.target.value)}
      />
      <textarea
        value={editDescription}
        placeholder="Edit description"
        type="text"
        onChange={(e) => setEditDescription(e.target.value)}
      />

      <button type="submit">Edit</button>
    </form>
  );
};

export default UpdateTask;
