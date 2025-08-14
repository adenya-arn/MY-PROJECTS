import useTaskStore from "../store/TaskStore";
import { useState } from "react";

const TaskForm = () => {
  const addTask = useTaskStore((state) => state.addTask);
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    addTask({ id: Date.now(), Title: title, Description: description });
    setTitle("");
    setDescription("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        value={title}
        type="text"
        placeholder="Task title"
        onChange={(e) => {
          setTitle(e.target.value);
        }}
      />

      <textarea
        value={description}
        type="text"
        placeholder="description"
        onChange={(e) => {
          setDescription(e.target.value);
        }}
      />

      <button type="submit"> Add Task</button>
    </form>
  );
};

export default TaskForm;
