<template>
  <div class="result-preview">
    <div class="preview-header">
      <h2 class="preview-title">解析结果预览</h2>
      <div class="preview-actions">
        <button class="action-btn" @click="copyContent">
          <Copy :size="16" />
          复制内容
        </button>
        <button class="action-btn primary" @click="downloadMd">
          <Download :size="16" />
          下载 Markdown
        </button>
      </div>
    </div>
    
    <div class="preview-content">
      <div v-if="loading" class="loading-state">
        <Loader2 :size="48" class="loading-icon" />
        <p>正在加载结果...</p>
      </div>
      
      <div v-else-if="error" class="error-state">
        <AlertCircle :size="48" class="error-icon" />
        <p>{{ error }}</p>
      </div>
      
      <div v-else class="markdown-content" v-html="renderedMarkdown"></div>
    </div>
  </div>
</template>

<script setup>import { ref, watch, computed } from 'vue';
import { Copy, Download, Loader2, AlertCircle } from 'lucide-vue-next';
import MarkdownIt from 'markdown-it';
const props = defineProps({
 content: {
 type: String,
 default: '',
 },
 fileName: {
 type: String,
 default: 'document',
 },
});
const loading = ref(false);
const error = ref('');
const copied = ref(false);
const markdown = ref('');
const md = new MarkdownIt({
 html: true,
 linkify: true,
 typographer: true,
});
const renderedMarkdown = computed(() => {
 return md.render(markdown.value);
});
watch(() => props.content, (newContent) => {
 if (newContent) {
 loading.value = true;
 setTimeout(() => {
 markdown.value = newContent;
 loading.value = false;
 }, 100);
 }
}, { immediate: true });
const copyContent = async () => {
 try {
 await navigator.clipboard.writeText(markdown.value);
 copied.value = true;
 setTimeout(() => copied.value = false, 2000);
 }
 catch (err) {
 console.error('复制失败:', err);
 }
};
const downloadMd = () => {
 const blob = new Blob([markdown.value], { type: 'text/markdown' });
 const url = URL.createObjectURL(blob);
 const a = document.createElement('a');
 a.href = url;
 a.download = `${props.fileName}.md`;
 document.body.appendChild(a);
 a.click();
 document.body.removeChild(a);
 URL.revokeObjectURL(url);
};
</script>

<style scoped>
.result-preview {
  background: #fff;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
  overflow: hidden;
}

.preview-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 24px;
  border-bottom: 1px solid #f0f0f0;
}

.preview-title {
  font-size: 18px;
  font-weight: 600;
  color: #333;
}

.preview-actions {
  display: flex;
  gap: 12px;
}

.action-btn {
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 8px 16px;
  border: none;
  border-radius: 6px;
  font-size: 13px;
  cursor: pointer;
  transition: all 0.2s;
  background-color: #f5f5f5;
  color: #666;
}

.action-btn:hover {
  background-color: #e8e8e8;
}

.action-btn.primary {
  background-color: #1890ff;
  color: #fff;
}

.action-btn.primary:hover {
  background-color: #40a9ff;
}

.preview-content {
  min-height: 400px;
  padding: 24px;
}

.loading-state,
.error-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 0;
}

.loading-icon {
  color: #1890ff;
  animation: spin 1s linear infinite;
  margin-bottom: 16px;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.error-icon {
  color: #f5222d;
  margin-bottom: 16px;
}

.error-state p {
  color: #f5222d;
  font-size: 14px;
}

.markdown-content {
  font-size: 15px;
  line-height: 1.8;
  color: #333;
}

.markdown-content h1 {
  font-size: 24px;
  font-weight: 600;
  margin-bottom: 16px;
  padding-bottom: 12px;
  border-bottom: 1px solid #f0f0f0;
}

.markdown-content h2 {
  font-size: 20px;
  font-weight: 600;
  margin: 20px 0 12px;
}

.markdown-content h3 {
  font-size: 16px;
  font-weight: 600;
  margin: 16px 0 10px;
}

.markdown-content p {
  margin-bottom: 12px;
}

.markdown-content ul,
.markdown-content ol {
  padding-left: 24px;
  margin-bottom: 12px;
}

.markdown-content li {
  margin-bottom: 6px;
}

.markdown-content code {
  background-color: #f6ffed;
  color: #52c41a;
  padding: 2px 6px;
  border-radius: 4px;
  font-size: 14px;
}

.markdown-content pre {
  background-color: #f5f5f5;
  padding: 16px;
  border-radius: 8px;
  overflow-x: auto;
  margin-bottom: 12px;
}

.markdown-content pre code {
  background: none;
  color: #333;
  padding: 0;
}

.markdown-content table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 16px;
}

.markdown-content th,
.markdown-content td {
  border: 1px solid #d9d9d9;
  padding: 10px;
  text-align: left;
}

.markdown-content th {
  background-color: #f5f5f5;
  font-weight: 600;
}

.markdown-content img {
  max-width: 100%;
  border-radius: 8px;
}

.markdown-content blockquote {
  border-left: 4px solid #1890ff;
  padding-left: 16px;
  margin: 16px 0;
  color: #666;
  background-color: #f6ffed;
  padding: 12px 16px;
  border-radius: 0 8px 8px 0;
}
</style>