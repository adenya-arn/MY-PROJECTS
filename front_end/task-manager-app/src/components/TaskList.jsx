import React, { useState } from "react";
import useTaskStore from "../store/taskStore"; // adjust path to your store

const TaskList = () => {
  const { tasks, deleteTask, updateTask } = useTaskStore();
  const [editingTaskId, setEditingTaskId] = useState(null);
  const [editTitle, setEditTitle] = useState("");
  const [editDescription, setEditDescription] = useState("");

  const startEditing = (task) => {
    setEditingTaskId(task.id);
    setEditTitle(task.Title);
    setEditDescription(task.Description);
  };

  const saveEdit = (id) => {
    updateTask(id, {
      Title: editTitle,
      Description: editDescription,
    });
    setEditingTaskId(null); // exit edit mode
  };

  const cancelEdit = () => {
    setEditingTaskId(null);
    setEditTitle("");
    setEditDescription("");
  };

  return (
    <div>
      {tasks.length === 0 && <p>No tasks yet.</p>}

      {tasks.map((task) => (
        <div
          key={task.id}
          style={{
            border: "1px solid #ccc",
            padding: "8px",
            marginBottom: "8px",
          }}
        >
          {editingTaskId === task.id ? (
            <>
              {/* Inline edit form */}
              <input
                type="text"
                value={editTitle}
                onChange={(e) => setEditTitle(e.target.value)}
                placeholder="Title"
              />
              <input
                type="text"
                value={editDescription}
                onChange={(e) => setEditDescription(e.target.value)}
                placeholder="Description"
              />
              <button onClick={() => saveEdit(task.id)}>Save</button>
              <button onClick={cancelEdit}>Cancel</button>
            </>
          ) : (
            <>
              {/* Display mode */}
              <h3>{task.Title}</h3>
              <p>{task.Description}</p>
              <button onClick={() => startEditing(task)}>Edit</button>
              <button onClick={() => deleteTask(task.id)}>Delete</button>
            </>
          )}
        </div>
      ))}
    </div>
  );
};

export default TaskList;
