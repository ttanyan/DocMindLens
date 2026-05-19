<template>
  <div class="upload-container">
    <div
      class="upload-area"
      :class="{ 'drag-over': isDragOver }"
      @dragover.prevent="isDragOver = true"
      @dragleave="isDragOver = false"
      @drop.prevent="handleDrop"
      @click="triggerFileInput"
    >
      <input
        ref="fileInput"
        type="file"
        multiple
        accept=".pdf,.png,.jpg,.jpeg,.webp,.gif,.bmp,.tiff,.docx,.pptx,.xlsx"
        class="file-input"
        @change="handleFileSelect"
      />
      <div class="upload-icon">
        <Upload :size="48" />
      </div>
      <p class="upload-text">点击或拖拽文件到此处上传</p>
      <p class="upload-hint">支持 PDF、图片、DOCX、PPTX、XLSX 格式</p>
    </div>
    
    <div v-if="files.length > 0" class="file-list">
      <h3 class="file-list-title">已选择文件 ({{ files.length }})</h3>
      <div v-for="(file, index) in files" :key="index" class="file-item">
        <FileText :size="20" />
        <span class="file-name">{{ file.name }}</span>
        <span class="file-size">{{ formatFileSize(file.size) }}</span>
        <button class="remove-btn" @click="removeFile(index)">
          <X :size="16" />
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { Upload, FileText, X } from 'lucide-vue-next';

const emit = defineEmits(['files-change']);

const isDragOver = ref(false);
const files = ref([]);
const fileInput = ref(null);

const triggerFileInput = () => {
  fileInput.value?.click();
};

const handleDrop = (event) => {
  isDragOver.value = false;
  const droppedFiles = Array.from(event.dataTransfer.files);
  addFiles(droppedFiles);
};

const handleFileSelect = (event) => {
  const selectedFiles = Array.from(event.target.files);
  addFiles(selectedFiles);
};

const addFiles = (newFiles) => {
  const validExtensions = ['.pdf', '.png', '.jpg', '.jpeg', '.webp', '.gif', '.bmp', '.tiff', '.docx', '.pptx', '.xlsx'];
  
  newFiles.forEach(file => {
    const ext = file.name.toLowerCase().substring(file.name.lastIndexOf('.'));
    if (validExtensions.includes(ext)) {
      if (!files.value.some(f => f.name === file.name && f.size === file.size)) {
        files.value.push(file);
      }
    } else {
      alert(`不支持的文件格式: ${file.name}`);
    }
  });
  
  emit('files-change', files.value);
};

const removeFile = (index) => {
  files.value.splice(index, 1);
  emit('files-change', files.value);
};

const formatFileSize = (bytes) => {
  if (bytes === 0) return '0 B';
  const k = 1024;
  const sizes = ['B', 'KB', 'MB', 'GB'];
  const i = Math.floor(Math.log(bytes) / Math.log(k));
  return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
};

const clearFiles = () => {
  files.value = [];
  emit('files-change', []);
};

defineExpose({ clearFiles });
</script>

<style scoped>
.upload-container {
  width: 100%;
}

.upload-area {
  border: 2px dashed #d9d9d9;
  border-radius: 12px;
  padding: 40px;
  text-align: center;
  cursor: pointer;
  transition: all 0.3s ease;
  background-color: #fff;
}

.upload-area:hover {
  border-color: #1890ff;
  background-color: #f6ffed;
}

.upload-area.drag-over {
  border-color: #1890ff;
  background-color: #e6f7ff;
}

.upload-icon {
  color: #1890ff;
  margin-bottom: 16px;
}

.upload-text {
  font-size: 16px;
  color: #333;
  margin-bottom: 8px;
}

.upload-hint {
  font-size: 14px;
  color: #999;
}

.file-input {
  display: none;
}

.file-list {
  margin-top: 20px;
}

.file-list-title {
  font-size: 14px;
  color: #666;
  margin-bottom: 12px;
}

.file-item {
  display: flex;
  align-items: center;
  padding: 12px;
  background-color: #fff;
  border-radius: 8px;
  margin-bottom: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
}

.file-item svg:first-child {
  color: #1890ff;
  margin-right: 12px;
}

.file-name {
  flex: 1;
  font-size: 14px;
  color: #333;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.file-size {
  font-size: 12px;
  color: #999;
  margin-right: 12px;
}

.remove-btn {
  background: none;
  border: none;
  color: #999;
  cursor: pointer;
  padding: 4px;
  border-radius: 4px;
  transition: all 0.2s;
}

.remove-btn:hover {
  background-color: #f5f5f5;
  color: #f5222d;
}
</style>