import { create } from "zustand";

const useTaskStore = create((set) => ({
  tasks: [],
  addTask: (newTask) => {
    set((state) => ({ tasks: [...state.tasks, newTask] }));
  },
  deleteTask: (taskId) =>
    set((state) => ({
      tasks: state.tasks.filter((task) => task.id !== taskId),
    })),
  updateTask: (updatedTask, taskId) =>
    set((state) => ({
      tasks: state.tasks.map((task) =>
        task.id === taskId ? { ...task, ...updatedTask } : task
      ),
    })),
  importTasks: [],
  addImportantTask: "",
}));

export default useTaskStore;
