import { defineStore } from 'pinia';
import { parseFile, submitTask, getTaskStatus, getTaskResult } from '../services/mineruApi';

export const useTaskStore = defineStore('task', {
  state: () => ({
    tasks: [],
    currentTask: null,
    isLoading: false,
    error: null,
    pollInterval: null,
  }),
  
  getters: {
    pendingTasks: (state) => state.tasks.filter(t => t.status === 'pending'),
    processingTasks: (state) => state.tasks.filter(t => t.status === 'processing'),
    completedTasks: (state) => state.tasks.filter(t => t.status === 'completed'),
    failedTasks: (state) => state.tasks.filter(t => t.status === 'failed'),
  },
  
  actions: {
    async submitParseTask(files, options) {
      this.isLoading = true;
      this.error = null;
      
      try {
        const response = options.asyncMode 
          ? await submitTask(files, options)
          : await parseFile(files, options);
        
        if (options.asyncMode) {
          const task = response.data;
          task.createdAt = new Date().toISOString();
          this.tasks.unshift(task);
          return task;
        } else {
          return response.data;
        }
      } catch (error) {
        this.error = error.response?.data?.message || error.message;
        throw error;
      } finally {
        this.isLoading = false;
      }
    },
    
    async fetchTaskStatus(taskId) {
      try {
        const response = await getTaskStatus(taskId);
        const taskIndex = this.tasks.findIndex(t => t.task_id === taskId);
        if (taskIndex !== -1) {
          this.tasks[taskIndex] = { ...this.tasks[taskIndex], ...response.data };
        }
        return response.data;
      } catch (error) {
        this.error = error.message;
        throw error;
      }
    },
    
    async fetchTaskResult(taskId) {
      try {
        const response = await getTaskResult(taskId);
        return response;
      } catch (error) {
        this.error = error.message;
        throw error;
      }
    },
    
    setCurrentTask(task) {
      this.currentTask = task;
    },
    
    clearError() {
      this.error = null;
    },
    
    removeTask(taskId) {
      const index = this.tasks.findIndex(t => t.task_id === taskId);
      if (index !== -1) {
        this.tasks.splice(index, 1);
      }
    },
    
    startPolling(taskId) {
      if (this.pollInterval) {
        clearInterval(this.pollInterval);
      }
      this.pollInterval = setInterval(async () => {
        try {
          await this.fetchTaskStatus(taskId);
          const task = this.tasks.find(t => t.task_id === taskId);
          if (task && ['completed', 'failed'].includes(task.status)) {
            this.stopPolling();
          }
        } catch (error) {
          console.error('Polling error:', error);
        }
      }, 3000);
    },
    
    stopPolling() {
      if (this.pollInterval) {
        clearInterval(this.pollInterval);
        this.pollInterval = null;
      }
    },
  },
});